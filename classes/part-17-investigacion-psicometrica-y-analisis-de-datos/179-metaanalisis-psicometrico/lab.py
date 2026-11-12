"""Laboratorio 179 - Generalizacion de la fiabilidad: metaanalisis de coeficientes alfa.

25 estudios informan el alfa de la misma escala, con n distintos y heterogeneidad real (el alfa
verdadero varia entre muestras: media 0.80, DE 0.05). Se transforma cada alfa con la
transformacion de Bonett (ln(1 - alfa)) y se aplica un modelo de efectos aleatorios
(DerSimonian-Laird): media agrupada, tau^2, I^2 e intervalo de prediccion para un estudio NUEVO.
Muestra que "el alfa de la escala" no es una constante: depende de la muestra.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
ESTUDIOS, K_ITEMS = 25, 10


def main() -> None:
    rng = random.Random(SEMILLA)
    ys, vs, alfas, ns = [], [], [], []
    for _ in range(ESTUDIOS):
        n = rng.choice([60, 90, 120, 200, 350, 500])
        a_verd = min(0.97, max(0.5, rng.gauss(0.80, 0.05)))
        # alfa observado ~ alrededor del verdadero con error de muestreo aproximado (van Zyl et al.)
        ee = math.sqrt(2 * K_ITEMS * (1 - a_verd) ** 2 / ((K_ITEMS - 1) * (n - 2)))
        a_obs = min(0.99, a_verd + rng.gauss(0, ee))
        y = math.log(1 - a_obs)
        v = (2 * K_ITEMS / (K_ITEMS - 1)) / (n - 2)                # varianza de ln(1-alfa) (Bonett)
        ys.append(y)
        vs.append(v)
        alfas.append(a_obs)
        ns.append(n)
    w = [1 / v for v in vs]
    y_fe = sum(wi * y for wi, y in zip(w, ys, strict=True)) / sum(w)
    q = sum(wi * (y - y_fe) ** 2 for wi, y in zip(w, ys, strict=True))
    c = sum(w) - sum(wi * wi for wi in w) / sum(w)
    tau2 = max(0.0, (q - (ESTUDIOS - 1)) / c)
    w_re = [1 / (v + tau2) for v in vs]
    y_re = sum(wi * y for wi, y in zip(w_re, ys, strict=True)) / sum(w_re)
    se_re = math.sqrt(1 / sum(w_re))
    i2 = max(0.0, (q - (ESTUDIOS - 1)) / q) if q > 0 else 0.0
    inv = lambda y: 1 - math.exp(y)  # noqa: E731
    pred_se = math.sqrt(tau2 + se_re**2)
    print(f"Estudios = {ESTUDIOS}; alfa observado: media simple = {statistics.fmean(alfas):.3f}, "
          f"rango [{min(alfas):.2f}; {max(alfas):.2f}]")
    print(f"Efectos aleatorios: alfa agrupado = {inv(y_re):.3f}  IC 95 % [{inv(y_re + 1.96 * se_re):.3f}; {inv(y_re - 1.96 * se_re):.3f}]")
    print(f"Heterogeneidad: tau^2 = {tau2:.4f}; I^2 = {i2:.0%}")
    print(f"Intervalo de PREDICCION para un estudio nuevo: [{inv(y_re + 1.96 * pred_se):.3f}; {inv(y_re - 1.96 * pred_se):.3f}]")
    print()
    print("Lectura: el alfa agrupado se estima con precision, pero un estudio NUEVO puede dar valores bastante")
    print("distintos (intervalo de prediccion mas ancho). Afirmar 'la escala tiene alfa 0.80' sin la muestra es")
    print("incompleto. La fiabilidad se estima en cada contexto de uso, o se declara la evidencia de generalizacion.")


if __name__ == "__main__":
    main()
