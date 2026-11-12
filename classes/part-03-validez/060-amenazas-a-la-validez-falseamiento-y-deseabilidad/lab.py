"""Laboratorio 060 - Falseamiento: que pasa en la cola alta cuando una parte se "mejora".

Escala de autoinforme de responsabilidad. El 25 % de los postulantes falsea: suma un
desplazamiento d al puntaje, con variacion individual. Se calcula, para una seleccion del
10 % superior, que fraccion son falseadores y cuanto cae la validez frente al desempeno.
El falseamiento se modela como desplazamiento aditivo: es una simplificacion.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 50000
R_VERDADERA = 0.30
PREVALENCIA = 0.25


def main() -> None:
    print(f"{'desplaz. medio':>14} {'falseadores en top 10%':>24} {'r con desempeno':>16}")
    print("=" * 58)
    for d in (0.0, 0.5, 1.0, 1.5):
        rng = random.Random(SEMILLA)
        hab, rend, falsea = [], [], []
        for _ in range(N):
            t = rng.gauss(0, 1)
            f = rng.random() < PREVALENCIA
            obs = t + rng.gauss(0, 0.5) + (rng.gauss(d, 0.3) if f else 0.0)
            hab.append(obs)
            rend.append(R_VERDADERA * t + math.sqrt(1 - R_VERDADERA**2) * rng.gauss(0, 1))
            falsea.append(f)
        corte = sorted(hab)[int(0.90 * N)]
        top = [f for h, f in zip(hab, falsea, strict=True) if h >= corte]
        print(f"{d:14.1f} {sum(top) / len(top):24.1%} {statistics.correlation(hab, rend):16.3f}")
    print()
    print("Lectura: con prevalencia de 25 %, un desplazamiento de 1.0 DE hace que los")
    print("falseadores ocupen buena parte del tramo superior y la validez caiga. Escalas de")
    print("validez, formatos de eleccion forzada y metodos de otro tipo ayudan, pero ninguno")
    print("elimina el problema (Ziegler et al., 2012); hay que declararlo como limite.")


if __name__ == "__main__":
    main()
