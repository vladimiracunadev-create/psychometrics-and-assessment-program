"""Laboratorio 170 - Por que se exagera la eficacia: sesgo de publicacion y asimetria del embudo.

Se simulan 80 estudios de una intervencion cuyo efecto verdadero es PEQUENO (d = 0.05, casi nulo)
con tamanos de muestra distintos (n por grupo de 15 a 200). Se comparan:
  - TODOS los estudios (lo que existiria sin sesgo de publicacion),
  - solo los PUBLICADOS: se publican los estadisticamente significativos (p < .05, a favor) y un
    10 % de los no significativos.
Se calcula el efecto medio en cada conjunto y la asimetria del embudo con la regresion de Egger
(intercepto distinto de 0 = asimetria). Muestra por que no se promete una mejora basada en un
conjunto de estudios publicados sin revisar el sesgo de publicacion.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
D_VERD, K = 0.05, 400


def estudio(rng: random.Random) -> tuple[float, float]:
    n = rng.choice([15, 20, 30, 50, 80, 120, 200])
    a = [rng.gauss(0, 1) for _ in range(n)]
    b = [rng.gauss(D_VERD, 1) for _ in range(n)]
    sp = math.sqrt((statistics.variance(a) + statistics.variance(b)) / 2)
    d = (statistics.fmean(b) - statistics.fmean(a)) / sp
    se = math.sqrt(2 / n + d * d / (4 * n))
    return d, se


def egger(estudios: list[tuple[float, float]]) -> float:
    x = [1 / se for _, se in estudios]
    y = [d / se for d, se in estudios]
    b = statistics.covariance(x, y) / statistics.variance(x)
    return statistics.fmean(y) - b * statistics.fmean(x)


def main() -> None:
    rng = random.Random(SEMILLA)
    todos = [estudio(rng) for _ in range(K)]
    pub = [(d, se) for d, se in todos if (d / se > 1.96) or rng.random() < 0.10]

    def media(es):
        w = [1 / se**2 for _, se in es]
        return sum(wi * d for wi, (d, _) in zip(w, es, strict=True)) / sum(w)

    print(f"Efecto verdadero d = {D_VERD}; estudios simulados: {K}; publicados: {len(pub)}")
    simple = lambda es: statistics.fmean(d for d, _ in es)  # noqa: E731
    print(f"{'conjunto':<24} {'media simple':>13} {'media ponderada':>16} {'intercepto de Egger':>21}")
    print(f"{'todos los estudios':<24} {simple(todos):13.2f} {media(todos):16.2f} {egger(todos):21.2f}")
    print(f"{'solo los publicados':<24} {simple(pub):13.2f} {media(pub):16.2f} {egger(pub):21.2f}")
    print()
    print("Lectura: si solo se publica lo significativo, la media simple se infla varias veces sobre el efecto")
    print("verdadero (los estudios pequenos publicados son los que 'tuvieron suerte'); la media ponderada se")
    print("infla menos porque los estudios grandes pesan mas. El test de Egger es poco potente aqui. Por eso, ante")
    print("afirmaciones como 'el entrenamiento cognitivo mejora la inteligencia', se pide revisar registros")
    print("previos de estudios, tamanos de muestra y transferencia: no se promete una mejora sin esa")
    print("evidencia. Distinguir recomendaciones pedagogicas, intervencion profesional y tratamiento clinico.")


if __name__ == "__main__":
    main()
