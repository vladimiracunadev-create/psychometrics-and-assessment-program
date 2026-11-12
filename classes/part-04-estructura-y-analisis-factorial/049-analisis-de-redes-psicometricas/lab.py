"""Laboratorio 049 - Redes psicometricas: correlacion marginal frente a correlacion parcial.

Estructura causal en cadena A -> B -> C -> D (cada eslabon r ~ 0.6). La correlacion
marginal entre A y C (o A y D) es apreciable aunque NO hay relacion directa; la
correlacion parcial (condicionada a las demas variables) la elimina. Una red psicometrica
dibuja las parciales. Aqui no se aplica regularizacion (EBICglasso): con muestras
pequenas, las parciales no regularizadas son ruidosas (Epskamp y Fried, 2018).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 5000
NOMBRES = "ABCD"


def inversa(m: list[list[float]]) -> list[list[float]]:
    n = len(m)
    a = [r[:] + [float(i == j) for j in range(n)] for i, r in enumerate(m)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[piv] = a[piv], a[i]
        d = a[i][i]
        a[i] = [x / d for x in a[i]]
        for r in range(n):
            if r != i:
                f = a[r][i]
                a[r] = [x - f * y for x, y in zip(a[r], a[i], strict=True)]
    return [r[n:] for r in a]


def mostrar(titulo: str, m: list[list[float]]) -> None:
    print(titulo)
    print("      " + "".join(f"{c:>7}" for c in NOMBRES))
    for i, fila in enumerate(m):
        print(f"   {NOMBRES[i]}  " + "".join(f"{x:7.2f}" for x in fila))


def main() -> None:
    rng = random.Random(SEMILLA)
    a = [rng.gauss(0, 1) for _ in range(N)]
    b = [0.6 * x + 0.8 * rng.gauss(0, 1) for x in a]
    c = [0.6 * x + 0.8 * rng.gauss(0, 1) for x in b]
    d = [0.6 * x + 0.8 * rng.gauss(0, 1) for x in c]
    cols = [a, b, c, d]
    r = [[1.0 if i == j else statistics.correlation(cols[i], cols[j]) for j in range(4)]
         for i in range(4)]
    p = inversa(r)
    parcial = [[1.0 if i == j else -p[i][j] / math.sqrt(p[i][i] * p[j][j]) for j in range(4)]
               for i in range(4)]
    mostrar("Correlaciones marginales", r)
    mostrar("Correlaciones parciales (condicionadas a las demas)", parcial)
    print("\nAristas con |parcial| > 0.10:",
          ", ".join(f"{NOMBRES[i]}-{NOMBRES[j]}" for i in range(4) for j in range(i + 1, 4)
                    if abs(parcial[i][j]) > 0.10))
    print()
    print("Lectura: la red recupera la cadena A-B-C-D; la correlacion marginal sugiere aristas")
    print("espurias (A-C, A-D, B-D). Pero una red de correlaciones parciales es una descripcion")
    print("estadistica de asociacion condicional: no establece causalidad ni direccion.")


if __name__ == "__main__":
    main()
