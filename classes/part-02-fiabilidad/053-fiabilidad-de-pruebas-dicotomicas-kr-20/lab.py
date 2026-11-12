"""Laboratorio 053 - KR-20 en pruebas de acierto/error.

    KR-20 = k/(k-1) * (1 - suma(p_i * q_i) / var_total)      q = 1 - p

Es el alfa de Cronbach aplicado a items 0/1 (con varianza poblacional). Se
comprueba la igualdad numerica y se muestra el efecto de la dificultad: una prueba
con items de dificultad muy heterogenea o extrema rinde menos fiabilidad que una
de dificultad media con el mismo numero de items.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 4000
K = 20


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def simula(dificultades: list[float], rng: random.Random) -> list[list[int]]:
    thetas = [rng.gauss(0, 1) for _ in range(N)]
    return [[int(rng.random() < logistica(1.2 * (t - b))) for t in thetas] for b in dificultades]


def kr20(items: list[list[int]]) -> float:
    k = len(items)
    pq = sum(statistics.fmean(i) * (1 - statistics.fmean(i)) for i in items)
    total = [sum(f) for f in zip(*items, strict=True)]
    return k / (k - 1) * (1 - pq / statistics.pvariance(total))


def alfa(items: list[list[int]]) -> float:
    k = len(items)
    total = [sum(f) for f in zip(*items, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(i) for i in items) / statistics.pvariance(total))


def main() -> None:
    rng = random.Random(SEMILLA)
    casos = {
        "dificultad media (b=0 en los 20)": [0.0] * K,
        "dispersa (b de -2 a 2)": [-2 + 4 * i / (K - 1) for i in range(K)],
        "toda facil (b=-2.5)": [-2.5] * K,
    }
    print(f"{'prueba de 20 items':<36} {'p media':>8} {'KR-20':>7} {'alfa':>7}")
    print("=" * 64)
    for nombre, bs in casos.items():
        items = simula(bs, rng)
        pm = statistics.fmean(statistics.fmean(i) for i in items)
        print(f"{nombre:<36} {pm:8.2f} {kr20(items):7.3f} {alfa(items):7.3f}")
    print()
    print("Lectura: KR-20 y alfa coinciden (mismo calculo). La prueba toda facil rinde")
    print("menos: con p cercana a 1 los items casi no tienen varianza que covariar.")
    print("KR-21 (que asume igual dificultad) subestima cuando la dificultad es dispersa.")


if __name__ == "__main__":
    main()
