"""Laboratorio 059 - Metaanalisis "bare-bones" y correccion por atenuacion.

Se simulan 40 estudios de una validez verdadera rho = 0.50 entre constructos, medidos con
fiabilidades (predictor 0.80, criterio 0.60) y muestras de tamano distinto. Se calcula:
  - r media ponderada por n;
  - varianza observada frente a la esperada por muestreo (el resto seria heterogeneidad real);
  - correccion por atenuacion con las fiabilidades medias (aproximacion tipo Hunter-Schmidt).
La correccion estima la relacion entre CONSTRUCTOS, no la validez operativa del test real.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
RHO, RXX, RYY = 0.50, 0.80, 0.60


def estudio(n: int, rng: random.Random) -> float:
    x = [rng.gauss(0, 1) for _ in range(n)]
    y = [RHO * a + math.sqrt(1 - RHO**2) * rng.gauss(0, 1) for a in x]
    xo = [a + rng.gauss(0, math.sqrt((1 - RXX) / RXX)) for a in x]
    yo = [a + rng.gauss(0, math.sqrt((1 - RYY) / RYY)) for a in y]
    return statistics.correlation(xo, yo)


def main() -> None:
    rng = random.Random(SEMILLA)
    ns = [rng.choice((30, 50, 80, 120, 200, 400)) for _ in range(40)]
    rs = [estudio(n, rng) for n in ns]
    w = [n / sum(ns) for n in ns]
    rbar = sum(wi * r for wi, r in zip(w, rs, strict=True))
    var_obs = sum(wi * (r - rbar) ** 2 for wi, r in zip(w, rs, strict=True))
    var_err = (1 - rbar**2) ** 2 / (statistics.fmean(ns) - 1)
    rho_est = rbar / math.sqrt(RXX * RYY)
    print(f"Estudios: {len(rs)} | n total = {sum(ns)}")
    print(f"r observada media ponderada          = {rbar:.3f}  (r esperada = {RHO * math.sqrt(RXX * RYY):.3f})")
    print(f"Varianza observada de r              = {var_obs:.4f}")
    print(f"Varianza esperada solo por muestreo  = {var_err:.4f}")
    print(f"=> varianza atribuible a otra cosa   = {max(0.0, var_obs - var_err):.4f}")
    print(f"r corregida por atenuacion (rho)     = {rho_est:.3f}  (verdadera = {RHO})")
    print()
    print("Lectura: casi toda la dispersion entre estudios es error de muestreo, y la")
    print("atenuacion explica por que las validezes observadas parecen 'bajas'. Pero esta")
    print("simulacion no tiene sesgo de publicacion ni heterogeneidad real: los metaanalisis")
    print("reales dependen de que los estudios incluidos sean representativos.")


if __name__ == "__main__":
    main()
