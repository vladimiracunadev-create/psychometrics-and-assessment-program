"""Laboratorio 057 - Informacion del test y "fiabilidad condicional".

Dos pruebas de 20 items 2PL (a = 1.2):
  - AMPLIA: dificultades repartidas de -2.5 a 2.5;
  - CONCENTRADA: dificultades entre -0.5 y 0.5.
Se tabula informacion y error tipico por nivel de theta, y la fiabilidad condicional
aproximada rho(theta) = I / (I + 1) (para theta con varianza 1). Una prueba puede ser muy
precisa en el centro y mala en las colas, aunque su "alfa" global parezca excelente.
"""
from __future__ import annotations

import math

THETAS = (-3, -2, -1, 0, 1, 2, 3)
A = 1.2


def banco(lo: float, hi: float, n: int = 20) -> list[float]:
    return [lo + (hi - lo) * i / (n - 1) for i in range(n)]


def info_test(t: float, bs: list[float]) -> float:
    total = 0.0
    for b in bs:
        p = 1 / (1 + math.exp(-A * (t - b)))
        total += A * A * p * (1 - p)
    return total


def main() -> None:
    pruebas = {"AMPLIA (-2.5..2.5)": banco(-2.5, 2.5), "CONCENTRADA (-0.5..0.5)": banco(-0.5, 0.5)}
    for nombre, bs in pruebas.items():
        print(nombre)
        print(f"  {'theta':<14}" + "".join(f"{t:7d}" for t in THETAS))
        infos = [info_test(t, bs) for t in THETAS]
        print(f"  {'informacion':<14}" + "".join(f"{x:7.2f}" for x in infos))
        print(f"  {'error tipico':<14}" + "".join(f"{1 / math.sqrt(x):7.2f}" for x in infos))
        print(f"  {'fiab. cond.':<14}" + "".join(f"{x / (x + 1):7.2f}" for x in infos))
        print()
    print("Lectura: la CONCENTRADA es la mas precisa en el centro (fiab. condicional 0.87) pero")
    print("cae a 0.44 en |theta| = 3, donde la AMPLIA conserva 0.64. Para un cribado con punto")
    print("de corte hay que concentrar la informacion donde esta el corte; para describir toda la")
    print("poblacion, hay que repartirla. La curva, no una cifra, guia ese diseno.")


if __name__ == "__main__":
    main()
