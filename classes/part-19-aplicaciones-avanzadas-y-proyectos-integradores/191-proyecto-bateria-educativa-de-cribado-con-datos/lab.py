"""Laboratorio 191 - Proyecto: bateria educativa de cribado en dos etapas (datos sinteticos).

Cribado de dificultades lectoras en 1.200 estudiantes sinteticos. Etapa 1: una prueba breve de 12
items (barata, para todos). Etapa 2: una prueba de seguimiento mas larga solo para quienes quedan
bajo el corte de la etapa 1. La "condicion de referencia" es una habilidad latente baja (10 %
inferior), que en la vida real no se observa: aqui se conoce porque los datos son simulados.
Se comparan: (a) etapa 1 sola y (b) etapa 1 + etapa 2 (se deriva solo si ambas estan bajo corte).
Un cribado orienta apoyo; NO diagnostica.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 1200


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def prueba(theta: float, k: int, rng: random.Random) -> int:
    return sum(rng.random() < logistica(1.3 * (theta - b)) for b in (-1.4 + 2.8 * j / (k - 1) for j in range(k)))


def main() -> None:
    rng = random.Random(SEMILLA)
    theta = [rng.gauss(0, 1) for _ in range(N)]
    corte_real = sorted(theta)[int(0.10 * N)]
    real = [t < corte_real for t in theta]
    e1 = [prueba(t, 12, rng) for t in theta]
    e2 = [prueba(t, 30, rng) for t in theta]
    c1 = sorted(e1)[int(0.25 * N)]               # etapa 1 deliberadamente generosa (sensible)
    bajo1 = [x <= c1 for x in e1]
    c2 = sorted(e2)[int(0.12 * N)]
    bajo2 = [x <= c2 for x in e2]
    print(f"{'estrategia':<34} {'derivados':>10} {'sensibilidad':>13} {'especificidad':>14} {'VPP':>6} {'pruebas largas':>15}")
    print("=" * 100)
    for nombre, marca, largas in (("etapa 1 sola (12 items)", bajo1, 0),
                                  ("etapa 1 + etapa 2 (ambas bajo corte)", [a and b for a, b in zip(bajo1, bajo2, strict=True)], sum(bajo1))):
        tp = sum(m and r for m, r in zip(marca, real, strict=True))
        fp = sum(m and not r for m, r in zip(marca, real, strict=True))
        pos = sum(real)
        print(f"{nombre:<34} {sum(marca):10d} {tp / pos:13.2f} {1 - fp / (N - pos):14.2f} {tp / max(tp + fp, 1):6.2f} {largas:15d}")
    print()
    print("Lectura: la etapa 1 sola atrapa a casi todos pero deriva a muchos que no lo necesitan (VPP bajo, porque")
    print("la condicion es poco frecuente). Exigir la segunda etapa sube el VPP a cambio de perder algo de")
    print("sensibilidad y de aplicar la prueba larga a todos los derivados de la etapa 1 (381). Un cribado orienta apoyo y seguimiento: no etiqueta.")
    print("El corte debe fijarse con datos del contexto y revisarse (clase 145). Datos sinteticos.")


if __name__ == "__main__":
    main()
