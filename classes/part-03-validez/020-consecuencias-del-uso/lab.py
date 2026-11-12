"""Laboratorio 020 - Consecuencias del uso: un mismo test, distintos efectos segun el corte.

Dos grupos con una diferencia media real en el puntaje del test de d = 0.5 DE
(la diferencia puede deberse a oportunidades, a sesgo del test o a ambas: el
laboratorio NO distingue las causas). Se calcula, segun el punto de corte, la tasa de
seleccion de cada grupo y la razon de impacto adverso. La regla de los cuatro quintos
(0.80) de las Uniform Guidelines (EEUU, 1978) se usa solo como alerta orientativa; no es
norma chilena ni prueba de discriminacion.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 50000
D = 0.5


def main() -> None:
    rng = random.Random(SEMILLA)
    g1 = [rng.gauss(0, 1) for _ in range(N)]
    g2 = [rng.gauss(-D, 1) for _ in range(N)]
    print(f"Diferencia media simulada: d = {D}. Razon = tasa del grupo 2 / tasa del grupo 1")
    print(f"{'corte (percentil global)':<26} {'tasa G1':>8} {'tasa G2':>8} {'razon':>7}  alerta 4/5")
    print("=" * 66)
    todos = sorted(g1 + g2)
    for pct in (10, 30, 50, 70, 90, 97):
        corte = todos[int(len(todos) * pct / 100)]
        t1 = statistics.fmean(a >= corte for a in g1)
        t2 = statistics.fmean(a >= corte for a in g2)
        print(f"{pct:<26} {t1:8.3f} {t2:8.3f} {t2 / t1:7.2f}  {'SI' if t2 / t1 < 0.8 else 'no'}")
    print()
    print("Lectura: cuanto mas selectivo el corte, mas cae la razon: la misma diferencia")
    print("pequena se amplifica en la cola. La consecuencia depende del USO (corte, peso en")
    print("la decision), no solo del test. Por eso las consecuencias son parte del argumento")
    print("de validez (Messick, 1995) y se evaluan ANTES de adoptar un instrumento.")


if __name__ == "__main__":
    main()
