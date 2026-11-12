"""Laboratorio 160 - Evaluar un programa de orientacion: tamano de muestra para detectar un efecto.

Diseno pre-post con grupo de comparacion y resultado continuo (p. ej. un indice de claridad
vocacional). Se calcula el numero de estudiantes por grupo para detectar un efecto estandarizado
d con potencia 80 % y alfa 0.05 (aproximacion normal), considerando:
  - la correlacion pre-post (un ANCOVA/ajuste por pretest reduce la varianza: 1 - r^2),
  - el efecto del diseno por agrupamiento (cursos completos): DEFF = 1 + (m - 1) * ICC.
Se verifica la potencia por simulacion para un caso. Cifras de efecto supuestas; la literatura de
programas de orientacion muestra efectos de magnitud variable.
"""
from __future__ import annotations

import math
import random
import statistics
from statistics import NormalDist

ND = NormalDist()
SEMILLA = 20260819


def n_por_grupo(d: float, r_pp: float = 0.0, potencia: float = 0.80, alfa: float = 0.05) -> float:
    z = ND.inv_cdf(1 - alfa / 2) + ND.inv_cdf(potencia)
    return 2 * (z / d) ** 2 * (1 - r_pp**2)


def simula_potencia(d: float, n: int, r_pp: float, reps: int, rng: random.Random) -> float:
    rechazos = 0
    for _ in range(reps):
        diffs = []
        for g in (0, 1):
            pre = [rng.gauss(0, 1) for _ in range(n)]
            post = [r_pp * a + math.sqrt(1 - r_pp**2) * rng.gauss(0, 1) + d * g for a in pre]
            b = statistics.covariance(pre, post) / statistics.variance(pre)
            res = [p - b * a for a, p in zip(pre, post, strict=True)]
            diffs.append(res)
        se = math.sqrt(statistics.variance(diffs[0]) / n + statistics.variance(diffs[1]) / n)
        z = (statistics.fmean(diffs[1]) - statistics.fmean(diffs[0])) / se
        rechazos += abs(z) > 1.96
    return rechazos / reps


def main() -> None:
    print(f"{'efecto d':>9} {'sin ajustar':>12} {'ajuste (r pre-post = 0.6)':>27} {'por cursos (m=30, ICC=0.05)':>30}")
    print("=" * 84)
    for d in (0.2, 0.3, 0.5):
        n0 = n_por_grupo(d)
        n1 = n_por_grupo(d, 0.6)
        deff = 1 + (30 - 1) * 0.05
        print(f"{d:9.1f} {math.ceil(n0):12d} {math.ceil(n1):27d} {math.ceil(n1 * deff):30d}")
    rng = random.Random(SEMILLA)
    n = math.ceil(n_por_grupo(0.5, 0.6))
    print(f"\nVerificacion: d = 0.5, r = 0.6, n = {n} por grupo -> potencia simulada = "
          f"{simula_potencia(0.5, n, 0.6, 600, rng):.2f} (objetivo 0.80)")
    print()
    print("Lectura: detectar un efecto pequeno exige muchos estudiantes, y mas si se asigna por curso.")
    print("Medir el pretest (y ajustar por el) reduce el tamano necesario. Un programa de orientacion")
    print("basado en evidencia declara su logica (insumos, actividades, resultados esperados), su medida y")
    print("su tamano de muestra ANTES de empezar, e informa tambien si no encuentra efectos.")


if __name__ == "__main__":
    main()
