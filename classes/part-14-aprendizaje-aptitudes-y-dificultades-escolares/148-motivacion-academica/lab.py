"""Laboratorio 148 - Motivacion y rendimiento: efectos cruzados y error de medida.

Modelo de dos ondas: motivacion (M) y rendimiento (R) en T1 y T2. Efectos verdaderos:
  estabilidad M: 0.6, estabilidad R: 0.6, R1 -> M2: 0.25 (el exito motiva), M1 -> R2: 0.00 (la
  motivacion NO causa rendimiento, por construccion). Se observan con fiabilidad 0.7 (motivacion
  autoinformada) y 0.9 (rendimiento). Se estiman por regresion los coeficientes cruzados
  observados. Resultado: con error de medida, aparece un efecto M1 -> R2 espurio y el R1 -> M2 se
  subestima. Datos sinteticos.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 50000


def beta2(x1: list[float], x2: list[float], y: list[float]) -> tuple[float, float]:
    s11, s22 = statistics.variance(x1), statistics.variance(x2)
    s12 = statistics.covariance(x1, x2)
    s1y, s2y = statistics.covariance(x1, y), statistics.covariance(x2, y)
    det = s11 * s22 - s12**2
    return (s22 * s1y - s12 * s2y) / det, (s11 * s2y - s12 * s1y) / det


def main() -> None:
    rng = random.Random(SEMILLA)
    m1 = [rng.gauss(0, 1) for _ in range(N)]
    r1 = [0.5 * a + math.sqrt(0.75) * rng.gauss(0, 1) for a in m1]           # M y R correlacionadas
    m2 = [0.6 * a + 0.25 * b + 0.55 * rng.gauss(0, 1) for a, b in zip(m1, r1, strict=True)]
    r2 = [0.6 * b + 0.00 * a + 0.55 * rng.gauss(0, 1) for a, b in zip(m1, r1, strict=True)]
    print(f"{'condicion de medida':<34} {'M1->R2 (verdad 0.00)':>22} {'R1->M2 (verdad 0.25)':>22}")
    print("=" * 82)
    for nombre, fm, fr in (("sin error de medida", 1.0, 1.0), ("fiab. M = 0.7 y R = 0.9", 0.7, 0.9)):
        def ruido(v, f):
            sd = math.sqrt((1 - f) / f) * statistics.pstdev(v)
            return [x + rng.gauss(0, sd) for x in v]
        om1, or1, om2, or2 = ruido(m1, fm), ruido(r1, fr), ruido(m2, fm), ruido(r2, fr)
        _, b_m_r = beta2(or1, om1, or2)          # R2 ~ R1 + M1: coef de M1
        a_r_m, _ = beta2(or1, om1, om2)          # M2 ~ R1 + M1: coef de R1
        print(f"{nombre:<34} {b_m_r:22.3f} {a_r_m:22.3f}")
    print()
    print("Lectura: con medidas ruidosas el control de la variable previa es incompleto: aparece un efecto")
    print("espurio (pequeno) de la motivacion sobre el rendimiento y el efecto de exito -> motivacion se")
    print("SOBREestima (0.32 frente a 0.25). Los estudios cruzados exigen modelos con variables latentes. Motivacion y")
    print("rendimiento pueden influirse mutuamente: no se concluye causalidad desde un par de ondas.")


if __name__ == "__main__":
    main()
