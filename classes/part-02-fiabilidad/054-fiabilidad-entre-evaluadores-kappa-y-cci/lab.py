"""Laboratorio 054 - Acuerdo entre evaluadores: porcentaje, kappa y CCI.

Parte 1: con una categoria muy prevalente, el acuerdo crudo es alto y kappa de Cohen
baja, porque descuenta el acuerdo esperado por azar.
Parte 2: dos jueces puntuan 0-10 a 300 productos. Un juez es sistematicamente mas
severo. La correlacion (y el CCI de consistencia) casi no lo ve; el CCI de acuerdo
absoluto si. Formulas de Shrout y Fleiss (1979) por ANOVA de dos factores.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 300


def kappa(a: list[int], b: list[int]) -> tuple[float, float]:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b, strict=True)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return po, (po - pe) / (1 - pe)


def icc(puntajes: list[list[float]]) -> tuple[float, float]:
    """Devuelve (ICC(3,1) consistencia, ICC(2,1) acuerdo absoluto). Filas = sujetos."""
    n, k = len(puntajes), len(puntajes[0])
    gm = statistics.fmean(v for f in puntajes for v in f)
    mf = [statistics.fmean(f) for f in puntajes]
    mc = [statistics.fmean(puntajes[i][j] for i in range(n)) for j in range(k)]
    msr = k * sum((m - gm) ** 2 for m in mf) / (n - 1)
    msc = n * sum((m - gm) ** 2 for m in mc) / (k - 1)
    sse = sum((puntajes[i][j] - mf[i] - mc[j] + gm) ** 2 for i in range(n) for j in range(k))
    mse = sse / ((n - 1) * (k - 1))
    icc31 = (msr - mse) / (msr + (k - 1) * mse)
    icc21 = (msr - mse) / (msr + (k - 1) * mse + k * (msc - mse) / n)
    return icc31, icc21


def main() -> None:
    rng = random.Random(SEMILLA)
    # Parte 1: 92 % de casos "sin hallazgo".
    verdad = [int(rng.random() < 0.08) for _ in range(1000)]
    a = [v if rng.random() < 0.93 else 1 - v for v in verdad]
    b = [v if rng.random() < 0.93 else 1 - v for v in verdad]
    po, k = kappa(a, b)
    print("Parte 1 - deteccion de un hallazgo raro por dos evaluadores")
    print(f"  acuerdo crudo = {po:.3f}   kappa de Cohen = {k:.3f}")
    print()

    # Parte 2: severidad distinta.
    real = [rng.gauss(5, 1.5) for _ in range(N)]
    j1 = [r + rng.gauss(0, 0.6) for r in real]
    j2 = [r - 1.5 + rng.gauss(0, 0.6) for r in real]          # juez 2: 1.5 puntos mas severo
    c, ab = icc(list(map(list, zip(j1, j2, strict=True))))
    print("Parte 2 - dos jueces, el segundo 1.5 puntos mas severo")
    print(f"  correlacion Pearson        = {statistics.correlation(j1, j2):.3f}")
    print(f"  CCI consistencia (3,1)     = {c:.3f}")
    print(f"  CCI acuerdo absoluto (2,1) = {ab:.3f}")
    print()
    print("Lectura: el porcentaje de acuerdo y la correlacion pueden verse excelentes")
    print("mientras kappa o el CCI de acuerdo revelan el problema. Hay que declarar")
    print("QUE tipo de acuerdo importa para la decision (clasificar vs puntuar).")


if __name__ == "__main__":
    main()
