"""Laboratorio 091 - Vigilancia: el decremento se ve en d' y en el criterio.

Tarea de desempeno continuo simulada: 4 bloques de 200 estimulos (10 % senales). El
observador tiene sensibilidad d' y criterio c que cambian entre bloques (la sensibilidad cae
un poco y el criterio se vuelve mas conservador). Se calculan aciertos, falsas alarmas, d' y c
con la correccion log-lineal (Hautus, 1995). Lo importante: "mas omisiones" puede ser un
cambio de criterio (cautela) y no de sensibilidad.
"""
from __future__ import annotations

import random
from statistics import NormalDist

SEMILLA = 20260819
BLOQUES, ENSAYOS, P_SENAL = 4, 200, 0.10
ND = NormalDist()


def simula(dprime: float, c: float, rng: random.Random) -> tuple[int, int, int, int]:
    h = fa = ns = nr = 0
    for _ in range(ENSAYOS):
        senal = rng.random() < P_SENAL
        x = rng.gauss(dprime if senal else 0.0, 1.0)
        dice_si = x > dprime / 2 + c
        if senal:
            ns += 1
            h += dice_si
        else:
            nr += 1
            fa += dice_si
    return h, ns, fa, nr


def sdt(h: int, ns: int, fa: int, nr: int) -> tuple[float, float, float, float]:
    ph, pf = (h + 0.5) / (ns + 1), (fa + 0.5) / (nr + 1)          # correccion log-lineal
    d = ND.inv_cdf(ph) - ND.inv_cdf(pf)
    c = -0.5 * (ND.inv_cdf(ph) + ND.inv_cdf(pf))
    return h / ns, fa / nr, d, c


def main() -> None:
    rng = random.Random(SEMILLA)
    verdad = [(2.0, 0.0), (1.9, 0.15), (1.8, 0.30), (1.7, 0.45)]
    print(f"{'bloque':>6} {'aciertos':>9} {'f. alarmas':>11} {'d prima':>8} {'criterio c':>11}   (verdad d', c)")
    print("=" * 74)
    # 40 observadores para estabilizar el promedio por bloque
    for b in range(BLOQUES):
        acum = [0.0, 0.0, 0.0, 0.0]
        for _ in range(40):
            r = sdt(*simula(*verdad[b], rng))
            acum = [a + x / 40 for a, x in zip(acum, r, strict=True)]
        print(f"{b + 1:6d} {acum[0]:9.3f} {acum[1]:11.3f} {acum[2]:8.2f} {acum[3]:11.2f}   {verdad[b]}")
    print()
    print("Lectura: la caida de aciertos se debe en buena parte al criterio (c sube) y solo en parte a")
    print("la sensibilidad (d'). Informar solo 'omisiones' confunde atencion con cautela. En muestras")
    print("pequenas d' y c por persona son ruidosos: con 20 senales por bloque, el error es grande.")


if __name__ == "__main__":
    main()
