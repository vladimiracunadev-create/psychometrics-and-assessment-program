"""Laboratorio 103 - Tipos frente a rasgos: la inestabilidad de dicotomizar un continuo.

Una dimension continua (extraversion), con fiabilidad test-retest alta (0.85), se convierte en
"tipo" (extravertido/introvertido) con un corte en la mediana. Se mide:
  - correlacion test-retest del puntaje continuo,
  - porcentaje de personas que CAMBIAN de tipo entre dos aplicaciones,
  - cuanto aumenta el cambio de tipo para quienes estan cerca del corte,
  - distribucion del puntaje: unimodal (continuo) aunque se rotule en dos tipos.
Con 4 dimensiones dicotomizadas, la probabilidad de conservar el tipo completo cae mucho.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, RHO = 20000, 0.85


def main() -> None:
    rng = random.Random(SEMILLA)
    sd_e = math.sqrt((1 - RHO) / RHO)
    t = [rng.gauss(0, 1) for _ in range(N)]
    a = [x + rng.gauss(0, sd_e) for x in t]
    b = [x + rng.gauss(0, sd_e) for x in t]
    corte_a, corte_b = statistics.median(a), statistics.median(b)
    cambian = sum((x > corte_a) != (y > corte_b) for x, y in zip(a, b, strict=True)) / N
    sd_a = statistics.pstdev(a)
    cerca = [(x, y) for x, y in zip(a, b, strict=True) if abs(x - corte_a) < 0.3 * sd_a]
    cambian_cerca = sum((x > corte_a) != (y > corte_b) for x, y in cerca) / len(cerca)
    print(f"Test-retest del puntaje continuo      r = {statistics.correlation(a, b):.3f}")
    print(f"Cambian de TIPO entre dos aplicaciones: {cambian:.1%}")
    print(f"  entre quienes estan cerca del corte (+-0.3 DE, {len(cerca) / N:.0%} de la muestra): {cambian_cerca:.1%}")

    # Cuatro dimensiones independientes dicotomizadas (tipo de 4 letras).
    iguales = 0
    for _ in range(5000):
        ok = True
        for _ in range(4):
            tt = rng.gauss(0, 1)
            x, y = tt + rng.gauss(0, sd_e), tt + rng.gauss(0, sd_e)
            ok &= (x > 0) == (y > 0)
        iguales += ok
    print(f"\nConservan los 4 rasgos dicotomizados ('tipo de 4 letras'): {iguales / 5000:.1%}")
    hist = [0] * 8
    for x in a:
        i = min(7, max(0, int((x + 2.4) // 0.6)))
        hist[i] += 1
    print("Distribucion del puntaje (barras):", " ".join(f"{h * 100 // N:2d}" for h in hist))
    print()
    print("Lectura: con una fiabilidad alta (0.85) igual cambia de tipo cerca del 17 %, y alrededor del")
    print("corte casi 4 de cada 10; con cuatro dimensiones, menos de la mitad conserva su 'tipo'. La")
    print("distribucion es unimodal: no hay dos tipos separados, hay un continuo. Las tipologias pueden")
    print("servir como lenguaje comun, no como evidencia de categorias naturales.")


if __name__ == "__main__":
    main()
