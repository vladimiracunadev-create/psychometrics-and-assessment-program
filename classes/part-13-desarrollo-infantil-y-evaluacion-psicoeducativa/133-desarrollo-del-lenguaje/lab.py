"""Laboratorio 133 - Vocabulario temprano: variabilidad, percentiles y "hablantes tardios".

Vocabulario expresivo a los 24 meses: distribucion asimetrica y muy variable entre ninos. Se
define "hablante tardio" como percentil < 10 a los 24 meses. Con una correlacion entre las
mediciones de 24 y 36 meses de 0.5 (supuesto del laboratorio), se estima cuantos hablantes
tardios siguen bajo el percentil 10 a los 36 meses y cuantos 'alcanzan' al grupo, y que
parte de eso es regresion a la media sin intervencion alguna.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, RHO = 50000, 0.5


def pctl(xs: list[float], q: float) -> float:
    return sorted(xs)[int(q * len(xs))]


def main() -> None:
    rng = random.Random(SEMILLA)
    z24 = [rng.gauss(0, 1) for _ in range(N)]
    z36 = [RHO * a + math.sqrt(1 - RHO**2) * rng.gauss(0, 1) for a in z24]
    v24 = [math.exp(4.6 + 0.8 * z) for z in z24]            # palabras (log-normal)
    print("Vocabulario expresivo a los 24 meses (palabras)")
    for q in (0.10, 0.25, 0.50, 0.75, 0.90):
        print(f"  percentil {int(q * 100):2d}: {pctl(v24, q):6.0f}")
    c24, c36 = pctl(z24, 0.10), pctl(z36, 0.10)
    tardios = [i for i in range(N) if z24[i] < c24]
    siguen = sum(z36[i] < c36 for i in tardios) / len(tardios)
    medio = statistics.fmean(z36[i] for i in tardios)
    medio24 = statistics.fmean(z24[i] for i in tardios)
    print(f"\nHablantes tardios a los 24 meses: {len(tardios) / N:.0%} (z medio = {medio24:.2f})")
    print(f"  siguen bajo el percentil 10 a los 36 meses: {siguen:.1%}")
    print(f"  z medio a los 36 meses: {medio:.2f} (regresion a la media sin intervencion)")
    print(f"Predictivo inverso: de quienes estan bajo el P10 a los 36, solo "
          f"{sum(z24[i] < c24 for i in range(N) if z36[i] < c36) / sum(z36[i] < c36 for i in range(N)):.1%} lo estaba a los 24")
    print()
    print("Lectura: con estabilidad moderada, la mayoria de los 'tardios' de 24 meses se acerca al promedio")
    print("sin intervencion: evaluar una vez es insuficiente para predecir. La decision de apoyar se basa")
    print("en la evaluacion global (comprension, gestos, juego), la trayectoria y el contexto bilingue o")
    print("familiar, y no en un percentil aislado. Los baremos deben corresponder a la lengua y poblacion.")


if __name__ == "__main__":
    main()
