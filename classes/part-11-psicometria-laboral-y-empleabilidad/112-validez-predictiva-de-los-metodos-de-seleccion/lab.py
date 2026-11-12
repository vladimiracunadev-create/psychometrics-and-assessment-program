"""Laboratorio 112 - Validez incremental y utilidad de combinar predictores (cifras ILUSTRATIVAS).

Los coeficientes de validez de la literatura de seleccion dependen de la poblacion, el criterio
y las correcciones aplicadas (Schmidt y Hunter, 1998; Sackett et al., 2022 revisaron varias
estimaciones a la baja). Aqui NO se citan como hechos: se usan valores ilustrativos para
mostrar el calculo.
  1. Validez de un compuesto de 2 predictores con intercorrelacion r12:
        R = sqrt( (v1^2 + v2^2 - 2 r12 v1 v2) / (1 - r12^2) )
  2. Utilidad (Brogden-Cronbach-Gleser): dU = N_sel * T * R * SD_y * lambda - costo_total
     con lambda = ordenada normal del corte / razon de seleccion.
"""
from __future__ import annotations

import math
from statistics import NormalDist

ND = NormalDist()


def compuesto(v1: float, v2: float, r12: float) -> float:
    return math.sqrt((v1**2 + v2**2 - 2 * r12 * v1 * v2) / (1 - r12**2))


def utilidad(r: float, razon_sel: float, n_postulantes: int, sd_y: float, anios: float,
             costo_por_postulante: float) -> float:
    z = ND.inv_cdf(1 - razon_sel)
    lam = ND.pdf(z) / razon_sel
    n_sel = n_postulantes * razon_sel
    return n_sel * anios * r * sd_y * lam - n_postulantes * costo_por_postulante


def main() -> None:
    print("Validez del compuesto (v1 = 0.35 test cognitivo, v2 = 0.35 entrevista estructurada)")
    print(f"{'r12':>5} {'R compuesto':>12} {'ganancia sobre el mejor':>25}")
    for r12 in (0.0, 0.2, 0.4, 0.6):
        R = compuesto(0.35, 0.35, r12)
        print(f"{r12:5.1f} {R:12.3f} {R - 0.35:25.3f}")
    print("\nUtilidad anual estimada (100 postulantes, razon de seleccion 20 %, SDy = 8 000 000 CLP, 2 anios; montos en CLP)")
    print(f"{'predictor(es)':<30} {'validez':>8} {'costo/postulante':>17} {'utilidad':>14}")
    casos = [("sin seleccion (azar)", 0.0, 0), ("solo entrevista", 0.35, 40_000),
             ("entrevista + test", compuesto(0.35, 0.35, 0.2), 70_000)]
    for nombre, r, c in casos:
        u = utilidad(r, 0.20, 100, 8_000_000, 2, c)
        print(f"{nombre:<30} {r:8.3f} {c:17,} {u:14,.0f}")
    print()
    print("Lectura: el segundo predictor suma validez solo en la medida en que NO este correlacionado")
    print("con el primero. La utilidad proyectada depende fuertemente de SDy (la variabilidad del valor")
    print("del desempeno), que es dificil de estimar: por eso se presenta como rango y con supuestos.")
    print("Estas cifras son ilustrativas; en un proceso real se usan estimaciones locales y recientes.")


if __name__ == "__main__":
    main()
