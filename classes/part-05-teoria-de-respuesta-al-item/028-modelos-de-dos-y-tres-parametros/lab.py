"""Laboratorio 028 - Modelos de 2 y 3 parametros.

    P(theta) = c + (1 - c) * logistica( a * (theta - b) )
        a: discriminacion (pendiente), b: dificultad, c: adivinacion (asintota inferior)

1. Tabla de la curva para varios (a, b, c).
2. Recuperacion de (a, b) de un item 2PL por regresion logistica con theta conocida.
3. Qué pasa al ajustar 2PL a un item que en verdad tiene adivinacion (c = 0.20): la
   discriminacion y la dificultad estimadas se distorsionan.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 30000


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def p3(t: float, a: float, b: float, c: float) -> float:
    return c + (1 - c) * logistica(a * (t - b))


def ajusta_2pl(thetas: list[float], ys: list[int]) -> tuple[float, float]:
    """Regresion logistica y ~ logistica(a*theta + d) por Newton; b = -d/a."""
    a, d = 1.0, 0.0
    for _ in range(40):
        g = [0.0, 0.0]
        h = [[0.0, 0.0], [0.0, 0.0]]
        for t, y in zip(thetas, ys, strict=True):
            p = logistica(a * t + d)
            r, w = y - p, p * (1 - p)
            g[0] += r * t
            g[1] += r
            h[0][0] += w * t * t
            h[0][1] += w * t
            h[1][1] += w
        h[1][0] = h[0][1]
        det = h[0][0] * h[1][1] - h[0][1] ** 2
        a += (h[1][1] * g[0] - h[0][1] * g[1]) / det
        d += (-h[1][0] * g[0] + h[0][0] * g[1]) / det
    return a, -d / a


def main() -> None:
    print("Curvas P(theta)")
    print(f"{'(a, b, c)':<16}" + "".join(f"{t:7.1f}" for t in (-3, -2, -1, 0, 1, 2, 3)))
    for a, b, c in ((1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.2)):
        print(f"({a:.1f}, {b:.1f}, {c:.1f})   "
              + "".join(f"{p3(t, a, b, c):7.2f}" for t in (-3, -2, -1, 0, 1, 2, 3)))

    rng = random.Random(SEMILLA)
    thetas = [rng.gauss(0, 1) for _ in range(N)]
    ys = [int(rng.random() < p3(t, 1.5, 0.5, 0.0)) for t in thetas]
    a_est, b_est = ajusta_2pl(thetas, ys)
    print(f"\nItem 2PL verdadero (a=1.50, b=0.50) -> estimado a={a_est:.2f}, b={b_est:.2f}")

    ys3 = [int(rng.random() < p3(t, 1.5, 0.5, 0.20)) for t in thetas]
    a3, b3 = ajusta_2pl(thetas, ys3)
    print(f"Item 3PL verdadero (a=1.50, b=0.50, c=0.20) ajustado como 2PL -> a={a3:.2f}, b={b3:.2f}")
    print()
    print("Lectura: sin el parametro c, el 2PL 'aplana' la curva (a baja) y desplaza b. En pruebas")
    print("de opcion multiple con adivinacion, ignorar c distorsiona la dificultad de los items.")
    print("Pero el 3PL exige muestras grandes (cientos a miles) para estimar c con estabilidad.")


if __name__ == "__main__":
    main()
