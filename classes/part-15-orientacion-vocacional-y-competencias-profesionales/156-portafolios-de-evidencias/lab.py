"""Laboratorio 156 - Reglas de decision con un portafolio: caracteristicas de operacion exactas.

Un portafolio tiene n evidencias, cada una "cumple el estandar" con probabilidad p. Una persona
competente cumple con p = 0.80; una no competente, con p = 0.40 (supuestos). La regla "al menos k
de n" tiene sensibilidad P(Bin(n, 0.8) >= k) y especificidad P(Bin(n, 0.4) < k), calculadas
exactamente. Se comparan reglas para distintos n y k, y se calcula el VPP con una prevalencia de
competencia de 70 %. Ensena cuantas evidencias y que regla hacen defendible la decision.
"""
from __future__ import annotations

import math


def cola(n: int, p: float, k: int) -> float:
    return sum(math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k, n + 1))


def main() -> None:
    print(f"{'regla':<14} {'sensibilidad':>13} {'especificidad':>14} {'VPP (prev. 70%)':>16} {'VPN':>6}")
    print("=" * 66)
    for n, k in ((3, 2), (5, 3), (5, 4), (8, 5), (8, 6), (12, 8)):
        sens = cola(n, 0.80, k)
        esp = 1 - cola(n, 0.40, k)
        prev = 0.70
        vpp = sens * prev / (sens * prev + (1 - esp) * (1 - prev))
        vpn = esp * (1 - prev) / (esp * (1 - prev) + (1 - sens) * prev)
        print(f"{f'{k} de {n}':<14} {sens:13.2f} {esp:14.2f} {vpp:16.2f} {vpn:6.2f}")
    print()
    print("Lectura: con 3 evidencias y 'al menos 2', casi la mitad de quienes NO son competentes aprueba.")
    print("Con 8 a 12 evidencias la regla separa mejor, pero cuesta mucho tiempo de producir y evaluar.")
    print("El portafolio ofrece validez de contenido y ecologica, y exige criterios explicitos, evaluadores")
    print("calibrados (clase 143) y autoria verificable. Las probabilidades de este laboratorio son supuestos.")


if __name__ == "__main__":
    main()
