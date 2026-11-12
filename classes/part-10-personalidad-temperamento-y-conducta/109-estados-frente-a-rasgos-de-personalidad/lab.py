"""Laboratorio 109 - Estado y rasgo: descomponer la varianza de mediciones repetidas.

Datos de muestreo de experiencias (30 personas x 20 dias). Dos variables:
  - "extraversion tipo rasgo": gran diferencia entre personas, poca fluctuacion diaria;
  - "animo tipo estado": poca diferencia entre personas, mucha fluctuacion diaria.
Con ANOVA de un factor se estima el CCI(1) = var_entre / (var_entre + var_dentro): la
proporcion de varianza que es "rasgo". Una escala medida una sola vez en una persona
mezcla ambos componentes, y el puntaje de UN dia es poco fiable como rasgo si el CCI es bajo.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, DIAS = 300, 20


def cci(datos: list[list[float]]) -> tuple[float, float, float]:
    k = len(datos[0])
    mg = statistics.fmean(v for f in datos for v in f)
    mp = [statistics.fmean(f) for f in datos]
    msb = k * sum((m - mg) ** 2 for m in mp) / (len(datos) - 1)
    msw = sum((v - m) ** 2 for f, m in zip(datos, mp, strict=True) for v in f) / (len(datos) * (k - 1))
    entre = max(0.0, (msb - msw) / k)
    return entre / (entre + msw), entre, msw


def main() -> None:
    rng = random.Random(SEMILLA)
    variables = {"extraversion (rasgo)": (1.0, 0.5), "animo (estado)": (0.3, 1.0)}
    print(f"{'variable':<24} {'var entre':>10} {'var dentro':>11} {'CCI(1)':>7} {'fiab. de UN dia':>16} "
          f"{'fiab. de promedio 20 d':>24}")
    print("=" * 98)
    for nombre, (sd_p, sd_d) in variables.items():
        datos = []
        for _ in range(N):
            base = rng.gauss(0, sd_p)
            datos.append([base + rng.gauss(0, sd_d) for _ in range(DIAS)])
        icc1, entre, dentro = cci(datos)
        sb = DIAS * icc1 / (1 + (DIAS - 1) * icc1)
        print(f"{nombre:<24} {entre:10.2f} {dentro:11.2f} {icc1:7.2f} {icc1:16.2f} {sb:24.2f}")
    print()
    print("Lectura: en la variable tipo rasgo, el 80 % de la varianza es entre personas y un solo dia")
    print("ya informa; en la tipo estado, solo ~8 % es de la persona, y recien el promedio de muchos")
    print("dias estima el nivel habitual. Preguntar 'como se siente HOY' y 'como es USUALMENTE' son")
    print("mediciones distintas: se elige el marco temporal del enunciado segun lo que se quiere inferir.")


if __name__ == "__main__":
    main()
