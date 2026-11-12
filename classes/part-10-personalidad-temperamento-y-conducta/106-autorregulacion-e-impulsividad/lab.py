"""Laboratorio 106 - Descuento temporal: estimar k de un descuento hiperbolico.

Valor presente de una recompensa R con demora D: V = R / (1 + k*D). Cada persona elige entre
$X ahora y $100 en D dias; elige lo demorado si V >= X (con ruido logistico). Se estima k por
maxima verosimilitud en una rejilla, y se compara el k estimado con el verdadero. Una k mayor
= mas impulsividad en esta tarea. Tambien se contrasta con una escala autoinformada simulada
(tipo BIS-11) para mostrar que ambos indicadores correlacionan poco (impulsividad no es una
sola cosa; autoinforme y tarea miden aspectos distintos).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 300
DEMORAS = (7, 30, 90, 180)
INMEDIATOS = (10, 25, 40, 55, 70, 85, 95)


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def elige_demorado(k: float, d: int, x: float, rng: random.Random, ruido: float = 6.0) -> bool:
    v = 100 / (1 + k * d)
    return rng.random() < logistica((v - x) / ruido)


def estima_k(elecciones: list[tuple[int, float, bool]]) -> float:
    mejor, mejor_ll = 0.0, -1e18
    for i in range(1, 400):
        k = i / 1000                                   # 0.001 .. 0.399
        ll = 0.0
        for d, x, dem in elecciones:
            p = logistica((100 / (1 + k * d) - x) / 6.0)
            ll += math.log(p if dem else 1 - p)
        if ll > mejor_ll:
            mejor, mejor_ll = k, ll
    return mejor


def main() -> None:
    rng = random.Random(SEMILLA)
    ks, khat, auto = [], [], []
    for _ in range(N):
        k = math.exp(rng.gauss(math.log(0.03), 0.8))
        el = [(d, x, elige_demorado(k, d, x, rng)) for d in DEMORAS for x in INMEDIATOS]
        ks.append(k)
        khat.append(estima_k(el))
        auto.append(0.15 * math.log(k) + rng.gauss(0, 1))          # autoinforme debilmente ligado
    lk, lh = [math.log(v) for v in ks], [math.log(v) for v in khat]
    print(f"Elecciones por persona: {len(DEMORAS) * len(INMEDIATOS)} | personas: {N}")
    print(f"k verdadera mediana = {statistics.median(ks):.3f}; k estimada mediana = {statistics.median(khat):.3f}")
    print(f"r(log k verdadera, log k estimada)  = {statistics.correlation(lk, lh):.3f}")
    print(f"r(log k estimada, autoinforme)      = {statistics.correlation(lh, auto):.3f}")
    print()
    print("Lectura: con 28 elecciones el parametro k se recupera bien, pero la tarea y el autoinforme")
    print("casi no se relacionan: 'impulsividad' agrupa constructos distintos (preferencia temporal,")
    print("control inhibitorio, busqueda de sensaciones). Una escala como la BIS-11 describe el")
    print("autoinforme, no sustituye una tarea conductual ni un diagnostico.")


if __name__ == "__main__":
    main()
