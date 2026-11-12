"""Laboratorio 055 - Testing adaptativo informatizado (CAT) frente a un test fijo.

Banco de 300 items 2PL. Para cada examinado simulado se compara:
  - CAT: arranca en theta = 0, elige el item NO usado de maxima informacion en la estimacion
    actual (EAP con prior normal), y termina con error tipico < 0.30 o a los 30 items;
  - Test fijo: 20 items al azar del banco.
Resultados: items administrados y RMSE de theta. El CAT es una tecnologia que depende de un
banco calibrado y de supuestos del modelo; aqui los parametros se conocen (caso ideal).
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N_BANCO, N_EXAM = 300, 300
GRID = [-4 + 0.1 * i for i in range(81)]
PRIOR = [math.exp(-0.5 * g * g) for g in GRID]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def eap(resp: list[tuple[float, float, int]]) -> tuple[float, float]:
    post = []
    for g, pr in zip(GRID, PRIOR, strict=True):
        w = pr
        for a, b, u in resp:
            p = logistica(a * (g - b))
            w *= p if u else 1 - p
        post.append(w)
    s = sum(post)
    m = sum(g * w for g, w in zip(GRID, post, strict=True)) / s
    sd = math.sqrt(sum((g - m) ** 2 * w for g, w in zip(GRID, post, strict=True)) / s)
    return m, sd


def info(t: float, a: float, b: float) -> float:
    p = logistica(a * (t - b))
    return a * a * p * (1 - p)


def main() -> None:
    rng = random.Random(SEMILLA)
    banco = [(rng.uniform(0.8, 2.0), rng.gauss(0, 1.2)) for _ in range(N_BANCO)]
    err_cat, err_fijo, usados = [], [], []
    for _ in range(N_EXAM):
        theta = rng.gauss(0, 1)
        # CAT
        resp, libres, est, sd = [], set(range(N_BANCO)), 0.0, 1.0
        while len(resp) < 30 and (len(resp) < 5 or sd > 0.30):
            j = max(libres, key=lambda k: info(est, *banco[k]))
            libres.discard(j)
            a, b = banco[j]
            resp.append((a, b, int(rng.random() < logistica(a * (theta - b)))))
            est, sd = eap(resp)
        err_cat.append(est - theta)
        usados.append(len(resp))
        # Test fijo de 20 items
        fijo = []
        for j in rng.sample(range(N_BANCO), 20):
            a, b = banco[j]
            fijo.append((a, b, int(rng.random() < logistica(a * (theta - b)))))
        err_fijo.append(eap(fijo)[0] - theta)
    rmse = lambda e: math.sqrt(sum(x * x for x in e) / len(e))  # noqa: E731
    print(f"{'':<22} {'items (media)':>14} {'RMSE theta':>11}")
    print("=" * 50)
    print(f"{'CAT (SE < 0.30)':<22} {sum(usados) / N_EXAM:14.1f} {rmse(err_cat):11.3f}")
    print(f"{'Fijo, 20 al azar':<22} {20:14.1f} {rmse(err_fijo):11.3f}")
    print()
    print("Lectura: el CAT logra precision comparable o mejor con menos items, porque cada item")
    print("se elige para dar la maxima informacion en el nivel de ESA persona. Costos: exige un")
    print("banco amplio y calibrado, control de exposicion de items (clase 060) y equidad en la")
    print("experiencia de quien responde (cada persona ve un test distinto).")


if __name__ == "__main__":
    main()
