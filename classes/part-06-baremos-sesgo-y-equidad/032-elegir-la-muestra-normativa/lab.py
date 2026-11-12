"""Laboratorio 032 - La muestra normativa: a quien se compara la persona.

Poblacion con tres niveles educativos (40 % basica, 40 % media, 20 % superior). El puntaje
sube con la educacion. Se construyen tres baremos y se compara el percentil que asignan a
una persona con puntaje 105:
  - POBLACIONAL (muestra aleatoria),
  - CONVENIENCIA (muestra reclutada en una universidad: 70 % superior),
  - CONVENIENCIA PONDERADA (post-estratificacion: se reponderan los estratos a su peso real).
"""
from __future__ import annotations

import random

SEMILLA = 20260819
PESOS = {"basica": 0.40, "media": 0.40, "superior": 0.20}
MEDIAS = {"basica": 92.0, "media": 100.0, "superior": 112.0}
DE = 14.0


def muestra(prop: dict[str, float], n: int, rng: random.Random) -> list[tuple[str, float]]:
    estratos = list(prop)
    return [(e, rng.gauss(MEDIAS[e], DE))
            for e in rng.choices(estratos, weights=[prop[x] for x in estratos], k=n)]


def percentil(datos: list[tuple[str, float]], v: float, pesos: dict[str, float] | None = None) -> float:
    if pesos is None:
        return 100 * sum(x < v for _, x in datos) / len(datos)
    tot = {e: sum(1 for g, _ in datos if g == e) for e in pesos}
    num = sum(pesos[g] / tot[g] for g, x in datos if x < v)
    return 100 * num


def main() -> None:
    rng = random.Random(SEMILLA)
    poblacional = muestra(PESOS, 20000, rng)
    conveniencia = muestra({"basica": 0.05, "media": 0.25, "superior": 0.70}, 3000, rng)
    print("Percentil asignado al puntaje 105:")
    print(f"  baremo poblacional                 : {percentil(poblacional, 105):5.1f}")
    print(f"  baremo de conveniencia (universidad): {percentil(conveniencia, 105):5.1f}")
    print(f"  conveniencia reponderada            : {percentil(conveniencia, 105, PESOS):5.1f}")
    print()
    print("Lectura: la misma persona, con el mismo puntaje, queda 'sobre la media' o 'bajo la")
    print("media' segun contra quien se la compare. La reponderacion corrige la composicion")
    print("conocida (educacion), no el resto de las diferencias entre la muestra y la poblacion.")
    print("Por eso la ficha de un baremo debe declarar: quienes, cuando, donde, cuantos y como se eligieron.")


if __name__ == "__main__":
    main()
