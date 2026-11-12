"""Laboratorio 065 - Datos ordinales: la correlacion de Pearson subestima el vinculo latente.

Dos variables latentes normales con correlacion verdadera 0.60 se registran como binarias
(0/1) con distintos puntos de corte. Pearson sobre los 0/1 (coeficiente phi) subestima; la
correlacion TETRACORICA, estimada aqui con la aproximacion cos(pi / (1 + sqrt(OR))) (Bonett y
Price, 2005), recupera mejor el valor latente. La correlacion POLICORICA generaliza la idea
a mas categorias y se estima por maxima verosimilitud en software especializado.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 60000
RHO = 0.60


def tetracorica_aprox(x: list[int], y: list[int]) -> float:
    a = sum(1 for p, q in zip(x, y, strict=True) if p and q) + 0.5
    b = sum(1 for p, q in zip(x, y, strict=True) if p and not q) + 0.5
    c = sum(1 for p, q in zip(x, y, strict=True) if not p and q) + 0.5
    d = sum(1 for p, q in zip(x, y, strict=True) if not p and not q) + 0.5
    odds = (a * d) / (b * c)
    return math.cos(math.pi / (1 + math.sqrt(odds)))


def main() -> None:
    rng = random.Random(SEMILLA)
    z1 = [rng.gauss(0, 1) for _ in range(N)]
    z2 = [RHO * a + math.sqrt(1 - RHO**2) * rng.gauss(0, 1) for a in z1]
    print(f"Correlacion latente verdadera = {RHO}")
    print(f"{'corte (z)':>10} {'% de 1':>8} {'Pearson/phi':>12} {'tetracorica':>12}")
    print("=" * 46)
    for corte in (0.0, 0.5, 1.0, 1.5, 2.0):
        x = [int(a > corte) for a in z1]
        y = [int(a > corte) for a in z2]
        print(f"{corte:10.1f} {statistics.fmean(x):8.1%} {statistics.correlation(x, y):12.3f} "
              f"{tetracorica_aprox(x, y):12.3f}")
    print()
    print("Nota: la aproximacion es buena con cortes centrales y burda en los extremos")
    print("(sobrestima con 2 % de unos); la estimacion correcta es por maxima verosimilitud.")
    print("Lectura: cuanto mas asimetrica la dicotomia (items 'faciles' o 'dificiles'), mas")
    print("subestima phi. Ese artefacto de dificultad crea 'factores de dificultad' espurios en")
    print("el analisis factorial de items dicotomicos con Pearson. Con 5 o mas categorias y")
    print("distribuciones razonables el problema es menor, pero con 2-4 categorias conviene usar")
    print("correlaciones policoricas (y estimadores como WLSMV) en lugar de Pearson.")


if __name__ == "__main__":
    main()
