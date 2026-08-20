"""Laboratorio 001 - Por que un test tiene muchos items y no uno solo.

Simula un rasgo latente y muestra como la correlacion entre el puntaje
observado y el rasgo verdadero crece al agregar items. Es la demostracion
numerica del supuesto central de la medicion psicologica.

Sin dependencias externas: solo la biblioteca estandar.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N_PERSONAS = 500
RUIDO = 1.0  # desviacion tipica del error especifico de cada item


def correlacion(xs: list[float], ys: list[float]) -> float:
    """Correlacion de Pearson, implementada a mano para no depender de scipy."""
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys, strict=True))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def simula(n_items: int, rasgo: list[float], rng: random.Random) -> list[float]:
    """Cada item = rasgo verdadero + error propio. El puntaje es la media."""
    puntajes = []
    for verdadero in rasgo:
        respuestas = [verdadero + rng.gauss(0, RUIDO) for _ in range(n_items)]
        puntajes.append(statistics.fmean(respuestas))
    return puntajes


def main() -> None:
    rng = random.Random(SEMILLA)
    # El rasgo verdadero es inobservable. En la vida real no lo tenemos; aqui
    # lo generamos justamente para poder comparar contra el.
    rasgo = [rng.gauss(0, 1) for _ in range(N_PERSONAS)]

    print(f"Simulacion con semilla {SEMILLA}, {N_PERSONAS} personas, ruido sd={RUIDO}")
    print()
    print(f"{'items':>6}  {'r(puntaje, rasgo)':>18}  {'r cuadrado':>10}")
    print("-" * 40)
    for n in (1, 2, 4, 8, 16, 32, 64, 120):
        obs = simula(n, rasgo, rng)
        r = correlacion(obs, rasgo)
        print(f"{n:6}  {r:18.3f}  {r * r:10.3f}")

    print()
    print("Lectura del resultado")
    print("  Con 1 item la correlacion con el rasgo real ronda .70: la mitad de")
    print("  la varianza del puntaje es ruido. Con 120 items supera .99.")
    print()
    print("  Ese es el motivo de que el IPIP-NEO-120 tenga 120 items y no 5.")
    print("  El precio es el tiempo de la persona: la parte 01 estudia ese")
    print("  intercambio entre precision y abandono.")


if __name__ == "__main__":
    main()
