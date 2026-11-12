"""Laboratorio 174 - Datos faltantes: MCAR, MAR y MNAR con distintos tratamientos.

Dos variables X (rendimiento previo) e Y (puntaje de una escala), r verdadera = 0.50. Se elimina
el 30 % de Y con tres mecanismos:
  MCAR: al azar; MAR: depende de X (los de bajo X responden menos); MNAR: depende del propio Y
  (quienes tendrian Y bajo no responden).
Se estiman la media de Y y la correlacion X-Y con: casos completos, imputacion por la media y
regresion estocastica (imputa Y desde X mas ruido). La regresion funciona bajo MAR; ningun metodo
simple arregla MNAR. Parametros: n = 2 000, 300 replicas.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, REPS, R = 2000, 300, 0.50


def una_replica(mecanismo: str, rng: random.Random):
    x = [rng.gauss(0, 1) for _ in range(N)]
    y = [R * a + math.sqrt(1 - R * R) * rng.gauss(0, 1) for a in x]
    faltan = []
    for a, b in zip(x, y, strict=True):
        if mecanismo == "MCAR":
            p = 0.30
        elif mecanismo == "MAR":
            p = 1 / (1 + math.exp(-(-0.9 - 1.2 * a)))
        else:
            p = 1 / (1 + math.exp(-(-0.9 - 1.2 * b)))
        faltan.append(rng.random() < p)
    obs = [(a, b) for a, b, f in zip(x, y, faltan, strict=True) if not f]
    xo, yo = [a for a, _ in obs], [b for _, b in obs]
    media_obs = statistics.fmean(yo)
    # completos
    res = {"completos": (media_obs, statistics.correlation(xo, yo))}
    # imputacion por la media
    yim = [media_obs if f else b for b, f in zip(y, faltan, strict=True)]
    res["media"] = (statistics.fmean(yim), statistics.correlation(x, yim))
    # regresion estocastica
    beta = statistics.covariance(xo, yo) / statistics.variance(xo)
    a0 = media_obs - beta * statistics.fmean(xo)
    sd_res = statistics.pstdev([b - (a0 + beta * a) for a, b in obs])
    yrg = [a0 + beta * a + rng.gauss(0, sd_res) if f else b for a, b, f in zip(x, y, faltan, strict=True)]
    res["regresion estocastica"] = (statistics.fmean(yrg), statistics.correlation(x, yrg))
    return res


def main() -> None:
    rng = random.Random(SEMILLA)
    print("Verdad: media de Y = 0.00; correlacion X-Y = 0.50")
    print(f"{'mecanismo':<8} {'metodo':<24} {'media de Y (sesgo)':>20} {'correlacion (sesgo)':>21}")
    print("=" * 78)
    for mec in ("MCAR", "MAR", "MNAR"):
        acum = {}
        for _ in range(REPS):
            for k, (m, r) in una_replica(mec, rng).items():
                acum.setdefault(k, ([], []))
                acum[k][0].append(m)
                acum[k][1].append(r)
        for k, (ms, rs) in acum.items():
            print(f"{mec:<8} {k:<24} {statistics.fmean(ms):+13.3f} {'':>6} {statistics.fmean(rs) - R:+14.3f}")
    print()
    print("Lectura: bajo MCAR los casos completos son insesgados (con menos datos). Bajo MAR, la media de")
    print("casos completos se sesga, pero se corrige si el modelo de imputacion incluye la variable causante")
    print("(X). Imputar por la media subestima la correlacion siempre. Bajo MNAR ningun metodo simple corrige:")
    print("se hace analisis de sensibilidad y, sobre todo, se previene la omision con buen diseno.")


if __name__ == "__main__":
    main()
