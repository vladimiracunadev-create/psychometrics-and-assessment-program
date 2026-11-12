"""Laboratorio 100 - Por que un resultado "bajo" no es un hallazgo: tasas base y bateria.

Parte 1: valor predictivo positivo (VPP) de un cribado con sensibilidad 0.85 y especificidad
0.90 segun la prevalencia del problema: con prevalencia baja, la mayoria de los positivos son
falsos positivos (teorema de Bayes).
Parte 2: en una bateria de 10 pruebas independientes con puntaje normal, ¿cuantas personas
sanas muestran al menos un resultado bajo (< -1.5 DE) por puro azar? Se calcula y se simula.
"""
from __future__ import annotations

import random
from statistics import NormalDist

SEMILLA = 20260819
ND = NormalDist()


def vpp(sens: float, esp: float, prev: float) -> float:
    return sens * prev / (sens * prev + (1 - esp) * (1 - prev))


def main() -> None:
    print("Parte 1 - VPP de un cribado (sensibilidad 0.85, especificidad 0.90)")
    print(f"{'prevalencia':>12} {'VPP':>7} {'por cada 100 positivos, falsos':>32}")
    for prev in (0.01, 0.05, 0.10, 0.30):
        v = vpp(0.85, 0.90, prev)
        print(f"{prev:12.0%} {v:7.1%} {100 * (1 - v):32.0f}")

    p_bajo = ND.cdf(-1.5)
    print(f"\nParte 2 - bateria de 10 pruebas independientes; P(puntaje < -1.5 DE) = {p_bajo:.3f} por prueba")
    teorico = 1 - (1 - p_bajo) ** 10
    rng = random.Random(SEMILLA)
    sim = sum(any(rng.gauss(0, 1) < -1.5 for _ in range(10)) for _ in range(50000)) / 50000
    print(f"  P(al menos un puntaje bajo) teorico = {teorico:.3f}; simulado = {sim:.3f}")
    print("  (con pruebas correlacionadas la cifra baja, pero sigue siendo alta)")
    print()
    print("Lectura: una evaluacion neuropsicologica no clinica (cribado, investigacion, escuela) no")
    print("diagnostica. Un puntaje bajo aislado es esperable por azar, y la probabilidad de que un")
    print("positivo sea real depende de la prevalencia. Los hallazgos se interpretan en conjunto, con")
    print("historia clinica y derivacion a un profesional habilitado (parte 16).")


if __name__ == "__main__":
    main()
