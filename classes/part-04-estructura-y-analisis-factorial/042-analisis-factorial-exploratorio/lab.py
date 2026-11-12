"""Laboratorio 042 - Cuantos factores retener: regla de Kaiser frente a analisis paralelo.

12 items con DOS factores verdaderos (6 items cada uno, cargas 0.6, factores
independientes). Se comparan:
  - regla de Kaiser (autovalores > 1),
  - analisis paralelo de Horn: se retienen los autovalores que superan el percentil 95
    de autovalores de datos aleatorios con el mismo n y numero de variables.
Despues se extraen las cargas de 2 factores por componentes principales (aproximacion
a la solucion factorial; para AFE con ejes principales ver la clase 046).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, P, REPS = 400, 12, 40


def jacobi(a: list[list[float]], tol: float = 1e-9) -> tuple[list[float], list[list[float]]]:
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


def matriz_r(cols: list[list[float]]) -> list[list[float]]:
    k = len(cols)
    r = [[1.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            r[i][j] = r[j][i] = statistics.correlation(cols[i], cols[j])
    return r


def autovalores(cols: list[list[float]]) -> list[float]:
    return sorted(jacobi(matriz_r(cols))[0], reverse=True)


def main() -> None:
    rng = random.Random(SEMILLA)
    f1 = [rng.gauss(0, 1) for _ in range(N)]
    f2 = [rng.gauss(0, 1) for _ in range(N)]
    cols = ([[0.6 * f + rng.gauss(0, 0.8) for f in f1] for _ in range(6)]
            + [[0.6 * f + rng.gauss(0, 0.8) for f in f2] for _ in range(6)])
    obs = autovalores(cols)
    aleatorios = [autovalores([[rng.gauss(0, 1) for _ in range(N)] for _ in range(P)])
                  for _ in range(REPS)]
    p95 = [sorted(a[i] for a in aleatorios)[int(0.95 * REPS) - 1] for i in range(P)]

    print(f"{'#':>2} {'autovalor':>10} {'azar p95':>9}  Kaiser  Paralelo")
    print("=" * 46)
    for i in range(6):
        print(f"{i + 1:2d} {obs[i]:10.2f} {p95[i]:9.2f}  {'si' if obs[i] > 1 else 'no':>6}"
              f"  {'si' if obs[i] > p95[i] else 'no':>8}")
    print(f"\nKaiser retiene {sum(x > 1 for x in obs)} | "
          f"analisis paralelo retiene {sum(o > a for o, a in zip(obs, p95, strict=True))} "
          "(verdad: 2)")

    vals, vec = jacobi(matriz_r(cols))
    orden = sorted(range(P), key=lambda i: -vals[i])[:2]
    print("\nCargas (componentes, sin rotar) - items 1-6 = factor 1, items 7-12 = factor 2")
    for i in range(P):
        print(f"  item {i + 1:2d}: " + "  ".join(f"{vec[i][o] * math.sqrt(vals[o]):6.2f}" for o in orden))
    print("\nLectura: sin rotar, las cargas mezclan los factores (cada item carga en ambos).")
    print("La rotacion (clase 046) es lo que hace interpretable la solucion; la retencion se")
    print("decide con evidencia convergente (paralelo, teoria, interpretabilidad), no con una regla.")


if __name__ == "__main__":
    main()
