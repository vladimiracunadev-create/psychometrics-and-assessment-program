"""Laboratorio 072 - Normas por edad: bandas discretas frente a normalizacion continua.

El rendimiento medio en una tarea crece con la edad (6 a 12 anos) de forma curvilinea. Dos
formas de construir normas:
  - BANDAS: un baremo por ano de edad cumplido;
  - CONTINUA: media (y DE) como funcion suave de la edad (regresion cuadratica).
Se muestra el "salto" artificial entre dos ninos de casi igual edad (6;11 y 7;0) con el mismo
puntaje bruto, y el error de cada metodo respecto de la media verdadera.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 3000
DE = 6.0


def media_real(e: float) -> float:
    return 10 + 9 * (e - 6) - 0.45 * (e - 6) ** 2


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


def main() -> None:
    rng = random.Random(SEMILLA)
    edades = [rng.uniform(6, 13) for _ in range(N)]
    y = [media_real(e) + rng.gauss(0, DE) for e in edades]
    # Regresion cuadratica por minimos cuadrados (ecuaciones normales).
    s = [sum(e ** k for e in edades) for k in range(5)]
    t = [sum(yy * e ** k for e, yy in zip(edades, y, strict=True)) for k in range(3)]
    c = resolver([[s[0], s[1], s[2]], [s[1], s[2], s[3]], [s[2], s[3], s[4]]], t)
    continua = lambda e: c[0] + c[1] * e + c[2] * e * e  # noqa: E731

    bandas = {}
    for a in range(6, 13):
        v = [yy for e, yy in zip(edades, y, strict=True) if a <= e < a + 1]
        bandas[a] = sum(v) / len(v)

    def T(x: float, media: float) -> float:
        return 50 + 10 * (x - media) / DE

    bruto = 30.0
    print(f"Mismo puntaje bruto = {bruto:.0f} para dos ninos casi de la misma edad:")
    for etiqueta, e in (("6;11 (6.92)", 6.92), ("7;00 (7.00)", 7.00)):
        print(f"  {etiqueta:<12} banda: T = {T(bruto, bandas[int(e)]):5.1f}"
              f" | continua: T = {T(bruto, continua(e)):5.1f}")
    print(f"\nError de la media (vs media real) en el borde de banda e = 7.0:  banda de 6 anos: "
          f"{abs(bandas[6] - media_real(7.0)):.2f}, banda de 7: {abs(bandas[7] - media_real(7.0)):.2f}, "
          f"continua: {abs(continua(7.0) - media_real(7.0)):.2f}")
    print()
    print("Lectura: con bandas, dos ninos casi iguales en edad reciben puntajes T muy distintos")
    print("solo por el lado del corte; la normalizacion continua los trata parecido. Exige modelar")
    print("bien la forma de la curva y la DE, y una muestra normativa que cubra toda la edad.")
    print("Normas por curso y por edad pueden diferir: el curso mide tambien instruccion recibida.")


if __name__ == "__main__":
    main()
