"""Laboratorio 024 - El hexagono de Holland como prediccion falsable.

Holland (1997) ordena R-I-A-S-E-C en un hexagono: las correlaciones deben DECRECER con
la distancia en el circulo (adyacentes > alternos > opuestos). Hay 72 comparaciones de
orden (6 pares a distancia 1 x 6 a distancia 2, 6x3 y 6x3). El indice de satisfaccion de
predicciones (Hubert y Arabie, 1987; Tracey, 2000) es la proporcion que se cumple.
Se evalua sobre (a) datos con estructura circular y (b) datos sin estructura.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 1500
LETRAS = "RIASEC"


def dist(i: int, j: int) -> int:
    d = abs(i - j)
    return min(d, 6 - d)


def predicciones(r: list[list[float]]) -> tuple[int, int]:
    pares = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    cumple = total = 0
    for a in pares:
        for b in pares:
            if dist(*a) < dist(*b):
                total += 1
                cumple += r[a[0]][a[1]] > r[b[0]][b[1]]
    return cumple, total


def matriz(cols: list[list[float]]) -> list[list[float]]:
    return [[1.0 if i == j else statistics.correlation(cols[i], cols[j]) for j in range(6)]
            for i in range(6)]


def main() -> None:
    rng = random.Random(SEMILLA)
    # (a) Circular: cada persona tiene un angulo y una intensidad; el interes por el tipo k
    # depende del coseno entre su angulo y el del tipo.
    cols = [[] for _ in range(6)]
    for _ in range(N):
        ang = rng.uniform(0, 2 * math.pi)
        for k in range(6):
            cols[k].append(math.cos(ang - k * math.pi / 3) + rng.gauss(0, 0.6))
    r = matriz(cols)
    c, t = predicciones(r)
    print("(a) Datos con estructura circular")
    for k, fila in enumerate(r):
        print(f"   {LETRAS[k]} " + " ".join(f"{x:5.2f}" for x in fila))
    print(f"   predicciones cumplidas: {c}/{t} = {c / t:.2f}")

    # (b) Sin estructura: seis intereses independientes.
    c2, t2 = predicciones(matriz([[rng.gauss(0, 1) for _ in range(N)] for _ in range(6)]))
    print(f"(b) Seis variables independientes: {c2}/{t2} = {c2 / t2:.2f} (azar ~0.5)")
    print()
    print("Lectura: el modelo hace una apuesta que los datos pueden desmentir. Un instrumento")
    print("que cumple todas las predicciones respalda la estructura hexagonal en esa muestra;")
    print("no prueba que el hexagono sea 'la' estructura de los intereses en toda poblacion.")


if __name__ == "__main__":
    main()
