"""Laboratorio 013 - La trampa de la elección forzada.

Se generan k escalas INDEPENDIENTES (correlacion verdadera 0) y se convierten a
formato ipsativo restando a cada persona su propia media. Resultado: las escalas
suman una constante y correlacionan negativamente por construccion, con valor
medio -1/(k-1), sin que exista ninguna relacion real entre los rasgos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 5000


def media_correlaciones(cols: list[list[float]]) -> float:
    k = len(cols)
    rs = [statistics.correlation(cols[i], cols[j]) for i in range(k) for j in range(i + 1, k)]
    return statistics.fmean(rs)


def main() -> None:
    rng = random.Random(SEMILLA)
    print("Correlacion media entre escalas (rasgos realmente independientes)")
    print("=" * 66)
    print(f"{'k escalas':>9} {'normativo':>10} {'ipsativo':>10} {'-1/(k-1)':>10}")
    for k in (3, 4, 6, 8):
        norm = [[rng.gauss(0, 1) for _ in range(N)] for _ in range(k)]
        ips = [[] for _ in range(k)]
        for p in range(N):
            m = statistics.fmean(c[p] for c in norm)
            for c in range(k):
                ips[c].append(norm[c][p] - m)
        suma_max = max(abs(sum(ips[c][p] for c in range(k))) for p in range(N))
        print(f"{k:9d} {media_correlaciones(norm):10.3f} "
              f"{media_correlaciones(ips):10.3f} {-1 / (k - 1):10.3f}"
              f"   (suma por persona: {suma_max:.1e})")
    print()
    print("Lectura: el formato ipsativo fabrica correlaciones negativas. Sirve para")
    print("ordenar preferencias DENTRO de una persona, no para compararla con otras.")


if __name__ == "__main__":
    main()
