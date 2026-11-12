"""Laboratorio 030 - Intervalos de confianza para el puntaje de UNA persona.

Dos construcciones, con puntaje observado X, media M, fiabilidad rho y DE s:
  (a) alrededor del observado:  X +/- 1.96 * ETM,         ETM = s*sqrt(1-rho)
  (b) alrededor del verdadero estimado:
        T_est = M + rho*(X - M),   error = s*sqrt(rho*(1-rho)),  T_est +/- 1.96*error
La (a) cubre 95 % en el conjunto de la poblacion, pero se queda corta para quienes
puntuan en los extremos. La (b) cubre ~95 % TAMBIEN condicionada al puntaje observado.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 200000
M, S, RHO = 100.0, 15.0, 0.80
Z = 1.96


def main() -> None:
    rng = random.Random(SEMILLA)
    etm = S * math.sqrt(1 - RHO)
    est = S * math.sqrt(RHO * (1 - RHO))
    datos = []
    for _ in range(N):
        t = rng.gauss(M, S * math.sqrt(RHO))
        datos.append((t + rng.gauss(0, etm), t))

    print(f"M={M}, DE={S}, fiabilidad={RHO}: ETM={etm:.2f}, error del verdadero estimado={est:.2f}")
    print("=" * 74)
    print(f"{'puntaje observado':<22} {'n':>7} {'cobertura (a)':>14} {'cobertura (b)':>14}")
    for nombre, lo, hi in (("todos", 0, 999), ("120 o mas", 120, 999), ("130 o mas", 130, 999),
                           ("85 a 115", 85, 115), ("70 o menos", 0, 70)):
        sub = [(x, t) for x, t in datos if lo <= x <= hi]
        a = sum(abs(x - t) <= Z * etm for x, t in sub) / len(sub)
        b = sum(abs(M + RHO * (x - M) - t) <= Z * est for x, t in sub) / len(sub)
        print(f"{nombre:<22} {len(sub):7d} {a:14.3f} {b:14.3f}")
    print()
    print("Lectura: el intervalo centrado en lo observado cubre ~95 % en promedio, pero")
    print("pierde cobertura justo donde las decisiones pesan (puntajes extremos), por la")
    print("regresion a la media. El intervalo sobre el verdadero estimado la mantiene.")
    print("Con fiabilidad alta la diferencia es chica; con fiabilidad baja, importa.")


if __name__ == "__main__":
    main()
