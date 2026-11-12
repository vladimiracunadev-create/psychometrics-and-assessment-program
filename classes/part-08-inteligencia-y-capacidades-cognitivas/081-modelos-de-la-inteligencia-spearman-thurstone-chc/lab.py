"""Laboratorio 081 - Un factor general o varios: las diferencias tetrada de Spearman.

Si UN solo factor general explica las correlaciones entre pruebas, las "diferencias tetrada"
r13*r24 - r14*r23 deben ser ~0 (Spearman, 1904). Se simulan 6 pruebas bajo dos modelos:
  A. un factor general (cargas 0.5-0.8);
  B. dos factores de grupo correlacionados 0.4 (pruebas 1-3 y 4-6).
Se calcula la media del valor absoluto de las tetradas, la proporcion de varianza del primer
componente y el patron de correlaciones (el "manifold positivo": todas positivas).
"""
from __future__ import annotations

import itertools
import math
import random
import statistics

SEMILLA = 20260819
N = 6000


def matriz(cols: list[list[float]]) -> list[list[float]]:
    k = len(cols)
    return [[1.0 if i == j else statistics.correlation(cols[i], cols[j]) for j in range(k)] for i in range(k)]


def tetradas(r: list[list[float]]) -> float:
    valores = []
    for a, b, c, d in itertools.combinations(range(len(r)), 4):
        valores.append(abs(r[a][c] * r[b][d] - r[a][d] * r[b][c]))
        valores.append(abs(r[a][b] * r[c][d] - r[a][d] * r[b][c]))
        valores.append(abs(r[a][b] * r[c][d] - r[a][c] * r[b][d]))
    return statistics.fmean(valores)


def primer_autovalor(r: list[list[float]]) -> float:
    k = len(r)
    v = [1.0] * k
    for _ in range(200):
        w = [sum(r[i][j] * v[j] for j in range(k)) for i in range(k)]
        n = math.sqrt(sum(x * x for x in w))
        v = [x / n for x in w]
    return sum(v[i] * sum(r[i][j] * v[j] for j in range(k)) for i in range(k))


def main() -> None:
    rng = random.Random(SEMILLA)
    g = [rng.gauss(0, 1) for _ in range(N)]
    cargas = [0.5, 0.55, 0.6, 0.7, 0.75, 0.8]
    modelo_a = [[c * x + rng.gauss(0, math.sqrt(1 - c * c)) for x in g] for c in cargas]
    f1 = [rng.gauss(0, 1) for _ in range(N)]
    f2 = [0.4 * a + math.sqrt(1 - 0.16) * rng.gauss(0, 1) for a in f1]
    modelo_b = ([[0.7 * x + rng.gauss(0, 0.714) for x in f1] for _ in range(3)]
                + [[0.7 * x + rng.gauss(0, 0.714) for x in f2] for _ in range(3)])
    print(f"{'modelo':<34} {'|tetrada| media':>16} {'% varianza 1er comp.':>22} {'min r':>7}")
    print("=" * 84)
    for nombre, cols in (("A. un factor general", modelo_a), ("B. dos factores de grupo", modelo_b)):
        r = matriz(cols)
        minimo = min(r[i][j] for i in range(6) for j in range(i + 1, 6))
        print(f"{nombre:<34} {tetradas(r):16.4f} {100 * primer_autovalor(r) / 6:21.1f}% {minimo:7.2f}")
    print()
    print("Lectura: bajo un solo factor las tetradas son ~0; con factores de grupo se alejan de 0.")
    print("Aun asi, en ambos casos todas las correlaciones son positivas y hay un primer componente")
    print("grande: el 'manifold positivo' NO distingue entre un g causal y varias capacidades")
    print("correlacionadas. El modelo CHC (Carroll/Cattell-Horn) organiza capacidades en estratos;")
    print("cual estructura es 'la verdadera' es un debate abierto, no un dato del test.")


if __name__ == "__main__":
    main()
