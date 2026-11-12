"""Laboratorio 064 - Sesgo predictivo (Cleary) y definiciones de equidad que chocan.

Dos grupos, A y B. El test X predice un criterio Y. Se simulan dos mundos:
  1. SIN SESGO PREDICTIVO: la misma recta Y~X en ambos grupos, pero B tiene media menor en X.
  2. CON SESGO PREDICTIVO: B rinde menos en Y a igual X (diferencia de intercepto).
Se ajusta la recta por grupo (modelo de Cleary) y se comparan, con un corte comun en X:
tasa de seleccion, tasa de verdaderos positivos (entre quienes SI tendran buen desempeno) y
valor predictivo positivo. Las tres definiciones no pueden igualarse a la vez si las tasas
base difieren (Kleinberg et al., 2016; Chouldechova, 2017).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 30000
R = 0.5


def grupo(media_x: float, interc: float, rng: random.Random):
    x = [rng.gauss(media_x, 1) for _ in range(N)]
    y = [interc + R * a + math.sqrt(1 - R * R) * rng.gauss(0, 1) for a in x]
    return x, y


def recta(x: list[float], y: list[float]) -> tuple[float, float]:
    b = statistics.covariance(x, y) / statistics.variance(x)
    return statistics.fmean(y) - b * statistics.fmean(x), b


def informe(titulo: str, ga, gb) -> None:
    print(titulo)
    for nombre, (x, y) in (("A", ga), ("B", gb)):
        a, b = recta(x, y)
        print(f"  grupo {nombre}: Y = {a:5.2f} + {b:4.2f}*X | media X = {statistics.fmean(x):5.2f}"
              f" | media Y = {statistics.fmean(y):5.2f}")
    corte_x, corte_y = 0.5, 0.0
    print(f"  Con corte comun X >= {corte_x} y 'buen desempeno' = Y > {corte_y}:")
    print(f"  {'':8}{'seleccion':>10}{'TPR':>8}{'VPP':>8}{'tasa base':>11}")
    for nombre, (x, y) in (("A", ga), ("B", gb)):
        sel = [a >= corte_x for a in x]
        bueno = [b > corte_y for b in y]
        tp = sum(s and g for s, g in zip(sel, bueno, strict=True))
        print(f"  {nombre:<8}{sum(sel) / N:10.3f}{tp / sum(bueno):8.3f}{tp / sum(sel):8.3f}{sum(bueno) / N:11.3f}")


def main() -> None:
    rng = random.Random(SEMILLA)
    a = grupo(0.0, 0.0, rng)
    informe("Mundo 1 - misma recta, B con media menor en X (sin sesgo predictivo)", a, grupo(-0.5, 0.0, rng))
    informe("\nMundo 2 - B rinde menos en Y a igual X (sesgo predictivo)", a, grupo(-0.5, -0.3, rng))
    print()
    print("Lectura: en el mundo 1 las rectas coinciden (el test predice igual en ambos grupos) y")
    print("aun asi las tasas de seleccion, TPR y VPP difieren, porque las tasas base y las medias")
    print("difieren: no existe un corte que iguale todas las metricas. Elegir que equidad priorizar")
    print("es una decision de valor, informada por las consecuencias (clase 035), no un calculo.")


if __name__ == "__main__":
    main()
