"""Laboratorio 114 - Errores del evaluador: halo, indulgencia y efecto del evaluador.

Cada empleado tiene un desempeno verdadero en 4 dimensiones (correlacion 0.2 entre si). Cada
supervisor evalua a 10 empleados con: (a) sesgo de indulgencia (suma constante al evaluador),
(b) efecto halo (parte de la impresion general contamina todas las dimensiones). Se calcula:
  - el efecto halo observado = correlacion media entre dimensiones (la verdadera es 0.2),
  - la proporcion de varianza de las evaluaciones atribuible al evaluador (CCI(1) por supervisor),
  - el cambio en ambos tras un "entrenamiento" que reduce indulgencia y halo a la mitad.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
SUP, POR_SUP, DIM = 80, 10, 4


def evalua(halo: float, indulgencia_sd: float, rng: random.Random):
    filas, grupos = [], []
    for s in range(SUP):
        ind = rng.gauss(0, indulgencia_sd)
        for _ in range(POR_SUP):
            g = rng.gauss(0, 1)
            verd = [math.sqrt(0.2) * g + math.sqrt(0.8) * rng.gauss(0, 1) for _ in range(DIM)]
            impresion = statistics.fmean(verd) + rng.gauss(0, 0.3)
            filas.append([v + halo * impresion + ind + rng.gauss(0, 0.5) for v in verd])
            grupos.append(s)
    return filas, grupos


def halo_obs(filas) -> float:
    cols = list(zip(*filas, strict=True))
    return statistics.fmean(statistics.correlation(cols[i], cols[j])
                            for i in range(DIM) for j in range(i + 1, DIM))


def varianza_evaluador(filas, grupos) -> float:
    total = [statistics.fmean(f) for f in filas]
    por_sup = [total[i * POR_SUP:(i + 1) * POR_SUP] for i in range(SUP)]
    mg = statistics.fmean(total)
    msb = POR_SUP * sum((statistics.fmean(g) - mg) ** 2 for g in por_sup) / (SUP - 1)
    msw = sum((v - statistics.fmean(g)) ** 2 for g in por_sup for v in g) / (SUP * (POR_SUP - 1))
    entre = max(0.0, (msb - msw) / POR_SUP)
    return entre / (entre + msw)


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'condicion':<28} {'correl. media entre dim.':>25} {'% varianza del evaluador':>26}")
    print("=" * 82)
    for nombre, halo, ind in (("sin errores", 0.0, 0.0), ("halo e indulgencia", 1.0, 0.8),
                              ("tras entrenamiento (mitad)", 0.5, 0.4)):
        filas, grupos = evalua(halo, ind, rng)
        print(f"{nombre:<28} {halo_obs(filas):25.2f} {varianza_evaluador(filas, grupos):26.1%}")
    print()
    print("Lectura: la correlacion entre dimensiones sin errores es ~0.15; con halo parece 0.64 y las")
    print("'dimensiones' dejan de ser distinguibles. Y una gran parte de la varianza se explica por QUIEN")
    print("evalua. Rubricas con anclas conductuales, entrenamiento, varios evaluadores y calibracion")
    print("reducen esos errores; no los eliminan. Un criterio de desempeno tambien tiene fiabilidad.")


if __name__ == "__main__":
    main()
