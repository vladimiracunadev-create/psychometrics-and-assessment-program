"""Laboratorio 027 - Pearson frente a Spearman y los supuestos que importan.

Cuatro situaciones sobre n = 200: relacion lineal, monotona no lineal, un valor
extremo aislado y restriccion de rango. Spearman se implementa con rangos (promedio
en empates) para no depender de la version de Python.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 200


def rangos(xs: list[float]) -> list[float]:
    orden = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and xs[orden[j + 1]] == xs[orden[i]]:
            j += 1
        for k in range(i, j + 1):
            r[orden[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def pearson(x: list[float], y: list[float]) -> float:
    return statistics.correlation(x, y)


def spearman(x: list[float], y: list[float]) -> float:
    return pearson(rangos(x), rangos(y))


def fila(nombre: str, x: list[float], y: list[float]) -> None:
    print(f"{nombre:<38} Pearson={pearson(x, y):6.3f}   Spearman={spearman(x, y):6.3f}")


def main() -> None:
    rng = random.Random(SEMILLA)
    x = [rng.gauss(0, 1) for _ in range(N)]
    print("Correlaciones sobre los mismos 200 sujetos simulados")
    print("=" * 66)
    fila("1. lineal con ruido", x, [0.7 * a + rng.gauss(0, 0.7) for a in x])
    fila("2. monotona no lineal (exp)", x, [math.exp(2 * a) + rng.gauss(0, 0.1) for a in x])
    y = [rng.gauss(0, 1) for _ in range(N)]                       # sin relacion
    fila("3a. sin relacion", x, y)
    fila("3b. igual + UN valor extremo (8, 8)", [*x, 8.0], [*y, 8.0])
    y2 = [0.7 * a + rng.gauss(0, 0.7) for a in x]
    sel = [(a, b) for a, b in zip(x, y2, strict=True) if a > 0.5]   # solo quienes pasaron un corte
    fila(f"4a. rango completo (n={N})", x, y2)
    fila(f"4b. rango restringido (n={len(sel)})", [a for a, _ in sel], [b for _, b in sel])
    print()
    print("Lectura")
    print("  2: Spearman capta la monotonia; Pearson subestima una relacion no lineal.")
    print("  3b: un solo punto fabrica una correlacion apreciable en Pearson; Spearman apenas se mueve.")
    print("  4b: seleccionar por X reduce la correlacion observada: es la restriccion de rango,")
    print("      y es la razon de que la validez medida en contratados subestime la real (clase 034).")


if __name__ == "__main__":
    main()
