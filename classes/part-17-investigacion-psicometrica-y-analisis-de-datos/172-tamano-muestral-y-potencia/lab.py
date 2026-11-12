"""Laboratorio 172 - Cuanta muestra hace falta para estimar bien las cargas de un factor.

Se simula un factor con 10 items (cargas verdaderas 0.4 a 0.8). Para cada tamano de muestra se
estima el modelo de un factor por ejes principales sobre la matriz de correlaciones de muestra y se
calcula el error cuadratico medio (RMSE) de las cargas respecto de las verdaderas, y el porcentaje
de replicas en que alguna carga se subestima en mas de 0.15. Tambien el SRMR de la matriz muestral.
Muestra por que las "reglas" de N minimo dependen de la fuerza de las cargas.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
CARGAS = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.8]
REPS = 40


def matriz_r(cols: list[list[float]]) -> list[list[float]]:
    k = len(cols)
    r = [[1.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            r[i][j] = r[j][i] = statistics.correlation(cols[i], cols[j])
    return r


def un_factor(r: list[list[float]]) -> list[float]:
    k = len(r)
    h = [max(abs(r[i][j]) for j in range(k) if j != i) for i in range(k)]
    carga = [math.sqrt(x) for x in h]
    for _ in range(100):
        red = [[(h[i] if i == j else r[i][j]) for j in range(k)] for i in range(k)]
        v = [1.0] * k
        for _ in range(50):
            w = [sum(red[i][j] * v[j] for j in range(k)) for i in range(k)]
            n = math.sqrt(sum(x * x for x in w))
            v = [x / n for x in w]
        lam = sum(v[i] * sum(red[i][j] * v[j] for j in range(k)) for i in range(k))
        carga = [abs(x) * math.sqrt(max(lam, 0)) for x in v]
        h = [min(c * c, 0.995) for c in carga]
    return carga


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'N':>6} {'RMSE de las cargas':>19} {'subestima alguna > 0.15':>25} {'SRMR muestral':>14}")
    print("=" * 70)
    for n in (50, 100, 200, 500, 1000):
        rmses, malas, srmrs = [], 0, []
        for _ in range(REPS):
            f = [rng.gauss(0, 1) for _ in range(n)]
            cols = [[c * x + rng.gauss(0, math.sqrt(1 - c * c)) for x in f] for c in CARGAS]
            r = matriz_r(cols)
            est = un_factor(r)
            err = [e - c for e, c in zip(est, CARGAS, strict=True)]
            rmses.append(math.sqrt(statistics.fmean(e * e for e in err)))
            malas += any(e < -0.15 for e in err)
            verd = [[CARGAS[i] * CARGAS[j] for j in range(10)] for i in range(10)]
            srmrs.append(math.sqrt(statistics.fmean((r[i][j] - verd[i][j]) ** 2 for i in range(10) for j in range(i))))
        print(f"{n:6d} {statistics.fmean(rmses):19.3f} {malas / REPS:25.0%} {statistics.fmean(srmrs):14.3f}")
    print()
    print("Lectura: con N = 50 las cargas se estiman con un error comparable a su diferencia entre items; la")
    print("precision mejora con la raiz de N, no linealmente. Las reglas del tipo 'N >= 200' son heuristicas:")
    print("con cargas altas y pocos factores bastan menos casos; con cargas bajas, muchos mas. El calculo")
    print("para tu estudio se hace por simulacion con tus supuestos (clase 173).")


if __name__ == "__main__":
    main()
