"""Laboratorio 042 - Un constructo, tres definiciones operacionales.

Una variable latente ("estres percibido") no se observa; se la operacionaliza. Se simulan tres
operacionalizaciones del MISMO constructo con distinta carga y error: autoinforme (carga 0.80),
valoracion de un tercero (0.60) y un indicador conductual (0.40). Se muestra:
  - la matriz de correlaciones entre operacionalizaciones (convergencia imperfecta),
  - que ordenan a las personas de forma distinta (porcentaje de coincidencia en el 20 % superior),
  - que un compuesto SIN ponderar no supera a la mejor medida individual cuando las otras son mucho
    mas debiles (la ponderacion importa).
Datos sinteticos; la "verdad" latente se conoce solo porque se simulo.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 3000
CARGAS = {"autoinforme": 0.80, "tercero": 0.60, "conductual": 0.40}


def main() -> None:
    rng = random.Random(SEMILLA)
    latente = [rng.gauss(0, 1) for _ in range(N)]
    medidas = {k: [c * t + math.sqrt(1 - c * c) * rng.gauss(0, 1) for t in latente] for k, c in CARGAS.items()}
    compuesto = [sum(medidas[k][i] for k in medidas) for i in range(N)]
    nombres = list(medidas)
    print("Correlaciones entre operacionalizaciones (teorica = producto de cargas):")
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            print(f"  {a:<12} - {b:<12} r = {statistics.correlation(medidas[a], medidas[b]):.2f} (teorica {CARGAS[a] * CARGAS[b]:.2f})")
    print("\nCorrelacion con el constructo latente (solo conocida por ser simulado):")
    for k in nombres:
        print(f"  {k:<12} r = {statistics.correlation(medidas[k], latente):.2f}")
    print(f"  {'compuesto':<12} r = {statistics.correlation(compuesto, latente):.2f}")
    corte = int(0.8 * N)
    top = {k: set(sorted(range(N), key=lambda i, k=k: medidas[k][i])[corte:]) for k in nombres}
    print(f"\nCoincidencia del 20 % superior: autoinforme-tercero {len(top['autoinforme'] & top['tercero']) / len(top['tercero']):.0%}, "
          f"autoinforme-conductual {len(top['autoinforme'] & top['conductual']) / len(top['conductual']):.0%}")
    print()
    print("Lectura: la definicion operacional decide quien aparece 'alto' en el constructo. Medidas distintas del mismo")
    print("constructo convergen solo parcialmente, por eso se triangulan metodos (clase 023). Un compuesto sin ponderar")
    print("(r = 0.80) no supera a la mejor medida (0.81): sumar medidas desiguales no mejora por si solo, y ninguno")
    print("corrige un constructo mal definido.")


if __name__ == "__main__":
    main()
