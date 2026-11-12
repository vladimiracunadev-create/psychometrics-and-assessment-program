"""Laboratorio 094 - Curva de posicion serial: primacia y recencia.

Modelo simple de dos componentes para el recuerdo libre de una lista de 15 palabras:
  - memoria a largo plazo (primacia): el recuerdo decrece con la posicion mientras la
    atencion/repaso se reparte entre mas palabras;
  - memoria a corto plazo (recencia): las ultimas ~4 palabras siguen disponibles si se evoca
    de inmediato.
Se compara la presentacion VISUAL con la AUDITIVA (en el modelo, la auditiva refuerza la
recencia: efecto de modalidad), y se calcula el recuerdo por posicion. Los parametros son
ilustrativos, no estimaciones empiricas.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, LISTA = 500, 15


def prob_recordar(pos: int, modalidad: str) -> float:
    ltm = 0.55 * (0.93 ** pos) + 0.05                     # primacia/ltm decreciente
    stm = 0.0
    if pos >= LISTA - 4:                                   # ultimas 4 posiciones
        stm = (0.35 if modalidad == "visual" else 0.50) * (1 - 0.1 * (LISTA - 1 - pos))
    return min(0.98, ltm + stm)


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'pos':>3} " + " ".join(f"{p + 1:5d}" for p in range(LISTA)))
    for mod in ("visual", "auditiva"):
        medias = []
        for p in range(LISTA):
            medias.append(statistics.fmean(rng.random() < prob_recordar(p, mod) for _ in range(N)))
        print(f"{mod[:3]:>3} " + " ".join(f"{m:5.2f}" for m in medias))
    totales = {m: statistics.fmean(sum(rng.random() < prob_recordar(p, m) for p in range(LISTA))
                                   for _ in range(N)) for m in ("visual", "auditiva")}
    print(f"\nPalabras recordadas (media de {LISTA}): visual = {totales['visual']:.2f}, "
          f"auditiva = {totales['auditiva']:.2f}")
    print()
    print("Lectura: la curva en U (primacia y recencia) muestra que el puntaje total mezcla procesos.")
    print("Un indice de recuerdo inmediato sube con la recencia; uno diferido (tras interferencia)")
    print("depende de la consolidacion. Por eso las pruebas de lista separan inmediato y diferido, y")
    print("comparar modalidades sin igualar condiciones atribuye al sentido lo que es del procedimiento.")


if __name__ == "__main__":
    main()
