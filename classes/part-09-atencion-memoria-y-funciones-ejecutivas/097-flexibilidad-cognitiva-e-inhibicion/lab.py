"""Laboratorio 097 - La "paradoja de la fiabilidad": efectos robustos, medidas individuales pobres.

Un efecto Stroop (incongruente - congruente) es muy robusto en el promedio del grupo, pero
las diferencias entre personas son pequenas frente al ruido de ensayo a ensayo. Se simula:
  RT = RT_base_persona + efecto_persona * incongruente + ruido de ensayo.
Se compara la fiabilidad por mitades del RT medio (alta) con la del EFECTO (una diferencia,
mucho menor), con distintas cantidades de ensayos (Hedge, Powell y Sumner, 2018).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 1000


def datos(ensayos: int, rng: random.Random):
    pares, impares, medias_p, medias_i = [], [], [], []
    for _ in range(N):
        base = rng.gauss(650, 80)
        efecto = rng.gauss(60, 15)                       # efecto Stroop individual
        ens = [(base + (efecto if inc else 0) + rng.gauss(0, 120), inc)
               for inc in ([True, False] * ensayos)]
        def eff(sub):
            i = [r for r, inc in sub if inc]
            c = [r for r, inc in sub if not inc]
            return statistics.fmean(i) - statistics.fmean(c)
        pares.append(eff(ens[0::4] + ens[1::4]))
        impares.append(eff(ens[2::4] + ens[3::4]))
        medias_p.append(statistics.fmean(r for r, _ in ens[0::2]))
        medias_i.append(statistics.fmean(r for r, _ in ens[1::2]))
    return pares, impares, medias_p, medias_i, statistics.fmean(pares + impares)


def sb(r: float) -> float:
    return 2 * r / (1 + r)


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'ensayos/cond.':>14} {'efecto medio (ms)':>18} {'fiab. RT medio':>15} {'fiab. del EFECTO':>17}")
    print("=" * 68)
    for n in (20, 60, 200):
        ep, ei, mp, mi, efecto = datos(n, rng)
        print(f"{n:14d} {efecto:18.1f} {sb(statistics.correlation(mp, mi)):15.3f} "
              f"{sb(statistics.correlation(ep, ei)):17.3f}")
    print()
    print("Lectura: el efecto promedio es estable (~60 ms) y el RT medio es fiable, pero el efecto")
    print("individual necesita cientos de ensayos para ser aceptable. Un efecto que nadie discute en")
    print("el grupo puede ser una mala medida diferencial; no se interpreta como rasgo sin esa evidencia.")


if __name__ == "__main__":
    main()
