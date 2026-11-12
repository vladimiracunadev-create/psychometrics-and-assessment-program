"""Laboratorio 059 - Equiparacion: formas distintas, puntajes comparables.

Forma X y forma Y de 40 items Rasch; Y es mas dificil (dificultades +0.4). Diseno de grupos
aleatorios: dos grupos equivalentes (theta ~ N(0,1)), cada uno rinde una forma. Se comparan
tres metodos para llevar los puntajes de Y a la escala de X:
    media:          Y + (media X - media Y)
    lineal:         media y DE iguales
    equipercentil:  mismo rango percentil
y se verifica el efecto sobre la tasa de aprobados con corte 22 en la escala X.
"""
from __future__ import annotations

import bisect
import math
import random
import statistics

SEMILLA = 20260819
N, K, CORTE = 6000, 40, 22


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def aplica(bs: list[float], rng: random.Random) -> list[int]:
    return [sum(rng.random() < logistica(rng.gauss(0, 1) - b) for b in bs) for _ in range(N)]


def rango_percentil(ordenado: list[int], v: float) -> float:
    return (bisect.bisect_left(ordenado, v) + bisect.bisect_right(ordenado, v)) / 2 / len(ordenado)


def cuantil(ordenado: list[int], q: float) -> float:
    return ordenado[min(len(ordenado) - 1, max(0, int(q * len(ordenado))))]


def main() -> None:
    rng = random.Random(SEMILLA)
    base = [-2.0 + 4.0 * i / (K - 1) for i in range(K)]
    x = aplica(base, rng)
    y = aplica([b + 0.4 for b in base], rng)
    xs = sorted(x)
    ys = sorted(y)
    mx, my, sx, sy = statistics.fmean(x), statistics.fmean(y), statistics.pstdev(x), statistics.pstdev(y)

    metodos = {
        "sin equiparar": lambda v: v,
        "media": lambda v: v + (mx - my),
        "lineal": lambda v: mx + sx / sy * (v - my),
        "equipercentil": lambda v: cuantil(xs, rango_percentil(ys, v)),
    }
    print(f"Media forma X = {mx:.2f} | media forma Y = {my:.2f} (Y es mas dificil)")
    print(f"{'metodo':<16} {'aprobados (Y equiparada, corte ' + str(CORTE) + ')':>40}")
    print("=" * 58)
    print(f"{'forma X (ref.)':<16} {sum(v >= CORTE for v in x) / N:40.3f}")
    for nombre, f in metodos.items():
        print(f"{nombre:<16} {sum(f(v) >= CORTE for v in y) / N:40.3f}")
    print()
    print("Lectura: sin equiparar, quienes rinden la forma dificil aprueban mucho menos solo por la")
    print("forma. Media y lineal corrigen parte (no la forma de la distribucion); el equipercentil")
    print("se acerca a la tasa de referencia porque iguala toda la distribucion, no solo sus momentos.")
    print("Requieren un diseno que justifique la equivalencia de los grupos (o items ancla) y")
    print("muestras grandes; con formas de contenido distinto solo hay 'vinculacion', no equiparacion.")


if __name__ == "__main__":
    main()
