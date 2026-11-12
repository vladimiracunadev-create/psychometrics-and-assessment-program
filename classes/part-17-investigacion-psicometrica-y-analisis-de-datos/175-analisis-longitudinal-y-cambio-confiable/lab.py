"""Laboratorio 175 - Cambio fiable con efecto de practica.

Una prueba se aplica dos veces. Hay un efecto de practica medio (+3 puntos) sin cambio real en la
habilidad. Se compara el indice de cambio fiable ingenuo (RCI = (X2 - X1)/EEdif), que ignora la
practica, con el RCI corregido por practica ((X2 - X1 - practica)/EEdif), midiendo:
  - el porcentaje de personas sin cambio real clasificadas como "mejoraron",
  - la deteccion de un cambio real de +6 puntos.
EEdif = sqrt(2) * ETM, con DE = 10 y fiabilidad 0.90 (ETM = 3.16, EEdif = 4.47). Parametros supuestos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N, DE, RHO, PRACTICA = 20000, 10.0, 0.90, 3.0
ETM = DE * math.sqrt(1 - RHO)
EEDIF = math.sqrt(2) * ETM


def clasifica(rci: float) -> str:
    return "mejoro" if rci > 1.96 else ("empeoro" if rci < -1.96 else "sin cambio")


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"ETM = {ETM:.2f}; EEdif = {EEDIF:.2f}; umbral de cambio fiable = {1.96 * EEDIF:.2f} puntos")
    print(f"{'condicion':<36} {'RCI ingenuo: mejoro':>20} {'RCI con practica: mejoro':>26}")
    print("=" * 86)
    for nombre, cambio in (("sin cambio real (solo practica)", 0.0), ("cambio real de +6 puntos", 6.0)):
        ing = corr = 0
        for _ in range(N):
            t = rng.gauss(50, DE * math.sqrt(RHO))
            x1 = t + rng.gauss(0, ETM)
            x2 = t + cambio + PRACTICA + rng.gauss(0, ETM)
            ing += clasifica((x2 - x1) / EEDIF) == "mejoro"
            corr += clasifica((x2 - x1 - PRACTICA) / EEDIF) == "mejoro"
        print(f"{nombre:<36} {ing / N:20.1%} {corr / N:26.1%}")
    print()
    print("Lectura: sin corregir la practica, un 10 % de personas SIN cambio real aparece como 'mejoro'")
    print("(el esperado por azar es 2.5 %). El efecto de practica se estima con un grupo de comparacion o")
    print("datos de repeticion y se descuenta. Y 'cambio fiable' no es 'cambio importante' (clase 162).")


if __name__ == "__main__":
    main()
