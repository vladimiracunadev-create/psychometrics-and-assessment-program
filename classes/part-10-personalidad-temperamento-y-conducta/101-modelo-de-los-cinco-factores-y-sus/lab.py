"""Laboratorio 101 - Dominios y facetas del modelo de cinco factores: amplitud frente a fidelidad.

Estructura jerarquica simulada: 1 dominio (p. ej. Responsabilidad) con 6 facetas. Cada faceta =
dominio comun + varianza propia de la faceta. Un criterio (desempeno academico) depende del
dominio y de UNA faceta especifica (orden/disciplina). Se compara la capacidad predictiva de:
  (a) el puntaje de dominio (promedio de las 6 facetas),
  (b) las 6 facetas por separado (regresion multiple, con validacion cruzada simple).
Los pesos son supuestos del laboratorio; muestran el dilema amplitud-fidelidad (Paunonen y Ashton, 2001).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, F = 3000, 6


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


def mco(x: list[list[float]], y: list[float]) -> list[float]:
    k = len(x[0]) + 1
    xs = [[1.0, *f] for f in x]
    xtx = [[sum(r[i] * r[j] for r in xs) for j in range(k)] for i in range(k)]
    xty = [sum(r[i] * yy for r, yy in zip(xs, y, strict=True)) for i in range(k)]
    return resolver(xtx, xty)


def main() -> None:
    rng = random.Random(SEMILLA)
    filas, crit = [], []
    for _ in range(N):
        dom = rng.gauss(0, 1)
        fac = [0.6 * dom + 0.8 * rng.gauss(0, 1) for _ in range(F)]
        crit.append(0.25 * dom + 0.30 * (fac[0] - 0.6 * dom) / 0.8 + rng.gauss(0, 1))
        filas.append(fac)
    mitad = N // 2
    dominio = [statistics.fmean(f) for f in filas]
    r_dom = statistics.correlation(dominio[mitad:], crit[mitad:])
    b = mco(filas[:mitad], crit[:mitad])
    pred = [b[0] + sum(c * v for c, v in zip(b[1:], f, strict=True)) for f in filas[mitad:]]
    r_fac = statistics.correlation(pred, crit[mitad:])
    r_f1 = statistics.correlation([f[0] for f in filas[mitad:]], crit[mitad:])
    print(f"{'predictor (validacion en la 2.a mitad)':<44} {'r con el criterio':>18}")
    print("=" * 64)
    print(f"{'puntaje de DOMINIO (promedio de 6 facetas)':<44} {r_dom:18.3f}")
    print(f"{'faceta 1 sola (la relevante)':<44} {r_f1:18.3f}")
    print(f"{'6 facetas (regresion multiple)':<44} {r_fac:18.3f}")
    print(f"Pesos estimados de las facetas: " + ", ".join(f"{c:.2f}" for c in b[1:]))
    print()
    print("Lectura: cuando el criterio depende de una faceta especifica, las facetas predicen mas que")
    print("el dominio; cuando el criterio es amplio, el dominio basta. Mas facetas = mas parametros, con")
    print("riesgo de sobreajuste en muestras pequenas. El nivel de medida debe coincidir con el del criterio.")


if __name__ == "__main__":
    main()
