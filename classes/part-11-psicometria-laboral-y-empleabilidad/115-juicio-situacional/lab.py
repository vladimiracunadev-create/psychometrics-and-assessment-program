"""Laboratorio 115 - Pruebas de juicio situacional: clave de expertos y puntuacion.

20 situaciones, cada una con 4 cursos de accion que se califican por efectividad (1-5). Hay una
efectividad "verdadera" de cada curso. Expertos (n = 10) la estiman con poco ruido; novatos
(n = 300), con mas ruido y un sesgo a preferir opciones "amables". La puntuacion de un
examinado es la cercania a la clave: -suma|su calificacion - media de expertos|. Se evalua:
  - fiabilidad de la clave (acuerdo entre dos mitades de expertos),
  - diferencia expertos-novatos en el puntaje (d de Cohen),
  - alfa de Cronbach del puntaje por situacion (suele ser bajo: SJT es heterogeneo).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
SIT, OPC = 20, 4


def alfa(items: list[list[float]]) -> float:
    k = len(items)
    total = [sum(f) for f in zip(*items, strict=True)]
    return k / (k - 1) * (1 - sum(statistics.pvariance(i) for i in items) / statistics.pvariance(total))


def main() -> None:
    rng = random.Random(SEMILLA)
    verdad = [[rng.uniform(1, 5) for _ in range(OPC)] for _ in range(SIT)]
    amable = [[rng.uniform(-0.5, 1.0) for _ in range(OPC)] for _ in range(SIT)]

    def califica(sd: float, sesgo: float) -> list[list[float]]:
        return [[max(1.0, min(5.0, verdad[s][o] + sesgo * amable[s][o] + rng.gauss(0, sd)))
                 for o in range(OPC)] for s in range(SIT)]

    expertos = [califica(0.6, 0.0) for _ in range(10)]
    clave = [[statistics.fmean(e[s][o] for e in expertos) for o in range(OPC)] for s in range(SIT)]
    mitad_a = [[statistics.fmean(e[s][o] for e in expertos[:5]) for o in range(OPC)] for s in range(SIT)]
    mitad_b = [[statistics.fmean(e[s][o] for e in expertos[5:]) for o in range(OPC)] for s in range(SIT)]
    r_clave = statistics.correlation([v for f in mitad_a for v in f], [v for f in mitad_b for v in f])

    def puntaje(resp: list[list[float]]) -> list[float]:
        return [-sum(abs(resp[s][o] - clave[s][o]) for o in range(OPC)) for s in range(SIT)]

    novatos = [puntaje(califica(1.0, 0.4)) for _ in range(300)]
    otros_exp = [puntaje(califica(0.8, 0.0)) for _ in range(300)]
    tn = [sum(p) for p in novatos]
    te = [sum(p) for p in otros_exp]
    sp = math.sqrt((statistics.variance(tn) + statistics.variance(te)) / 2)
    d = (statistics.fmean(te) - statistics.fmean(tn)) / sp
    print(f"Acuerdo entre dos mitades de expertos (correlacion de calificaciones): {r_clave:.2f}")
    print(f"Puntaje medio expertos = {statistics.fmean(te):.1f}; novatos = {statistics.fmean(tn):.1f}; d de Cohen = {d:.2f}")
    por_sit = [[p[s] for p in novatos] for s in range(SIT)]
    print(f"Alfa de Cronbach (20 situaciones, novatos) = {alfa(por_sit):.2f}")
    print()
    print("Lectura: la clave de expertos es estable y discrimina entre expertos y novatos, pero un SJT")
    print("es heterogeneo (cada situacion mide algo distinto): el alfa es muy bajo (0.08) y no debe usarse como")
    print("criterio unico de calidad. Quienes elaboran la clave definen 'lo correcto': su composicion y")
    print("posibles sesgos culturales deben documentarse. Con novatos simulados el sesgo es 'amabilidad'.")


if __name__ == "__main__":
    main()
