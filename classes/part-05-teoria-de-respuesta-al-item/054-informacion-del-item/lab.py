"""Laboratorio 054 - Funcion de informacion: donde mide bien cada item.

Para el modelo 2PL:  I(theta) = a^2 * P(theta) * (1 - P(theta))
El error tipico de estimacion de theta es  1 / sqrt(I_test(theta)),  y la informacion del
test es la SUMA de las informaciones de sus items. La informacion de un item es maxima en
theta = b y crece con a^2.
"""
from __future__ import annotations

import math

ITEMS = {"A (a=0.6, b=-2)": (0.6, -2.0), "B (a=1.0, b=0)": (1.0, 0.0),
         "C (a=2.0, b=0)": (2.0, 0.0), "D (a=1.5, b=1.5)": (1.5, 1.5), "E (a=2.0, b=-1)": (2.0, -1.0)}
THETAS = (-3, -2, -1, 0, 1, 2, 3)


def info(t: float, a: float, b: float) -> float:
    p = 1 / (1 + math.exp(-a * (t - b)))
    return a * a * p * (1 - p)


def main() -> None:
    print(f"{'item':<18}" + "".join(f"{t:7d}" for t in THETAS))
    print("=" * 67)
    for nombre, (a, b) in ITEMS.items():
        print(f"{nombre:<18}" + "".join(f"{info(t, a, b):7.2f}" for t in THETAS))
    total = [sum(info(t, a, b) for a, b in ITEMS.values()) for t in THETAS]
    print(f"{'TEST (suma)':<18}" + "".join(f"{x:7.2f}" for x in total))
    print(f"{'error tipico':<18}" + "".join(f"{1 / math.sqrt(x):7.2f}" for x in total))
    mejor0 = max(ITEMS, key=lambda k: info(0, *ITEMS[k]))
    print(f"\nItem mas informativo en theta = 0: {mejor0}")
    print()
    print("Lectura: C (a=2) aporta 4 veces la informacion de B (a=1) en su zona; A casi no aporta")
    print("en ninguna parte. La precision de un test NO es una cifra unica (como el alfa): es una")
    print("curva. Este test mide mejor entre -1 y 1 y peor en los extremos, y eso se decide al")
    print("elegir items, no al interpretar puntajes.")


if __name__ == "__main__":
    main()
