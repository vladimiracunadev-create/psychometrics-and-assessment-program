"""Laboratorio 142 - Palabras correctas por minuto (PCM): error de medida y eleccion de textos.

Cada lectura de un texto de 1 minuto da PCM = habilidad + efecto del texto (dificultad) + ruido
del dia. Se calcula, para un grupo de 500 estudiantes de segundo basico (habilidad ~ N(80, 25)):
  - el error tipico de una sola lectura,
  - la fiabilidad de 1 lectura frente a la mediana de 3 lecturas con textos distintos,
  - cuantos estudiantes cambian de lado respecto de un criterio de logro (60 PCM) segun el numero de
    lecturas (error de clasificacion).
Valores supuestos del laboratorio; los criterios de logro reales vienen de estudios locales.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, CORTE = 500, 60.0
SD_TEXTO, SD_DIA = 8.0, 9.0


def lecturas(hab: float, k: int, rng: random.Random) -> list[float]:
    return [hab + rng.gauss(0, SD_TEXTO) + rng.gauss(0, SD_DIA) for _ in range(k)]


def main() -> None:
    rng = random.Random(SEMILLA)
    hab = [rng.gauss(80, 25) for _ in range(N)]
    una_a = [lecturas(h, 1, rng)[0] for h in hab]
    una_b = [lecturas(h, 1, rng)[0] for h in hab]
    med_a = [statistics.median(lecturas(h, 3, rng)) for h in hab]
    med_b = [statistics.median(lecturas(h, 3, rng)) for h in hab]
    err_una = (SD_TEXTO**2 + SD_DIA**2) ** 0.5
    print(f"Error tipico de UNA lectura = {err_una:.1f} PCM (texto {SD_TEXTO} + dia {SD_DIA})")
    print(f"{'procedimiento':<28} {'fiabilidad (test-retest)':>25} {'cambian de lado del corte':>27}")
    for nombre, a, b in (("1 lectura", una_a, una_b), ("mediana de 3 lecturas", med_a, med_b)):
        cambian = sum((x >= CORTE) != (y >= CORTE) for x, y in zip(a, b, strict=True)) / N
        print(f"{nombre:<28} {statistics.correlation(a, b):25.2f} {cambian:27.1%}")
    cerca = sum(abs(h - CORTE) <= 1.96 * err_una for h in hab) / N
    print(f"\nEstudiantes a menos de ±{1.96 * err_una:.0f} PCM del corte (zona de incertidumbre): {cerca:.0%}")
    print()
    print("Lectura: una sola lectura clasifica distinto a una parte importante de los estudiantes cerca")
    print("del corte; la mediana de tres textos reduce el error. Fluidez incluye precision y prosodia, no solo")
    print("velocidad: leer mas rapido no es leer mejor. Los criterios de logro por curso se verifican en")
    print("fuentes oficiales o estudios locales; los valores de este laboratorio son ilustrativos.")


if __name__ == "__main__":
    main()
