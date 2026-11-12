"""Laboratorio 009 - Longitud del test: Spearman-Brown frente a simulacion.

Cada item = puntaje verdadero T + error. La fiabilidad de un item (su correlacion
con otro item paralelo) es r1. La formula de Spearman-Brown predice la fiabilidad de
una escala de k items; aqui se contrasta con el alfa de Cronbach simulado.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 4000
VARIANZA_ERROR = 3.0          # r1 = 1 / (1 + 3) = 0.25
R1 = 1 / (1 + VARIANZA_ERROR)


def alfa(items: list[list[float]]) -> float:
    k = len(items)
    suma_var = sum(statistics.pvariance(i) for i in items)
    total = [sum(col) for col in zip(*items, strict=True)]
    return k / (k - 1) * (1 - suma_var / statistics.pvariance(total))


def spearman_brown(r1: float, k: int) -> float:
    return k * r1 / (1 + (k - 1) * r1)


def longitud_para(objetivo: float, r1: float) -> float:
    """k necesario para alcanzar `objetivo` (formula inversa)."""
    return objetivo * (1 - r1) / (r1 * (1 - objetivo))


def main() -> None:
    rng = random.Random(SEMILLA)
    verdadero = [rng.gauss(0, 1) for _ in range(N)]
    banco = [[t + rng.gauss(0, VARIANZA_ERROR ** 0.5) for t in verdadero] for _ in range(40)]
    print(f"Fiabilidad por item r1 = {R1:.2f}")
    print("=" * 52)
    print(f"{'k items':>8} {'Spearman-Brown':>15} {'alfa simulado':>14}")
    prev = 0.0
    for k in (2, 5, 10, 20, 40):
        sb, a = spearman_brown(R1, k), alfa(banco[:k])
        print(f"{k:8d} {sb:15.3f} {a:14.3f}   (+{sb - prev:.3f})")
        prev = sb
    print()
    for obj in (0.80, 0.90):
        print(f"Items necesarios para fiabilidad {obj:.2f}: {longitud_para(obj, R1):.0f}")
    print()
    print("Lectura: los rendimientos decrecen. Pasar de 20 a 40 items agrega poca")
    print("fiabilidad pero duplica el cansancio y el abandono del evaluado.")


if __name__ == "__main__":
    main()
