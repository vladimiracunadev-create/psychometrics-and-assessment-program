"""Laboratorio 087 - Evaluar el aprendizaje: la fiabilidad de los puntajes de ganancia.

Evaluacion dinamica: se mide antes (pre) y despues (post) de una breve instruccion. El puntaje
de ganancia G = post - pre tiene fiabilidad
    rho_G = (rho_pre*sd_pre^2 + rho_post*sd_post^2 - 2*r_pp*sd_pre*sd_post) / (sd_pre^2 + sd_post^2 - 2*r_pp*sd_pre*sd_post)
que cae cuando pre y post estan muy correlacionados. Se verifica la formula por simulacion.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 20000


def rho_ganancia(rho_x: float, rho_y: float, r_xy: float, sx: float = 1.0, sy: float = 1.0) -> float:
    num = rho_x * sx**2 + rho_y * sy**2 - 2 * r_xy * sx * sy
    den = sx**2 + sy**2 - 2 * r_xy * sx * sy
    return num / den


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'r(pre,post)':>12} {'fiab. pre/post':>15} {'fiab. ganancia (formula)':>26} {'simulada':>9}")
    print("=" * 68)
    for r_pp in (0.2, 0.5, 0.7, 0.9):
        rho = 0.9
        # Verdadero: T_pre y T_post con correlacion r_true; r observada = rho * r_true.
        r_true = r_pp / rho
        if r_true >= 1:
            continue
        tp = [rng.gauss(0, 1) for _ in range(N)]
        tq = [r_true * a + math.sqrt(1 - r_true**2) * rng.gauss(0, 1) for a in tp]
        sd_e = math.sqrt((1 - rho) / rho)
        pre = [a + rng.gauss(0, sd_e) for a in tp]
        post = [b + rng.gauss(0, sd_e) for b in tq]
        g_ver = [b - a for a, b in zip(tp, tq, strict=True)]
        g_obs = [b - a for a, b in zip(pre, post, strict=True)]
        sim = statistics.correlation(g_ver, g_obs) ** 2
        formula = rho_ganancia(rho, rho, statistics.correlation(pre, post), statistics.pstdev(pre), statistics.pstdev(post))
        print(f"{statistics.correlation(pre, post):12.2f} {rho:15.2f} {formula:26.3f} {sim:9.3f}")
    print()
    print("Lectura: aunque pre y post tengan fiabilidad 0.90, la ganancia puede tener fiabilidad baja")
    print("si pre y post correlacionan alto. Una 'ganancia' individual casi siempre se interpreta con")
    print("cautela: se prefieren analisis de grupo, el nivel post controlando el pre, o indices de")
    print("cambio fiable (clase 015). Que alguien 'aprenda rapido' no se concluye de un solo par de puntajes.")


if __name__ == "__main__":
    main()
