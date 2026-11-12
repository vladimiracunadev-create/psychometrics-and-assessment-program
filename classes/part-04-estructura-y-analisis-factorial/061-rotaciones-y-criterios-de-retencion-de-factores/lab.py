"""Laboratorio 061 - Rotacion varimax: la misma solucion, mas interpretable.

Se parte de las cargas de 2 componentes (solucion sin rotar) de 8 items con estructura
simple verdadera (items 1-4 en el factor 1, items 5-8 en el factor 2). Se rota con varimax
de dos factores (angulo de Kaiser, 1958). Se comprueba que la rotacion NO cambia lo que el
modelo explica (comunalidades y varianza total) y que si cambia la interpretabilidad.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 1500


def jacobi(a: list[list[float]], tol: float = 1e-10):
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


def varimax2(carga: list[list[float]]) -> tuple[list[list[float]], float]:
    """Angulo de varimax para dos factores (maximiza la varianza de las cargas al cuadrado)."""
    x = [c[0] for c in carga]
    y = [c[1] for c in carga]
    u = [a * a - b * b for a, b in zip(x, y, strict=True)]
    w = [2 * a * b for a, b in zip(x, y, strict=True)]
    p = len(x)
    num = 2 * (p * sum(a * b for a, b in zip(u, w, strict=True)) - sum(u) * sum(w))
    den = p * sum(a * a - b * b for a, b in zip(u, w, strict=True)) - (sum(u) ** 2 - sum(w) ** 2)
    ang = 0.25 * math.atan2(num, den)
    c, s = math.cos(ang), math.sin(ang)
    return [[a * c + b * s, -a * s + b * c] for a, b in zip(x, y, strict=True)], ang


def main() -> None:
    rng = random.Random(SEMILLA)
    f1 = [rng.gauss(0, 1) for _ in range(N)]
    f2 = [rng.gauss(0, 1) for _ in range(N)]
    cols = ([[0.7 * f + rng.gauss(0, 0.71) for f in f1] for _ in range(4)]
            + [[0.7 * f + rng.gauss(0, 0.71) for f in f2] for _ in range(4)])
    k = len(cols)
    r = [[1.0 if i == j else statistics.correlation(cols[i], cols[j]) for j in range(k)] for i in range(k)]
    vals, vec = jacobi(r)
    top = sorted(range(k), key=lambda i: -vals[i])[:2]
    sin_rotar = [[vec[i][t] * math.sqrt(vals[t]) for t in top] for i in range(k)]
    rotada, ang = varimax2(sin_rotar)
    print(f"{'item':>4} | {'sin rotar':^15} | {'varimax':^15}")
    for i in range(k):
        a, b = sin_rotar[i], rotada[i]
        print(f"{i + 1:4d} | {a[0]:7.2f} {a[1]:7.2f} | {b[0]:7.2f} {b[1]:7.2f}")
    com0 = sum(x * x for c in sin_rotar for x in c)
    com1 = sum(x * x for c in rotada for x in c)
    print(f"\nAngulo de rotacion = {math.degrees(ang):.1f} grados")
    print(f"Varianza explicada total: sin rotar = {com0:.3f}, rotada = {com1:.3f} (identica)")
    print()
    print("Lectura: la rotacion redistribuye la varianza entre factores, no crea ni destruye")
    print("ajuste. Tras rotar, cada item carga en un factor (estructura simple). Existen rotaciones")
    print("oblicuas (oblimin, promax) que permiten factores correlacionados: si el constructo lo")
    print("sugiere, forzar ortogonalidad con varimax es una decision con costo.")


if __name__ == "__main__":
    main()
