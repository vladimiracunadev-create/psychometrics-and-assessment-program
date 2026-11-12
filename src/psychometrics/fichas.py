"""Catalogo ampliado de fichas documentales (catalogo/fichas.yaml).

Una ficha NO es un test ejecutable: separa cinco estados que no deben
confundirse (documentado, disponible-legalmente, implementado, en-investigacion,
validado-uso-especifico). Solo `implementado` puede apuntar a instruments/.
"""
from __future__ import annotations

import pathlib
from collections import Counter

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
RUTA = RAIZ / "catalogo" / "fichas.yaml"

FAMILIAS = {"A", "B", "C", "D", "E", "F", "G", "H"}
USOS = {"educativo", "laboral", "clinico", "investigacion", "orientacion"}
ESTADOS = {"documentado", "disponible-legalmente", "implementado",
           "en-investigacion", "validado-uso-especifico"}
LICENCIAS = {"propietaria", "dominio-publico", "abierta", "no-aplica", "no-verificado"}


def cargar_fichas(ruta: pathlib.Path = RUTA) -> list[dict]:
    crudo = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    base = crudo.get("defaults", {})
    return [{**base, **f} for f in crudo["fichas"]]


def validar_fichas(fichas: list[dict], instrumentos: set[str]) -> list[str]:
    """Devuelve la lista de problemas; vacia si el catalogo es coherente."""
    errores: list[str] = []
    vistos: set[str] = set()
    for f in fichas:
        i = f.get("id", "?")
        if i in vistos:
            errores.append(f"{i}: id duplicado")
        vistos.add(i)
        if not str(i).isascii():
            errores.append(f"{i}: el id debe ser ASCII")
        if not f.get("nombre"):
            errores.append(f"{i}: falta nombre")
        if f.get("familia") not in FAMILIAS:
            errores.append(f"{i}: familia invalida {f.get('familia')!r}")
        if not f.get("uso") or not set(f["uso"]) <= USOS:
            errores.append(f"{i}: uso invalido {f.get('uso')!r}")
        if f.get("estado") not in ESTADOS:
            errores.append(f"{i}: estado invalido {f.get('estado')!r}")
        if f.get("licencia") not in LICENCIAS:
            errores.append(f"{i}: licencia invalida {f.get('licencia')!r}")
        impl = f.get("implementacion")
        if f.get("estado") == "implementado":
            if impl not in instrumentos:
                errores.append(f"{i}: implementado sin instrumento real ({impl!r})")
        elif impl:
            errores.append(f"{i}: tiene implementacion pero estado {f.get('estado')!r}")
        if f.get("estado") == "validado-uso-especifico" and not f.get("evidencia"):
            errores.append(f"{i}: validado sin 'evidencia' declarada")
        if f.get("verificado") is True and not f.get("estado") == "implementado":
            errores.append(f"{i}: solo se marca verificado lo que se contrasto con fuente primaria")
        if f.get("licencia") == "propietaria" and f.get("redistribuible") == "si":
            errores.append(f"{i}: propietaria no puede declararse redistribuible")
    return errores


def resumen(fichas: list[dict]) -> dict[str, int]:
    c = Counter(f["estado"] for f in fichas)
    return {"fichas": len(fichas), **{e: c.get(e, 0) for e in sorted(ESTADOS)}}
