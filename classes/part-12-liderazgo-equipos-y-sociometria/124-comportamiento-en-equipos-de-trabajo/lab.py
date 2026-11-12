"""Laboratorio 124 - Modelo insumo-proceso-resultado: efecto indirecto con intervalo bootstrap.

Cadena simulada: composicion del equipo (X, p. ej. nivel medio de una competencia) ->
procesos de equipo (M, p. ej. coordinacion) -> desempeno (Y). X afecta Y solo a traves de M
(mediacion total). Se estima el efecto indirecto a*b con regresiones simples y un intervalo
bootstrap percentil (2 000 remuestreos), con 80 equipos. Se compara con el efecto directo ignorando M.
Un efecto indirecto estadisticamente distinto de 0 NO prueba causalidad: requiere un diseno que
la sostenga (asignacion, temporalidad).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
EQUIPOS, BOOT = 80, 2000


def pendiente(x: list[float], y: list[float]) -> float:
    return statistics.covariance(x, y) / statistics.variance(x)


def indirecto(x: list[float], m: list[float], y: list[float]) -> float:
    a = pendiente(x, m)
    # b: coeficiente de m en y controlando x (regresion de y sobre x y m).
    sxx, smm, sxm = statistics.variance(x), statistics.variance(m), statistics.covariance(x, m)
    sxy, smy = statistics.covariance(x, y), statistics.covariance(m, y)
    det = sxx * smm - sxm**2
    b = (sxx * smy - sxm * sxy) / det
    return a * b


def main() -> None:
    rng = random.Random(SEMILLA)
    x = [rng.gauss(0, 1) for _ in range(EQUIPOS)]
    m = [0.6 * a + rng.gauss(0, 0.8) for a in x]
    y = [0.5 * b + rng.gauss(0, 0.8) for b in m]            # sin efecto directo de x sobre y
    est = indirecto(x, m, y)
    boots = []
    for _ in range(BOOT):
        idx = [rng.randrange(EQUIPOS) for _ in range(EQUIPOS)]
        boots.append(indirecto([x[i] for i in idx], [m[i] for i in idx], [y[i] for i in idx]))
    boots.sort()
    lo, hi = boots[int(0.025 * BOOT)], boots[int(0.975 * BOOT)]
    print(f"Efecto indirecto verdadero = 0.6 x 0.5 = 0.300 | estimado = {est:.3f}")
    print(f"Intervalo bootstrap 95 % = [{lo:.3f}, {hi:.3f}]  -> {'excluye' if lo > 0 or hi < 0 else 'incluye'} el 0")
    print(f"Efecto total de X sobre Y (ignorando M) = {pendiente(x, y):.3f}")
    print()
    print("Lectura: con 80 equipos el efecto indirecto se estima con un intervalo amplio. El analisis de")
    print("equipos exige tamanos de muestra al nivel del equipo (no de personas). Y 'mediacion' es una")
    print("hipotesis causal: con datos transversales, otros modelos ajustan igual de bien.")


if __name__ == "__main__":
    main()
