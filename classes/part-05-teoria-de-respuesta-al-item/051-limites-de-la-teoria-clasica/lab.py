"""Laboratorio 051 - Los limites de la teoria clasica: indices que dependen de la muestra.

Los MISMOS 10 items (dificultades verdaderas fijas) se aplican a dos grupos: uno de baja
habilidad (media -1) y uno de alta (media +1). Se comparan:
  - dificultad clasica p y discriminacion clasica r item-resto: cambian mucho entre grupos;
  - la dificultad del modelo logistico (parametro b) estimada con la habilidad conocida:
    recupera el MISMO valor en ambos grupos (invarianza de parametros).
Aviso: aqui la habilidad se conoce porque se simula. En datos reales hay que estimarla a la
vez que los parametros (clases 052 y 056), y la invarianza vale solo si el modelo se sostiene.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 4000
B_VERDADERO = [-1.8, -1.2, -0.7, -0.3, 0.0, 0.3, 0.7, 1.2, 1.8, 2.4]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def b_estimado(thetas: list[float], col: list[int]) -> float:
    """Resuelve sum logistica(theta - b) = sum respuestas por biseccion (Rasch con theta conocida)."""
    objetivo = sum(col)
    lo, hi = -8.0, 8.0
    for _ in range(60):
        mid = (lo + hi) / 2
        esperado = sum(logistica(t - mid) for t in thetas)
        lo, hi = (mid, hi) if esperado > objetivo else (lo, mid)
    return (lo + hi) / 2


def main() -> None:
    rng = random.Random(SEMILLA)
    resultados = {}
    for nombre, media in (("baja", -1.0), ("alta", 1.0)):
        thetas = [rng.gauss(media, 1) for _ in range(N)]
        cols = [[int(rng.random() < logistica(t - b)) for t in thetas] for b in B_VERDADERO]
        totales = [sum(f) for f in zip(*cols, strict=True)]
        info = []
        for col in cols:
            resto = [t - x for t, x in zip(totales, col, strict=True)]
            info.append((statistics.fmean(col),
                         statistics.correlation([float(x) for x in col], [float(x) for x in resto]),
                         b_estimado(thetas, col)))
        resultados[nombre] = info
    print(f"{'item':>4} {'b real':>7} | {'p baja':>7} {'p alta':>7} | {'r baja':>7} {'r alta':>7} | "
          f"{'b est. baja':>11} {'b est. alta':>11}")
    print("=" * 84)
    for i, b in enumerate(B_VERDADERO):
        lo, hi = resultados["baja"][i], resultados["alta"][i]
        print(f"{i + 1:4d} {b:7.1f} | {lo[0]:7.2f} {hi[0]:7.2f} | {lo[1]:7.2f} {hi[1]:7.2f} | "
              f"{lo[2]:11.2f} {hi[2]:11.2f}")
    print()
    print("Lectura: p y r cambian drasticamente con el grupo (el item 'dificil' pasa a 'facil');")
    print("b estimado coincide con el verdadero en ambos. Esa propiedad (parametros del item")
    print("independientes de la muestra, y habilidad independiente de los items) es lo que la TRI")
    print("agrega a la teoria clasica. Rige solo si el modelo se ajusta a los datos.")


if __name__ == "__main__":
    main()
