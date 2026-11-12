"""Laboratorio 132 - Etapas o gradualidad: consistencia entre tareas del mismo "estadio".

Piaget describio estadios; la evidencia posterior muestra decalajes (distinto desempeno en tareas
supuestamente del mismo estadio) y gran influencia de la tarea y el contexto. Modelo: la
capacidad crece de forma continua con la edad; cada tarea tiene su propio umbral y un ruido de
tarea. Se calcula:
  - la proporcion de aciertos por edad en tres tareas "del mismo estadio",
  - la consistencia entre tareas dentro de cada nino (correlacion de aciertos),
  - el efecto de la ayuda del adulto (zona de desarrollo proximo): el umbral baja con andamiaje.
Datos sinteticos; el modelo es una ilustracion, no una prueba de ninguna teoria.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 4000


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def main() -> None:
    rng = random.Random(SEMILLA)
    umbrales = {"conservacion de numero": 5.0, "conservacion de liquido": 6.0, "conservacion de peso": 7.5}
    edades = [rng.uniform(4, 10) for _ in range(N)]
    cap = [0.9 * (e - 4) + rng.gauss(0, 0.6) for e in edades]          # capacidad individual
    print(f"{'edad':>5} " + " ".join(f"{t[-22:]:>24}" for t in umbrales))
    for lo in (4, 5, 6, 7, 8, 9):
        fila = []
        for _, u in umbrales.items():
            idx = [i for i in range(N) if lo <= edades[i] < lo + 1]
            fila.append(statistics.fmean(rng.random() < logistica(2.0 * (cap[i] - 0.9 * (u - 4))) for i in idx))
        print(f"{lo:5d} " + " ".join(f"{p:24.2f}" for p in fila))
    res = {t: [int(rng.random() < logistica(2.0 * (c - 0.9 * (u - 4)))) for c in cap] for t, u in umbrales.items()}
    nombres = list(res)
    r = statistics.correlation([float(x) for x in res[nombres[0]]], [float(x) for x in res[nombres[1]]])
    print(f"\nConsistencia entre dos tareas del 'mismo estadio' (phi de aciertos) = {r:.2f}")
    sin = statistics.fmean(rng.random() < logistica(2.0 * (c - 0.9 * 2.0)) for c in cap if c < 1.2)
    con = statistics.fmean(rng.random() < logistica(2.0 * (c + 0.8 - 0.9 * 2.0)) for c in cap if c < 1.2)
    print(f"Ninos de menor capacidad: aciertan solos {sin:.1%}; con andamiaje del adulto {con:.1%}")
    print()
    print("Lectura: el desempeno cambia de forma gradual y depende de la tarea; la consistencia entre")
    print("tareas es moderada. La ayuda del adulto cambia el resultado: lo que el nino hace solo y con")
    print("apoyo informa cosas distintas (Vygotsky). Evaluar es describir ambos, no asignar un estadio.")


if __name__ == "__main__":
    main()
