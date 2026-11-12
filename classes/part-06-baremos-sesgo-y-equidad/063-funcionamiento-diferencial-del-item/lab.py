"""Laboratorio 063 - DIF con Mantel-Haenszel.

Dos grupos (referencia y focal), 20 items Rasch. El grupo focal tiene MENOS habilidad media
(-0.5: diferencia real = IMPACTO, no sesgo). El item 7 es mas dificil para el grupo focal a
igual habilidad (+0.8): DIF uniforme. Se compara a las personas con el mismo puntaje total y
se estima:
    alfa_MH = suma(A*D/T) / suma(B*C/T)        Delta_MH = -2.35 * ln(alfa_MH)
Clasificacion ETS por magnitud: A (|Delta| < 1), B (1 a 1.5), C (> 1.5). La version completa
exige ademas significacion estadistica; aqui se informa tambien el chi-cuadrado MH.
"""
from __future__ import annotations

import math
import random
from collections import defaultdict

SEMILLA = 20260819
N, K, ITEM_DIF, SHIFT = 4000, 20, 6, 0.8


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def simula(media: float, focal: bool, bs: list[float], rng: random.Random):
    filas = []
    for _ in range(N):
        t = rng.gauss(media, 1)
        r = [int(rng.random() < logistica(t - (b + (SHIFT if focal and i == ITEM_DIF else 0))))
             for i, b in enumerate(bs)]
        filas.append(r)
    return filas


def mantel_haenszel(ref, foc, item: int) -> tuple[float, float, float]:
    estratos = defaultdict(lambda: [0, 0, 0, 0])      # A, B, C, D
    for grupo, filas in ((0, ref), (1, foc)):
        for f in filas:
            s = sum(f)
            e = estratos[s]
            e[(0 if f[item] else 1) + 2 * grupo] += 1
    num = den = 0.0
    sa = ev = vr = 0.0
    for a, b, c, d in estratos.values():
        t = a + b + c + d
        if t < 2:
            continue
        num += a * d / t
        den += b * c / t
        n1, n0, m1, m0 = a + b, c + d, a + c, b + d
        sa += a
        ev += n1 * m1 / t
        vr += n1 * n0 * m1 * m0 / (t * t * (t - 1))
    alfa = num / den
    chi2 = (abs(sa - ev) - 0.5) ** 2 / vr
    return alfa, -2.35 * math.log(alfa), chi2


def main() -> None:
    rng = random.Random(SEMILLA)
    bs = [-1.5 + 3.0 * i / (K - 1) for i in range(K)]
    ref = simula(0.0, False, bs, rng)
    foc = simula(-0.5, True, bs, rng)
    print(f"{'item':>4} {'alfa MH':>8} {'Delta':>7} {'chi2':>8}  clase")
    print("=" * 40)
    for i in range(K):
        a, d, x2 = mantel_haenszel(ref, foc, i)
        clase = "A" if abs(d) < 1 else ("B" if abs(d) < 1.5 else "C")
        marca = "   <-- item con DIF sembrado" if i == ITEM_DIF else ""
        if i == ITEM_DIF or clase != "A" or i < 3:
            print(f"{i + 1:4d} {a:8.2f} {d:7.2f} {x2:8.1f}  {clase}{marca}")
    print("  ...")
    medias = (sum(map(sum, ref)) / N, sum(map(sum, foc)) / N)
    print(f"\nPuntaje total medio: referencia = {medias[0]:.1f}, focal = {medias[1]:.1f} "
          "(diferencia = impacto real)")
    print()
    print("Lectura: el grupo focal puntua menos en TODOS los items, y aun asi el metodo solo")
    print("senala el item 7: compara personas del mismo nivel. Impacto (diferencia de grupos) no")
    print("es DIF (diferencia a igual nivel). Y un item con DIF no se elimina automaticamente:")
    print("se revisa su contenido para entender si el sesgo es irrelevante para el constructo.")


if __name__ == "__main__":
    main()
