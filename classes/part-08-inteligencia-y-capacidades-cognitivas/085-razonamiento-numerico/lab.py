"""Laboratorio 085 - Items numericos con distractores basados en errores tipicos.

Item: "¿Cual es el X % de N?". Cada distractor corresponde a un error conceptual conocido:
    E1: confundir X% de N con N/X;   E2: sumar en vez de multiplicar;   E3: error de decimal.
Se simulan estudiantes con perfiles de error y se hace un analisis de distractores: la opcion
mas elegida por cada perfil debe coincidir con SU error, lo que da informacion diagnostica
(que corregir), ademas del puntaje.
"""
from __future__ import annotations

import collections
import random

SEMILLA = 20260819
PERFILES = {"domina": None, "confunde_division": "E1", "suma_en_vez_de_multiplicar": "E2",
            "error_de_decimal": "E3"}


def item(rng: random.Random) -> tuple[str, dict[str, int]]:
    x, n = rng.choice([10, 20, 25, 40, 50]), rng.choice([60, 80, 120, 200, 240])
    opciones = {"correcta": x * n // 100, "E1": n // x, "E2": x + n, "E3": x * n // 10}
    return f"{x}% de {n}", opciones


def responde(perfil: str | None, opciones: dict[str, int], rng: random.Random) -> str:
    if perfil is None:
        return "correcta" if rng.random() < 0.9 else rng.choice(list(opciones))
    return perfil if rng.random() < 0.7 else rng.choice(list(opciones))


def main() -> None:
    rng = random.Random(SEMILLA)
    items = [item(rng) for _ in range(40)]
    print("Ejemplo:", items[0][0], "->", items[0][1])
    print(f"\n{'perfil':<28} {'correcta':>9} {'E1':>5} {'E2':>5} {'E3':>5}   opcion mas elegida")
    print("=" * 78)
    for nombre, perfil in PERFILES.items():
        cuenta = collections.Counter()
        for _ in range(100):
            for _, ops in items:
                cuenta[responde(perfil, ops, rng)] += 1
        total = sum(cuenta.values())
        mas = cuenta.most_common(1)[0][0]
        print(f"{nombre:<28} {cuenta['correcta'] / total:9.2f} {cuenta['E1'] / total:5.2f} "
              f"{cuenta['E2'] / total:5.2f} {cuenta['E3'] / total:5.2f}   {mas}")
    print()
    print("Lectura: el analisis de distractores convierte un puntaje en un diagnostico: cada perfil")
    print("de error tiene una 'firma'. Los perfiles aqui son SINTETICOS; en la practica hay que")
    print("validar que el distractor refleje de verdad el error que se supone (entrevista cognitiva).")


if __name__ == "__main__":
    main()
