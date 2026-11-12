"""Laboratorio 065 - Adaptacion transcultural: similitud factorial no es equivalencia de medida.

Version original (grupo 1) y version adaptada (grupo 2) de una escala de 8 items. En la
adaptacion el item 3 quedo mal traducido (carga baja) y el item 5 tiene un desplazamiento
sistematico del nivel (se asiente mas a igual rasgo). Los grupos tienen el MISMO rasgo medio.
Se calcula el coeficiente de congruencia de Tucker (phi) entre las cargas de ambos grupos y
la diferencia de medias de la escala. phi > 0.95 es una regla citada para "similitud
factorial" (Lorenzo-Seva y ten Berge, 2006), pero NO implica que las medias sean comparables.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 4000, 8


def congruencia(x: list[float], y: list[float]) -> float:
    return sum(a * b for a, b in zip(x, y, strict=True)) / math.sqrt(
        sum(a * a for a in x) * sum(b * b for b in y))


def grupo(cargas: list[float], desplaz: list[float], rng: random.Random):
    theta = [rng.gauss(0, 1) for _ in range(N)]
    items = [[c * t + d + rng.gauss(0, math.sqrt(1 - c * c)) for t in theta]
             for c, d in zip(cargas, desplaz, strict=True)]
    return theta, items


def carga_estimada(theta: list[float], item: list[float]) -> float:
    return statistics.correlation(theta, item)       # con rasgo conocido (simulacion)


def main() -> None:
    rng = random.Random(SEMILLA)
    cargas1 = [0.7] * K
    cargas2 = cargas1[:]
    cargas2[2] = 0.35                                 # mala traduccion del item 3
    d2 = [0.0] * K
    d2[4] = 0.6                                       # item 5 desplazado
    th1, it1 = grupo(cargas1, [0.0] * K, rng)
    th2, it2 = grupo(cargas2, d2, rng)
    l1 = [carga_estimada(th1, i) for i in it1]
    l2 = [carga_estimada(th2, i) for i in it2]
    print("item | carga orig. | carga adapt. | media orig. | media adapt.")
    for j in range(K):
        print(f"{j + 1:4d} | {l1[j]:11.2f} | {l2[j]:12.2f} | {statistics.fmean(it1[j]):11.2f} | "
              f"{statistics.fmean(it2[j]):12.2f}")
    t1 = [sum(f) for f in zip(*it1, strict=True)]
    t2 = [sum(f) for f in zip(*it2, strict=True)]
    print(f"\nCongruencia de Tucker entre cargas: phi = {congruencia(l1, l2):.3f}")
    print(f"Diferencia de medias de la escala (adapt. - orig.): {statistics.fmean(t2) - statistics.fmean(t1):.2f} "
          f"(DE de la escala = {statistics.pstdev(t1):.2f}); el rasgo medio es IGUAL en ambos")
    print()
    print("Lectura: phi alto (patron de cargas parecido) coexiste con un item mal traducido y con")
    print("un item desplazado que sesga la comparacion de medias. La adaptacion transcultural")
    print("requiere traduccion y retraduccion, prueba piloto cognitiva y pruebas de invarianza")
    print("(configural, metrica, escalar) antes de comparar puntajes entre idiomas (ITC, 2017).")


if __name__ == "__main__":
    main()
