"""Laboratorio 122 - Agregar valoraciones de un equipo: acuerdo (rwg) y CCI.

60 lideres, cada uno valorado por los 6 integrantes de su equipo en una escala 1-5. Para
justificar que el promedio del equipo represente al lider se necesitan dos cosas:
  - ACUERDO dentro del equipo: rwg = 1 - s^2 / sigma_nula^2, con nula uniforme (A^2-1)/12 = 2.0 (James, Demaree y Wolf, 1984);
  - DIFERENCIAS entre equipos: CCI(1) y CCI(2) = fiabilidad del promedio del equipo.
Dos condiciones: lideres con efecto real (los equipos coinciden) y sin efecto (cada integrante
valora por su cuenta).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
LIDERES, EQ = 60, 6
NULA = (5 ** 2 - 1) / 12


def clip(x: float) -> float:
    return max(1.0, min(5.0, round(x)))


def analiza(sd_lider: float, sd_ind: float, rng: random.Random) -> tuple[float, float, float]:
    equipos = []
    for _ in range(LIDERES):
        base = 3.0 + rng.gauss(0, sd_lider)
        equipos.append([clip(base + rng.gauss(0, sd_ind)) for _ in range(EQ)])
    rwg = statistics.fmean(max(0.0, 1 - statistics.variance(e) / NULA) for e in equipos)
    mg = statistics.fmean(v for e in equipos for v in e)
    msb = EQ * sum((statistics.fmean(e) - mg) ** 2 for e in equipos) / (LIDERES - 1)
    msw = sum((v - statistics.fmean(e)) ** 2 for e in equipos for v in e) / (LIDERES * (EQ - 1))
    icc1 = (msb - msw) / (msb + (EQ - 1) * msw)
    icc2 = (msb - msw) / msb
    return rwg, icc1, icc2


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'condicion':<46} {'rwg medio':>10} {'CCI(1)':>7} {'CCI(2)':>7}")
    print("=" * 74)
    for nombre, sl, si in (("lideres distintos, integrantes coinciden", 0.9, 0.5),
                           ("lideres iguales, cada uno valora distinto", 0.1, 1.2)):
        rwg, i1, i2 = analiza(sl, si, rng)
        print(f"{nombre:<46} {rwg:10.2f} {i1:7.2f} {i2:7.2f}")
    print()
    print("Lectura: para agregar al nivel del equipo se pide acuerdo (rwg alto) Y diferencias entre")
    print("equipos (CCI(1) apreciable). En la segunda condicion el promedio del equipo casi no tiene")
    print("fiabilidad: describe al evaluador, no al lider. Las convenciones (p. ej. rwg > 0.70, CCI(2) > 0.70)")
    print("son guias, y rwg depende de la distribucion nula que se elija (aqui, uniforme).")


if __name__ == "__main__":
    main()
