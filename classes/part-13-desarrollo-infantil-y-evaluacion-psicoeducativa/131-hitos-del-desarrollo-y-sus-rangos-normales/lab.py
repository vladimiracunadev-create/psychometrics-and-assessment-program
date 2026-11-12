"""Laboratorio 131 - Hitos del desarrollo: variabilidad normal y listas de verificacion.

Edades de logro de un hito (en meses) siguen una distribucion log-normal asimetrica. Se
calcula, para un hito simulado (caminar solo, mediana 12 meses, parametros ilustrativos):
  - la "ventana normal" (percentiles 1-99), mas ancha de lo que se suele imaginar;
  - la proporcion de ninos sanos que aun no lo logran a una edad dada;
  - con una lista de 10 hitos independientes, la proporcion de ninos tipicos con AL MENOS un
    hito "atrasado" respecto del percentil 95 (el azar de las listas).
Valores ilustrativos: los rangos reales dependen del hito, la poblacion y la fuente (p. ej. WHO
Multicentre Growth Reference Study, 2006).
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 100000
MU, SIGMA = math.log(12.0), 0.15


def cuantil(xs: list[float], q: float) -> float:
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def main() -> None:
    rng = random.Random(SEMILLA)
    edades = sorted(math.exp(rng.gauss(MU, SIGMA)) for _ in range(N))
    print("Edad de logro de un hito (meses), distribucion simulada")
    for q in (0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99):
        print(f"  percentil {int(q * 100):2d}: {cuantil(edades, q):5.1f}")
    print("\nNinos sanos que AUN no lo logran a cada edad:")
    for m in (12, 14, 16, 18):
        print(f"  a los {m} meses: {sum(e > m for e in edades) / N:6.1%}")
    p95 = cuantil(edades, 0.95)
    print("\nLista de 10 hitos independientes; 'atraso' = por sobre el percentil 95 (p = 5 % cada uno)")
    n_atraso = [sum(rng.random() < 0.05 for _ in range(10)) for _ in range(20000)]
    print(f"  ninos tipicos con al menos un hito 'atrasado': {sum(x >= 1 for x in n_atraso) / 20000:.1%}")
    print(f"  con dos o mas: {sum(x >= 2 for x in n_atraso) / 20000:.1%}")
    print(f"  (percentil 95 del hito simulado = {p95:.1f} meses)")
    print()
    print("Lectura: la variacion normal es amplia y asimetrica (cola hacia la derecha). Un solo hito")
    print("fuera del rango es esperable en 4 de cada 10 ninos tipicos al revisar 10: se interpreta el")
    print("patron global, la trayectoria y el contexto, y se deriva segun un protocolo, no por un item.")


if __name__ == "__main__":
    main()
