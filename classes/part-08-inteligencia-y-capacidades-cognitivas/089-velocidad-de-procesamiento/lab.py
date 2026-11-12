"""Laboratorio 089 - Velocidad y precision: el compromiso que contamina el "tiempo de reaccion".

Un modelo de difusion minimo (random walk con dos barreras): la evidencia se acumula con
deriva v hasta cruzar +a (respuesta correcta) o -a (error). Una barrera mayor (mas cautela)
produce respuestas mas lentas y mas precisas con la MISMA capacidad (v). Se muestra:
  - el tiempo medio y la precision para tres niveles de cautela;
  - que el RT por si solo confunde cautela con capacidad;
  - el indice de eficiencia inversa (IES = RT medio / precision), una correccion parcial.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
ENSAYOS, DT, SIGMA = 1500, 0.01, 1.0


def ensayo(v: float, a: float, rng: random.Random) -> tuple[float, bool]:
    x, t = 0.0, 0.0
    while abs(x) < a:
        x += v * DT + SIGMA * (DT ** 0.5) * rng.gauss(0, 1)
        t += DT
    return t + 0.3, x > 0                            # + tiempo no decisional de 0.3 s


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'caso':<30} {'RT medio (s)':>13} {'precision':>10} {'IES':>7}")
    print("=" * 64)
    casos = [("capacidad media, cauto", 1.0, 1.2), ("capacidad media, apurado", 1.0, 0.5),
             ("capacidad ALTA, apurado", 2.0, 0.5), ("capacidad BAJA, cauto", 0.5, 1.2)]
    for nombre, v, a in casos:
        res = [ensayo(v, a, rng) for _ in range(ENSAYOS)]
        rt = statistics.fmean(t for t, _ in res)
        acc = statistics.fmean(c for _, c in res)
        print(f"{nombre:<30} {rt:13.3f} {acc:10.3f} {rt / acc:7.3f}")
    print()
    print("Lectura: con la MISMA capacidad (primeras dos filas) el RT cambia de 1.36 a 0.58 s y la")
    print("precision de 0.93 a 0.77 solo por la cautela. El IES no elimina ese efecto de estrategia")
    print("(1.47 frente a 0.76). Por eso se informa velocidad y precision por separado, se")
    print("estandarizan las instrucciones y, cuando importa, se usan modelos que separan ambos.")


if __name__ == "__main__":
    main()
