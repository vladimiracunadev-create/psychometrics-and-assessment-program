"""Laboratorio 116 - Rasgos y ventas: relacion no lineal y contaminacion del criterio.

Dos fuentes de error al estudiar "personalidad de vendedores" (sin usar ninguna prueba comercial):
  1. Relacion curvilinea: el rasgo ayuda hasta un nivel y luego aporta menos (rendimientos
     decrecientes). Un ajuste LINEAL subestima el efecto en el rango bajo-medio.
  2. Contaminacion del criterio: las ventas dependen del territorio (que el vendedor no controla).
     Si el criterio incluye mucho "territorio", la validez observada cae.
Se ajusta una regresion lineal y una cuadratica (mnimos cuadrados) y se compara R^2.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 4000


def resolver(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    m = [fila[:] + [b[i]] for i, fila in enumerate(a)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[piv] = m[piv], m[i]
        for r in range(n):
            if r != i:
                f = m[r][i] / m[i][i]
                m[r] = [x - f * y for x, y in zip(m[r], m[i], strict=True)]
    return [m[i][n] / m[i][i] for i in range(n)]


def r2(x: list[float], y: list[float], grado: int) -> float:
    k = grado + 1
    xtx = [[sum(xi ** (i + j) for xi in x) for j in range(k)] for i in range(k)]
    xty = [sum(yy * xi ** i for xi, yy in zip(x, y, strict=True)) for i in range(k)]
    b = resolver(xtx, xty)
    pred = [sum(b[i] * xi ** i for i in range(k)) for xi in x]
    sse = sum((yy - p) ** 2 for yy, p in zip(y, pred, strict=True))
    sst = sum((yy - statistics.fmean(y)) ** 2 for yy in y)
    return 1 - sse / sst


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'peso del territorio en las ventas':<36} {'R2 lineal':>10} {'R2 cuadratica':>14}")
    print("=" * 64)
    for w in (0.0, 0.5, 1.0, 2.0):
        x = [rng.gauss(0, 1) for _ in range(N)]
        territorio = [rng.gauss(0, 1) for _ in range(N)]
        ventas = [0.7 * min(a, 0.5) + w * t * 0.6 + rng.gauss(0, 0.8)
                  for a, t in zip(x, territorio, strict=True)]
        print(f"{w:<36.1f} {r2(x, ventas, 1):10.3f} {r2(x, ventas, 2):14.3f}")
    print()
    print("Lectura: (1) con una relacion que se aplana en el extremo, el modelo cuadratico explica mas")
    print("que el lineal: el efecto no es constante. (2) A medida que el criterio incluye mas")
    print("'territorio' (algo ajeno al vendedor), el R2 de ambos cae: la validez mide tambien la calidad")
    print("del criterio. Evaluar 'personalidad de vendedores' exige un criterio depurado (ventas")
    print("ajustadas por territorio, evaluacion de conductas) y evidencia local, no un perfil generico.")


if __name__ == "__main__":
    main()
