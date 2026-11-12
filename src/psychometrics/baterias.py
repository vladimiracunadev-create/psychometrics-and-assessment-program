"""Baterias de evaluacion: agrupar instrumentos, registrar respuestas y reanudar sesiones.

Componente reutilizable y SIN dependencias del resto del repositorio educativo: una `Bateria`
es una lista ordenada de instrumentos del catalogo, y una `Sesion` guarda el avance de UNA
persona (identificada por un codigo seudonimo, nunca por nombre o RUT). La sesion se serializa
a un diccionario JSON-compatible: se puede pausar y reanudar, y el resultado final no depende de
haber pausado.

Decisiones de diseno:
  - El estado guarda solo respuestas y una bitacora de eventos; los puntajes se RECALCULAN con el
    motor al pedirlos (nunca se persisten, para que una correccion del motor no deje datos viejos).
  - Cada evento de la bitacora lleva un indice incremental, no una hora: el modulo no consulta el
    reloj, lo que lo hace determinista y facil de probar.
  - Un instrumento esta "completo" cuando todos sus items tienen respuesta (o omision explicita).
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

from .motor import Instrumento, Respuesta, Resultado, cargar, puntuar


class BateriaInvalida(ValueError):
    """La bateria o la sesion no son coherentes."""


@dataclass(frozen=True, slots=True)
class Bateria:
    codigo: str
    instrumentos: tuple[str, ...]
    descripcion: str = ""

    def __post_init__(self) -> None:
        if not self.instrumentos:
            raise BateriaInvalida(f"{self.codigo}: una bateria necesita al menos un instrumento")
        if len(set(self.instrumentos)) != len(self.instrumentos):
            raise BateriaInvalida(f"{self.codigo}: instrumentos repetidos")


@dataclass
class Sesion:
    bateria: Bateria
    sujeto: str
    respuestas: dict[str, dict[str, int | None]] = field(default_factory=dict)
    bitacora: list[dict] = field(default_factory=list)
    _cache: dict[str, Instrumento] = field(default_factory=dict, repr=False)

    # --- acceso a instrumentos -------------------------------------------------------------
    def instrumento(self, codigo: str) -> Instrumento:
        if codigo not in self.bateria.instrumentos:
            raise BateriaInvalida(f"{codigo} no pertenece a la bateria {self.bateria.codigo}")
        if codigo not in self._cache:
            self._cache[codigo] = cargar(codigo)
        return self._cache[codigo]

    # --- registro --------------------------------------------------------------------------
    def responder(self, codigo: str, item_id: str, valor: int | None) -> None:
        ins = self.instrumento(codigo)
        if item_id not in {i.id for i in ins.items}:
            raise BateriaInvalida(f"{codigo}: no existe el item {item_id}")
        if valor is not None:
            valores = [o.valor for o in ins.opciones]
            if valor not in valores:
                raise BateriaInvalida(f"{codigo}/{item_id}: valor {valor} fuera de {valores}")
        self.respuestas.setdefault(codigo, {})[item_id] = valor
        self.bitacora.append({"n": len(self.bitacora), "evento": "respuesta", "instrumento": codigo,
                              "item": item_id, "omitida": valor is None})

    # --- estado ----------------------------------------------------------------------------
    def pendientes(self, codigo: str) -> list[str]:
        hechos = self.respuestas.get(codigo, {})
        return [i.id for i in self.instrumento(codigo).items if i.id not in hechos]

    def completo(self, codigo: str) -> bool:
        return not self.pendientes(codigo)

    def siguiente(self) -> tuple[str, str] | None:
        """Proximo (instrumento, item) por responder, en el orden de la bateria."""
        for codigo in self.bateria.instrumentos:
            p = self.pendientes(codigo)
            if p:
                return codigo, p[0]
        return None

    def avance(self) -> dict[str, tuple[int, int]]:
        return {c: (len(self.respuestas.get(c, {})), len(self.instrumento(c).items))
                for c in self.bateria.instrumentos}

    # --- resultados ------------------------------------------------------------------------
    def resultado(self, codigo: str) -> Resultado:
        if not self.completo(codigo):
            raise BateriaInvalida(f"{codigo}: faltan {len(self.pendientes(codigo))} items")
        resp = [Respuesta(i, v) for i, v in self.respuestas[codigo].items()]
        return puntuar(self.instrumento(codigo), resp)

    # --- persistencia (pausar / reanudar) --------------------------------------------------
    def guardar(self) -> dict:
        cuerpo = {"bateria": self.bateria.codigo, "instrumentos": list(self.bateria.instrumentos),
                  "sujeto": self.sujeto, "respuestas": self.respuestas, "bitacora": self.bitacora}
        cuerpo["huella"] = _huella(cuerpo)
        return cuerpo

    @classmethod
    def cargar(cls, estado: dict) -> Sesion:
        esperado = estado.get("huella")
        sin_huella = {k: v for k, v in estado.items() if k != "huella"}
        if esperado != _huella(sin_huella):
            raise BateriaInvalida("la huella de la sesion no coincide: el estado fue alterado")
        bat = Bateria(estado["bateria"], tuple(estado["instrumentos"]))
        return cls(bat, estado["sujeto"], {c: dict(r) for c, r in estado["respuestas"].items()},
                   list(estado["bitacora"]))


def _huella(cuerpo: dict) -> str:
    return hashlib.sha256(json.dumps(cuerpo, sort_keys=True, ensure_ascii=True).encode()).hexdigest()[:16]
