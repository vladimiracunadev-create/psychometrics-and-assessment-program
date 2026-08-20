"""Carga instrumentos declarados en YAML y los valida antes de devolverlos.

La validación es deliberadamente estricta. Un instrumento mal declarado no falla
al cargarse sino al puntuar, y un error de puntuación silencioso produce un
informe que parece correcto sobre una persona real. Preferimos romper aquí.
"""

from __future__ import annotations

import pathlib
from typing import Any

import yaml

from .modelos import (
    Escala,
    Instrumento,
    Item,
    Licencia,
    OpcionLikert,
    Procedencia,
    TipoRespuesta,
)


def _raiz_instrumentos() -> pathlib.Path:
    """Resuelve donde vive el catalogo.

    Se busca en tres lugares, en orden: la variable de entorno (util para
    catalogos privados), la raiz del repositorio en instalacion editable, y el
    propio paquete cuando se instala como wheel.
    """
    import os

    if ruta := os.environ.get("PSYCHOMETRICS_INSTRUMENTS"):
        return pathlib.Path(ruta)
    aqui = pathlib.Path(__file__).resolve()
    for candidata in (aqui.parents[3] / "instruments", aqui.parents[1] / "instruments"):
        if candidata.is_dir():
            return candidata
    return aqui.parents[3] / "instruments"


RAIZ_INSTRUMENTOS = _raiz_instrumentos()

# Campos que todo instrumento debe declarar. Van en ASCII porque son claves YAML.
OBLIGATORIOS = ("codigo", "version", "nombre", "tipo_respuesta", "procedencia",
                "escalas", "items")


class InstrumentoInvalido(ValueError):
    """El archivo se leyó pero no describe un instrumento utilizable."""

    def __init__(self, codigo: str, errores: list[str]) -> None:
        self.codigo = codigo
        self.errores = errores
        detalle = "\n  - ".join(errores)
        super().__init__(f"{codigo}: instrumento inválido\n  - {detalle}")


def _texto_ml(valor: Any, campo: str, errores: list[str]) -> dict[str, str]:
    """Normaliza un campo multiidioma a dict[idioma, texto]."""
    if isinstance(valor, str):
        return {"es": valor}
    if isinstance(valor, dict) and valor:
        return {str(k): str(v) for k, v in valor.items()}
    errores.append(f"{campo}: se esperaba texto o mapa de idiomas, hay {type(valor).__name__}")
    return {}


def cargar_desde_texto(contenido: str, origen: str = "<memoria>") -> Instrumento:
    """Construye un Instrumento a partir del YAML ya leído."""
    crudo = yaml.safe_load(contenido)
    if not isinstance(crudo, dict):
        raise InstrumentoInvalido(origen, ["el archivo no contiene un mapa YAML"])

    errores: list[str] = []
    codigo = str(crudo.get("codigo") or origen)

    for campo in OBLIGATORIOS:
        if campo not in crudo:
            errores.append(f"falta el campo obligatorio {campo!r}")
    if errores:
        raise InstrumentoInvalido(codigo, errores)

    try:
        tipo = TipoRespuesta(crudo["tipo_respuesta"])
    except ValueError:
        errores.append(
            f"tipo_respuesta {crudo['tipo_respuesta']!r} no es uno de "
            f"{[t.value for t in TipoRespuesta]}"
        )
        tipo = TipoRespuesta.LIKERT

    proc_crudo = crudo["procedencia"] or {}
    try:
        licencia = Licencia(proc_crudo.get("licencia"))
    except ValueError:
        errores.append(
            f"licencia {proc_crudo.get('licencia')!r} no es una de "
            f"{[x.value for x in Licencia]}"
        )
        licencia = Licencia.AUTORIA_PROPIA

    if not proc_crudo.get("fuente"):
        errores.append("procedencia.fuente es obligatoria: sin fuente no hay instrumento")

    procedencia = Procedencia(
        autores=str(proc_crudo.get("autores", "")),
        anio=proc_crudo.get("anio"),
        fuente=str(proc_crudo.get("fuente", "")),
        licencia=licencia,
        cita=proc_crudo.get("cita"),
        notas={str(k): str(v) for k, v in (proc_crudo.get("notas") or {}).items()},
    )

    if licencia is Licencia.PROPIETARIA and crudo.get("items"):
        errores.append(
            "un instrumento de licencia propietaria no puede incluir ítems; "
            "solo se cataloga su ficha"
        )

    escalas: list[Escala] = []
    for n, e in enumerate(crudo["escalas"] or []):
        cod = e.get("codigo")
        if not cod:
            errores.append(f"escalas[{n}]: falta 'codigo'")
            continue
        escalas.append(
            Escala(
                codigo=str(cod),
                nombre=_texto_ml(e.get("nombre"), f"escalas[{cod}].nombre", errores),
                descripcion=_texto_ml(e.get("descripcion", {}), "", []),
                padre=str(e["padre"]) if e.get("padre") else None,
                alfa=float(e["alfa"]) if e.get("alfa") is not None else None,
                polo_bajo=_texto_ml(e.get("polo_bajo", {}), "", []),
                polo_alto=_texto_ml(e.get("polo_alto", {}), "", []),
            )
        )

    codigos = {e.codigo for e in escalas}
    if len(codigos) != len(escalas):
        errores.append("hay códigos de escala repetidos")
    for e in escalas:
        if e.padre and e.padre not in codigos:
            errores.append(f"escala {e.codigo}: su padre {e.padre!r} no existe")

    items: list[Item] = []
    vistos: set[str] = set()
    for n, i in enumerate(crudo["items"] or []):
        iid = str(i.get("id") or f"#{n}")
        if iid in vistos:
            errores.append(f"ítem {iid}: id repetido")
        vistos.add(iid)
        clave = int(i.get("clave", 1))
        if clave not in (1, -1):
            errores.append(f"ítem {iid}: clave {clave} inválida (debe ser 1 o -1)")
            clave = 1
        escala_item = str(i.get("escala", ""))
        if escala_item not in codigos:
            errores.append(f"ítem {iid}: apunta a la escala inexistente {escala_item!r}")
        items.append(
            Item(
                id=iid,
                texto=_texto_ml(i.get("texto"), f"ítem {iid}.texto", errores),
                escala=escala_item,
                clave=clave,
                bloque=str(i["bloque"]) if i.get("bloque") else None,
            )
        )

    # Una escala hoja sin ítems no se puede puntuar. Una escala con hijas las
    # agrega, así que solo se exige ítems a las que no tienen descendencia.
    con_hijas = {e.padre for e in escalas if e.padre}
    for e in escalas:
        if e.codigo not in con_hijas and not any(i.escala == e.codigo for i in items):
            errores.append(f"escala {e.codigo}: es hoja y no tiene ningún ítem")

    opciones = tuple(
        OpcionLikert(valor=int(o["valor"]), etiqueta=_texto_ml(o.get("etiqueta"), "", []))
        for o in (crudo.get("opciones") or [])
    )
    if tipo is TipoRespuesta.LIKERT and len(opciones) < 2:
        errores.append("un instrumento Likert necesita al menos 2 opciones declaradas")

    if errores:
        raise InstrumentoInvalido(codigo, errores)

    dur = crudo.get("duracion_min")
    return Instrumento(
        codigo=codigo,
        version=str(crudo["version"]),
        nombre=_texto_ml(crudo["nombre"], "nombre", []),
        descripcion=_texto_ml(crudo.get("descripcion", {}), "", []),
        tipo_respuesta=tipo,
        procedencia=procedencia,
        escalas=tuple(escalas),
        items=tuple(items),
        opciones=opciones,
        duracion_min=(int(dur[0]), int(dur[1])) if dur else None,
        ipsativo=bool(crudo.get("ipsativo", False)),
    )


def cargar(codigo: str, raiz: pathlib.Path | None = None) -> Instrumento:
    """Carga un instrumento del catálogo por su código."""
    base = raiz or RAIZ_INSTRUMENTOS
    ruta = base / f"{codigo}.yaml"
    if not ruta.is_file():
        disponibles = ", ".join(sorted(i.stem for i in base.glob("*.yaml"))) or "ninguno"
        raise FileNotFoundError(
            f"no existe el instrumento {codigo!r} en {base}. Disponibles: {disponibles}"
        )
    return cargar_desde_texto(ruta.read_text(encoding="utf-8"), origen=codigo)


def catalogo(raiz: pathlib.Path | None = None) -> list[Instrumento]:
    """Carga todos los instrumentos del catálogo, ordenados por código."""
    base = raiz or RAIZ_INSTRUMENTOS
    return [cargar(r.stem, base) for r in sorted(base.glob("*.yaml"))]
