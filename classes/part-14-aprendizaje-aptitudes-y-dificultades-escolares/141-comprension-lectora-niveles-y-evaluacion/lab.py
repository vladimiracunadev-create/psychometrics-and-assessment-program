"""Laboratorio 141 - Comprension lectora por niveles: jerarquia de dificultad y subpuntajes.

Prueba de 24 items en tres niveles (literal, inferencial, critico), 8 items cada uno, con
dificultad creciente. Se simulan 2 000 estudiantes con una habilidad lectora unica. Se calcula:
  - el porcentaje de aciertos por nivel (la jerarquia de dificultad),
  - la fiabilidad (alfa) del total y de cada subpuntaje de 8 items,
  - la correlacion entre subpuntajes, y la fiabilidad de la DIFERENCIA inferencial - literal.
Muestra por que se informa el total y se cuida la interpretacion de perfiles por nivel.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, POR_NIVEL = 2000, 8
NIVELES = {"literal": -0.8, "inferencial": 0.0, "critico": 0.8}


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def alfa(cols: list[list[int]]) -> float:
    k = len(cols)
    total = [sum(f) for f in zip(*cols, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(c) for c in cols) / statistics.pvariance(total))


def main() -> None:
    rng = random.Random(SEMILLA)
    theta = [rng.gauss(0, 1) for _ in range(N)]
    datos = {}
    for nivel, base in NIVELES.items():
        datos[nivel] = [[int(rng.random() < logistica(1.1 * (t - (base + rng.gauss(0, 0.4))))) for t in theta]
                        for _ in range(POR_NIVEL)]
    print(f"{'nivel':<12} {'% aciertos':>11} {'alfa (8 items)':>15}")
    sub = {}
    for nivel, cols in datos.items():
        sub[nivel] = [sum(f) for f in zip(*cols, strict=True)]
        print(f"{nivel:<12} {statistics.fmean(c for col in cols for c in col):11.1%} {alfa(cols):15.2f}")
    todas = [c for cols in datos.values() for c in cols]
    print(f"{'TOTAL (24)':<12} {statistics.fmean(c for col in todas for c in col):11.1%} {alfa(todas):15.2f}")
    r = statistics.correlation(sub["literal"], sub["inferencial"])
    dif = [a - b for a, b in zip(sub["inferencial"], sub["literal"], strict=True)]
    print(f"\nCorrelacion entre subpuntajes literal-inferencial = {r:.2f}")
    rl, ri = alfa(datos["literal"]), alfa(datos["inferencial"])
    sd_l, sd_i = statistics.pstdev(sub["literal"]), statistics.pstdev(sub["inferencial"])
    rho_dif = (rl * sd_l**2 + ri * sd_i**2 - 2 * r * sd_l * sd_i) / (sd_l**2 + sd_i**2 - 2 * r * sd_l * sd_i)
    print(f"Fiabilidad de la diferencia (inferencial - literal) = {rho_dif:.2f}")
    print()
    print("Lectura: la jerarquia de dificultad se reproduce (literal > inferencial > critico), pero los")
    print("niveles no son habilidades separables: correlacionan alto y la diferencia entre ellos casi no")
    print("tiene fiabilidad. Se informa el total y, si se informa por nivel, con cautela. El nivel de")
    print("dificultad tambien depende del texto (clase 084) y del conocimiento previo del lector.")


if __name__ == "__main__":
    main()
