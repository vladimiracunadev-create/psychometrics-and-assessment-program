"""Laboratorio 006 - Galton y la regresion a la media, y el origen de la correlacion.

Galton (1886) observo que los hijos de padres muy altos tendian a ser altos pero menos extremos que
sus padres ("regresion hacia la mediocridad"). Pearson formalizo despues la correlacion. Se simulan
5.000 pares padre-hijo con correlacion 0.5 y se muestra que:
  - la pendiente de regresar el hijo sobre el padre es r (aprox. 0.5), no 1,
  - el 10 % de padres mas altos tiene hijos mas altos que la media pero MENOS extremos,
  - la regresion no significa que la poblacion se vuelva mas homogenea (la varianza se mantiene).
Datos sinteticos en unidades estandarizadas; el fenomeno es estadistico, no biologico.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, R = 5000, 0.5


def main() -> None:
    rng = random.Random(SEMILLA)
    padres = [rng.gauss(0, 1) for _ in range(N)]
    hijos = [R * p + math.sqrt(1 - R * R) * rng.gauss(0, 1) for p in padres]
    r = statistics.correlation(padres, hijos)
    pendiente = statistics.linear_regression(padres, hijos).slope
    corte = sorted(padres)[int(0.9 * N)]
    sel = [(p, h) for p, h in zip(padres, hijos, strict=True) if p >= corte]
    print(f"Correlacion padre-hijo r = {r:.2f}; pendiente de regresar hijo sobre padre = {pendiente:.2f}")
    print(f"10 % de padres mas altos: media del padre = {statistics.fmean(p for p, _ in sel):.2f} DE; "
          f"media de sus hijos = {statistics.fmean(h for _, h in sel):.2f} DE")
    print(f"DE de los padres = {statistics.pstdev(padres):.2f}; DE de los hijos = {statistics.pstdev(hijos):.2f} (la dispersion se mantiene)")
    print()
    print("Lectura: los hijos de padres extremos estan por encima de la media pero menos lejos que sus padres.")
    print("No es una fuerza que 'empuje al centro': ocurre siempre que dos medidas se correlacionan de forma")
    print("imperfecta, y explica por que quien puntua extremo en una medicion suele puntuar menos extremo en la")
    print("siguiente (clase 175). Spearman (1904) y Binet y Simon (1905) continuaron esta tradicion.")


if __name__ == "__main__":
    main()
