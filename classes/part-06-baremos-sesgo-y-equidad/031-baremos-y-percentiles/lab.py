"""Laboratorio 031 - Baremos: percentiles, puntajes tipificados e incertidumbre del baremo.

1. A partir de una muestra normativa se calcula, para un puntaje bruto, su rango percentil
   (con empates por rango medio), z y T = 50 + 10*z.
2. Los percentiles NO son equidistantes: la misma diferencia de 5 puntos brutos cambia mucho
   el percentil en el centro y poco en las colas.
3. Una norma construida con pocas personas es incierta: se estima por bootstrap el error del
   percentil de un mismo puntaje con muestras normativas de n = 100 y n = 2000.
"""
from __future__ import annotations

import bisect
import random
import statistics

SEMILLA = 20260819
MEDIA, DE = 100.0, 15.0


def rango_percentil(ordenado: list[float], v: float) -> float:
    return 100 * (bisect.bisect_left(ordenado, v) + bisect.bisect_right(ordenado, v)) / 2 / len(ordenado)


def main() -> None:
    rng = random.Random(SEMILLA)
    norma = sorted(round(rng.gauss(MEDIA, DE)) for _ in range(5000))
    m, s = statistics.fmean(norma), statistics.pstdev(norma)
    print(f"Muestra normativa n = {len(norma)}: media = {m:.1f}, DE = {s:.1f}")
    print(f"{'bruto':>6} {'percentil':>10} {'z':>6} {'T':>6}")
    for v in (70, 85, 100, 115, 130):
        z = (v - m) / s
        print(f"{v:6d} {rango_percentil(norma, v):10.1f} {z:6.2f} {50 + 10 * z:6.1f}")

    print("\nMisma diferencia de 5 puntos brutos, distinto salto de percentil:")
    for a, b in ((97, 102), (82, 87), (127, 132)):
        print(f"  {a} -> {b}: percentil {rango_percentil(norma, a):.1f} -> {rango_percentil(norma, b):.1f}"
              f"  (salto {rango_percentil(norma, b) - rango_percentil(norma, a):.1f})")

    print("\nIncertidumbre del baremo: percentil del puntaje bruto 120 (bootstrap de la muestra normativa)")
    for n in (100, 2000):
        base = [round(rng.gauss(MEDIA, DE)) for _ in range(n)]
        estim = []
        for _ in range(300):
            re = sorted(rng.choice(base) for _ in range(n))
            estim.append(rango_percentil(re, 120))
        print(f"  n = {n:5d}: percentil medio = {statistics.fmean(estim):.1f}, error tipico = {statistics.pstdev(estim):.2f}")
    print()
    print("Lectura: el percentil exagera las diferencias en el centro de la distribucion; las")
    print("puntuaciones tipificadas (z, T) las conservan proporcionales. Y un baremo con pocas")
    print("personas tiene su propio error: se informa el tamano de la muestra normativa.")


if __name__ == "__main__":
    main()
