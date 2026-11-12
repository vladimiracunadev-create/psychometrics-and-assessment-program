"""Laboratorio 107 - Medir valores: el estilo de respuesta oculta la estructura (centrado).

Seis valores con estructura circular conocida (vecinos se parecen, opuestos se oponen). Cada
persona tiene un "nivel general de uso de la escala" (estilo de respuesta) que sube todas
sus respuestas. Se calculan las correlaciones entre valores:
  - SIN corregir: dominadas por el estilo (todas positivas),
  - tras CENTRAR por la media de cada persona (corrige el estilo; Schwartz, 1992):
    reaparece el patron: vecinos positivos, opuestos negativos.
Se cuantifica con la correlacion promedio por distancia en el circulo. Nota: centrar convierte
las respuestas en parcialmente ipsativas (efecto -1/(k-1), clase 013).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 4000, 6


def main() -> None:
    rng = random.Random(SEMILLA)
    datos = []
    for _ in range(N):
        ang = rng.uniform(0, 2 * math.pi)
        estilo = rng.gauss(0, 1.0)
        datos.append([0.8 * math.cos(ang - k * math.pi / 3) + 1.2 * estilo + rng.gauss(0, 0.5) for k in range(K)])
    centrado = [[v - statistics.fmean(f) for v in f] for f in datos]

    def por_distancia(m: list[list[float]]) -> dict[int, float]:
        res: dict[int, list[float]] = {1: [], 2: [], 3: []}
        for i in range(K):
            for j in range(i + 1, K):
                d = min(j - i, K - (j - i))
                res[d].append(statistics.correlation([f[i] for f in m], [f[j] for f in m]))
        return {d: statistics.fmean(v) for d, v in res.items()}

    print(f"{'':<22} {'distancia 1':>12} {'distancia 2':>12} {'distancia 3 (opuestos)':>24}")
    print("=" * 74)
    for nombre, m in (("sin corregir", datos), ("centrado por persona", centrado)):
        r = por_distancia(m)
        print(f"{nombre:<22} {r[1]:12.2f} {r[2]:12.2f} {r[3]:24.2f}")
    print()
    print("Lectura: sin corregir, el estilo de respuesta hace que todos los valores correlacionen")
    print("positivo y la estructura (opuestos negativos) desaparece. El centrado la recupera, pero el")
    print("costo es que los puntajes pasan a ser relativos a la propia persona: dicen que valora MAS,")
    print("no cuanto valora. Elegir entre puntaje bruto y centrado depende de la pregunta.")


if __name__ == "__main__":
    main()
