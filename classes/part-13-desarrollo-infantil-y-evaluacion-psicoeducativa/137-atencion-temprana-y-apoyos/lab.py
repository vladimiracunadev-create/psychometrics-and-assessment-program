"""Laboratorio 137 - Evaluar el progreso de un nino: diseno AB y solapamiento (NAP).

Datos de un caso unico: 8 mediciones de linea base (A) y 8 durante el apoyo (B) de una conducta
objetivo (mas = mejor). NAP = proporcion de pares (a, b) con b > a (mas 0.5 de empates), la
"no superposicion de todos los pares" (Parker y Vannest, 2009). Tres escenarios:
  1. efecto real del apoyo,
  2. sin efecto y sin tendencia,
  3. sin efecto pero con TENDENCIA previa de mejora (maduracion): el NAP engana.
Para cada escenario se simulan 2 000 casos y se informa NAP medio y % con NAP >= 0.90 (un umbral
que algunos autores llaman "efecto grande"; es una convencion).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
REPS, NA, NB = 2000, 8, 8


def nap(a: list[float], b: list[float]) -> float:
    pares = sum((y > x) + 0.5 * (y == x) for x in a for y in b)
    return pares / (len(a) * len(b))


def escenario(efecto: float, tendencia: float, rng: random.Random):
    naps = []
    for _ in range(REPS):
        base = [10 + tendencia * t + rng.gauss(0, 1.5) for t in range(NA)]
        trat = [10 + tendencia * (NA + t) + efecto + rng.gauss(0, 1.5) for t in range(NB)]
        naps.append(nap(base, trat))
    return naps


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'escenario':<40} {'NAP medio':>10} {'% con NAP >= 0.90':>19}")
    print("=" * 72)
    for nombre, e, t in (("1. efecto real (+3), sin tendencia", 3.0, 0.0),
                         ("2. sin efecto, sin tendencia", 0.0, 0.0),
                         ("3. sin efecto, con tendencia previa", 0.0, 0.5)):
        n = escenario(e, t, rng)
        print(f"{nombre:<40} {statistics.fmean(n):10.2f} {sum(x >= 0.90 for x in n) / REPS:19.1%}")
    print()
    print("Lectura: el NAP discrimina un efecto real, pero una tendencia de mejora previa (maduracion u")
    print("otro apoyo) produce 'efectos grandes' sin que el apoyo haga nada. Un diseno AB es debil:")
    print("se refuerza con linea base estable, replicacion (retirada, linea base multiple) y registro de")
    print("otros cambios. Medir el progreso informa decisiones de apoyo; no demuestra eficacia por si solo.")


if __name__ == "__main__":
    main()
