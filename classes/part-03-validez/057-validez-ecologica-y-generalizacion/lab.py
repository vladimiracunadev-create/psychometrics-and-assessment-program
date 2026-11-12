"""Laboratorio 057 - Generalizacion: cuantas tareas hacen falta para un puntaje estable.

Diseno personas x tareas. Cada puntaje = persona + tarea + interaccion persona-tarea +
error. Se estiman los componentes de varianza por ANOVA (un solo juez) y se calcula el
coeficiente de generalizabilidad para n tareas:
    G(n) = var_persona / (var_persona + var_interaccion_y_error / n)
Muestra por que una sola tarea de laboratorio generaliza mal a otras situaciones: la
varianza especifica de la tarea (persona x tarea) no se promedia con una sola tarea.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N_PERSONAS, N_TAREAS = 400, 12
SD_PERSONA, SD_TAREA, SD_PXT = 1.0, 0.5, 1.2


def main() -> None:
    rng = random.Random(SEMILLA)
    persona = [rng.gauss(0, SD_PERSONA) for _ in range(N_PERSONAS)]
    tarea = [rng.gauss(0, SD_TAREA) for _ in range(N_TAREAS)]
    x = [[persona[p] + tarea[t] + rng.gauss(0, SD_PXT) for t in range(N_TAREAS)]
         for p in range(N_PERSONAS)]
    gm = statistics.fmean(v for f in x for v in f)
    mp = [statistics.fmean(f) for f in x]
    mt = [statistics.fmean(x[p][t] for p in range(N_PERSONAS)) for t in range(N_TAREAS)]
    msp = N_TAREAS * sum((m - gm) ** 2 for m in mp) / (N_PERSONAS - 1)
    sse = sum((x[p][t] - mp[p] - mt[t] + gm) ** 2
              for p in range(N_PERSONAS) for t in range(N_TAREAS))
    mse = sse / ((N_PERSONAS - 1) * (N_TAREAS - 1))
    var_p = (msp - mse) / N_TAREAS
    print(f"Varianza de persona estimada = {var_p:.2f} (real {SD_PERSONA ** 2:.2f})")
    print(f"Varianza persona x tarea + error = {mse:.2f} (real {SD_PXT ** 2:.2f})")
    print()
    print(f"{'tareas':>7} {'G estimado':>11}")
    for n in (1, 2, 4, 8, 12):
        print(f"{n:7d} {var_p / (var_p + mse / n):11.3f}")
    print()
    print("Lectura: con una sola tarea menos de la mitad de la varianza es 'persona'.")
    print("Generalizar a otras situaciones exige muestrear situaciones, no solo ítems.")


if __name__ == "__main__":
    main()
