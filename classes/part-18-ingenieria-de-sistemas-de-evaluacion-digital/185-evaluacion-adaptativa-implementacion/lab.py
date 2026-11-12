"""Laboratorio 185 - CAT con balance de contenido: el costo de las restricciones.

Banco de 240 items 2PL en 3 areas de contenido (80 cada una). Un CAT puro elige siempre el item de
maxima informacion y puede concentrar el test en un area. Un CAT con BALANCE exige que cada area
aporte 5 de los 15 items (cuotas). Se compara:
  - precision (RMSE de theta),
  - distribucion real de items por area (el CAT puro puede desbalancearse),
siendo la validez de contenido (clase 032) el motivo de las cuotas. Datos sinteticos; las
dificultades de las areas difieren a proposito (area 2 mas informativa para theta alta).
"""
from __future__ import annotations

import collections
import math
import random

SEMILLA = 20260819
POR_AREA, LARGO, N_EXAM = 80, 15, 150
GRID = [-4 + 0.1 * i for i in range(81)]
PRIOR = [math.exp(-0.5 * g * g) for g in GRID]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def eap(resp) -> float:
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


def cat(banco, balance: bool, theta: float, rng: random.Random):
    usados, resp, est = set(), [], 0.0
    cuenta = collections.Counter()
    for _ in range(LARGO):
        cand = [j for j in range(len(banco)) if j not in usados]
        if balance:
            validas = [j for j in cand if cuenta[banco[j][2]] < LARGO // 3]
            cand = validas or cand
        j = max(cand, key=lambda k: info(est, banco[k][0], banco[k][1]))
        usados.add(j)
        a, b, area = banco[j]
        cuenta[area] += 1
        resp.append((a, b, int(rng.random() < logistica(a * (theta - b)))))
        est = eap(resp)
    return est, cuenta


def main() -> None:
    rng = random.Random(SEMILLA)
    banco = []
    for area, (mb, ma) in enumerate(((0.0, 1.0), (0.3, 1.2), (-0.3, 1.8))):
        banco += [(max(0.6, rng.gauss(ma, 0.25)), rng.gauss(mb, 1.0), area) for _ in range(POR_AREA)]
    print(f"{'estrategia':<22} {'RMSE theta':>11} {'items por area (media)':>26} {'% tests con un area > 8':>25}")
    print("=" * 88)
    for nombre, bal in (("CAT puro", False), ("CAT con balance 5/5/5", True)):
        err, cuentas = [], []
        for _ in range(N_EXAM):
            t = rng.gauss(0, 1)
            est, c = cat(banco, bal, t, rng)
            err.append(est - t)
            cuentas.append(c)
        rmse = math.sqrt(sum(e * e for e in err) / len(err))
        media = [sum(c[a] for c in cuentas) / len(cuentas) for a in range(3)]
        desb = sum(max(c.values()) > 8 for c in cuentas) / len(cuentas)
        print(f"{nombre:<22} {rmse:11.3f} {str([round(m, 1) for m in media]):>26} {desb:25.0%}")
    print()
    print("Lectura: el CAT puro concentra los items en el area mas informativa (la 3), lo que compromete la")
    print("representatividad del contenido; el balance garantiza cobertura al costo de algo de precision.")
    print("La eleccion es de validez, no solo estadistica. Ademas se controla la exposicion (clase 060).")


if __name__ == "__main__":
    main()
