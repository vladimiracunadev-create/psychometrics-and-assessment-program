"""Laboratorio 088 - Perfiles de aptitudes: cuando una diferencia entre subpruebas es real.

Cinco aptitudes (verbal, espacial, razonamiento, numerica, fluidez) tipo Thurstone, con
correlaciones verdaderas de 0.4 entre ellas y fiabilidad 0.85 cada una. Para una persona con
perfil observado dado, la diferencia entre dos subpruebas es "fiable" solo si supera el error
tipico de la diferencia:
    EE_dif = DE * sqrt(2 - rho_a - rho_b)        (puntajes estandar, DE = 15)
Se muestra la proporcion de personas SIN diferencias reales cuyo perfil igual muestra al menos
una diferencia de 10+ puntos entre subpruebas (por azar de medida).
"""
from __future__ import annotations

import itertools
import math
import random

SEMILLA = 20260819
N, RHO, DE, K = 20000, 0.85, 15.0, 5


def main() -> None:
    ee_dif = DE * math.sqrt(2 - 2 * RHO)
    umbral = 1.96 * ee_dif
    print(f"Error tipico de la diferencia entre dos subpruebas = {ee_dif:.2f} puntos")
    print(f"Diferencia minima 'fiable' al 95 % = {umbral:.1f} puntos")
    rng = random.Random(SEMILLA)
    plano = sin_dif = 0
    for _ in range(N):
        verdadero = rng.gauss(100, DE * math.sqrt(RHO))      # persona con perfil PLANO verdadero
        obs = [verdadero + rng.gauss(0, DE * math.sqrt(1 - RHO)) for _ in range(K)]
        dmax = max(abs(a - b) for a, b in itertools.combinations(obs, 2))
        plano += dmax >= 10
        sin_dif += dmax >= umbral
    print(f"\nPersonas con perfil verdaderamente plano ({N}):")
    print(f"  con alguna diferencia observada >= 10 puntos : {plano / N:.1%}")
    print(f"  con alguna diferencia > umbral fiable ({umbral:.1f})    : {sin_dif / N:.1%}")
    print(f"  comparaciones por persona (pares de subpruebas): {K * (K - 1) // 2}")
    print()
    print("Lectura: con cinco subpruebas hay 10 comparaciones por persona; sin correccion, lo normal")
    print("es encontrar 'fortalezas y debilidades' en perfiles que son planos. Un perfil se interpreta")
    print("con diferencias fiables y de forma acotada; interpretaciones de perfil (ipsativas) tienen")
    print("evidencia de validez incremental limitada y deben tratarse como hipotesis.")


if __name__ == "__main__":
    main()
