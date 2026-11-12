"""Laboratorio 010 - Estadistica descriptiva para evaluacion: que resumen elegir.

Se simulan dos conjuntos de datos de 1.000 personas:
  - puntajes de un test aproximadamente simetricos,
  - tiempos de respuesta con cola larga (asimetricos) con unos pocos valores extremos.
Se calculan media, mediana, desviacion tipica, rango intercuartil, asimetria y percentiles, y se
muestra con un histograma de texto por que la media es enganosa en el segundo caso. Tambien se
anade un valor extremo (un error de digitacion) y se mide que resumenes lo toleran.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 1000


def asimetria(x: list[float]) -> float:
    m, s = statistics.fmean(x), statistics.pstdev(x)
    return sum(((v - m) / s) ** 3 for v in x) / len(x)


def percentil(x: list[float], p: float) -> float:
    return statistics.quantiles(x, n=100, method="inclusive")[int(p) - 1]


def resumen(nombre: str, x: list[float]) -> None:
    q1, q3 = percentil(x, 25), percentil(x, 75)
    print(f"{nombre:<26} media {statistics.fmean(x):7.1f}  mediana {statistics.median(x):7.1f}  DE {statistics.stdev(x):6.1f}  "
          f"RIC {q3 - q1:6.1f}  asimetria {asimetria(x):5.2f}  P90 {percentil(x, 90):7.1f}")


def histograma(x: list[float], bins: int = 10) -> None:
    lo, hi = min(x), max(x)
    ancho = (hi - lo) / bins
    cuentas = [0] * bins
    for v in x:
        cuentas[min(bins - 1, int((v - lo) / ancho))] += 1
    for i, c in enumerate(cuentas):
        print(f"   {lo + i * ancho:7.1f} | {'#' * (c * 50 // max(cuentas))} {c}")


def main() -> None:
    rng = random.Random(SEMILLA)
    puntajes = [max(0, min(100, rng.gauss(55, 12))) for _ in range(N)]
    tiempos = [math.exp(rng.gauss(1.4, 0.7)) for _ in range(N)]
    resumen("puntajes (simetricos)", puntajes)
    resumen("tiempos (cola larga)", tiempos)
    print("\nHistograma de los tiempos (segundos):")
    histograma(tiempos)
    con_error = tiempos + [9999.0]
    print("\nAgregando UN valor erroneo (9999 s):")
    resumen("tiempos + 1 error", con_error)
    print()
    print("Lectura: con datos simetricos la media y la mediana coinciden; con cola larga la media queda por encima")
    print("de la mediana y un solo error de digitacion la arrastra, mientras que la mediana y el rango intercuartil")
    print("casi no cambian. Antes de resumir hay que graficar; el resumen se elige segun la forma, y los valores")
    print("extremos se investigan, no se borran sin registro. Datos sinteticos.")


if __name__ == "__main__":
    main()
