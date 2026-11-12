"""Laboratorio 166 - Informar satisfaccion: media, porcentaje favorable y su incertidumbre.

Encuesta con item 1-5. Para cada unidad (curso, equipo) se reporta el porcentaje "favorable"
(respuestas 4 y 5) y su intervalo de Wilson al 95 %. Se simulan 30 unidades con distinto tamano y
la MISMA satisfaccion real. Se muestra cuantas unidades quedan "en lo mas alto" o "en lo mas bajo"
solo por azar de muestreo, y como el intervalo de Wilson evita conclusiones con pocos respondentes.
Datos sinteticos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
P_REAL = 0.62
UNIDADES = [8, 10, 12, 15, 20, 25, 30, 40, 60, 100] * 3


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    den = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / den
    mitad = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return centro - mitad, centro + mitad


def main() -> None:
    rng = random.Random(SEMILLA)
    filas = []
    for n in UNIDADES:
        k = sum(rng.random() < P_REAL for _ in range(n))
        lo, hi = wilson(k, n)
        filas.append((n, k / n, lo, hi))
    filas.sort(key=lambda f: -f[1])
    print(f"Satisfaccion REAL igual en las 30 unidades: {P_REAL:.0%} favorable")
    print(f"{'puesto':>6} {'n':>4} {'% favorable':>12} {'IC 95 % de Wilson':>22}")
    for i, (n, p, lo, hi) in list(enumerate(filas, 1))[:4] + list(enumerate(filas, 1))[-3:]:
        print(f"{i:6d} {n:4d} {p:12.0%} {f'[{lo:.0%}, {hi:.0%}]':>22}")
    pequenas_arriba = sum(1 for n, *_ in filas[:6] if n <= 15)
    pequenas_abajo = sum(1 for n, *_ in filas[-6:] if n <= 15)
    significativas = sum(1 for _, _, lo, hi in filas if lo > P_REAL or hi < P_REAL)
    print(f"\nEntre las 6 unidades de arriba, {pequenas_arriba} tienen n <= 15; entre las 6 de abajo, {pequenas_abajo}.")
    print(f"Unidades cuyo intervalo EXCLUYE el valor real {P_REAL:.0%}: {significativas} de 30")
    print()
    print("Lectura: los extremos del ranking los ocupan las unidades pequenas por pura variacion. El intervalo")
    print("de Wilson muestra que los intervalos de unidades pequenas son tan anchos que no permiten")
    print("rankear. Se reportan intervalos, se suprime lo que no cumple un minimo de respuestas (clase 128) y")
    print("se evita comparar unidades como si la diferencia fuera real. La satisfaccion no es desempeno.")


if __name__ == "__main__":
    main()
