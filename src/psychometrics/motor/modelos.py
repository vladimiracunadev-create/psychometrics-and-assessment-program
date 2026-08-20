"""Modelo de dominio del motor psicométrico.

El principio de diseño es que un instrumento es DATO, no código: se declara en un
archivo YAML y el motor lo interpreta. Agregar un test nuevo no requiere tocar
Python. Estas clases son la representación en memoria de ese archivo.

CONVENCIÓN DE CODIFICACIÓN
La prosa va en castellano con tildes. Todo lo estructural —nombres de campo,
claves YAML, valores de enumeración, identificadores— va en ASCII sin tildes.
Mezclar ambos rompe la carga de forma silenciosa, y `tests/test_estructura.py`
verifica que se respete.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class TipoRespuesta(StrEnum):
    """Cómo responde la persona a un ítem.

    El tipo condiciona tanto la interfaz como el algoritmo de puntuación, por eso
    vive en el modelo y no en el frontend.
    """

    LIKERT = "likert"
    """Escala ordinal de N puntos. Cada ítem se puntúa de forma independiente."""

    ELECCION_FORZADA = "eleccion_forzada"
    """Bloque de opciones donde se elige la que MÁS y la que MENOS describe.

    Produce puntajes ipsativos: solo comparables dentro de la misma persona.
    """

    RANKING = "ranking"
    """Ordenamiento completo de un bloque de opciones. También ipsativo."""

    SUMA_CONSTANTE = "suma_constante"
    """Reparto de un total fijo de puntos entre opciones. También ipsativo."""


class Licencia(StrEnum):
    """Situación legal del banco de ítems. Determina si es redistribuible."""

    DOMINIO_PUBLICO = "dominio-publico"
    CC_BY_4_0 = "CC-BY-4.0"
    AUTORIA_PROPIA = "autoria-propia"
    PROPIETARIA = "propietaria"
    """Solo para catalogar instrumentos de terceros. NUNCA se incluyen sus ítems."""

    @property
    def redistribuible(self) -> bool:
        return self is not Licencia.PROPIETARIA


@dataclass(frozen=True, slots=True)
class Item:
    """Una pregunta o afirmación individual."""

    id: str
    texto: dict[str, str]
    """Texto por código de idioma ISO-639-1, p. ej. {"en": "...", "es": "..."}."""

    escala: str
    """Código de la escala a la que aporta este ítem."""

    clave: int = 1
    """+1 ítem directo, -1 ítem invertido (se refleja antes de sumar)."""

    bloque: str | None = None
    """Agrupador para ítems ipsativos (elección forzada, ranking)."""

    def enunciado(self, idioma: str, respaldo: str = "en") -> str:
        return self.texto.get(idioma) or self.texto[respaldo]


@dataclass(frozen=True, slots=True)
class Escala:
    """Una dimensión medida: un dominio, una faceta, un tipo o un valor."""

    codigo: str
    nombre: dict[str, str]
    descripcion: dict[str, str] = field(default_factory=dict)

    padre: str | None = None
    """Código de la escala superior. Permite jerarquía dominio -> faceta."""

    alfa: float | None = None
    """Consistencia interna reportada por la fuente. None si no hay dato."""

    polo_bajo: dict[str, str] = field(default_factory=dict)
    polo_alto: dict[str, str] = field(default_factory=dict)
    """Glosa interpretativa de cada extremo. Es la base del informe narrativo."""

    def rotulo(self, idioma: str, respaldo: str = "en") -> str:
        return self.nombre.get(idioma) or self.nombre[respaldo]


@dataclass(frozen=True, slots=True)
class OpcionLikert:
    """Un punto de anclaje de una escala Likert."""

    valor: int
    etiqueta: dict[str, str]


@dataclass(frozen=True, slots=True)
class Procedencia:
    """De dónde sale el instrumento. Es obligatoria: sin fuente no hay instrumento.

    Un test sin procedencia verificable no es un test, es una encuesta de revista.
    Por eso el motor rechaza cargar un instrumento que no la declare.
    """

    autores: str
    anio: int | None
    fuente: str
    """URL o referencia bibliográfica canónica."""

    licencia: Licencia
    cita: str | None = None
    notas: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class Instrumento:
    """Un test completo: metadatos, escalas, ítems y reglas de puntuación."""

    codigo: str
    version: str
    nombre: dict[str, str]
    descripcion: dict[str, str]
    tipo_respuesta: TipoRespuesta
    procedencia: Procedencia
    escalas: tuple[Escala, ...]
    items: tuple[Item, ...]
    opciones: tuple[OpcionLikert, ...] = ()
    duracion_min: tuple[int, int] | None = None
    ipsativo: bool = False
    """Si es True, los puntajes NO son comparables entre personas."""

    def escala(self, codigo: str) -> Escala:
        for e in self.escalas:
            if e.codigo == codigo:
                return e
        raise KeyError(f"{self.codigo}: no existe la escala {codigo!r}")

    def items_de(self, codigo_escala: str) -> tuple[Item, ...]:
        return tuple(i for i in self.items if i.escala == codigo_escala)

    def hijas_de(self, codigo_escala: str) -> tuple[Escala, ...]:
        return tuple(e for e in self.escalas if e.padre == codigo_escala)

    @property
    def raices(self) -> tuple[Escala, ...]:
        return tuple(e for e in self.escalas if e.padre is None)


@dataclass(frozen=True, slots=True)
class Respuesta:
    """Lo que contestó la persona a un ítem."""

    item_id: str
    valor: int | None
    """None = omitida. El motor decide cómo tratarla, no la asume como cero."""


@dataclass(frozen=True, slots=True)
class PuntajeEscala:
    """Resultado en una escala."""

    codigo: str
    bruto: float
    items_respondidos: int
    items_totales: int
    media_item: float
    """Bruto normalizado por número de ítems respondidos.

    Es lo único comparable entre escalas con distinta cantidad de ítems.
    """

    percentil: float | None = None
    z: float | None = None
    baremo: str | None = None
    """Identificador de la norma aplicada. None = puntaje sin baremar."""

    @property
    def completa(self) -> bool:
        return self.items_respondidos == self.items_totales


@dataclass(frozen=True, slots=True)
class Resultado:
    """Perfil completo de una persona en un instrumento."""

    instrumento: str
    version: str
    puntajes: dict[str, PuntajeEscala]
    omitidas: int = 0
    advertencias: tuple[str, ...] = ()
    """Alertas de calidad: demasiadas omisiones, respuestas invariantes, etc."""

    def __getitem__(self, codigo: str) -> PuntajeEscala:
        return self.puntajes[codigo]
