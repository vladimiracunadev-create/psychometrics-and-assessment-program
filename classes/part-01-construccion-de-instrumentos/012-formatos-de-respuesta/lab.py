"""Laboratorio 012 - Cuanta informacion se pierde al discretizar la respuesta.

Un rasgo continuo z ~ N(0,1) se registra con k categorias de umbrales equiespaciados.
Se mide la correlacion entre la categoria y z: es la fidelidad con que el formato
de respuesta conserva el rasgo (un limite superior para cualquier fiabilidad).
Con k=2 y umbral en 0 el valor teorico es sqrt(2/pi) = 0.798.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 20000


def categoriza(z: float, k: int, rango: float = 2.5) -> int:
    if k == 2:
        return int(z > 0)
    paso = 2 * rango / k
    return max(0, min(k - 1, int((z + rango) // paso)))


def main() -> None:
    rng = random.Random(SEMILLA)
    zs = [rng.gauss(0, 1) for _ in range(N)]
    print("Fidelidad del formato de respuesta (r entre categoria y rasgo)")
    print("=" * 56)
    print(f"{'categorias':>10} {'r':>8}  barra")
    prev = None
    for k in (2, 3, 4, 5, 7, 11):
        r = statistics.correlation(zs, [categoriza(z, k) for z in zs])
        ganancia = "" if prev is None else f"  (+{r - prev:.3f})"
        print(f"{k:10d} {r:8.3f}  {'#' * round(r * 40)}{ganancia}")
        prev = r
    print()
    print("Lectura: de 2 a 5 categorias se gana mucho; de 7 a 11 casi nada, y")
    print("esas categorias extra exceden lo que una persona discrimina al responder.")


if __name__ == "__main__":
    main()
