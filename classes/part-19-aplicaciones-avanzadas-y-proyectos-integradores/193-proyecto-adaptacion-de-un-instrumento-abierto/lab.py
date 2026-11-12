"""Laboratorio 193 - Proyecto: protocolo de adaptacion con compuertas (gates).

Una adaptacion cultural/linguistica de un instrumento abierto avanza por etapas y NO se pasa a la
siguiente si la compuerta no se cumple:
  1. permiso/licencia verificados,
  2. traduccion y retrotraduccion,
  3. validez de contenido por expertos (I-CVI >= 0.78 con 6 o mas expertos, Lynn 1986),
  4. entrevistas cognitivas,
  5. estudio piloto (alfa >= 0.70),
  6. invarianza/DIF antes de comparar grupos.
Datos de expertos y piloto SINTETICOS. El laboratorio implementa el motor de compuertas y calcula el
I-CVI de 12 items; los items que no llegan al umbral se reescriben antes de seguir.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819


def icvi(calif: list[int]) -> float:
    return sum(c >= 3 for c in calif) / len(calif)       # relevancia 3 o 4 en escala 1-4


def alfa(m: list[list[float]]) -> float:
    k = len(m[0])
    cols = list(zip(*m, strict=True))
    tot = [sum(f) for f in m]
    return k / (k - 1) * (1 - sum(statistics.pvariance(c) for c in cols) / statistics.pvariance(tot))


def main() -> None:
    rng = random.Random(SEMILLA)
    expertos = 6
    items = {}
    for j in range(12):
        calidad = 0.9 if j not in (3, 8) else 0.45          # items 4 y 9 mal traducidos (a proposito)
        items[f"i{j + 1:02d}"] = [4 if rng.random() < calidad else rng.choice([1, 2, 3]) for _ in range(expertos)]
    ic = {k: icvi(v) for k, v in items.items()}
    malos = [k for k, v in ic.items() if v < 0.78]
    s_icvi = statistics.fmean(ic.values())
    print("I-CVI por item: " + ", ".join(f"{k}={v:.2f}" for k, v in ic.items()))
    print(f"Items bajo 0.78: {malos}; S-CVI/Ave = {s_icvi:.2f}")
    theta = [rng.gauss(0, 1) for _ in range(250)]
    piloto = [[1 + 4 * (1 / (1 + 2.718 ** (-(t + rng.gauss(0, 0.9))))) for _ in range(12)] for t in theta]
    a = alfa(piloto)
    etapas = [("1 permiso y licencia verificados", True),
              ("2 traduccion y retrotraduccion", True),
              ("3 validez de contenido (todos los items >= 0.78)", not malos),
              ("4 entrevistas cognitivas", True),
              ("5 piloto con alfa >= 0.70", a >= 0.70),
              ("6 invarianza/DIF antes de comparar grupos", True)]
    print(f"Alfa del piloto (sintetico, n = 250): {a:.2f}\n")
    print("Estado del protocolo:")
    detenido = False
    for nombre, ok in etapas:
        if detenido:
            print(f"  [ pendiente ] {nombre}")
        elif ok:
            print(f"  [ superada  ] {nombre}")
        else:
            print(f"  [ DETENIDO  ] {nombre}  -> reescribir los items {malos} y repetir la etapa")
            detenido = True
    print()
    print("Lectura: las compuertas impiden construir un estudio piloto sobre items que los expertos ya cuestionan.")
    print("Las etapas 1, 2, 4 y 6 requieren personas reales: aqui se marcan superadas solo para ensenar el flujo.")
    print("Una adaptacion no es una traduccion: sin equivalencia demostrada no se comparan puntajes entre culturas.")


if __name__ == "__main__":
    main()
