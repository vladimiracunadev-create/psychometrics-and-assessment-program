"""Laboratorio 026 - Estadistica descriptiva de un puntaje total: forma, suelo y techo.

Se simulan 10 items Likert (1-5) en dos escalas del MISMO rasgo: una "facil" (la
mayoria asiente) y otra "equilibrada". Se describe el puntaje total con media, DE,
asimetria, curtosis exceso y porcentaje en suelo y techo. Un puntaje asimetrico con
techo marcado pierde capacidad de discriminar en la parte alta.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 5000
K = 10


def momento(xs: list[float], r: int) -> float:
    m, s = statistics.fmean(xs), statistics.pstdev(xs)
    return statistics.fmean(((x - m) / s) ** r for x in xs)


def simula(sesgo: float, rng: random.Random) -> list[int]:
    """`sesgo` desplaza todos los umbrales: >0 vuelve los items mas faciles de asentir."""
    totales = []
    for _ in range(N):
        theta = rng.gauss(0, 1)
        total = 0
        for _ in range(K):
            latente = theta * 0.8 + sesgo + rng.gauss(0, 0.8)
            total += max(1, min(5, round(3 + latente)))
        totales.append(total)
    return totales


def describe(nombre: str, t: list[int]) -> None:
    suelo = sum(x == K for x in t) / len(t)
    techo = sum(x == 5 * K for x in t) / len(t)
    cerca = sum(x >= 5 * K - 3 for x in t) / len(t)
    print(f"{nombre:<14} media={statistics.fmean(t):5.1f} DE={statistics.pstdev(t):4.1f} "
          f"asim={momento(t, 3):6.2f} curt={momento(t, 4) - 3:6.2f} "
          f"suelo={suelo:5.1%} techo={techo:5.1%} (techo-3: {cerca:5.1%})")


def main() -> None:
    rng = random.Random(SEMILLA)
    print("Puntaje total de 10 items Likert 1-5 (rango 10-50)")
    print("=" * 100)
    describe("equilibrada", simula(0.0, rng))
    describe("facil (+1.2)", simula(1.2, rng))
    print()
    print("Lectura: la escala facil tiene media alta, asimetria negativa y muchas")
    print("personas pegadas al techo: no distingue entre quienes estan arriba.")
    print("Regla practica citada en la literatura: |asimetria| > 1 o mas de ~15 % en")
    print("suelo/techo sugiere problemas de cobertura; es una alerta, no una norma.")


if __name__ == "__main__":
    main()
