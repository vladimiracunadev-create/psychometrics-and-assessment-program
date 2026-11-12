"""Laboratorio 011 - La teoria clasica del error, verificada con datos simulados.

Modelo: X = T + E, con E de media cero e independiente de T. De ahi se deduce:
    var(X) = var(T) + var(E)            (descomposicion de la varianza)
    fiabilidad = var(T) / var(X)        (proporcion de varianza que es senal)
    fiabilidad = r(X, X')               (correlacion entre formas paralelas)
El laboratorio comprueba las tres igualdades y muestra que T NUNCA se observa:
aqui lo conocemos solo porque nosotros generamos los datos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 20000


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'sd(E)':>6} {'var(T)':>7} {'var(E)':>7} {'var(X)':>7} "
          f"{'T+E':>7} {'var(T)/var(X)':>14} {'r(X,X*)':>8} {'r(E,T)':>7}")
    print("=" * 76)
    for sd_error in (0.5, 1.0, 2.0):
        t = [rng.gauss(0, 1) for _ in range(N)]
        e1 = [rng.gauss(0, sd_error) for _ in range(N)]
        e2 = [rng.gauss(0, sd_error) for _ in range(N)]
        x1 = [a + b for a, b in zip(t, e1, strict=True)]
        x2 = [a + b for a, b in zip(t, e2, strict=True)]   # forma paralela
        vt, ve, vx = (statistics.pvariance(v) for v in (t, e1, x1))
        print(f"{sd_error:6.1f} {vt:7.3f} {ve:7.3f} {vx:7.3f} {vt + ve:7.3f} "
              f"{vt / vx:14.3f} {statistics.correlation(x1, x2):8.3f} "
              f"{statistics.correlation(e1, t):7.3f}")
    print()
    print("Lectura")
    print("  - var(X) coincide con var(T)+var(E) salvo ruido de muestreo.")
    print("  - La proporcion var(T)/var(X) y la correlacion entre formas paralelas")
    print("    dan el mismo numero: son dos caminos a la misma fiabilidad.")
    print("  - r(E,T) ~ 0: el error no depende del nivel verdadero (supuesto del modelo).")
    print("  - En la practica solo se ve X; la fiabilidad se ESTIMA, no se observa.")


if __name__ == "__main__":
    main()
