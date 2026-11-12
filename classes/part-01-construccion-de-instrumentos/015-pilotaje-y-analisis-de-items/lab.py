"""Laboratorio 015 - Analisis de items de un piloto simulado.

Se simulan 300 personas y 12 items dicotomicos. Dos items son defectuosos a
proposito: uno demasiado facil (casi todos aciertan) y uno que no discrimina
(se responde al azar). El analisis clasico debe detectarlos con dos indices:
dificultad (proporcion de aciertos) y discriminacion (correlacion item-resto).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 300


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def simula(rng: random.Random) -> tuple[list[list[int]], dict[int, str]]:
    thetas = [rng.gauss(0, 1) for _ in range(N)]
    dificultades = [-1.0, -0.5, -0.2, 0.0, 0.2, 0.5, 0.8, 1.0, -0.8, 0.3]
    cols = [[int(rng.random() < logistica(1.3 * (t - b))) for t in thetas]
            for b in dificultades]
    cols.append([int(rng.random() < logistica(1.3 * (t + 2.5))) for t in thetas])  # facil
    cols.append([int(rng.random() < 0.5) for _ in thetas])                           # azar
    return cols, {10: "defecto: demasiado facil", 11: "defecto: no discrimina"}


def main() -> None:
    rng = random.Random(SEMILLA)
    cols, defectos = simula(rng)
    totales = [sum(c) for c in zip(*cols, strict=True)]
    print(f"{'item':>4} {'dificultad p':>13} {'discrim. r':>11}  veredicto")
    print("=" * 62)
    detectados = set()
    for i, col in enumerate(cols):
        p = statistics.fmean(col)
        resto = [t - x for t, x in zip(totales, col, strict=True)]  # total sin el item
        if len(set(col)) == 1:  # sin varianza no hay discriminacion posible
            r = 0.0
        else:
            r = statistics.correlation([float(x) for x in col], [float(x) for x in resto])
        marcas = []
        if p > 0.90 or p < 0.10:
            marcas.append("p extrema")
        if r < 0.20:
            marcas.append("discrimina poco")
        if marcas:
            detectados.add(i)
        etiqueta = ", ".join(marcas) or "ok"
        real = f"   <- {defectos[i]}" if i in defectos else ""
        print(f"{i + 1:4d} {p:13.2f} {r:11.2f}  {etiqueta}{real}")
    print()
    print(f"Defectos sembrados: {sorted(i + 1 for i in defectos)} | "
          f"marcados: {sorted(i + 1 for i in detectados)}")
    print("Usar el total SIN el item (item-resto) evita inflar la discriminacion.")


if __name__ == "__main__":
    main()
