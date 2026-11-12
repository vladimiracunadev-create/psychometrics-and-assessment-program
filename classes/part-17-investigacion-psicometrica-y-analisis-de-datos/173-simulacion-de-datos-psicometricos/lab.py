"""Laboratorio 173 - Simulacion de Monte Carlo: cobertura de un intervalo de confianza.

El intervalo de Fisher para una correlacion supone aproximadamente normalidad bivariada. Se
simula la cobertura REAL de un intervalo nominal del 95 % con r verdadera = 0.40 y n = 30, 60 y
200, en tres condiciones de distribucion:
   normal | asimetrica (exponencial) | con valores extremos (mezcla con 10 % de contaminacion).
Una cobertura distinta de 95 % indica que el metodo no cumple lo que promete en esa condicion.
La simulacion usa 2 000 replicas por celda (semilla fija).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
REPS, R_VERD = 2000, 0.40


def genera(n: int, dist: str, rng: random.Random):
    x, y = [], []
    for _ in range(n):
        a, e = rng.gauss(0, 1), rng.gauss(0, 1)
        b = R_VERD * a + math.sqrt(1 - R_VERD**2) * e
        if dist == "asimetrica":
            a, b = math.exp(a), math.exp(b)                    # lognormal: correlacion distinta de 0.40
        elif dist == "extremos" and rng.random() < 0.10:
            a, b = a * 4, b * 4
        x.append(a)
        y.append(b)
    return x, y


def objetivo(dist: str, rng: random.Random) -> float:
    x, y = genera(200000, dist, rng)
    return statistics.correlation(x, y)


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'distribucion':<14} {'r poblacional':>14}" + "".join(f"{f'cobertura n={n}':>17}" for n in (30, 60, 200)))
    print("=" * 80)
    for dist in ("normal", "asimetrica", "extremos"):
        rho = objetivo(dist, rng)
        fila = f"{dist:<14} {rho:14.3f}"
        for n in (30, 60, 200):
            cubre = 0
            for _ in range(REPS):
                x, y = genera(n, dist, rng)
                r = statistics.correlation(x, y)
                z, se = math.atanh(r), 1 / math.sqrt(n - 3)
                lo, hi = math.tanh(z - 1.96 * se), math.tanh(z + 1.96 * se)
                cubre += lo <= rho <= hi
            fila += f"{cubre / REPS:17.1%}"
        print(fila)
    print()
    print("Lectura: con datos normales la cobertura es ~95 %; con asimetria fuerte o valores extremos cae,")
    print("incluso con n = 200, porque el intervalo supone una distribucion que no se cumple. Simular los")
    print("metodos bajo las condiciones plausibles de tus datos es una forma barata de saber si merecen")
    print("confianza. Una simulacion solo prueba lo que se le pregunta: los escenarios se justifican.")


if __name__ == "__main__":
    main()
