"""Laboratorio 127 - Aislamiento y liderazgo informal: estabilidad entre dos mediciones.

Grupo ficticio de 30 personas medido dos veces (olas 1 y 2) con 3 elecciones cada una. El
atractivo social de cada persona es estable pero cada nominacion tiene ruido. Se calcula:
  - aislados: personas que nadie elige (grado de entrada 0) en cada ola, y cuantos lo siguen
    siendo en la ola 2,
  - lideres informales: el 10 % con mayor grado de entrada; solapamiento entre olas.
El resultado: los aislados puntuales son frecuentes por azar y poco estables; el liderazgo
informal es mas estable. Datos sinteticos.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N, K, REPS = 30, 3, 300


def ola(atractivo: list[float], rng: random.Random) -> list[int]:
    entrada = [0] * N
    for i in range(N):
        otros = [j for j in range(N) if j != i]
        pesos = [2.718 ** (0.9 * atractivo[j]) for j in otros]
        sel: set[int] = set()
        while len(sel) < K:
            sel.add(rng.choices(otros, weights=pesos)[0])
        for j in sel:
            entrada[j] += 1
    return entrada


def main() -> None:
    rng = random.Random(SEMILLA)
    aisl1 = aisl_ambas = 0
    solap = []
    n_aislados_ola = []
    for _ in range(REPS):
        at = [rng.gauss(0, 1) for _ in range(N)]
        e1, e2 = ola(at, rng), ola(at, rng)
        a1 = {j for j in range(N) if e1[j] == 0}
        a2 = {j for j in range(N) if e2[j] == 0}
        n_aislados_ola.append(len(a1))
        aisl1 += len(a1)
        aisl_ambas += len(a1 & a2)
        top = max(1, N // 10)
        l1 = set(sorted(range(N), key=lambda j: -e1[j])[:top])
        l2 = set(sorted(range(N), key=lambda j: -e2[j])[:top])
        solap.append(len(l1 & l2) / top)
    print(f"Personas que nadie elige en la ola 1: {aisl1 / REPS:.1f} de {N} (media de {REPS} grupos)")
    print(f"  de ellas, siguen sin ser elegidas en la ola 2: {aisl_ambas / aisl1:.1%}")
    print(f"Solapamiento del 10 % de mayor grado de entrada entre olas (liderazgo informal): "
          f"{sum(solap) / REPS:.1%}")
    print()
    print("Lectura: una sola medicion sobreestima el aislamiento: muchos 'no elegidos' de hoy son elegidos")
    print("manana. Antes de intervenir, un patron de aislamiento se confirma con mediciones repetidas y")
    print("con observacion o entrevista. Un resultado sociometrico nunca se comunica al grupo.")


if __name__ == "__main__":
    main()
