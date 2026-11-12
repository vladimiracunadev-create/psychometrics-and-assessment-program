"""Laboratorio 050 - Bancos de items: huella por item, diff entre versiones y regla de comparabilidad.

Con los items REALES de `valores-spranger` se calcula una huella SHA-256 del texto de cada item. Se
simula una "version 2" con 4 items reescritos y 2 items nuevos y 1 retirado, y se compara con la
version 1: items intactos, modificados, nuevos y retirados. Regla de comparabilidad: los puntajes de
dos versiones solo se comparan directamente si una proporcion suficiente de items ANCLA (identicos)
se mantiene (aqui se usa 80 % como regla de ejemplo, no como norma). La clave de un item invertido
tambien forma parte de la huella.
"""
from __future__ import annotations

import hashlib
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import cargar  # noqa: E402

UMBRAL_ANCLA = 0.80


def huella(texto: str, clave: int) -> str:
    return hashlib.sha256(f"{clave}|{texto}".encode()).hexdigest()[:10]


def main() -> None:
    ins = cargar("valores-spranger")
    v1 = {i.id: huella(i.texto["es"], i.clave) for i in ins.items}
    v2 = dict(v1)
    editados = [ins.items[2].id, ins.items[10].id, ins.items[20].id, ins.items[30].id]
    for iid in editados:
        v2[iid] = huella("texto reescrito de ejemplo " + iid, 1)
    retirado = ins.items[5].id
    del v2[retirado]
    v2["nuevo1"] = huella("item nuevo uno", 1)
    v2["nuevo2"] = huella("item nuevo dos", -1)
    intactos = [k for k in v1 if k in v2 and v1[k] == v2[k]]
    modificados = [k for k in v1 if k in v2 and v1[k] != v2[k]]
    retirados = [k for k in v1 if k not in v2]
    nuevos = [k for k in v2 if k not in v1]
    ancla = len(intactos) / len(v1)
    print(f"Version 1: {len(v1)} items | Version 2: {len(v2)} items")
    print(f"  intactos   : {len(intactos)}\n  modificados: {len(modificados)} {modificados}\n  retirados  : {len(retirados)} {retirados}\n  nuevos     : {len(nuevos)} {nuevos}")
    print(f"\nProporcion de items ancla = {ancla:.0%} (umbral de ejemplo {UMBRAL_ANCLA:.0%}) -> "
          f"{'comparables con cautela' if ancla >= UMBRAL_ANCLA else 'NO comparables sin equiparacion (clase 072)'}")
    print("Version sugerida del instrumento: " + ("menor (1.1.0): documentar y recalcular" if ancla >= UMBRAL_ANCLA else "mayor (2.0.0): ruptura"))
    print()
    print("Lectura: la huella detecta cambios silenciosos, incluso de un solo caracter o de la clave. Reescribir un")
    print("item cambia el estimulo (clase 182); con suficientes items ancla se pueden equiparar las versiones, y")
    print("sin ellos no. El control de cambios es parte de la validez: un banco que cambia sin registro")
    print("no permite reproducir ni comparar puntajes.")


if __name__ == "__main__":
    main()
