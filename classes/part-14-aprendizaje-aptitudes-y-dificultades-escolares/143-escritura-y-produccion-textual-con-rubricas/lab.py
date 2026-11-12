"""Laboratorio 143 - Estudio D (decision) de un puntaje de escritura: cuantas tareas y cuantos jueces.

Diseno personas x tareas x jueces (cruzado). Componentes de varianza SUPUESTOS (en la practica se
estiman con un estudio G):
    persona 1.00 | tarea 0.20 | juez 0.15 | persona x tarea 0.80 | persona x juez 0.30 | residual 0.50
Coeficiente de generalizabilidad relativo para n_t tareas y n_j jueces:
    G = var_p / ( var_p + var_pt/n_t + var_pj/n_j + var_ptj,e/(n_t*n_j) )
Se tabula G y se simula un estudio con 300 estudiantes para comprobar el calculo.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
V = {"p": 1.0, "t": 0.20, "j": 0.15, "pt": 0.80, "pj": 0.30, "e": 0.50}


def g_rel(nt: int, nj: int) -> float:
    return V["p"] / (V["p"] + V["pt"] / nt + V["pj"] / nj + V["e"] / (nt * nj))


def simula(nt: int, nj: int, n: int, rng: random.Random) -> float:
    tarea = [rng.gauss(0, math.sqrt(V["t"])) for _ in range(nt)]
    juez = [rng.gauss(0, math.sqrt(V["j"])) for _ in range(nj)]
    ver, prom = [], []
    for _ in range(n):
        p = rng.gauss(0, math.sqrt(V["p"]))
        pt = [rng.gauss(0, math.sqrt(V["pt"])) for _ in range(nt)]
        pj = [rng.gauss(0, math.sqrt(V["pj"])) for _ in range(nj)]
        obs = [p + tarea[t] + juez[j] + pt[t] + pj[j] + rng.gauss(0, math.sqrt(V["e"]))
               for t in range(nt) for j in range(nj)]
        prom.append(statistics.fmean(obs))
        ver.append(p)
    return statistics.correlation(prom, ver) ** 2


def main() -> None:
    print("Coeficiente G relativo segun el diseno (filas: tareas; columnas: jueces)")
    print(f"{'':>8}" + "".join(f"{f'{j} juez(es)':>12}" for j in (1, 2, 3)))
    for nt in (1, 2, 3, 4, 6):
        print(f"{nt:5d} t. " + "".join(f"{g_rel(nt, nj):12.2f}" for nj in (1, 2, 3)))
    rng = random.Random(SEMILLA)
    print(f"\nVerificacion por simulacion (300 estudiantes, 2 tareas x 2 jueces): "
          f"G teorico = {g_rel(2, 2):.2f}; r^2 simulado = {statistics.fmean(simula(2, 2, 300, rng) for _ in range(40)):.2f}")
    print()
    print("Lectura: agregar tareas mejora mas la fiabilidad que agregar jueces, porque la mayor fuente de")
    print("error es la variacion persona x tarea (un estudiante escribe distinto segun el tema). Una sola")
    print("tarea con varios jueces no basta. Con rubricas claras y jueces calibrados, el error de juez baja.")
    print("Los componentes aqui son supuestos; un estudio real los estima con un diseno cruzado.")


if __name__ == "__main__":
    main()
