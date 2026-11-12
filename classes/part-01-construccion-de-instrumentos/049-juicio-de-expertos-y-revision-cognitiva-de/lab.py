"""Laboratorio 049 - Juicio de expertos y revision cognitiva de items.

(1) Juicio de expertos: 8 expertos califican la relevancia (1-4) de 10 items. Se calcula el I-CVI
    (proporcion de 3 o 4) y el kappa modificado k* = (I-CVI - Pc) / (1 - Pc), con
    Pc = C(N, A) * 0.5^N, que descuenta el acuerdo esperado por azar (Polit, Beck y Owen, 2007).
(2) Revision cognitiva: 12 personas parafrasean cada item; un item se marca si mas del 25 % lo
    interpreta distinto de lo previsto.
Las dos fuentes detectan problemas distintos: se cruzan. Datos sinteticos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
EXPERTOS, ENTREVISTADOS, ITEMS = 8, 12, 10


def pc(n: int, a: int) -> float:
    return math.comb(n, a) * 0.5 ** n


def main() -> None:
    rng = random.Random(SEMILLA)
    rel = {0: 0.95, 1: 0.95, 2: 0.9, 3: 0.4, 4: 0.9, 5: 0.9, 6: 0.85, 7: 0.9, 8: 0.5, 9: 0.9}     # items 4 y 9 poco relevantes
    ambiguedad = {0: 0.05, 1: 0.05, 2: 0.45, 3: 0.1, 4: 0.05, 5: 0.5, 6: 0.05, 7: 0.1, 8: 0.1, 9: 0.05}   # items 3 y 6 ambiguos
    print(f"{'item':<5} {'acuerdan':>9} {'I-CVI':>6} {'k*':>6} {'mal interpretado':>17}  decision")
    print("=" * 76)
    for j in range(ITEMS):
        a = sum(rng.random() < rel[j] for _ in range(EXPERTOS))
        icvi = a / EXPERTOS
        p = pc(EXPERTOS, a)
        kmod = (icvi - p) / (1 - p)
        mal = sum(rng.random() < ambiguedad[j] for _ in range(ENTREVISTADOS)) / ENTREVISTADOS
        problemas = []
        if icvi < 0.78:
            problemas.append("revisar relevancia")
        if mal > 0.25:
            problemas.append("reescribir (ambiguo)")
        print(f"{j + 1:<5} {a:>6}/{EXPERTOS} {icvi:6.2f} {kmod:6.2f} {mal:17.0%}  {'; '.join(problemas) if problemas else 'conservar'}")
    print()
    print("Lectura: los expertos juzgan el contenido (relevancia), las entrevistas cognitivas revelan como lo")
    print("entiende la poblacion objetivo; un item puede ser relevante y ambiguo, o claro e irrelevante. El k*")
    print("corrige el I-CVI por el acuerdo esperado al azar. Ninguna de las dos fuentes reemplaza el piloto con")
    print("datos (clase 010). Los umbrales son convenciones, no verdades. Datos sinteticos.")


if __name__ == "__main__":
    main()
