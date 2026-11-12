"""Laboratorio 058 - Modelo de respuesta graduada (Samejima, 1969).

Item Likert de 5 categorias con discriminacion a = 1.5 y umbrales b1<b2<b3<b4:
    P*(k) = logistica(a * (theta - b_k))        (probabilidad de responder k o mas)
    P(categoria k) = P*(k) - P*(k+1),  con P*(1) = 1 y P*(6) = 0
Se tabulan las probabilidades por categoria, la puntuacion esperada, y se comprueba por
simulacion que las frecuencias de categorias coinciden con las del modelo (theta ~ N(0,1)).
"""
from __future__ import annotations

import math
import random

A = 1.5
UMBRALES = [-1.5, -0.5, 0.5, 1.5]
SEMILLA = 20260819


def probs(t: float) -> list[float]:
    pstar = [1.0] + [1 / (1 + math.exp(-A * (t - b))) for b in UMBRALES] + [0.0]
    return [pstar[k] - pstar[k + 1] for k in range(5)]


def main() -> None:
    print(f"{'theta':>6} " + " ".join(f"{'cat ' + str(k):>6}" for k in range(1, 6)) + f" {'suma':>6} {'esperada':>9}")
    print("=" * 62)
    for t in (-3, -2, -1, 0, 1, 2, 3):
        p = probs(t)
        esp = sum((k + 1) * q for k, q in enumerate(p))
        print(f"{t:6d} " + " ".join(f"{q:6.2f}" for q in p) + f" {sum(p):6.2f} {esp:9.2f}")

    rng = random.Random(SEMILLA)
    conteo = [0] * 5
    teorico = [0.0] * 5
    n = 20000
    for _ in range(n):
        t = rng.gauss(0, 1)
        p = probs(t)
        for k, q in enumerate(p):
            teorico[k] += q / n
        u, acum = rng.random(), 0.0
        for k, q in enumerate(p):
            acum += q
            if u < acum:
                conteo[k] += 1
                break
    print("\nFrecuencia de categorias con theta ~ N(0,1)")
    print("  simulada: " + " ".join(f"{c / n:6.3f}" for c in conteo))
    print("  modelo:   " + " ".join(f"{q:6.3f}" for q in teorico))
    print()
    print("Lectura: cada categoria es la 'mas probable' en un tramo de theta; si una categoria")
    print("nunca es la mas probable, esta mal disenada o los umbrales estan desordenados. El GRM")
    print("trata las respuestas como ordinales: no supone que la distancia entre 1 y 2 sea la de 4 y 5.")


if __name__ == "__main__":
    main()
