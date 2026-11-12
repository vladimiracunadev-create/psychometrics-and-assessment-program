"""Laboratorio 138 - Rubrica de desarrollo (4 niveles): acuerdo ponderado entre educadoras.

Dos educadoras clasifican a 120 ninos y ninas en 4 niveles (1 = inicial ... 4 = logrado) para 3
ambitos. Se calcula el kappa ponderado cuadratico (penaliza mas los desacuerdos lejanos) y el
kappa simple, con dos rubricas: una de descriptores ambiguos (mas desacuerdos) y otra con
descriptores observables (menos). Tambien se muestra el efecto de un "sesgo de indulgencia" de una
educadora. Datos sinteticos.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N, NIV = 120, 4


def kappa(a: list[int], b: list[int], ponderado: bool) -> float:
    n = len(a)
    obs = [[0] * NIV for _ in range(NIV)]
    for x, y in zip(a, b, strict=True):
        obs[x - 1][y - 1] += 1
    fa = [sum(f) / n for f in obs]
    fb = [sum(obs[i][j] for i in range(NIV)) / n for j in range(NIV)]
    num = den = 0.0
    for i in range(NIV):
        for j in range(NIV):
            w = (i - j) ** 2 / (NIV - 1) ** 2 if ponderado else float(i != j)
            num += w * obs[i][j] / n
            den += w * fa[i] * fb[j]
    return 1 - num / den


def clasifica(nivel_real: float, ruido: float, sesgo: float, rng: random.Random) -> int:
    return max(1, min(NIV, round(nivel_real + sesgo + rng.gauss(0, ruido))))


def main() -> None:
    rng = random.Random(SEMILLA)
    real = [min(4.4, max(0.6, rng.gauss(2.5, 0.9))) for _ in range(N)]
    print(f"{'rubrica / condicion':<44} {'kappa simple':>13} {'kappa ponderado':>16}")
    print("=" * 76)
    for nombre, ruido, sesgo in (("descriptores ambiguos", 0.9, 0.0),
                                 ("descriptores observables", 0.4, 0.0),
                                 ("observables + una educadora indulgente (+0.6)", 0.4, 0.6)):
        a = [clasifica(r, ruido, 0.0, rng) for r in real]
        b = [clasifica(r, ruido, sesgo, rng) for r in real]
        print(f"{nombre:<44} {kappa(a, b, False):13.2f} {kappa(a, b, True):16.2f}")
    print()
    print("Lectura: descriptores observables suben el acuerdo; un sesgo sistematico de una evaluadora lo")
    print("reduce aunque ambas 'coincidan en orden'. Con 4 niveles, el kappa ponderado es mas indulgente con")
    print("los desacuerdos de un nivel. La calibracion entre educadoras (revisar casos juntas) es parte")
    print("del instrumento. Los niveles describen lo observado en un periodo, no etiquetan a la persona.")


if __name__ == "__main__":
    main()
