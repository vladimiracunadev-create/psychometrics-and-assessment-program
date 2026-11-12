"""Laboratorio 120 - Impacto adverso: razon de tasas y prueba exacta de Fisher.

Dos grupos. La "regla de los cuatro quintos" (razon de tasas < 0.80) es una alerta de origen
estadounidense (Uniform Guidelines, 1978), NO una norma chilena ni una prueba de
discriminacion. Se contrasta con una prueba de significacion (Fisher exacto, bilateral) en
cuatro escenarios, para mostrar que:
  - con muestras pequenas una razon < 0.80 puede ser compatible con el azar,
  - con muestras grandes una razon > 0.80 (diferencia pequena) puede ser significativa.
El analisis juridico en Chile (principio de no discriminacion, Codigo del Trabajo) es otra cosa y
corresponde a profesionales del derecho.
"""
from __future__ import annotations

import math


def hipergeom(k: int, n1: int, n2: int, m: int) -> float:
    """P(X = k): de n1+n2 personas, m son seleccionadas; n1 en el grupo 1."""
    return math.comb(n1, k) * math.comb(n2, m - k) / math.comb(n1 + n2, m)


def fisher_bilateral(a: int, n1: int, b: int, n2: int) -> float:
    m = a + b
    p_obs = hipergeom(a, n1, n2, m)
    lo, hi = max(0, m - n2), min(n1, m)
    return min(1.0, sum(p for k in range(lo, hi + 1) if (p := hipergeom(k, n1, n2, m)) <= p_obs * (1 + 1e-9)))


def main() -> None:
    casos = [
        ("muestras pequenas (n=20 y 20), razon 0.67", 9, 20, 6, 20),
        ("muestras medianas (n=100 y 100), razon 0.67", 45, 100, 30, 100),
        ("muestras grandes (n=3000 y 3000), razon 0.90", 1500, 3000, 1350, 3000),
        ("sin diferencia (n=300 y 300), razon 1.00", 90, 300, 90, 300),
    ]
    print(f"{'escenario':<48} {'tasa G1':>8} {'tasa G2':>8} {'razon':>6} {'alerta 4/5':>11} {'p (Fisher)':>11}")
    print("=" * 100)
    for nombre, a, n1, b, n2 in casos:
        t1, t2 = a / n1, b / n2
        print(f"{nombre:<48} {t1:8.3f} {t2:8.3f} {t2 / t1:6.2f} {'SI' if t2 / t1 < 0.8 else 'no':>11} "
              f"{fisher_bilateral(a, n1, b, n2):11.4f}")
    print()
    print("Lectura: la regla de los 4/5 y la significacion estadistica miden cosas distintas. Con n=20")
    print("la razon 0.67 NO es estadisticamente distinguible del azar; con n=3000 una razon 0.90 si.")
    print("Ninguna prueba dice POR SI SOLA si hay discriminacion: se requiere analizar la justificacion")
    print("(validez del proceso para el puesto), alternativas con menor impacto y el marco legal local.")


if __name__ == "__main__":
    main()
