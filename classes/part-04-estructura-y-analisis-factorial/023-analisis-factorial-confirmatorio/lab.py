"""Laboratorio 023 - Ajuste de un modelo: la logica del residuo (sin motor SEM).

NO es un AFC con maxima verosimilitud: es la idea central en miniatura. Se ajusta un
modelo de UN factor por ejes principales iterativos y se mide el desajuste con el
SRMR (raiz del promedio de residuos cuadrados entre la matriz observada y la que
implica el modelo). Se aplica a datos generados por 1 factor (el modelo es correcto) y
por 2 factores (el modelo esta mal especificado). Regla orientativa de la literatura:
SRMR < 0.08 (Hu y Bentler, 1999) - un indicio, no un veredicto.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 1000, 8


def matriz_r(cols: list[list[float]]) -> list[list[float]]:
    k = len(cols)
    r = [[1.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            r[i][j] = r[j][i] = statistics.correlation(cols[i], cols[j])
    return r


def un_factor(r: list[list[float]], iteraciones: int = 200) -> list[float]:
    """Ejes principales de un factor: iteracion de comunalidades (potencia sobre R reducida)."""
    k = len(r)
    h = [max(abs(r[i][j]) for j in range(k) if j != i) for i in range(k)]
    carga = [math.sqrt(x) for x in h]
    for _ in range(iteraciones):
        red = [[(h[i] if i == j else r[i][j]) for j in range(k)] for i in range(k)]
        v = [1.0] * k
        for _ in range(60):
            w = [sum(red[i][j] * v[j] for j in range(k)) for i in range(k)]
            nrm = math.sqrt(sum(x * x for x in w))
            v = [x / nrm for x in w]
        lam = sum(v[i] * sum(red[i][j] * v[j] for j in range(k)) for i in range(k))
        carga = [abs(x) * math.sqrt(max(lam, 0)) for x in v]
        h = [min(c * c, 0.995) for c in carga]
    return carga


def srmr(r: list[list[float]], carga: list[float]) -> float:
    k = len(r)
    res = [(r[i][j] - carga[i] * carga[j]) ** 2 for i in range(k) for j in range(i)]
    return math.sqrt(sum(res) / len(res))


def datos(dos_factores: bool, rng: random.Random) -> list[list[float]]:
    f1 = [rng.gauss(0, 1) for _ in range(N)]
    f2 = [rng.gauss(0, 1) for _ in range(N)]
    cols = []
    for i in range(K):
        f = f2 if (dos_factores and i >= K // 2) else f1
        cols.append([0.65 * a + rng.gauss(0, 0.76) for a in f])
    return cols


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'datos generados por':<26} {'SRMR (modelo de 1 factor)':>26}")
    print("=" * 54)
    for etiqueta, dos in (("1 factor (modelo correcto)", False), ("2 factores (mal especificado)", True)):
        r = matriz_r(datos(dos, rng))
        print(f"{etiqueta:<30} {srmr(r, un_factor(r)):22.3f}")
    print()
    print("Lectura: el residuo delata la mala especificacion. Un AFC real usa maxima")
    print("verosimilitud, chi-cuadrado e indices (clase 062) y, sobre todo, un modelo")
    print("fijado ANTES de ver los datos: reajustarlo hasta que ajuste vuelve el AFC exploratorio.")


if __name__ == "__main__":
    main()
