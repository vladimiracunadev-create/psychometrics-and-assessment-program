"""Laboratorio 126 - Metricas de red sobre una sociomatriz sintetica.

Dos cursos ficticios de 24 estudiantes con 3 elecciones cada uno:
  - ALEATORIO: las elecciones se reparten al azar;
  - CON SUBGRUPOS: dos grupos de 12 y las elecciones son mayormente dentro del grupo.
Metricas: densidad, reciprocidad (proporcion de elecciones devueltas), concentracion (indice de
centralizacion de grado de entrada), numero de componentes debilmente conexos y proporcion de
elecciones dentro del grupo (homofilia). Sin personas reales.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N, K = 24, 3


def genera(prob_dentro: float, rng: random.Random) -> list[set[int]]:
    elige = []
    for i in range(N):
        grupo = i // 12
        sel: set[int] = set()
        while len(sel) < K:
            if rng.random() < prob_dentro:
                j = rng.choice([x for x in range(grupo * 12, grupo * 12 + 12) if x != i])
            else:
                j = rng.choice([x for x in range(N) if x != i])
            sel.add(j)
        elige.append(sel)
    return elige


def componentes(elige: list[set[int]]) -> int:
    ady = {i: set() for i in range(N)}
    for i, s in enumerate(elige):
        for j in s:
            ady[i].add(j)
            ady[j].add(i)
    vistos, c = set(), 0
    for i in range(N):
        if i in vistos:
            continue
        c += 1
        pila = [i]
        while pila:
            u = pila.pop()
            if u not in vistos:
                vistos.add(u)
                pila.extend(ady[u] - vistos)
    return c


def metricas(elige: list[set[int]]) -> dict[str, float]:
    total = sum(len(s) for s in elige)
    recip = sum(1 for i, s in enumerate(elige) for j in s if i in elige[j])
    grado = [sum(1 for s in elige if j in s) for j in range(N)]
    cmax = max(grado)
    central = sum(cmax - g for g in grado) / ((N - 1) * (N - 2))      # Freeman, grado de entrada (aprox.)
    dentro = sum(1 for i, s in enumerate(elige) for j in s if i // 12 == j // 12)
    return {"densidad": total / (N * (N - 1)), "reciprocidad": recip / total,
            "centralizacion (entrada)": central, "componentes": componentes(elige),
            "elecciones dentro del grupo": dentro / total}


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'metrica':<30} {'aleatorio':>10} {'con subgrupos':>14}")
    print("=" * 58)
    a, b = metricas(genera(0.0, rng)), metricas(genera(0.95, rng))
    for k in a:
        print(f"{k:<30} {a[k]:10.3f} {b[k]:14.3f}")
    print()
    print("Lectura: en el curso 'aleatorio' ~48 % de las elecciones cae dentro del grupo por simple")
    print("azar (11 de 23 posibles); con subgrupos sube a ~96 % y la reciprocidad se triplica. La")
    print("estructura se detecta comparando contra un modelo nulo, no mirando la metrica aislada. Los")
    print("graficos de redes con menores se comparten solo de forma anonimizada y con un fin pedagogico.")


if __name__ == "__main__":
    main()
