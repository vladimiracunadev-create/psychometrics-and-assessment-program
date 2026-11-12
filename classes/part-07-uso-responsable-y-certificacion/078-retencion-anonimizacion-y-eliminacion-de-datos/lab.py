"""Laboratorio 078 - k-anonimato: cuanto se puede reidentificar un conjunto "anonimizado".

Conjunto sintetico de 2 000 evaluados con tres cuasi-identificadores (edad, comuna, sexo) y
un resultado. Aunque se quiten nombre y RUT, la combinacion de cuasi-identificadores puede
singularizar a una persona. k = tamano del grupo mas pequeno que comparte la misma combinacion.
Se aplica generalizacion (edad en tramos, comuna en macrozona) y se mide k y el porcentaje de
personas unicas. Es una medida de riesgo basica; no garantiza anonimato (clase 079 sobre inferencia).
"""
from __future__ import annotations

import collections
import random

SEMILLA = 20260819
N = 2000
COMUNAS = [f"comuna{i:02d}" for i in range(40)]
MACRO = {c: f"zona{i // 10}" for i, c in enumerate(COMUNAS)}


def riesgo(filas: list[tuple]) -> tuple[int, float, float]:
    cuenta = collections.Counter(filas)
    k = min(cuenta.values())
    unicos = sum(1 for f in filas if cuenta[f] == 1) / len(filas)
    menores5 = sum(1 for f in filas if cuenta[f] < 5) / len(filas)
    return k, unicos, menores5


def main() -> None:
    rng = random.Random(SEMILLA)
    datos = [(rng.randint(18, 70), rng.choice(COMUNAS), rng.choice("MF")) for _ in range(N)]
    niveles = {
        "sin generalizar (edad, comuna, sexo)": datos,
        "edad en tramos de 10 anos": [(e // 10 * 10, c, s) for e, c, s in datos],
        "tramos de 10 + macrozona": [(e // 10 * 10, MACRO[c], s) for e, c, s in datos],
        "tramos de 20 + macrozona": [(e // 20 * 20, MACRO[c], s) for e, c, s in datos],
    }
    print(f"{'nivel de generalizacion':<40} {'k':>4} {'unicos':>8} {'grupos < 5':>11}")
    print("=" * 66)
    for nombre, filas in niveles.items():
        k, u, m5 = riesgo(filas)
        print(f"{nombre:<40} {k:4d} {u:8.1%} {m5:11.1%}")
    print()
    print("Lectura: quitar el nombre no anonimiza. Con tres campos corrientes, la mayoria queda")
    print("singularizada; generalizando se reduce el riesgo a costa de resolucion analitica.")
    print("Seudonimizar (cambiar identificadores por codigos) no es anonimizar: el dato sigue siendo")
    print("personal mientras exista la tabla de equivalencias o la reidentificacion sea razonable.")


if __name__ == "__main__":
    main()
