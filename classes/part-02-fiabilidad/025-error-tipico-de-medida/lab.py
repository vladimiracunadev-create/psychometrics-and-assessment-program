"""Laboratorio 025 - Error tipico de medida (ETM) e intervalos de un puntaje.

    ETM = SD * sqrt(1 - fiabilidad)
    intervalo del puntaje observado: X +/- 1.96 * ETM  (95 %)
    ETM de una diferencia entre dos puntajes: ETM * sqrt(2)

Se simula una prueba con media 100, SD 15 y fiabilidad 0.90 (ETM = 4.74) y se
comprueba por simulacion: (a) la cobertura del intervalo, (b) cuantas diferencias
"significativas" aparecen entre dos medidas de personas que NO cambiaron.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 50000
MEDIA, SD, FIABILIDAD = 100.0, 15.0, 0.90
Z = 1.96


def main() -> None:
    rng = random.Random(SEMILLA)
    etm = SD * math.sqrt(1 - FIABILIDAD)
    sd_verdadero = SD * math.sqrt(FIABILIDAD)

    print(f"SD={SD}, fiabilidad={FIABILIDAD} -> ETM = {etm:.2f}")
    print(f"Intervalo 95 % de un puntaje observado: +/- {Z * etm:.1f} puntos")
    print("=" * 60)

    verdaderos = [rng.gauss(MEDIA, sd_verdadero) for _ in range(N)]
    obs1 = [t + rng.gauss(0, etm) for t in verdaderos]
    obs2 = [t + rng.gauss(0, etm) for t in verdaderos]      # misma persona, sin cambio

    cubre = sum(abs(x - t) <= Z * etm for x, t in zip(obs1, verdaderos, strict=True)) / N
    print(f"(a) Cobertura del intervalo X +/- 1.96 ETM sobre el puntaje verdadero: {cubre:.3f}")

    umbral = Z * etm * math.sqrt(2)
    falsos = sum(abs(b - a) > umbral for a, b in zip(obs1, obs2, strict=True)) / N
    print(f"(b) Umbral de cambio fiable: {umbral:.1f} puntos")
    print(f"    Personas SIN cambio real marcadas como cambiadas: {falsos:.3f} (esperado ~0.05)")

    brecha = sum(abs(b - a) > 10 for a, b in zip(obs1, obs2, strict=True)) / N
    print(f"(c) Diferencias de mas de 10 puntos entre dos medidas sin cambio real: {brecha:.3f}")
    print()
    print("Lectura: con fiabilidad 0.90, que es alta, un puntaje se mueve +/- 9 puntos")
    print("solo por error. Una diferencia de 10 puntos entre dos aplicaciones NO es")
    print("evidencia de cambio: ocurre en cerca de una de cada siete personas sin cambio alguno.")
    print("Nota: este intervalo centrado en el observado es una aproximacion; el")
    print("intervalo sobre el puntaje verdadero estimado se centra en el valor regresado.")


if __name__ == "__main__":
    main()
