"""Laboratorio 052 - Modelo de Rasch: estimacion conjunta de personas e items.

    P(acierto) = logistica(theta_persona - b_item)

Estimacion por maxima verosimilitud conjunta (JMLE) con Newton-Raphson alternado:
  1. theta de cada persona dado b; 2. b de cada item dado theta; 3. centrar b en media 0.
Las personas con puntaje 0 o perfecto no tienen estimacion finita y se excluyen. JMLE sesga
las dificultades; se aplica la correccion habitual (K-1)/K. Es una implementacion DIDACTICA:
para trabajo real se usan paquetes revisados (eRm, TAM, mirt).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 800, 15


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def main() -> None:
    rng = random.Random(SEMILLA)
    b_real = [-2.0 + 4.0 * i / (K - 1) for i in range(K)]
    th_real = [rng.gauss(0, 1) for _ in range(N)]
    datos = [[int(rng.random() < logistica(t - b)) for b in b_real] for t in th_real]

    validos = [i for i, f in enumerate(datos) if 0 < sum(f) < K]
    x = [datos[i] for i in validos]
    th_ref = [th_real[i] for i in validos]
    n = len(x)
    b = [0.0] * K
    th = [math.log(sum(f) / (K - sum(f))) for f in x]
    for _ in range(40):
        for p in range(n):
            for _ in range(3):
                pr = [logistica(th[p] - bj) for bj in b]
                g = sum(x[p]) - sum(pr)
                h = -sum(q * (1 - q) for q in pr)
                th[p] = max(-6, min(6, th[p] - g / h))
        for j in range(K):
            for _ in range(3):
                pr = [logistica(th[p] - b[j]) for p in range(n)]
                g = -(sum(x[p][j] for p in range(n)) - sum(pr))
                h = -sum(q * (1 - q) for q in pr)
                b[j] = max(-6, min(6, b[j] - g / h))
        m = statistics.fmean(b)
        b = [v - m for v in b]
    b = [v * (K - 1) / K for v in b]

    print(f"Personas usadas: {n} de {N} | items: {K}")
    print(f"{'item':>4} {'b real':>8} {'b estimado':>11}")
    for j in range(K):
        print(f"{j + 1:4d} {b_real[j]:8.2f} {b[j]:11.2f}")
    rmse = math.sqrt(statistics.fmean((a - c) ** 2 for a, c in zip(b, b_real, strict=True)))
    print(f"\nr(b real, b estimado) = {statistics.correlation(b, b_real):.3f}   RMSE = {rmse:.3f}")
    print(f"r(theta real, theta estimado) = {statistics.correlation(th, th_ref):.3f}")
    print()
    print("Lectura: en Rasch el puntaje total es estadistico suficiente de theta: dos personas con")
    print("el mismo puntaje tienen el mismo theta estimado, sin importar CUALES items acertaron.")
    print("Esa simplicidad tiene un precio: asume igual discriminacion en todos los items (clase 053).")


if __name__ == "__main__":
    main()
