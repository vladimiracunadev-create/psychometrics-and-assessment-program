"""Laboratorio 134 - Observacion sistematica: cuanto tiempo observar y como acordar.

Cada nino tiene una tasa propia de una conducta (eventos por hora, Poisson). Dos observadores
registran la conducta durante T minutos. Se calcula, segun T:
  - la correlacion entre dos sesiones independientes (fiabilidad de la tasa observada),
  - el acuerdo entre observadores con registro de intervalos de 10 s: porcentaje de acuerdo, kappa
    y acuerdo en la ocurrencia (excluyendo intervalos en que ambos registran ausencia).
Es un modelo; un procedimiento real define la conducta de forma operacional y entrena observadores.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 400


def poisson(lam: float, rng: random.Random) -> int:
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def main() -> None:
    rng = random.Random(SEMILLA)
    tasas = [max(0.2, rng.gauss(6.0, 3.0)) for _ in range(N)]            # eventos por hora
    print(f"{'minutos observados':>19} {'fiabilidad entre sesiones':>26}")
    for t in (5, 15, 30, 60, 120):
        a = [poisson(r * t / 60, rng) for r in tasas]
        b = [poisson(r * t / 60, rng) for r in tasas]
        print(f"{t:19d} {statistics.correlation(a, b):26.2f}")

    # Acuerdo entre observadores por intervalos (180 intervalos de 10 s = 30 min).
    n_int, p_ocurre, p_error = 180, 0.12, 0.07
    ac = oc = ko = 0.0
    reps = 300
    for _ in range(reps):
        verdad = [rng.random() < p_ocurre for _ in range(n_int)]
        o1 = [v != (rng.random() < p_error) for v in verdad]
        o2 = [v != (rng.random() < p_error) for v in verdad]
        po = sum(x == y for x, y in zip(o1, o2, strict=True)) / n_int
        p1, p2 = sum(o1) / n_int, sum(o2) / n_int
        pe = p1 * p2 + (1 - p1) * (1 - p2)
        ambos = sum(x and y for x, y in zip(o1, o2, strict=True))
        alguno = sum(x or y for x, y in zip(o1, o2, strict=True))
        ac += po
        ko += (po - pe) / (1 - pe)
        oc += ambos / alguno if alguno else 1.0
    print(f"\nAcuerdo entre observadores (30 min, intervalos de 10 s, conducta en 12 % de los intervalos):")
    print(f"  acuerdo total = {ac / reps:.2f}; kappa = {ko / reps:.2f}; acuerdo en la ocurrencia = {oc / reps:.2f}")
    print()
    print("Lectura: 5 minutos de observacion no bastan para ordenar a los ninos; hace falta mas tiempo o")
    print("mas sesiones. Con conductas poco frecuentes, el acuerdo total es enganosamente alto (muchos")
    print("intervalos 'sin conducta'): se informa kappa o el acuerdo en la ocurrencia. Un registro")
    print("anecdotico complementa, pero no reemplaza, un registro sistematico con definiciones operacionales.")


if __name__ == "__main__":
    main()
