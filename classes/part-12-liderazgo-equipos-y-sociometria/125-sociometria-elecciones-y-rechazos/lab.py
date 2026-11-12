"""Laboratorio 125 - Estatus sociometrico de un curso SINTETICO (Coie, Dodge y Coppotelli, 1982).

Un curso de 30 estudiantes ficticios: cada uno nomina hasta 3 companeros que le gustan (LM) y
hasta 3 que le gustan menos (LL). Se calculan, por estudiante, LM y LL recibidos, se
estandarizan y se obtienen preferencia social SP = zLM - zLL e impacto social SI = zLM + zLL
(vuelto a estandarizar). Clasificacion habitual: popular, rechazado, ignorado, controvertido y
promedio. Los umbrales son convenciones, y aqui NO hay personas reales.
ETICA: la sociometria con menores exige consentimiento informado y asentimiento; no se muestran
resultados de rechazo a los pares ni se publican; se usa para apoyar la convivencia con
profesionales. Este laboratorio solo ensena el calculo.
"""
from __future__ import annotations

import collections
import random
import statistics

SEMILLA = 20260819
N = 30


def z(valores: list[float]) -> list[float]:
    m, s = statistics.fmean(valores), statistics.pstdev(valores)
    return [(v - m) / s if s else 0.0 for v in valores]


def clasifica(zsp: float, zsi: float, zlm: float, zll: float) -> str:
    if zsp > 1 and zlm > 0 and zll < 0:
        return "popular"
    if zsp < -1 and zll > 0 and zlm < 0:
        return "rechazado"
    if zsi < -1 and zlm < 0 and zll < 0:
        return "ignorado"
    if zsi > 1 and zlm > 0 and zll > 0:
        return "controvertido"
    return "promedio"


def main() -> None:
    rng = random.Random(SEMILLA)
    atractivo = [rng.gauss(0, 1) for _ in range(N)]
    lm, ll = [0] * N, [0] * N
    for i in range(N):
        otros = [j for j in range(N) if j != i]
        pesos_pos = [2.718 ** (1.1 * atractivo[j]) for j in otros]
        pesos_neg = [2.718 ** (-1.1 * atractivo[j]) for j in otros]
        gusta = set()
        while len(gusta) < 3:
            gusta.add(rng.choices(otros, weights=pesos_pos)[0])
        for j in gusta:
            lm[j] += 1
        disgusta = set()
        while len(disgusta) < 3:
            c = rng.choices(otros, weights=pesos_neg)[0]
            if c not in gusta:
                disgusta.add(c)
        for j in disgusta:
            ll[j] += 1
    zlm, zll = z([float(v) for v in lm]), z([float(v) for v in ll])
    zsp = z([a - b for a, b in zip(zlm, zll, strict=True)])
    zsi = z([a + b for a, b in zip(zlm, zll, strict=True)])
    estatus = [clasifica(zsp[i], zsi[i], zlm[i], zll[i]) for i in range(N)]
    print(f"Curso ficticio de {N} estudiantes (3 'me gusta' y 3 'me gusta menos' cada uno)")
    print("Distribucion de estatus:", dict(collections.Counter(estatus)))
    print(f"\n{'estudiante':>10} {'LM':>3} {'LL':>3} {'SP':>6} {'SI':>6}  estatus")
    for i in sorted(range(N), key=lambda k: -zsp[k])[:3] + sorted(range(N), key=lambda k: zsp[k])[:3]:
        print(f"{i:10d} {lm[i]:3d} {ll[i]:3d} {zsp[i]:6.2f} {zsi[i]:6.2f}  {estatus[i]}")
    print()
    print("Lectura: el estatus es relativo al curso y cambia con el tiempo. Sirve para ver dinamicas de")
    print("convivencia (quienes no son elegidos, quienes concentran rechazo), no para etiquetar ninos.")


if __name__ == "__main__":
    main()
