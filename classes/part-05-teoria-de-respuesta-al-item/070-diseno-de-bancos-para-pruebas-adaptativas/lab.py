"""Laboratorio 070 - Diseno del banco de un CAT: cobertura y exposicion.

Dos bancos de 150 items 2PL: AMPLIO (dificultades -3..3) y ESTRECHO (concentrados en -1..1).
Test adaptativo de 15 items, 400 examinados con theta ~ N(0, 1.3) (hay colas).
Se mide el RMSE global y en las colas (|theta| > 1.5), y la exposicion de items (proporcion de
examinados que ve cada item) con dos reglas de seleccion:
  - maxima informacion pura,
  - "randomesque": elegir al azar entre los 5 mas informativos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N_BANCO, N_EXAM, LARGO = 150, 400, 15
GRID = [-4 + 0.1 * i for i in range(81)]
PRIOR = [math.exp(-0.5 * g * g) for g in GRID]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def eap(resp: list[tuple[float, float, int]]) -> float:
    num = den = 0.0
    for g, pr in zip(GRID, PRIOR, strict=True):
        w = pr
        for a, b, u in resp:
            p = logistica(a * (g - b))
            w *= p if u else 1 - p
        num += g * w
        den += w
    return num / den


def info(t: float, a: float, b: float) -> float:
    p = logistica(a * (t - b))
    return a * a * p * (1 - p)


def cat(banco, thetas, k_top: int, rng: random.Random):
    uso = [0] * len(banco)
    errores = []
    for th in thetas:
        resp, libres, est = [], set(range(len(banco))), 0.0
        for _ in range(LARGO):
            ranking = sorted(libres, key=lambda j: -info(est, *banco[j]))[:k_top]
            j = rng.choice(ranking)
            libres.discard(j)
            uso[j] += 1
            a, b = banco[j]
            resp.append((a, b, int(rng.random() < logistica(a * (th - b)))))
            est = eap(resp)
        errores.append(est - th)
    return errores, uso


def main() -> None:
    rng = random.Random(SEMILLA)
    thetas = [rng.gauss(0, 1.3) for _ in range(N_EXAM)]
    bancos = {"AMPLIO": [(rng.uniform(0.9, 1.9), rng.uniform(-3, 3)) for _ in range(N_BANCO)],
              "ESTRECHO": [(rng.uniform(0.9, 1.9), rng.uniform(-1, 1)) for _ in range(N_BANCO)]}
    print(f"{'banco / regla':<24} {'RMSE':>6} {'RMSE colas':>11} {'expos. max':>11} {'items sin uso':>14}")
    print("=" * 72)
    for nombre, banco in bancos.items():
        for regla, k in (("max. info", 1), ("randomesque", 5)):
            err, uso = cat(banco, thetas, k, rng)
            colas = [e for e, t in zip(err, thetas, strict=True) if abs(t) > 1.5]
            rm = lambda e: math.sqrt(sum(x * x for x in e) / len(e))  # noqa: E731
            print(f"{nombre + ' / ' + regla:<24} {rm(err):6.3f} {rm(colas):11.3f} "
                  f"{max(uso) / N_EXAM:11.2f} {sum(u == 0 for u in uso):14d}")
    print()
    print("Lectura: el banco estrecho mide peor en las colas: no tiene items que informen ahi.")
    print("La maxima informacion pura sobreexpone unos pocos items (riesgo de filtracion de un")
    print("banco de alto impacto) y deja muchos sin usar; la regla aleatorizada reparte la")
    print("exposicion con un costo pequeno de precision. Disenar el banco es decidir su cobertura.")


if __name__ == "__main__":
    main()
