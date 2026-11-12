"""Laboratorio 121 - Estilos de liderazgo en dos dimensiones: clasificacion y error de medida.

Modelo bidimensional (orientacion a la tarea y orientacion a las personas, tradicion de los
estudios de Ohio State y no la tipologia autocratico/democratico/laissez-faire de Lewin, que es
un marco conceptual de 1939). Cada lider tiene dos puntajes verdaderos independientes; se
observan con fiabilidad 0.80 por dimension (promedio de varios evaluadores). Los cuatro
cuadrantes se definen por la mediana de cada dimension. Se calcula cuantos lideres cambian de
cuadrante entre dos mediciones paralelas y la distancia al corte de los que cambian.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, RHO = 20000, 0.80


def main() -> None:
    rng = random.Random(SEMILLA)
    sd_e = math.sqrt((1 - RHO) / RHO)
    tarea = [rng.gauss(0, 1) for _ in range(N)]
    pers = [rng.gauss(0, 1) for _ in range(N)]

    def medir(v: list[float]) -> list[float]:
        return [x + rng.gauss(0, sd_e) for x in v]

    a1, a2 = medir(tarea), medir(tarea)
    b1, b2 = medir(pers), medir(pers)
    ma1, ma2 = statistics.median(a1), statistics.median(a2)
    mb1, mb2 = statistics.median(b1), statistics.median(b2)
    cuad = lambda a, b, ma, mb: (a > ma) * 2 + (b > mb)  # noqa: E731
    q1 = [cuad(a, b, ma1, mb1) for a, b in zip(a1, b1, strict=True)]
    q2 = [cuad(a, b, ma2, mb2) for a, b in zip(a2, b2, strict=True)]
    cambian = sum(x != y for x, y in zip(q1, q2, strict=True)) / N
    print(f"Fiabilidad de cada dimension = {RHO}; r test-retest observada = {statistics.correlation(a1, a2):.2f}")
    print(f"Lideres que CAMBIAN de cuadrante entre dos mediciones paralelas: {cambian:.1%} (azar puro: 75 %)")
    nombres = ["bajo-bajo", "bajo tarea/alto personas", "alto tarea/bajo personas", "alto-alto"]
    for q in range(4):
        grupo = [i for i in range(N) if q1[i] == q]
        igual = sum(q2[i] == q for i in grupo) / len(grupo)
        print(f"  {nombres[q]:<26} mantiene el cuadrante: {igual:5.1%}")
    print()
    print("Lectura: dos dimensiones con buena fiabilidad (0.80) aun asi clasifican de forma distinta")
    print("a cerca de un tercio de los lideres en una segunda medicion. Un estilo es una descripcion")
    print("util de tendencias, no una categoria estable de la persona; y el estilo 'efectivo' depende de")
    print("la situacion y del criterio de efectividad (clase 122).")


if __name__ == "__main__":
    main()
