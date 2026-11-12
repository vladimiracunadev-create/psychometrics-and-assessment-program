"""Laboratorio 153 - Comparaciones por pares: escalar valores con Bradley-Terry.

Seis valores laborales (autonomia, seguridad, ingreso, servicio, prestigio, equilibrio). Cada
persona compara los 15 pares y elige cual valora mas. Con el modelo de Bradley-Terry
P(i supera a j) = w_i / (w_i + w_j), se estima la fuerza w de cada valor (algoritmo iterativo de
Zermelo/MM) a partir de las elecciones de un grupo de 60 personas. Se compara el orden
estimado con el verdadero y se estima la estabilidad con remuestreo. Datos sinteticos.
"""
from __future__ import annotations

import itertools
import random

SEMILLA = 20260819
VALORES = ["autonomia", "seguridad", "ingreso", "servicio", "prestigio", "equilibrio"]
W_VERDAD = [1.6, 1.4, 1.2, 1.0, 0.6, 1.5]


def bradley_terry(victorias: list[list[int]], iteraciones: int = 200) -> list[float]:
    k = len(victorias)
    w = [1.0] * k
    for _ in range(iteraciones):
        nuevo = []
        for i in range(k):
            gan = sum(victorias[i])
            den = sum((victorias[i][j] + victorias[j][i]) / (w[i] + w[j]) for j in range(k) if j != i)
            nuevo.append(gan / den if den else w[i])
        s = sum(nuevo) / k
        w = [x / s for x in nuevo]
    return w


def simula(n: int, rng: random.Random) -> list[list[int]]:
    k = len(VALORES)
    vic = [[0] * k for _ in range(k)]
    for _ in range(n):
        for i, j in itertools.combinations(range(k), 2):
            if rng.random() < W_VERDAD[i] / (W_VERDAD[i] + W_VERDAD[j]):
                vic[i][j] += 1
            else:
                vic[j][i] += 1
    return vic


def main() -> None:
    rng = random.Random(SEMILLA)
    w = bradley_terry(simula(60, rng))
    print(f"{'valor':<12} {'w verdadero':>12} {'w estimado':>11}  puesto est.")
    orden = sorted(range(len(w)), key=lambda i: -w[i])
    for i in orden:
        print(f"{VALORES[i]:<12} {W_VERDAD[i] / (sum(W_VERDAD) / 6):12.2f} {w[i]:11.2f}  {orden.index(i) + 1}")
    verd = sorted(range(6), key=lambda i: -W_VERDAD[i])
    coincide_top = 0
    reps = 300
    for _ in range(reps):
        est = bradley_terry(simula(60, rng))
        coincide_top += sorted(range(6), key=lambda i: -est[i])[:3] == verd[:3]
    print(f"\nOrden verdadero: {[VALORES[i] for i in verd]}")
    print(f"Repitiendo el estudio con otra muestra de 60: el TOP 3 identico en el orden verdadero: {coincide_top / reps:.0%}")
    print()
    print("Lectura: las comparaciones por pares dan una escala de preferencia sin los sesgos de aquiescencia")
    print("de la Likert, pero son relativas (quien valora mas, no cuanto) y crecen con el cuadrado del numero")
    print("de valores. Con valores de fuerza parecida, el orden exacto es inestable: se informa el grupo de")
    print("valores mas importantes, no el puesto de cada uno. Los valores orientan; no predicen satisfaccion por si solos.")


if __name__ == "__main__":
    main()
