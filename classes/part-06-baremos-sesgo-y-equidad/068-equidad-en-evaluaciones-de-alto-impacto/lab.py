"""Laboratorio 068 - Validez frente a impacto adverso: el dilema de los pesos.

Se combinan dos predictores en un compuesto: P1 (alta validez, gran diferencia entre grupos)
y P2 (validez menor, diferencia pequena). Los valores son SUPUESTOS ilustrativos:
    P1: validez 0.50, d = 1.0 | P2: validez 0.30, d = 0.2 | intercorrelacion 0.20
Se calculan, segun el peso w del P1 en el compuesto, la validez del compuesto, su diferencia
de grupos y la razon de seleccion del grupo minoritario con una seleccion del 20 % superior
del grupo mayoritario (aproximacion normal). Ver Pyburn et al. (2008) sobre el dilema
diversidad-validez.
"""
from __future__ import annotations

import math
from statistics import NormalDist

V1, V2, D1, D2, R12 = 0.50, 0.30, 1.0, 0.2, 0.20
SELECCION_MAYORITARIA = 0.20


def main() -> None:
    nd = NormalDist()
    z_corte = nd.inv_cdf(1 - SELECCION_MAYORITARIA)
    print(f"{'peso P1':>8} {'validez R':>10} {'d compuesto':>12} {'tasa minoria':>13} {'razon':>7}")
    print("=" * 56)
    for w1 in (1.0, 0.8, 0.6, 0.5, 0.4, 0.2, 0.0):
        w2 = 1 - w1
        sd = math.sqrt(w1 * w1 + w2 * w2 + 2 * w1 * w2 * R12)
        validez = (w1 * V1 + w2 * V2) / sd
        d = (w1 * D1 + w2 * D2) / sd
        tasa_min = 1 - nd.cdf(z_corte + d)
        print(f"{w1:8.1f} {validez:10.3f} {d:12.3f} {tasa_min:13.3f} {tasa_min / SELECCION_MAYORITARIA:7.2f}")
    print()
    print("Lectura: bajar el peso del predictor con mayor diferencia de grupos reduce el impacto")
    print("adverso, pero tambien la validez: el costo de cada punto de diversidad en validez se")
    print("puede calcular, y esa es la discusion honesta. Los numeros dependen de los supuestos;")
    print("con valores de otro contexto la curva cambia. No hay ponderacion 'correcta' sin decidir")
    print("antes que se valora, y quien lo decide.")


if __name__ == "__main__":
    main()
