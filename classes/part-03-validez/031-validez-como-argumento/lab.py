"""Laboratorio 031 - Fiable no es valido: un test perfecto que mide otra cosa.

Se compara el uso de dos puntajes para predecir un criterio (rendimiento en matematica):
  A. una prueba de VOCABULARIO muy fiable (rho = 0.95) pero casi irrelevante para el criterio,
  B. una prueba de razonamiento numerico algo menos fiable (rho = 0.80) pero relevante.
Tambien se verifica el techo teorico: r(X, Y) <= sqrt(rho_x * rho_y).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 20000


def main() -> None:
    rng = random.Random(SEMILLA)
    razonamiento = [rng.gauss(0, 1) for _ in range(N)]                 # constructo relevante
    vocabulario = [0.15 * r + math.sqrt(1 - 0.15**2) * rng.gauss(0, 1) for r in razonamiento]
    criterio_verdadero = [0.7 * r + math.sqrt(1 - 0.49) * rng.gauss(0, 1) for r in razonamiento]
    criterio = [c + rng.gauss(0, 0.4) for c in criterio_verdadero]      # criterio medido con error

    def con_error(t: list[float], rho: float) -> list[float]:
        sd = math.sqrt((1 - rho) / rho)
        return [a + rng.gauss(0, sd) for a in t]

    A, B = con_error(vocabulario, 0.95), con_error(razonamiento, 0.80)
    ryy = statistics.correlation(criterio_verdadero, criterio) ** 2
    print(f"{'prueba':<34} {'fiabilidad':>10} {'r con criterio':>15} {'techo':>7}")
    print("=" * 70)
    for nombre, x, rho in (("A. vocabulario (muy fiable)", A, 0.95),
                           ("B. razonamiento numerico", B, 0.80)):
        r = statistics.correlation(x, criterio)
        print(f"{nombre:<34} {rho:10.2f} {r:15.3f} {math.sqrt(rho * ryy):7.3f}")
    print()
    print("Lectura: A es casi perfecta como medida y casi inutil para este proposito.")
    print("La fiabilidad es condicion necesaria de la validez, no suficiente. Y 'valida'")
    print("no es propiedad de A o B: depende de PARA QUE se la use (el argumento).")


if __name__ == "__main__":
    main()
