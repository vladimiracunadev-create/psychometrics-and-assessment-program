"""Laboratorio 195 - Proyecto: informe agregado para una organizacion (supresion y intervalos).

Una encuesta de clima sintetica (item de 5 opciones) se resume por equipo como porcentaje de
respuestas favorables (4-5) con intervalo de Wilson al 95 %. Reglas de proteccion:
  - n < 5 por equipo: el resultado se SUPRIME (podria identificar a personas),
  - tampoco se publican diferencias entre equipos cuyos intervalos se solapan,
  - se evita la supresion complementaria (derivar un equipo pequeno por resta).
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
MIN_N = 5


def wilson(x: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = x / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def main() -> None:
    rng = random.Random(SEMILLA)
    equipos = {"Operaciones": (48, 0.62), "Comercial": (31, 0.58), "Finanzas": (14, 0.71), "TI": (9, 0.44), "Legal": (3, 0.67)}
    datos = {}
    for eq, (n, p) in equipos.items():
        datos[eq] = (n, sum(rng.random() < p for _ in range(n)))
    print(f"{'equipo':<14} {'n':>4} {'favorables':>11}  {'IC 95 % (Wilson)':<20} publicacion")
    print("=" * 78)
    publicados = {}
    for eq, (n, x) in datos.items():
        if n < MIN_N:
            print(f"{eq:<14} {n:4d} {'-':>11}  {'-':<20} SUPRIMIDO (n < {MIN_N})")
            continue
        lo, hi = wilson(x, n)
        publicados[eq] = (lo, hi)
        print(f"{eq:<14} {n:4d} {x / n:11.0%}  [{lo:.0%}, {hi:.0%}]{'':<8} publicado")
    nombres = list(publicados)
    print("\nComparaciones entre equipos (solo si los intervalos NO se solapan):")
    hubo = False
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            if publicados[a][0] > publicados[b][1] or publicados[b][0] > publicados[a][1]:
                print(f"  {a} y {b}: diferencia sustentada por los intervalos")
                hubo = True
    if not hubo:
        print("  ninguna: los intervalos se solapan, no se afirma diferencia entre equipos")
    print()
    print("Lectura: con pocas personas los intervalos son amplios: un porcentaje puntual no autoriza a decir que un")
    print("equipo 'esta peor': solo cuentan las diferencias con intervalos separados, y aun asi son descriptivas. La supresion con n minimo protege la identidad; el informe explica el criterio. El")
    print("clima es una percepcion colectiva, no un diagnostico de las personas ni una evaluacion de quien lidera.")


if __name__ == "__main__":
    main()
