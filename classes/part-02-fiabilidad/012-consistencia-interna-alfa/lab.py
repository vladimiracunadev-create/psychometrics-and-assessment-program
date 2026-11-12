"""Laboratorio 012 - Alfa de Cronbach: que mide y que NO demuestra.

    alfa = k/(k-1) * (1 - suma(var_i) / var_total)

Tres escenarios con 12 items, N grande y semilla fija:
  A. Unidimensional: todos los items miden un solo factor.
  B. Dos dimensiones independientes (6 items cada una): alfa sigue siendo
     "aceptable" aunque la escala mezcla dos constructos.
  C. Un solo item defectuoso (ruido puro) entre 11 buenos.
La leccion: un alfa alto NO prueba unidimensionalidad.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 5000
K = 12


def alfa(items: list[list[float]]) -> float:
    k = len(items)
    total = [sum(fila) for fila in zip(*items, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(i) for i in items) / statistics.pvariance(total))


def escenario_unidimensional(rng: random.Random) -> list[list[float]]:
    f = [rng.gauss(0, 1) for _ in range(N)]
    return [[0.6 * a + rng.gauss(0, 0.8) for a in f] for _ in range(K)]


def escenario_bidimensional(rng: random.Random) -> list[list[float]]:
    f1 = [rng.gauss(0, 1) for _ in range(N)]
    f2 = [rng.gauss(0, 1) for _ in range(N)]
    mitad = K // 2
    return ([[0.7 * a + rng.gauss(0, 0.7) for a in f1] for _ in range(mitad)]
            + [[0.7 * a + rng.gauss(0, 0.7) for a in f2] for _ in range(mitad)])


def escenario_item_malo(rng: random.Random) -> list[list[float]]:
    items = escenario_unidimensional(rng)
    items[-1] = [rng.gauss(0, 1) for _ in range(N)]
    return items


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'escenario':<42} {'alfa':>6}")
    print("=" * 50)
    a = escenario_unidimensional(rng)
    b = escenario_bidimensional(rng)
    c = escenario_item_malo(rng)
    print(f"{'A. unidimensional (12 items)':<42} {alfa(a):6.3f}")
    print(f"{'B. DOS dimensiones independientes':<42} {alfa(b):6.3f}")
    print(f"{'C. unidimensional con 1 item de ruido':<42} {alfa(c):6.3f}")
    print()
    print("Alfa si se elimina cada item (escenario C):")
    for i in range(K):
        resto = [col for j, col in enumerate(c) if j != i]
        marca = "  <- eliminarlo SUBE alfa (es el item de ruido)" if alfa(resto) > alfa(c) else ""
        print(f"  item {i + 1:2d}: {alfa(resto):.3f}{marca}")
    print()
    print("Lectura: en B alfa no delata que la escala mezcla dos constructos.")
    print("Alfa mide covarianza media entre items, no estructura: para eso hace")
    print("falta el analisis factorial (parte 04).")


if __name__ == "__main__":
    main()
