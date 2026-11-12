"""Laboratorio 044 - Velocidad y potencia: lo que hace un limite de tiempo.

Una prueba de 40 items con tiempo limitado. Cada persona tiene una habilidad (theta) y una
velocidad (tau) correlacionadas 0.3. El tiempo por item crece con la dificultad y baja con la
velocidad; al agotarse el tiempo, los items no alcanzados quedan sin responder y cuentan como
incorrectos. Se compara una prueba de POTENCIA (sin limite) con una limitada:
  - proporcion de items no alcanzados por posicion,
  - correlacion del puntaje con la habilidad y con la velocidad,
  - fiabilidad (alfa) de ambas.
Datos sinteticos.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 1500, 40
LIMITE = 28.0     # minutos disponibles


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def alfa(m: list[list[int]]) -> float:
    k = len(m[0])
    cols = list(zip(*m, strict=True))
    tot = [sum(f) for f in m]
    return k / (k - 1) * (1 - sum(statistics.pvariance(c) for c in cols) / statistics.pvariance(tot))


def main() -> None:
    rng = random.Random(SEMILLA)
    personas = []
    for _ in range(N):
        th = rng.gauss(0, 1)
        tau = 0.3 * th + math.sqrt(1 - 0.09) * rng.gauss(0, 1)
        personas.append((th, tau))
    dif = [-1.5 + 3.0 * j / (K - 1) for j in range(K)]
    pot, lim = [], []
    no_alc = [0] * K
    for th, tau in personas:
        reloj = 0.0
        fila_p, fila_l = [], []
        for j, b in enumerate(dif):
            correcta = int(rng.random() < logistica(1.2 * (th - b)))
            reloj += math.exp(0.1 - 0.35 * tau + 0.2 * b) * 0.9 + rng.uniform(0, 0.2)
            fila_p.append(correcta)
            if reloj <= LIMITE:
                fila_l.append(correcta)
            else:
                fila_l.append(0)
                no_alc[j] += 1
        pot.append(fila_p)
        lim.append(fila_l)
    sp, sl = [sum(f) for f in pot], [sum(f) for f in lim]
    th = [p[0] for p in personas]
    ta = [p[1] for p in personas]
    print("Items no alcanzados por posicion (%): " + ", ".join(f"{j + 1}:{no_alc[j] / N:.0%}" for j in (0, 19, 29, 34, 39)))
    print(f"\n{'':<22} {'r con habilidad':>16} {'r con velocidad':>16} {'alfa':>6}")
    print("=" * 66)
    print(f"{'prueba de potencia':<22} {statistics.correlation(sp, th):16.2f} {statistics.correlation(sp, ta):16.2f} {alfa(pot):6.2f}")
    print(f"{'prueba con limite':<22} {statistics.correlation(sl, th):16.2f} {statistics.correlation(sl, ta):16.2f} {alfa(lim):6.2f}")
    print()
    print("Lectura: el limite de tiempo mezcla habilidad con velocidad: el puntaje correlaciona mas con la rapidez")
    print("y los ultimos items dejan de ser 'dificiles' para ser 'no alcanzados'. El alfa casi no cambia, de modo que")
    print("NO delata el problema: la fiabilidad alta no prueba que se mida habilidad. Si se quiere medir")
    print("habilidad, el tiempo debe ser holgado; si se quiere medir velocidad, debe declararse (clase 044).")


if __name__ == "__main__":
    main()
