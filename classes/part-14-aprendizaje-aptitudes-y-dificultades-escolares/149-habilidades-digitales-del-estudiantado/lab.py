"""Laboratorio 149 - Autoinforme frente a desempeno en habilidades digitales.

Cada estudiante tiene una habilidad digital real. Se mide con (a) un autoinforme y (b) una tarea
de desempeno (resolver 6 problemas). Dos grupos: con y sin acceso previo a computadores en casa
(sin acceso: menos habilidad media). Hallazgos simulados:
  - la correlacion autoinforme-desempeno es moderada,
  - los grupos difieren distinto en autoinforme que en desempeno (sesgo de confianza diferencial),
  - quienes se autoevaluan "alto" pero rinden bajo (y al reves).
Supuestos del laboratorio; un marco de referencia (p. ej. DigComp) define las competencias y se
consulta en su version vigente.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 4000


def d_cohen(a: list[float], b: list[float]) -> float:
    sp = ((statistics.variance(a) + statistics.variance(b)) / 2) ** 0.5
    return (statistics.fmean(a) - statistics.fmean(b)) / sp


def main() -> None:
    rng = random.Random(SEMILLA)
    datos = []
    for _ in range(N):
        acceso = rng.random() < 0.6
        hab = rng.gauss(0.5 if acceso else -0.5, 1.0)
        auto = hab + (0.9 if acceso else 0.2) + rng.gauss(0, 0.9)          # mas confianza con acceso
        desemp = hab + rng.gauss(0, 0.6)
        datos.append((acceso, auto, desemp))
    a = [x for x in datos if x[0]]
    b = [x for x in datos if not x[0]]
    r = statistics.correlation([x[1] for x in datos], [x[2] for x in datos])
    print(f"Correlacion autoinforme - desempeno = {r:.2f}")
    print(f"Diferencia entre grupos (d): autoinforme = {d_cohen([x[1] for x in a], [x[1] for x in b]):.2f}; "
          f"desempeno = {d_cohen([x[2] for x in a], [x[2] for x in b]):.2f}")
    za = (statistics.fmean(x[1] for x in datos), statistics.pstdev(x[1] for x in datos))
    zd = (statistics.fmean(x[2] for x in datos), statistics.pstdev(x[2] for x in datos))
    alto_bajo = sum((x[1] - za[0]) / za[1] > 0.5 and (x[2] - zd[0]) / zd[1] < -0.5 for x in datos) / N
    bajo_alto = sum((x[1] - za[0]) / za[1] < -0.5 and (x[2] - zd[0]) / zd[1] > 0.5 for x in datos) / N
    print(f"Se creen 'altos' pero rinden 'bajo': {alto_bajo:.1%}; se creen 'bajos' pero rinden 'alto': {bajo_alto:.1%}")
    print()
    print("Lectura: el autoinforme mezcla habilidad con confianza, y la confianza difiere por contexto: una")
    print("diferencia entre grupos en autoinforme no equivale a una diferencia de habilidad. Una tarea de")
    print("desempeno es mas informativa, aunque mas costosa y sensible al dispositivo. Medir habilidades")
    print("digitales tambien implica considerar acceso y brechas: describir no es culpar al estudiante.")


if __name__ == "__main__":
    main()
