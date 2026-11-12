"""Laboratorio 105 - Estabilidad de un rasgo en el desarrollo: el patron simplex.

Modelo autorregresivo: el rasgo verdadero en la ocasion t+1 es rho_paso * rasgo(t) + innovacion
(rho_paso = 0.85 por intervalo de 2 anos). El puntaje observado agrega error de medida
(fiabilidad 0.80). Se muestran las correlaciones entre ocasiones (matriz y por distancia):
  - decaen con el intervalo (patron simplex),
  - la correlacion observada subestima la verdadera por la fiabilidad,
  - correccion por atenuacion: r_obs / fiabilidad.
Las cifras son del modelo, no estimaciones del temperamento real.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, OCASIONES, RHO_PASO, FIAB = 5000, 5, 0.85, 0.80


def main() -> None:
    rng = random.Random(SEMILLA)
    sd_e = math.sqrt((1 - FIAB) / FIAB)
    verd = [[rng.gauss(0, 1)] for _ in range(N)]
    for fila in verd:
        for _ in range(OCASIONES - 1):
            fila.append(RHO_PASO * fila[-1] + math.sqrt(1 - RHO_PASO**2) * rng.gauss(0, 1))
    obs = [[v + rng.gauss(0, sd_e) for v in f] for f in verd]
    col = lambda m, j: [f[j] for f in m]  # noqa: E731
    print("Correlaciones observadas entre ocasiones (T1..T5, un paso = 2 anos)")
    for i in range(OCASIONES):
        print("  " + " ".join(f"{statistics.correlation(col(obs, i), col(obs, j)) if i != j else 1.0:5.2f}"
                              for j in range(OCASIONES)))
    print(f"\n{'distancia (pasos)':>18} {'r observada':>12} {'r verdadera':>12} {'corregida (obs/fiab.)':>22}")
    for d in range(1, OCASIONES):
        ro = statistics.fmean(statistics.correlation(col(obs, i), col(obs, i + d)) for i in range(OCASIONES - d))
        rv = RHO_PASO ** d
        print(f"{d:18d} {ro:12.3f} {rv:12.3f} {ro / FIAB:22.3f}")
    print()
    print("Lectura: la estabilidad cae con el intervalo aunque el rasgo sea 'estable': estable no es")
    print("inmutable. Y parte de la inestabilidad aparente es error de medida (la correccion por")
    print("atenuacion recupera el valor verdadero). Los puntajes de ninos pequenos suelen ser menos")
    print("fiables, lo que hace que la estabilidad parezca menor de lo que es.")


if __name__ == "__main__":
    main()
