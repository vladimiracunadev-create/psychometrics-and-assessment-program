"""Laboratorio 063 - Bifactor: omega total, omega jerarquico y ECV.

Estructura verdadera conocida: 9 items, un factor GENERAL (carga 0.5) y tres factores de
grupo de 3 items (carga especifica 0.5). Con las cargas verdaderas se calculan:
    omega total        = (varianza general + varianza de grupo) / varianza del total
    omega jerarquico   = varianza atribuible al factor general / varianza del total
    ECV                = varianza comun explicada por el general / varianza comun total
Un omega total alto puede coexistir con un omega jerarquico moderado: el puntaje total no
mide solo el factor general. (Rodriguez, Reise y Haviland, 2016.)
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 20000
G, S = 0.5, 0.5          # cargas general y especifica de cada item
GRUPOS, POR_GRUPO = 3, 3


def indices(g: float, s: float) -> tuple[float, float, float]:
    k = GRUPOS * POR_GRUPO
    var_gen = (k * g) ** 2
    var_esp = GRUPOS * (POR_GRUPO * s) ** 2
    var_unica = k * (1 - g * g - s * s)
    total = var_gen + var_esp + var_unica
    omega_t = (var_gen + var_esp) / total
    omega_h = var_gen / total
    ecv = (k * g * g) / (k * g * g + k * s * s)
    return omega_t, omega_h, ecv


def main() -> None:
    print(f"{'general':>8} {'especif.':>9} {'omega total':>12} {'omega jerarq.':>14} {'ECV':>6}")
    print("=" * 56)
    for g, s in ((0.7, 0.2), (0.5, 0.5), (0.3, 0.6)):
        ot, oh, ecv = indices(g, s)
        print(f"{g:8.1f} {s:9.1f} {ot:12.3f} {oh:14.3f} {ecv:6.3f}")

    # Comprobacion por simulacion del caso (0.5, 0.5): correlacion del total con el factor general.
    rng = random.Random(SEMILLA)
    gen = [rng.gauss(0, 1) for _ in range(N)]
    esp = [[rng.gauss(0, 1) for _ in range(N)] for _ in range(GRUPOS)]
    total = []
    for i in range(N):
        t = 0.0
        for gr in range(GRUPOS):
            for _ in range(POR_GRUPO):
                t += G * gen[i] + S * esp[gr][i] + rng.gauss(0, math.sqrt(1 - G * G - S * S))
        total.append(t)
    r = statistics.correlation(total, gen)
    print(f"\nSimulacion (0.5, 0.5): r(puntaje total, factor general) = {r:.3f}; r^2 = {r * r:.3f}")
    print("(coincide con el omega jerarquico del caso 0.5/0.5)")
    print()
    print("Lectura: en el caso 0.5/0.5 la escala es fiable (omega total 0.86) pero solo ~64 %")
    print("de la varianza del total es el factor general (ECV = 0.50). Interpretar el total como 'el rasgo")
    print("general' exige omega jerarquico y ECV altos; si no, hay que reportar subpuntajes.")


if __name__ == "__main__":
    main()
