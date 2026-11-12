"""Laboratorio 104 - Estabilidad del "estilo dominante" en un modelo de 4 estilos.

Cuatro escalas (tipo DISC; el instrumento comercial no se reproduce) con puntajes normativos
independientes y fiabilidad test-retest r. Se pregunta: ¿con que frecuencia coincide el estilo
DOMINANTE (la escala mas alta) entre dos aplicaciones? El azar da 25 %. Tambien se calcula
cuantas personas tienen una diferencia entre la 1.a y la 2.a escala menor que el error de
medida (estilo dominante no distinguible).
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 20000
K = 4


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'fiab. de cada escala':>20} {'mismo estilo dominante':>24} {'1.o vs 2.o no distinguibles':>29}")
    print("=" * 76)
    for rho in (0.6, 0.7, 0.8, 0.9):
        sd_e = math.sqrt((1 - rho) / rho)
        igual = indist = 0
        for _ in range(N):
            t = [rng.gauss(0, 1) for _ in range(K)]
            a = [x + rng.gauss(0, sd_e) for x in t]
            b = [x + rng.gauss(0, sd_e) for x in t]
            igual += a.index(max(a)) == b.index(max(b))
            ordenado = sorted(a, reverse=True)
            indist += (ordenado[0] - ordenado[1]) < 1.96 * sd_e * math.sqrt(2) * math.sqrt(rho)
        print(f"{rho:20.1f} {igual / N:24.1%} {indist / N:29.1%}")
    print()
    print("Lectura: aun con escalas de fiabilidad 0.8, el estilo dominante coincide en apenas dos de")
    print("cada tres aplicaciones, y para muchas personas la diferencia entre el primer y el segundo")
    print("estilo es menor que el error. Rotular a alguien con UN estilo sobreafirma. Ademas el formato")
    print("ipsativo (clase 013) distorsiona las comparaciones entre personas.")


if __name__ == "__main__":
    main()
