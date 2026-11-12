"""Laboratorio 161 - Un item o una escala: validez y tamano de muestra.

Satisfaccion con la vida medida con (a) UN item (fiabilidad test-retest supuesta 0.60) y (b) una
escala de 5 items (alfa 0.85). Ambos reflejan el mismo constructo y se relacionan con un criterio
externo (por ejemplo, salud percibida) con r verdadera = 0.40 a nivel de constructo. Se calcula:
  - el coeficiente observado con cada medida (atenuado por la fiabilidad),
  - el tamano de muestra para detectar esa relacion con 80 % de potencia,
  - el efecto techo (porcentaje en los dos valores mas altos) con la distribucion simulada.
Parametros supuestos.
"""
from __future__ import annotations

import math
import random
import statistics
from statistics import NormalDist

SEMILLA = 20260819
N = 20000
ND = NormalDist()


def n_para(r: float, potencia: float = 0.80, alfa: float = 0.05) -> int:
    z = ND.inv_cdf(1 - alfa / 2) + ND.inv_cdf(potencia)
    return math.ceil((z / math.atanh(r)) ** 2 + 3)


def main() -> None:
    rng = random.Random(SEMILLA)
    verdadero = [rng.gauss(0, 1) for _ in range(N)]
    criterio = [0.40 * v + math.sqrt(1 - 0.16) * rng.gauss(0, 1) for v in verdadero]
    print(f"{'medida':<22} {'fiabilidad':>10} {'r observada':>12} {'r esperada':>11} {'n (80 % potencia)':>19}")
    print("=" * 80)
    for nombre, rel in (("1 item", 0.60), ("escala de 5 items", 0.85)):
        sd = math.sqrt((1 - rel) / rel)
        medida = [v + rng.gauss(0, sd) for v in verdadero]
        r = statistics.correlation(medida, criterio)
        print(f"{nombre:<22} {rel:10.2f} {r:12.3f} {0.40 * math.sqrt(rel):11.3f} {n_para(r):19d}")
    # Efecto techo de un item 1-7 sesgado hacia lo alto
    items = [min(7, max(1, round(5.2 + 1.3 * v))) for v in verdadero]
    techo = sum(x >= 6 for x in items) / N
    print(f"\nEfecto techo en un item 1-7 (media simulada alta): {techo:.1%} responde 6 o 7")
    print()
    print("Lectura: un solo item pierde validez observada por su menor fiabilidad y exige mas personas para")
    print("detectar la misma relacion, pero sirve para estudios con muchas personas y poco tiempo. En un")
    print("individuo, un item no es suficiente para ninguna decision. El bienestar es multidimensional:")
    print("una escala de satisfaccion no mide salud mental ni calidad de vida en sentido amplio.")


if __name__ == "__main__":
    main()
