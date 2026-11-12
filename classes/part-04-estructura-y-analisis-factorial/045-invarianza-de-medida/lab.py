"""Laboratorio 045 - Invarianza metrica: que ocurre si las cargas difieren entre grupos.

Dos grupos con el MISMO nivel medio del rasgo. Un item carga 0.8 en el grupo A y 0.3 en el
grupo B (el item "significa algo distinto" en B). Como el laboratorio conoce el rasgo
latente, estima la carga de cada item por grupo con regresion de item sobre rasgo y
muestra: (1) cargas distintas, (2) fiabilidad de la escala distinta por grupo y (3) que la
correlacion con un criterio casi no cambia: el problema puede pasar inadvertido.
En datos reales el rasgo no se observa: la invarianza se prueba con modelos factoriales
multigrupo (clase 070).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 5000, 6


def alfa(items: list[list[float]]) -> float:
    k = len(items)
    total = [sum(f) for f in zip(*items, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(i) for i in items) / statistics.pvariance(total))


def grupo(carga_item6: float, rng: random.Random):
    theta = [rng.gauss(0, 1) for _ in range(N)]
    cargas = [0.7] * (K - 1) + [carga_item6]
    items = [[c * t + rng.gauss(0, math.sqrt(1 - c * c)) for t in theta] for c in cargas]
    criterio = [0.5 * t + rng.gauss(0, math.sqrt(0.75)) for t in theta]
    return theta, items, criterio


def pendiente(x: list[float], y: list[float]) -> float:
    return statistics.covariance(x, y) / statistics.variance(x)


def main() -> None:
    rng = random.Random(SEMILLA)
    resultados = {}
    for nombre, c6 in (("A", 0.8), ("B", 0.3)):
        theta, items, crit = grupo(c6, rng)
        total = [sum(f) for f in zip(*items, strict=True)]
        resultados[nombre] = (
            [pendiente(theta, it) for it in items], alfa(items), statistics.correlation(total, crit))
    print(f"{'':<8} {'carga item 6':>13} {'alfa':>7} {'r(escala, criterio)':>21}")
    print("=" * 54)
    for nombre, (cargas, a, r) in resultados.items():
        print(f"Grupo {nombre:<2} {cargas[-1]:13.2f} {a:7.3f} {r:21.3f}")
    print()
    print("Lectura: con el mismo rasgo medio, la escala NO funciona igual en ambos grupos: su")
    print("fiabilidad baja en B. Pero la correlacion con el criterio casi no se mueve (un solo")
    print("item de seis), asi que la validez de criterio por si sola NO delata el problema.")
    print("Comparar fiabilidades o estructuras entre grupos sin invarianza metrica mezcla")
    print("diferencias del rasgo con diferencias del instrumento.")


if __name__ == "__main__":
    main()
