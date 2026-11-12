"""Laboratorio 108 - "Fortalezas distintivas": cuanto se repite el top-5 entre dos aplicaciones.

Lee la estructura de instruments/ipip-via-r.yaml (cuantas fortalezas y cuantos items por
fortaleza) y simula respuestas con fiabilidad por escala segun el numero de items (Spearman-Brown
desde r1 = 0.30 por item). Para cada persona se identifican las 5 fortalezas mas altas en dos
aplicaciones paralelas y se cuenta cuantas coinciden. Se compara con el azar (5 de 24 -> 1.04).
"""
from __future__ import annotations

import collections
import math
import pathlib
import random
import statistics

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]
SEMILLA = 20260819
N, R1 = 3000, 0.30


def main() -> None:
    d = yaml.safe_load((RAIZ / "instruments" / "ipip-via-r.yaml").read_text(encoding="utf-8"))
    por_escala = collections.Counter(it["escala"] for it in d["items"])
    fort = [c for c in por_escala if len(c) > 1 or c.isdigit() or True]
    # Las fortalezas son las escalas mas finas (las que tienen items directamente).
    k_items = sorted(por_escala.values())
    print(f"Instrumento {d['codigo']}: {len(d['items'])} items, {len(por_escala)} escalas con items; "
          f"items por escala: {k_items[0]}-{k_items[-1]}")
    n_f = len(por_escala)
    k = statistics.mode(por_escala.values())
    rel = k * R1 / (1 + (k - 1) * R1)
    print(f"Fiabilidad supuesta por escala de {k} items (r1 = {R1}): {rel:.2f}")
    rng = random.Random(SEMILLA)
    sd_e = math.sqrt((1 - rel) / rel)
    coinc = []
    for _ in range(N):
        t = [rng.gauss(0, 1) for _ in range(n_f)]
        a = [x + rng.gauss(0, sd_e) for x in t]
        b = [x + rng.gauss(0, sd_e) for x in t]
        top = lambda v: set(sorted(range(n_f), key=lambda i: -v[i])[:5])  # noqa: E731
        coinc.append(len(top(a) & top(b)))
    print(f"\nCoincidencia media del top-5 entre dos aplicaciones: {statistics.fmean(coinc):.2f} de 5")
    print(f"Azar puro (5 de {n_f}): {25 / n_f:.2f}")
    print(f"Personas con al menos 4 de 5 coincidentes: {sum(c >= 4 for c in coinc) / N:.1%}")
    print()
    print("Lectura: las fortalezas 'distintivas' de una persona cambian mucho entre aplicaciones porque")
    print("las escalas tienen pocos items y las fortalezas se parecen entre si. El top-5 es una lectura")
    print("conversacional, no un perfil estable; los instrumentos abiertos como IPIP-VIA-R sirven para")
    print("aprender y explorar, no para clasificar personas.")


if __name__ == "__main__":
    main()
