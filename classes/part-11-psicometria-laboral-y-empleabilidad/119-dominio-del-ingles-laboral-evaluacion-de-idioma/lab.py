"""Laboratorio 119 - Clasificar niveles de idioma (A2/B1/B2) desde un test: error de clasificacion.

Prueba de 40 items 2PL. Los niveles corresponden a intervalos de la habilidad theta con cortes
fijados (aqui: A2 < -0.5 <= B1 < 0.7 <= B2; los cortes los fija un panel con un procedimiento de
establecimiento de estandares, clase 075). Se estima theta con EAP y se calcula la matriz de
clasificacion (nivel verdadero vs asignado) y la exactitud, que cae cerca de los cortes.
Los niveles se nombran por analogia con marcos de referencia; este test NO es un examen
oficial ni esta equiparado a un marco.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
K, N = 40, 4000
CORTES = (-0.5, 0.7)
NIVELES = ("A2", "B1", "B2")
GRID = [-4 + 0.1 * i for i in range(81)]
PRIOR = [math.exp(-0.5 * g * g) for g in GRID]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def nivel(t: float) -> int:
    return sum(t >= c for c in CORTES)


def eap(u: list[int], items: list[tuple[float, float]]) -> float:
    num = den = 0.0
    for g, pr in zip(GRID, PRIOR, strict=True):
        w = pr
        for (a, b), x in zip(items, u, strict=True):
            p = logistica(a * (g - b))
            w *= p if x else 1 - p
        num += g * w
        den += w
    return num / den


def main() -> None:
    rng = random.Random(SEMILLA)
    items = [(rng.uniform(0.8, 1.8), rng.uniform(-2.0, 2.0)) for _ in range(K)]
    mat = [[0] * 3 for _ in range(3)]
    for _ in range(N):
        t = rng.gauss(0, 1)
        u = [int(rng.random() < logistica(a * (t - b))) for a, b in items]
        mat[nivel(t)][nivel(eap(u, items))] += 1
    print(f"{'verdadero \\ asignado':>20} " + " ".join(f"{n:>6}" for n in NIVELES) + "   exactitud del nivel")
    for i, fila in enumerate(mat):
        tot = sum(fila)
        print(f"{NIVELES[i]:>20} " + " ".join(f"{v:6d}" for v in fila) + f"   {fila[i] / tot:6.1%}")
    exact = sum(mat[i][i] for i in range(3)) / N
    adyac = sum(mat[i][j] for i in range(3) for j in range(3) if abs(i - j) == 1) / N
    print(f"\nExactitud global = {exact:.1%}; errores a un nivel adyacente = {adyac:.1%}; "
          f"errores a dos niveles = {max(0.0, 1 - exact - adyac):.1%}")
    print()
    print("Lectura: casi todos los errores son a niveles adyacentes y ocurren cerca de los cortes, donde")
    print("el error de medida cruza la frontera. Un nivel de idioma 'B2' es una clasificacion con")
    print("incertidumbre; para decisiones de alto impacto se informa el intervalo, se evalua la")
    print("produccion (hablar, escribir) y no solo la comprension, y se usan examenes con evidencia.")


if __name__ == "__main__":
    main()
