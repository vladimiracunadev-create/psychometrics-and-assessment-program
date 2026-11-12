"""Laboratorio 021 - Que se puede leer en una matriz de correlaciones.

Seis items: tres miden el factor A y tres el factor B (factores correlacionados 0.3).
Se muestra la estructura en bloques, los autovalores (metodo de Jacobi, sin librerias)
y dos comprobaciones previas a cualquier analisis factorial: determinante y KMO global.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 2000


def jacobi(a: list[list[float]], tol: float = 1e-10) -> tuple[list[float], list[list[float]]]:
    n = len(a)
    a = [r[:] for r in a]
    v = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(100 * n * n):
        p = q = 0
        m = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > m:
                    m, p, q = abs(a[i][j]), i, j
        if m < tol:
            break
        th = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(th), math.sin(th)
        for k in range(n):
            a[k][p], a[k][q] = c * a[k][p] - s * a[k][q], s * a[k][p] + c * a[k][q]
        for k in range(n):
            a[p][k], a[q][k] = c * a[p][k] - s * a[q][k], s * a[p][k] + c * a[q][k]
            v[k][p], v[k][q] = c * v[k][p] - s * v[k][q], s * v[k][p] + c * v[k][q]
    return [a[i][i] for i in range(n)], v


def inversa(m: list[list[float]]) -> list[list[float]]:
    n = len(m)
    a = [r[:] + [float(i == j) for j in range(n)] for i, r in enumerate(m)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[piv] = a[piv], a[i]
        d = a[i][i]
        a[i] = [x / d for x in a[i]]
        for r in range(n):
            if r != i:
                f = a[r][i]
                a[r] = [x - f * y for x, y in zip(a[r], a[i], strict=True)]
    return [r[n:] for r in a]


def kmo(r: list[list[float]]) -> float:
    inv = inversa(r)
    n = len(r)
    parcial = [[-inv[i][j] / math.sqrt(inv[i][i] * inv[j][j]) for j in range(n)] for i in range(n)]
    num = sum(r[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
    den = num + sum(parcial[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
    return num / den


def determinante(m: list[list[float]]) -> float:
    a = [r[:] for r in m]
    n, det = len(a), 1.0
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(a[r][i]))
        if abs(a[piv][i]) < 1e-14:
            return 0.0
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            det = -det
        det *= a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            a[r] = [x - f * y for x, y in zip(a[r], a[i], strict=True)]
    return det


def main() -> None:
    rng = random.Random(SEMILLA)
    fa = [rng.gauss(0, 1) for _ in range(N)]
    fb = [0.3 * a + math.sqrt(1 - 0.09) * rng.gauss(0, 1) for a in fa]
    cols = ([[0.7 * a + rng.gauss(0, 0.714) for a in fa] for _ in range(3)]
            + [[0.7 * b + rng.gauss(0, 0.714) for b in fb] for _ in range(3)])
    k = len(cols)
    r = [[1.0 if i == j else statistics.correlation(cols[i], cols[j]) for j in range(k)]
         for i in range(k)]
    print("Matriz de correlaciones (items 1-3: factor A; items 4-6: factor B)")
    for fila in r:
        print("  " + " ".join(f"{x:6.2f}" for x in fila))
    dentro = [r[i][j] for i in range(k) for j in range(i + 1, k) if (i < 3) == (j < 3)]
    entre = [r[i][j] for i in range(3) for j in range(3, 6)]
    print(f"\nCorrelacion media dentro de bloque = {statistics.fmean(dentro):.3f}")
    print(f"Correlacion media entre bloques    = {statistics.fmean(entre):.3f}")
    vals, _ = jacobi(r)
    print("Autovalores:", " ".join(f"{x:.2f}" for x in sorted(vals, reverse=True)),
          f"(suma = {sum(vals):.2f} = n de items)")
    print(f"Determinante = {determinante(r):.3f}   KMO global = {kmo(r):.3f}")
    print()
    print("Lectura: los bloques y el primer autovalor dominante delatan que hay estructura;")
    print("un KMO cercano a 0 sugiere que la matriz no tiene correlaciones compartidas que")
    print("factorizar. Un determinante ~0 senala multicolinealidad (items casi duplicados).")


if __name__ == "__main__":
    main()
