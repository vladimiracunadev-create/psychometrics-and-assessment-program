"""Laboratorio 096 - Aprendizaje de listas: indices derivados y su incertidumbre.

Lista de 15 palabras repetida en 5 ensayos, evocacion tras interferencia y tras 20 minutos.
Cada persona tiene una tasa de aprendizaje y una tasa de olvido. Indices:
  aprendizaje total = suma de los 5 ensayos; ganancia = ensayo 5 - ensayo 1;
  retencion = diferido / ensayo 5; intrusiones = palabras no presentadas.
Se calcula la fiabilidad entre dos formas paralelas de la lista y el error tipico de cada
indice (los indices "derivados" como retencion y ganancia son los menos fiables).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 800, 15


def sesion(habil: float, olvido: float, rng: random.Random) -> dict[str, float]:
    ensayos = []
    for t in range(1, 6):
        p = 1 - math.exp(-(0.18 + 0.12 * habil) * t)
        ensayos.append(sum(rng.random() < p for _ in range(K)))
    p_dif = max(0.02, ensayos[-1] / K * (1 - olvido))
    diferido = sum(rng.random() < p_dif for _ in range(K))
    intrus = sum(rng.random() < 0.04 for _ in range(5))
    return {"aprendizaje total": sum(ensayos), "ganancia": ensayos[4] - ensayos[0],
            "retencion": diferido / max(1, ensayos[4]), "intrusiones": intrus}


def main() -> None:
    rng = random.Random(SEMILLA)
    a, b = [], []
    for _ in range(N):
        h, o = rng.gauss(0, 1), min(0.6, max(0.0, rng.gauss(0.2, 0.1)))
        a.append(sesion(h, o, rng))
        b.append(sesion(h, o, rng))
    print(f"{'indice':<20} {'media':>7} {'DE':>6} {'fiab. formas paralelas':>24}")
    print("=" * 62)
    for k in a[0]:
        x, y = [s[k] for s in a], [s[k] for s in b]
        print(f"{k:<20} {statistics.fmean(x):7.2f} {statistics.pstdev(x):6.2f} {statistics.correlation(x, y):24.3f}")
    print()
    print("Lectura: el aprendizaje total es el indice mas fiable porque usa todos los ensayos; la")
    print("ganancia y la retencion (cocientes y diferencias) pierden fiabilidad, y las intrusiones,")
    print("por ser eventos raros, casi no son fiables. Se informa cada indice con su error y se evita")
    print("interpretar indices derivados individualmente sin evidencia (clases 025 y 087).")


if __name__ == "__main__":
    main()
