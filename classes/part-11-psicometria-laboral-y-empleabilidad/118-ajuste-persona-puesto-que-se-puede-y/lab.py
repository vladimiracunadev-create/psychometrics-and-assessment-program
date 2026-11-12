"""Laboratorio 118 - "Porcentaje de ajuste": por que no es un numero con significado propio.

Un puesto tiene un perfil objetivo de 8 competencias (escala 1-5). Tres candidatos tienen
perfiles distintos. Se calcula el "ajuste" de tres maneras razonables:
  A. 100 * (1 - distancia euclidiana / distancia maxima),
  B. 100 * porcentaje de competencias que alcanzan el nivel requerido,
  C. 100 * (correlacion entre perfiles + 1)/2.
Los tres indices ordenan a los candidatos de forma distinta y dan "porcentajes" muy diferentes
para la misma persona. Sin un estudio que relacione cada indice con un criterio (desempeno,
permanencia), ninguno es un "porcentaje de exito".
"""
from __future__ import annotations

import math
import statistics

REQUERIDO = [4, 4, 3, 5, 3, 4, 2, 4]
CANDIDATOS = {
    "ana":   [5, 4, 3, 4, 4, 4, 2, 3],
    "beto":  [4, 4, 3, 5, 3, 4, 2, 2],
    "carla": [3, 3, 2, 3, 2, 3, 1, 3],
}


def a(p: list[int]) -> float:
    dist = math.sqrt(sum((x - r) ** 2 for x, r in zip(p, REQUERIDO, strict=True)))
    dmax = math.sqrt(sum(max(r - 1, 5 - r) ** 2 for r in REQUERIDO))
    return 100 * (1 - dist / dmax)


def b(p: list[int]) -> float:
    return 100 * sum(x >= r for x, r in zip(p, REQUERIDO, strict=True)) / len(REQUERIDO)


def c(p: list[int]) -> float:
    return 100 * (statistics.correlation(p, REQUERIDO) + 1) / 2


def main() -> None:
    print(f"{'candidato':<10} {'A: distancia':>13} {'B: % cumple':>12} {'C: correlacion':>15}")
    print("=" * 54)
    filas = {n: (a(p), b(p), c(p)) for n, p in CANDIDATOS.items()}
    for n, v in filas.items():
        print(f"{n:<10} {v[0]:13.0f} {v[1]:12.0f} {v[2]:15.0f}")
    for i, nombre in enumerate(("A", "B", "C")):
        orden = sorted(filas, key=lambda k: -filas[k][i])
        print(f"Orden segun {nombre}: {' > '.join(orden)}")
    print()
    print("Lectura: 'carla' obtiene 60, 0 o 96 puntos de ajuste segun el indice, porque cada uno mide algo")
    print("distinto (distancia, cumplimiento, forma del perfil). Ninguno tiene una interpretacion")
    print("probabilistica sin evidencia de validez: un '85 % de ajuste' no es una probabilidad de exito.")
    print("Lo defendible es mostrar los datos (que competencias se cumplen y con que margen) y")
    print("evitar pesos y porcentajes inventados (clases 031 y 074).")


if __name__ == "__main__":
    main()
