"""Laboratorio 032 - Validez de contenido: I-CVI y V de Aiken con jueces simulados.

Seis jueces califican la relevancia de 12 items en una escala 1-4.
  I-CVI = proporcion de jueces que da 3 o 4.
  V de Aiken = suma(r - minimo) / (n * (categorias - 1)).
Se siembran 2 items poco relevantes para ver si los indicadores los detectan.
Los umbrales (I-CVI >= 0.78 con 6 o mas jueces; Lynn, 1986; Polit y Beck, 2006) son
convenciones de la literatura, no leyes.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
JUECES, CATS = 6, 4
RELEVANCIA_REAL = [3.6] * 10 + [2.0, 1.8]      # items 11 y 12 son los defectuosos


def califica(media: float, rng: random.Random) -> int:
    return max(1, min(CATS, round(rng.gauss(media, 0.7))))


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'item':>4} {'I-CVI':>6} {'V Aiken':>8}  juicio")
    print("=" * 40)
    icvis = []
    for i, media in enumerate(RELEVANCIA_REAL, start=1):
        r = [califica(media, rng) for _ in range(JUECES)]
        icvi = sum(x >= 3 for x in r) / JUECES
        v = sum(x - 1 for x in r) / (JUECES * (CATS - 1))
        icvis.append(icvi)
        print(f"{i:4d} {icvi:6.2f} {v:8.2f}  {'revisar' if icvi < 0.78 else 'ok'}")
    print()
    print(f"S-CVI/Ave (media de I-CVI) = {statistics.fmean(icvis):.2f}")
    print()
    print("Lectura: los indicadores cuantifican el ACUERDO de los jueces, no la cobertura.")
    print("Un banco puede tener todos los items 'relevantes' y omitir una faceta entera:")
    print("eso se detecta contra la tabla de especificaciones (clase 016), no con el I-CVI.")


if __name__ == "__main__":
    main()
