"""Laboratorio 150 - Escalamiento de logro de metas (GAS): el puntaje T y sus supuestos.

Metas individuales con niveles de logro -2 (mucho menos de lo esperado) a +2 (mucho mas), con
pesos w_i. Puntaje T de GAS (Kiresuk y Sherman, 1968):
    T = 50 + 10 * sum(w_i x_i) / sqrt( (1 - rho) * sum(w_i^2) + rho * (sum w_i)^2 ),  rho = 0.3
Se calcula T para dos estudiantes, se muestra la sensibilidad a los pesos y por que el T de GAS
NO es comparable entre estudiantes (cada uno tiene metas distintas con dificultades distintas).
rho = 0.3 es una convencion historica.
"""
from __future__ import annotations

import math

RHO = 0.3


def gas_t(logros: list[int], pesos: list[float]) -> float:
    num = sum(w * x for w, x in zip(pesos, logros, strict=True))
    den = math.sqrt((1 - RHO) * sum(w * w for w in pesos) + RHO * sum(pesos) ** 2)
    return 50 + 10 * num / den


def main() -> None:
    print("Estudiante A: 3 metas")
    print(f"  logros (0, +1, 0) pesos iguales      -> T = {gas_t([0, 1, 0], [1, 1, 1]):.1f}")
    print(f"  logros (0, +1, 0) peso 3 a la meta 2 -> T = {gas_t([0, 1, 0], [1, 3, 1]):.1f}")
    print(f"  logros (+1, 0, 0) peso 3 a la meta 1 -> T = {gas_t([1, 0, 0], [3, 1, 1]):.1f}")
    print("Estudiante B: 5 metas, todas 'se logra lo esperado' (0) -> "
          f"T = {gas_t([0, 0, 0, 0, 0], [1] * 5):.1f}")
    print(f"Estudiante B: 5 metas con +1 en una sola                -> T = {gas_t([1, 0, 0, 0, 0], [1] * 5):.1f}")
    print(f"Estudiante B: 5 metas con +1 en todas                    -> T = {gas_t([1] * 5, [1] * 5):.1f}")
    print()
    print("Lectura: T = 50 significa 'se logro lo esperado' en las metas que se fijaron; no dice nada sobre")
    print("el nivel de partida ni la dificultad de las metas, ni permite comparar estudiantes. Es util para")
    print("seguir el logro de objetivos individualizados (con redaccion observable y acuerdo con la familia)")
    print("y complementa, sin reemplazar, la evaluacion del progreso curricular. El T depende de rho y de los pesos.")


if __name__ == "__main__":
    main()
