"""Laboratorio 018 - Validez de constructo: patron convergente y discriminante.

Tres escalas: A (constructo X), B (el mismo constructo X con otro formato) y C (otro
constructo, correlacionado 0.30 con X). La prediccion teorica es r(A,B) alto,
r(A,C) y r(B,C) moderados. Despues se agrega varianza de metodo compartida entre A y C
(mismo formato de autoinforme): la correlacion discriminante se infla y el patron
se degrada. Es la idea de la matriz multirrasgo-multimetodo (clase 056).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 20000


def main() -> None:
    rng = random.Random(SEMILLA)
    x = [rng.gauss(0, 1) for _ in range(N)]
    z = [0.3 * a + math.sqrt(1 - 0.09) * rng.gauss(0, 1) for a in x]      # constructo C
    metodo = [rng.gauss(0, 1) for _ in range(N)]                            # estilo de respuesta

    def escala(t: list[float], peso_metodo: float = 0.0) -> list[float]:
        return [0.85 * a + peso_metodo * m + rng.gauss(0, 0.5) for a, m in zip(t, metodo, strict=True)]

    for titulo, w in (("Sin varianza de metodo compartida", 0.0),
                      ("A y C comparten formato (varianza de metodo)", 0.6)):
        A = escala(x, w)
        B = escala(x, 0.0)
        C = escala(z, w)
        print(titulo)
        print(f"  r(A,B)  convergente   = {statistics.correlation(A, B):.3f}")
        print(f"  r(A,C)  discriminante = {statistics.correlation(A, C):.3f}")
        print(f"  r(B,C)  discriminante = {statistics.correlation(B, C):.3f}")
        print()
    print("Lectura: con metodo compartido r(A,C) se infla frente a r(B,C): parte de lo que")
    print("parece 'relacion entre constructos' es relacion entre formatos. La evidencia de")
    print("constructo es un patron de predicciones, no un unico coeficiente.")


if __name__ == "__main__":
    main()
