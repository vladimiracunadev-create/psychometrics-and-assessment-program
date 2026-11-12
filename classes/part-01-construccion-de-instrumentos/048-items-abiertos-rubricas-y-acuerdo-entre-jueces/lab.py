"""Laboratorio 048 - Rubricas y acuerdo entre jueces: efecto de la severidad y del entrenamiento.

400 respuestas abiertas con calidad verdadera (nivel 0-3 de una rubrica de 4 niveles) son calificadas
por dos jueces. Se comparan dos condiciones:
  - SIN entrenamiento: cada juez tiene una severidad propia (+/- 0.5 niveles) y mas ruido.
  - CON entrenamiento (anclas y calibracion): severidad y ruido menores.
Indicadores: acuerdo exacto, acuerdo adyacente, kappa ponderado cuadratico y diferencia media entre
jueces (sesgo de severidad). Datos sinteticos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, NIV = 400, 4


def califica(verdadero: float, severidad: float, ruido: float, rng: random.Random) -> int:
    return min(NIV - 1, max(0, round(verdadero + severidad + rng.gauss(0, ruido))))


def kappa_cuad(a: list[int], b: list[int]) -> float:
    n = len(a)
    obs = [[0.0] * NIV for _ in range(NIV)]
    for x, y in zip(a, b, strict=True):
        obs[x][y] += 1 / n
    pa = [sum(obs[i]) for i in range(NIV)]
    pb = [sum(obs[i][j] for i in range(NIV)) for j in range(NIV)]
    w = lambda i, j: ((i - j) / (NIV - 1)) ** 2          # noqa: E731
    num = sum(w(i, j) * obs[i][j] for i in range(NIV) for j in range(NIV))
    den = sum(w(i, j) * pa[i] * pb[j] for i in range(NIV) for j in range(NIV))
    return 1 - num / den


def main() -> None:
    rng = random.Random(SEMILLA)
    verdad = [min(NIV - 1.0, max(0.0, rng.gauss(1.5, 0.9))) for _ in range(N)]
    print(f"{'condicion':<24} {'exacto':>7} {'adyacente':>10} {'kappa pond.':>12} {'dif. media J2-J1':>17}")
    print("=" * 76)
    for nombre, sev, ruido in (("sin entrenamiento", (-0.4, 0.4), 0.55), ("con entrenamiento", (-0.05, 0.05), 0.30)):
        j1 = [califica(v, sev[0], ruido, rng) for v in verdad]
        j2 = [califica(v, sev[1], ruido, rng) for v in verdad]
        exacto = sum(a == b for a, b in zip(j1, j2, strict=True)) / N
        ady = sum(abs(a - b) <= 1 for a, b in zip(j1, j2, strict=True)) / N
        dif = statistics.fmean(b - a for a, b in zip(j1, j2, strict=True))
        print(f"{nombre:<24} {exacto:7.2f} {ady:10.2f} {kappa_cuad(j1, j2):12.2f} {dif:+17.2f}")
    print()
    print("Lectura: el acuerdo adyacente puede ser alto aun cuando el exacto es bajo, por eso se informa mas de un")
    print("indicador. La diferencia media revela que un juez es sistematicamente mas severo, algo que el kappa")
    print("ponderado no descompone. El entrenamiento con anclas y la calibracion periodica reducen ambos errores;")
    print("tambien la rubrica (descriptores observables por nivel). Datos sinteticos.")


if __name__ == "__main__":
    main()
