"""Laboratorio 005 - Cuanto sesgo de aquiescencia elimina la clave equilibrada.

Simula personas con el MISMO rasgo pero distinta tendencia a asentir, y compara
el perfil que produce una escala de clave unica frente a una equilibrada.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N_ITEMS = 20
MINIMO, MAXIMO = 1, 5


def refleja(valor: int) -> int:
    return MINIMO + MAXIMO - valor


def responde(rasgo: float, aquiescencia: float, clave: int, rng: random.Random) -> int:
    """El valor observado mezcla el rasgo con la tendencia a asentir.

    La aquiescencia empuja SIEMPRE hacia arriba, sin importar la clave del item:
    esa es exactamente la propiedad que permite cancelarla al reflejar.
    """
    latente = (rasgo if clave == 1 else -rasgo) + aquiescencia + rng.gauss(0, 0.5)
    return max(MINIMO, min(MAXIMO, round(3 + latente)))


def perfil(rasgo: float, aquiescencia: float, invertidos: int, rng: random.Random) -> float:
    claves = [1] * (N_ITEMS - invertidos) + [-1] * invertidos
    efectivos = []
    for clave in claves:
        crudo = responde(rasgo, aquiescencia, clave, rng)
        efectivos.append(crudo if clave == 1 else refleja(crudo))
    return statistics.fmean(efectivos)


def main() -> None:
    print("Tres personas con el MISMO rasgo (0.0) y distinta aquiescencia")
    print("=" * 72)
    print(f"{'aquiescencia':>13} {'clave unica':>13} {'equilibrada':>13}")
    print("-" * 72)

    unica, equilibrada = [], []
    for aquiescencia in (-1.0, -0.5, 0.0, 0.5, 1.0):
        rng = random.Random(SEMILLA)
        a = perfil(0.0, aquiescencia, invertidos=0, rng=rng)
        rng = random.Random(SEMILLA)
        b = perfil(0.0, aquiescencia, invertidos=N_ITEMS // 2, rng=rng)
        unica.append(a)
        equilibrada.append(b)
        print(f"{aquiescencia:13.1f} {a:13.2f} {b:13.2f}")

    print("-" * 72)
    print(f"{'rango':>13} {max(unica) - min(unica):13.2f} "
          f"{max(equilibrada) - min(equilibrada):13.2f}")
    print()
    print("Lectura del resultado")
    print("  Las cinco personas tienen identico rasgo. Con clave unica el puntaje")
    print("  se mueve casi dos puntos solo por su estilo de respuesta: el test")
    print("  esta midiendo aquiescencia y llamandolo rasgo.")
    print()
    print("  Con clave equilibrada el rango se comprime: el sesgo se cancela al")
    print("  reflejar, porque empujaba hacia arriba en ambas direcciones.")


if __name__ == "__main__":
    main()
