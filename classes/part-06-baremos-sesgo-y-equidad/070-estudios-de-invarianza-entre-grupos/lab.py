"""Laboratorio 070 - Invarianza parcial y comparacion de medias de grupos.

Dos grupos con el MISMO rasgo medio. En el grupo B, `m` de 10 items tienen un desplazamiento
de intercepto (+delta): se asiente mas a igual rasgo (no invarianza escalar). Se compara la
diferencia estandarizada de la escala (d de Cohen) con TODOS los items y tras excluir los
items con desplazamiento (invarianza parcial: se conservan los items invariantes). Como el
laboratorio conoce cuales items estan desplazados, los excluye; en la practica se
identifican con modelos multigrupo (por ejemplo, comparando ajuste configural, metrico y
escalar; Cheung y Rensvold, 2002 sugieren delta CFI <= .01 como guia).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 4000, 10
CARGA = 0.7


def d_cohen(a: list[float], b: list[float]) -> float:
    sp = math.sqrt((statistics.variance(a) + statistics.variance(b)) / 2)
    return (statistics.fmean(b) - statistics.fmean(a)) / sp


def main() -> None:
    rng = random.Random(SEMILLA)
    theta_a = [rng.gauss(0, 1) for _ in range(N)]
    theta_b = [rng.gauss(0, 1) for _ in range(N)]
    print(f"{'items sesgados':>14} {'delta':>6} {'d (todos)':>10} {'d (solo invariantes)':>22}")
    print("=" * 56)
    for m, delta in ((0, 0.0), (1, 0.6), (3, 0.6), (5, 0.6), (3, 1.2)):
        sesgo = [delta if j < m else 0.0 for j in range(K)]

        def escala(theta, desp, todos=True):
            filas = []
            for t in theta:
                v = 0.0
                for j in range(K):
                    if not todos and sesgo[j] != 0:
                        continue
                    v += CARGA * t + desp[j] + rng.gauss(0, math.sqrt(1 - CARGA**2))
                filas.append(v)
            return filas

        d_todos = d_cohen(escala(theta_a, [0.0] * K), escala(theta_b, sesgo))
        d_inv = d_cohen(escala(theta_a, [0.0] * K, False), escala(theta_b, sesgo, False))
        print(f"{m:14d} {delta:6.1f} {d_todos:10.2f} {d_inv:22.2f}")
    print()
    print("Lectura: el rasgo medio es IGUAL, pero con items desplazados aparece una 'diferencia de")
    print("grupos' que es puro artefacto del instrumento y crece con la cantidad y el tamano del")
    print("desplazamiento. Al conservar solo items invariantes (invarianza parcial) vuelve a ~0.")
    print("Exige que haya suficientes items invariantes y justificacion sustantiva de los excluidos.")


if __name__ == "__main__":
    main()
