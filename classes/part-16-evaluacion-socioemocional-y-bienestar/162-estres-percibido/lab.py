"""Laboratorio 162 - Que cambio es importante: tres definiciones de diferencia minima.

Escala de estres percibido de 10 items (rango 0-40) con alfa 0.85 (ilustrativa). Para decidir si un
cambio entre dos mediciones es importante hay criterios distintos:
  - basado en la distribucion: 0.5 DE de la escala;
  - basado en el error: 1 ETM;
  - cambio fiable individual: 1.96 * ETM * sqrt(2).
Se calcula cada umbral con DE = 7 y se simula cuantas personas SIN cambio real superan cada uno
(falsos cambios). Los umbrales son convenciones; la "diferencia minima importante" clinica requiere
un criterio externo (ancla).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, DE, ALFA = 20000, 7.0, 0.85


def main() -> None:
    etm = DE * math.sqrt(1 - ALFA)
    umbrales = {"0.5 DE": 0.5 * DE, "1 ETM": etm, "cambio fiable (1.96*ETM*raiz2)": 1.96 * etm * math.sqrt(2)}
    rng = random.Random(SEMILLA)
    verd = [rng.gauss(18, DE * math.sqrt(ALFA)) for _ in range(N)]
    a = [v + rng.gauss(0, etm) for v in verd]
    b = [v + rng.gauss(0, etm) for v in verd]                       # SIN cambio real
    print(f"DE = {DE}, alfa = {ALFA}, ETM = {etm:.2f}")
    print(f"{'criterio':<34} {'umbral (puntos)':>16} {'falsos cambios (sin cambio real)':>34}")
    print("=" * 88)
    for nombre, u in umbrales.items():
        falsos = statistics.fmean(abs(y - x) >= u for x, y in zip(a, b, strict=True))
        print(f"{nombre:<34} {u:16.2f} {falsos:34.1%}")
    print()
    print("Lectura: 'cambio importante' depende del criterio: con 0.5 DE o 1 ETM, la mitad o mas de las personas")
    print("sin cambio real parecen haber cambiado. El cambio fiable controla el error de medida (5 %), pero")
    print("no dice si el cambio importa para la persona: eso requiere un criterio externo (ancla). Una")
    print("escala de estres percibido describe percepciones; no diagnostica ni reemplaza una evaluacion clinica.")


if __name__ == "__main__":
    main()
