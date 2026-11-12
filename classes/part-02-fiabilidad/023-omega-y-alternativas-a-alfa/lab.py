"""Laboratorio 023 - Omega frente a alfa cuando las cargas no son iguales.

Alfa supone tau-equivalencia: todos los items cargan igual en el factor. Si no,
alfa SUBESTIMA la fiabilidad. Omega total usa las cargas:

    omega = (suma lambda)^2 / ( (suma lambda)^2 + suma psi )

AQUI las cargas son las verdaderas porque nosotros generamos los datos. En datos
reales hay que ESTIMARlas con un modelo factorial (parte 04); omega con cargas
mal estimadas es tan fragil como cualquier otra cifra.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 20000


def alfa(items: list[list[float]]) -> float:
    k = len(items)
    total = [sum(f) for f in zip(*items, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(i) for i in items) / statistics.pvariance(total))


def omega(cargas: list[float]) -> float:
    psi = [1 - c * c for c in cargas]            # varianza unica con items estandarizados
    s = sum(cargas) ** 2
    return s / (s + sum(psi))


def simula(cargas: list[float], rng: random.Random) -> list[list[float]]:
    f = [rng.gauss(0, 1) for _ in range(N)]
    return [[c * a + rng.gauss(0, (1 - c * c) ** 0.5) for a in f] for c in cargas]


def main() -> None:
    rng = random.Random(SEMILLA)
    casos = {
        "cargas iguales (0.6 x6)": [0.6] * 6,
        "cargas desiguales (0.9 .. 0.3)": [0.9, 0.8, 0.6, 0.5, 0.4, 0.3],
        "muy desiguales (0.95 x2, 0.2 x4)": [0.95, 0.95, 0.2, 0.2, 0.2, 0.2],
    }
    print(f"{'caso':<36} {'alfa':>6} {'omega':>6} {'diferencia':>11}")
    print("=" * 64)
    for nombre, cargas in casos.items():
        a, o = alfa(simula(cargas, rng)), omega(cargas)
        print(f"{nombre:<36} {a:6.3f} {o:6.3f} {o - a:11.3f}")
    print()
    print("Lectura: con cargas iguales alfa = omega. Cuanto mas desiguales las")
    print("cargas, mas subestima alfa. Omega no es 'mejor' por decreto: es mas")
    print("adecuado cuando el modelo de un factor con cargas libres se sostiene.")


if __name__ == "__main__":
    main()
