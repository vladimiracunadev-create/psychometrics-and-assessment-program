"""Laboratorio 164 - Entre personas y dentro de la persona: el problema de generalizar una asociacion.

Datos de diarios (100 personas x 30 dias). Estrategia de regulacion X (uso del dia) y afecto
negativo Y. Por construccion:
  - ENTRE personas: quienes usan mas la estrategia en promedio tienen MAS afecto negativo
    (la usan porque lo sienten mas),
  - DENTRO de la persona: los dias que la usa mas, su afecto negativo es MENOR.
Se calculan la correlacion agregada (promedios por persona), la agrupada ingenua (todos los dias
juntos) y la correlacion dentro de la persona (centrando por persona). Es el paradoja de Simpson
en datos intensivos longitudinales.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
PERSONAS, DIAS = 100, 30


def main() -> None:
    rng = random.Random(SEMILLA)
    xs, ys, px, py, xc, yc = [], [], [], [], [], []
    for _ in range(PERSONAS):
        base = rng.gauss(0, 1)                                  # nivel habitual de la persona
        dx = [base + rng.gauss(0, 1) for _ in range(DIAS)]
        # Entre personas: +0.8 por nivel base; dentro: -0.5 por desviacion del dia
        medx = statistics.fmean(dx)
        dy = [0.8 * base - 0.5 * (x - medx) + rng.gauss(0, 0.7) for x in dx]
        xs += dx
        ys += dy
        px.append(medx)
        py.append(statistics.fmean(dy))
        xc += [x - medx for x in dx]
        yc += [y - statistics.fmean(dy) for y in dy]
    print(f"{'analisis':<44} {'correlacion':>12}")
    print("=" * 58)
    print(f"{'ENTRE personas (promedios por persona)':<44} {statistics.correlation(px, py):12.2f}")
    print(f"{'agrupada ingenua (todos los dias juntos)':<44} {statistics.correlation(xs, ys):12.2f}")
    print(f"{'DENTRO de la persona (centrada)':<44} {statistics.correlation(xc, yc):12.2f}")
    print()
    print("Lectura: lo que es cierto entre personas (quien usa mas la estrategia siente mas afecto negativo)")
    print("puede ser lo contrario dentro de cada persona (los dias que la usa, se siente mejor). Un estudio")
    print("transversal no distingue ambos. Para hablar de 'regulacion emocional' de una persona se necesitan")
    print("datos intensivos de esa persona; una escala general describe tendencias, no el proceso diario.")


if __name__ == "__main__":
    main()
