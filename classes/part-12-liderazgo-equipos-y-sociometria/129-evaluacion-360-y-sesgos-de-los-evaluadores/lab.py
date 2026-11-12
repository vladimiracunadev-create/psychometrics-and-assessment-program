"""Laboratorio 129 - Evaluacion 360: fuentes de varianza y fiabilidad del promedio de pares.

Cada rating = desempeno verdadero del evaluado + sesgo idiosincratico del evaluador + error.
Se simulan 300 evaluados con 1, 3, 6 y 10 pares, mas una autoevaluacion (con indulgencia). Se
calcula:
  - la fiabilidad del promedio de n pares (CCI(1,k) = icc1*k/(1+(k-1)*icc1)), con icc1 = acuerdo
    entre UN par y otro,
  - la correlacion entre autoevaluacion y promedio de pares (auto-otros),
  - la diferencia media auto - pares (indulgencia de la autoevaluacion).
Parametros supuestos del laboratorio.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 300
SD_VERD, SD_SESGO, SD_ERR = 1.0, 0.7, 0.5


def main() -> None:
    rng = random.Random(SEMILLA)
    verd = [rng.gauss(0, SD_VERD) for _ in range(N)]
    # Un par: v + sesgo del par + error. Dos pares distintos solo comparten v.
    def par(v: float) -> float:
        return v + rng.gauss(0, SD_SESGO) + rng.gauss(0, SD_ERR)

    pares = [[par(v) for _ in range(10)] for v in verd]
    icc1 = statistics.correlation([p[0] for p in pares], [p[1] for p in pares])
    print(f"Acuerdo entre dos pares distintos (icc1) = {icc1:.2f}  [teorico {SD_VERD**2 / (SD_VERD**2 + SD_SESGO**2 + SD_ERR**2):.2f}]")
    print(f"\n{'pares':>6} {'fiabilidad del promedio':>25} {'r promedio-verdad':>19}")
    for k in (1, 3, 6, 10):
        prom = [statistics.fmean(p[:k]) for p in pares]
        rel = k * icc1 / (1 + (k - 1) * icc1)
        print(f"{k:6d} {rel:25.2f} {statistics.correlation(prom, verd):19.2f}")
    auto = [v * 0.6 + 0.8 + rng.gauss(0, 0.9) for v in verd]          # indulgente y menos ligada al desempeno
    prom6 = [statistics.fmean(p[:6]) for p in pares]
    print(f"\nCorrelacion autoevaluacion - promedio de 6 pares = {statistics.correlation(auto, prom6):.2f}")
    print(f"Diferencia media (auto - pares) = {statistics.fmean(auto) - statistics.fmean(prom6):+.2f} puntos (indulgencia)")
    print()
    print("Lectura: un solo evaluador es poco fiable porque el sesgo idiosincratico domina; con 6 a 10")
    print("pares la fiabilidad es aceptable. La autoevaluacion difiere de los demas por indulgencia y")
    print("por distinta informacion, no necesariamente por 'falta de autoconocimiento'. Un 360 es")
    print("un insumo para el desarrollo; usarlo para decisiones de personal exige evidencia adicional.")


if __name__ == "__main__":
    main()
