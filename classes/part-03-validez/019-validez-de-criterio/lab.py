"""Laboratorio 019 - Validez de criterio: restriccion de rango y utilidad de seleccion.

1. Se simula una poblacion de postulantes con validez verdadera r = 0.40 entre el test
   y el desempeno. Solo se observa el desempeno de quienes fueron CONTRATADOS (30 %
   superior en el test): la correlacion observada se subestima.
2. Se corrige con la formula de Thorndike (Caso II) para restriccion directa.
3. Se compara la tasa de "buen desempeno" entre contratados segun la validez del test.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 100000


def poblacion(r: float, rng: random.Random) -> tuple[list[float], list[float]]:
    x = [rng.gauss(0, 1) for _ in range(N)]
    y = [r * a + math.sqrt(1 - r * r) * rng.gauss(0, 1) for a in x]
    return x, y


def thorndike_ii(r: float, u: float) -> float:
    """u = DE sin restringir / DE restringida del predictor."""
    return r * u / math.sqrt(1 + r * r * (u * u - 1))


def main() -> None:
    rng = random.Random(SEMILLA)
    x, y = poblacion(0.40, rng)
    corte = sorted(x)[int(0.70 * N)]
    sel = [(a, b) for a, b in zip(x, y, strict=True) if a >= corte]
    xs, ys = [a for a, _ in sel], [b for _, b in sel]
    r_obs = statistics.correlation(xs, ys)
    u = statistics.pstdev(x) / statistics.pstdev(xs)
    print("Validez verdadera en la poblacion de postulantes: 0.400")
    print(f"Correlacion observada solo en contratados (30 % superior): {r_obs:.3f}")
    print(f"Corregida por restriccion de rango (Thorndike II, u={u:.2f}): {thorndike_ii(r_obs, u):.3f}")
    print()
    print("Tasa de buen desempeno (y > mediana) entre los contratados (30 % superior):")
    print(f"{'validez del test':>18} {'tasa buen desempeno':>22}")
    for r in (0.0, 0.2, 0.4, 0.6):
        xx, yy = poblacion(r, rng)
        c = sorted(xx)[int(0.70 * N)]
        buenos = [b for a, b in zip(xx, yy, strict=True) if a >= c]
        print(f"{r:18.1f} {sum(b > 0 for b in buenos) / len(buenos):22.3f}")
    print()
    print("Lectura: sin validez la seleccion rinde 0.50 (azar). Incluso con r = 0.40")
    print("la mejora es real pero acotada. Y la formula corrige un supuesto: que la seleccion")
    print("fue solo por el predictor; con seleccion por otras vias el ajuste es otro.")


if __name__ == "__main__":
    main()
