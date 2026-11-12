"""Laboratorio 171 - Plan de un estudio de validacion: que muestra exige cada afirmacion.

Para cada componente de evidencia de un estudio de validacion se calcula el tamano de muestra
minimo (aproximaciones estandar) con supuestos EXPLICITOS:
  - alfa de Cronbach con precision de +-0.05 (aprox. de van Zyl, Neudecker y Nel, 2000):
        EE(alfa) ~ sqrt( 2k(1-alfa)^2 / ((k-1)(n-2)) ),  n = 2k(1-alfa)^2 (1.96/mitad)^2/(k-1) + 2
  - correlacion convergente r = 0.50 frente a discriminante r = 0.30 (dif. de correlaciones
    independientes, Fisher z),
  - diferencia entre dos grupos d = 0.30 (potencia 80 %),
  - AFC: 10 casos por parametro libre (una regla heuristica, no una garantia).
Las filas son un punto de partida; el plan real se ajusta a la poblacion y al uso previsto.
"""
from __future__ import annotations

import math
from statistics import NormalDist

ND = NormalDist()
Z_A, Z_B = ND.inv_cdf(0.975), ND.inv_cdf(0.80)


def n_alfa(alfa: float, k: int, mitad: float = 0.05) -> int:
    return math.ceil(2 * k * (1 - alfa) ** 2 * (Z_A / mitad) ** 2 / (k - 1) + 2)


def n_dif_corr(r1: float, r2: float) -> int:
    dz = math.atanh(r1) - math.atanh(r2)
    return math.ceil(2 * ((Z_A + Z_B) / dz) ** 2 + 6)


def n_corr(r: float) -> int:
    return math.ceil(((Z_A + Z_B) / math.atanh(r)) ** 2 + 3)


def n_d(d: float) -> int:
    return math.ceil(2 * ((Z_A + Z_B) / d) ** 2) * 2


def main() -> None:
    k_items, parametros = 12, 12 + 12 + 1            # cargas + varianzas unicas + varianza del factor (aprox.)
    filas = [
        ("fiabilidad (alfa = 0.80, 12 items, +-0.05)", n_alfa(0.80, k_items)),
        ("fiabilidad (alfa = 0.90, 12 items, +-0.05)", n_alfa(0.90, k_items)),
        ("correlacion con un criterio (r = 0.30)", n_corr(0.30)),
        ("convergente 0.50 > discriminante 0.30", n_dif_corr(0.50, 0.30)),
        ("diferencia entre grupos conocidos (d = 0.30), total", n_d(0.30)),
        (f"AFC (10 casos x {parametros} parametros)", 10 * parametros),
    ]
    print(f"{'componente de evidencia':<56} {'N minimo':>9}")
    print("=" * 68)
    for nombre, n in filas:
        print(f"{nombre:<56} {n:9d}")
    print(f"\nEl componente mas exigente fija el N del estudio: {max(n for _, n in filas)} personas")
    print()
    print("Lectura: cada afirmacion de validez tiene su propio costo muestral. Un estudio con 150 personas")
    print("puede estimar un alfa con precision razonable, pero no distingue una correlacion convergente de")
    print("una discriminante cercana. El plan (muestra, hipotesis, analisis) se declara ANTES de ver los datos")
    print("(clase 178); los supuestos del calculo (efectos, fiabilidad esperada) se documentan.")


if __name__ == "__main__":
    main()
