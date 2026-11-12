"""Laboratorio 043 - Rendimiento maximo frente a desempeno tipico: que pasa si la persona quiere "verse bien".

Dos tipos de prueba con 2.000 personas sinteticas:
  - Rendimiento MAXIMO (opcion multiple de 4 alternativas): la respuesta correcta es unica; querer
    verse bien no sube el puntaje mas alla de lo que la persona sabe (solo puede adivinar).
  - Desempeno TIPICO (autoinforme Likert 1-5): no hay respuesta objetivamente correcta; con la
    consigna de "causar buena impresion" las respuestas se desplazan hacia el polo deseable.
Se compara el tamano del cambio (d de Cohen) entre la consigna honesta y la de impresion.
Datos sinteticos.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 2000, 30


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def maximo(theta: float, motivada: bool, rng: random.Random) -> int:
    puntaje = 0
    for j in range(K):
        b = -1.5 + 3.0 * j / (K - 1)
        sabe = rng.random() < logistica(1.2 * (theta - b))
        # Si no sabe, adivina (1/4) en ambas consignas: la motivacion no crea conocimiento.
        puntaje += sabe or rng.random() < 0.25
    return puntaje


def tipico(rasgo: float, impresion: bool, rng: random.Random) -> float:
    total = 0.0
    for _ in range(K):
        v = 3 + 0.9 * rasgo + rng.gauss(0, 0.8) + (0.7 if impresion else 0.0)
        total += min(5, max(1, round(v)))
    return total


def d(a: list[float], b: list[float]) -> float:
    sp = math.sqrt((statistics.variance(a) + statistics.variance(b)) / 2)
    return (statistics.fmean(b) - statistics.fmean(a)) / sp


def main() -> None:
    rng = random.Random(SEMILLA)
    base = [rng.gauss(0, 1) for _ in range(N)]
    max_h = [maximo(t, False, rng) for t in base]
    max_i = [maximo(t, True, rng) for t in base]
    tip_h = [tipico(t, False, rng) for t in base]
    tip_i = [tipico(t, True, rng) for t in base]
    print(f"{'tipo de prueba':<28} {'media honesta':>14} {'media impresion':>16} {'d de Cohen':>11}")
    print("=" * 75)
    print(f"{'rendimiento maximo (MC)':<28} {statistics.fmean(max_h):14.1f} {statistics.fmean(max_i):16.1f} {d(max_h, max_i):11.2f}")
    print(f"{'desempeno tipico (Likert)':<28} {statistics.fmean(tip_h):14.1f} {statistics.fmean(tip_i):16.1f} {d(tip_h, tip_i):11.2f}")
    print()
    print("Lectura: en la prueba de rendimiento maximo, 'querer verse bien' no cambia el puntaje porque no hay forma")
    print("de saber mas de lo que se sabe; en el autoinforme el desplazamiento es grande. Por eso las pruebas de")
    print("personalidad en seleccion requieren cautela (clases 060 y 099) y los resultados de ambos tipos no se")
    print("interpretan igual. Datos sinteticos; los tamanos dependen de los parametros elegidos.")


if __name__ == "__main__":
    main()
