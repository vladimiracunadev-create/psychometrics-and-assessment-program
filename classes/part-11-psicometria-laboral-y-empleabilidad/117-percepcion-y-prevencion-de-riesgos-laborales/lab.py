"""Laboratorio 117 - Evaluar percepcion de riesgos: deteccion de peligros y el problema del criterio.

Parte 1: prueba de deteccion de peligros en 40 imagenes (50 % con peligro). Cada trabajador
tiene sensibilidad d' y criterio c; se calcula d' (separa capacidad de cautela).
Parte 2: validar contra ACCIDENTES es dificil porque son eventos raros. Con tasa media de 0.05
accidentes por trabajador-ano (Poisson) y un efecto real moderado del rasgo, se estima la
potencia para detectar la correlacion en N = 200 y N = 2 000 trabajadores, y se compara con un
criterio proximal (conductas seguras observadas) que es mas frecuente y fiable.
"""
from __future__ import annotations

import math
import random
import statistics
from statistics import NormalDist

SEMILLA = 20260819
ND = NormalDist()


def poisson(lam: float, rng: random.Random) -> int:
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def main() -> None:
    rng = random.Random(SEMILLA)
    ds = []
    for _ in range(200):
        dprime, c = rng.gauss(1.5, 0.5), rng.gauss(0.0, 0.3)
        h = fa = 0
        for _ in range(20):
            h += rng.gauss(dprime, 1) > dprime / 2 + c
            fa += rng.gauss(0, 1) > dprime / 2 + c
        ds.append(ND.inv_cdf((h + 0.5) / 21) - ND.inv_cdf((fa + 0.5) / 21))
    print(f"Parte 1 - d' estimado por trabajador (20 + 20 imagenes): media = {statistics.fmean(ds):.2f}, "
          f"DE = {statistics.pstdev(ds):.2f} (la DE verdadera de d' es 0.5)")

    print("\nParte 2 - potencia de la correlacion test-accidentes (efecto real moderado)")
    print(f"{'N':>6} {'r con accidentes':>17} {'r con conductas seguras':>25} {'detecta (p<.05) acc.':>22}")
    for n in (200, 2000):
        detect = 0
        rs_acc, rs_con = [], []
        for _ in range(60):
            t = [rng.gauss(0, 1) for _ in range(n)]
            acc = [poisson(0.05 * math.exp(-0.35 * x), rng) for x in t]
            con = [0.45 * x + rng.gauss(0, 0.9) for x in t]
            r = statistics.correlation(t, [float(a) for a in acc])
            rs_acc.append(r)
            rs_con.append(statistics.correlation(t, con))
            z = abs(r) * math.sqrt(n - 3)
            detect += z > 1.96
        print(f"{n:6d} {statistics.fmean(rs_acc):17.3f} {statistics.fmean(rs_con):25.3f} {detect / 60:22.0%}")
    print()
    print("Lectura: con eventos raros, la correlacion con accidentes es minuscula y exige miles de")
    print("trabajadores para detectarse; las conductas seguras observadas son un criterio proximal mas")
    print("util. Tambien es una advertencia contra culpar al trabajador: la prevencion se apoya en el")
    print("sistema (peligros, procedimientos, supervision) y la evaluacion individual es un componente.")


if __name__ == "__main__":
    main()
