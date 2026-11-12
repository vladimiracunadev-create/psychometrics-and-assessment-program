"""Laboratorio 040 - Establecer un punto de corte con Angoff modificado y evaluar su calidad.

12 jueces estiman, para cada uno de 30 items, la probabilidad de que una persona "minimamente
competente" lo acierte. El corte es la suma de las medias de los jueces. Se calcula:
  - el error tipico del corte por la variacion entre jueces,
  - la tasa de aprobados en una poblacion simulada de candidatos,
  - la consistencia de clasificacion (si se rinde una forma paralela, ¿se repite aprobar/reprobar?).
Los items y las estimaciones son sinteticos. Los jueces tienen un sesgo individual de severidad.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
K, JUECES, CANDIDATOS = 30, 12, 8000


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def main() -> None:
    rng = random.Random(SEMILLA)
    b = [rng.gauss(0, 1) for _ in range(K)]
    p_mc = [logistica(1.2 * (0.0 - bj)) for bj in b]      # lo que un MC acierta (theta_MC = 0)
    estimaciones = []
    for _ in range(JUECES):
        sesgo = rng.gauss(0, 0.06)
        estimaciones.append([min(0.99, max(0.05, p + sesgo + rng.gauss(0, 0.08))) for p in p_mc])
    cortes = [sum(e) for e in estimaciones]
    corte = statistics.fmean(cortes)
    ee = statistics.stdev(cortes) / math.sqrt(JUECES)
    print(f"Corte (suma de medias de jueces) = {corte:.1f} de {K}")
    print(f"Error tipico del corte entre jueces = {ee:.2f} puntos (DE entre jueces = {statistics.stdev(cortes):.2f})")

    thetas = [rng.gauss(0.3, 1) for _ in range(CANDIDATOS)]

    def rinde() -> list[int]:
        return [sum(rng.random() < logistica(1.2 * (t - bj)) for bj in b) for t in thetas]

    f1, f2 = rinde(), rinde()
    aprob1 = [x >= corte for x in f1]
    aprob2 = [x >= corte for x in f2]
    consist = sum(a == c for a, c in zip(aprob1, aprob2, strict=True)) / CANDIDATOS
    print(f"Tasa de aprobados (forma 1) = {sum(aprob1) / CANDIDATOS:.3f}")
    print(f"Consistencia de clasificacion entre formas paralelas = {consist:.3f}")
    cerca = sum(abs(x - corte) <= 1.96 * 2.0 for x in f1) / CANDIDATOS
    print(f"Candidatos a menos de ~4 puntos del corte (zona de incertidumbre) = {cerca:.1%}")
    print()
    print("Lectura: el corte no es un hecho: es el resultado de un procedimiento de juicio y tiene")
    print("su propio error. La consistencia de clasificacion muestra cuantas decisiones cambiarian")
    print("con otra forma de la prueba. Una certificacion defendible documenta jueces, procedimiento,")
    print("error del corte y vias de revision.")


if __name__ == "__main__":
    main()
