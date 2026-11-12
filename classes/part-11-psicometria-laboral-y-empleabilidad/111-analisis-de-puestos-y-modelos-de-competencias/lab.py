"""Laboratorio 111 - Analisis de puestos: criticidad de tareas y fiabilidad de los evaluadores.

8 especialistas califican 12 tareas de un puesto en importancia (1-5) y frecuencia (1-5). La
criticidad = importancia x frecuencia. Se calcula:
  - la fiabilidad del promedio de evaluadores, CCI(3,k) = (MSR - MSE)/MSR (ANOVA de dos factores),
  - el ranking de tareas por criticidad, y cuales entran al modelo de competencias (criticidad
    media >= 12, umbral del laboratorio),
  - cuanto cambia el ranking al usar solo 3 de los 8 evaluadores.
Datos sinteticos; el puesto es hipotetico.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
TAREAS, EVAL = 12, 8


def cci_k(m: list[list[float]]) -> float:
    n, k = len(m), len(m[0])
    gm = statistics.fmean(v for f in m for v in f)
    mf = [statistics.fmean(f) for f in m]
    mc = [statistics.fmean(m[i][j] for i in range(n)) for j in range(k)]
    msr = k * sum((x - gm) ** 2 for x in mf) / (n - 1)
    sse = sum((m[i][j] - mf[i] - mc[j] + gm) ** 2 for i in range(n) for j in range(k))
    mse = sse / ((n - 1) * (k - 1))
    return (msr - mse) / msr


def clip(x: float) -> float:
    return max(1.0, min(5.0, x))


def main() -> None:
    rng = random.Random(SEMILLA)
    imp_v = [rng.uniform(1.5, 5.0) for _ in range(TAREAS)]
    frec_v = [rng.uniform(1.5, 5.0) for _ in range(TAREAS)]
    imp = [[clip(round(v + rng.gauss(0, 0.7))) for _ in range(EVAL)] for v in imp_v]
    frec = [[clip(round(v + rng.gauss(0, 0.7))) for _ in range(EVAL)] for v in frec_v]
    crit = [[i * f for i, f in zip(ri, rf, strict=True)] for ri, rf in zip(imp, frec, strict=True)]
    print(f"CCI(3,k) del promedio de {EVAL} evaluadores:  importancia = {cci_k(imp):.2f},  "
          f"frecuencia = {cci_k(frec):.2f},  criticidad = {cci_k(crit):.2f}")
    medias = [statistics.fmean(f) for f in crit]
    orden = sorted(range(TAREAS), key=lambda i: -medias[i])
    print(f"\n{'tarea':>6} {'criticidad media':>17}  entra al modelo (>= 12)")
    for i in orden[:6]:
        print(f"{i + 1:6d} {medias[i]:17.1f}  {'si' if medias[i] >= 12 else 'no'}")
    print("  ...")
    sub = [statistics.fmean(f[:3]) for f in crit]
    orden3 = sorted(range(TAREAS), key=lambda i: -sub[i])
    print(f"\nTop-4 con 8 evaluadores: {[i + 1 for i in orden[:4]]}; con solo 3: {[i + 1 for i in orden3[:4]]}")
    print(f"Tareas que entran al modelo: {sum(m >= 12 for m in medias)} de {TAREAS}")
    print()
    print("Lectura: con 8 evaluadores el promedio es fiable; con 3 cambia el orden del ranking. Un modelo de")
    print("competencias nace de un analisis del puesto documentado y reproducible: quien lo evaluo,")
    print("cuanto acuerdo hubo y que umbral se uso. 'Competencias' sin ese respaldo son opinion.")


if __name__ == "__main__":
    main()
