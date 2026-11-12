"""Laboratorio 177 - DIF uniforme y no uniforme: Mantel-Haenszel frente a regresion logistica.

Tres items de una prueba de 20 (Rasch con discriminacion variable) en dos grupos con la misma
habilidad: SIN DIF, con DIF UNIFORME (el item es mas dificil para el grupo focal) y con DIF NO
UNIFORME (la discriminacion difiere entre grupos: las curvas se cruzan). Se detecta con:
  - Mantel-Haenszel (chi2 con 1 gl): sensible a DIF uniforme,
  - regresion logistica: item ~ total, +grupo, +total*grupo con razon de verosimilitud (2 gl).
Se informa la tasa de deteccion (p < .05) en 40 replicas de n = 600 por grupo.
"""
from __future__ import annotations

import math
import random
from collections import defaultdict

SEMILLA = 20260819
N, K, REPS = 600, 20, 40


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def mh_chi2(items: list[tuple[int, int, int]]) -> float:
    est = defaultdict(lambda: [0, 0, 0, 0])
    for total, grupo, r in items:
        est[total][(0 if r else 1) + 2 * grupo] += 1
    sa = ev = vr = 0.0
    for a, b, c, d in est.values():
        t = a + b + c + d
        if t < 2:
            continue
        n1, n0, m1, m0 = a + b, c + d, a + c, b + d
        sa += a
        ev += n1 * m1 / t
        vr += n1 * n0 * m1 * m0 / (t * t * (t - 1))
    return (abs(sa - ev) - 0.5) ** 2 / vr if vr else 0.0


def loglik(x: list[list[float]], y: list[int], iters: int = 12) -> float:
    k = len(x[0])
    b = [0.0] * k
    for _ in range(iters):
        g = [0.0] * k
        h = [[0.0] * k for _ in range(k)]
        for f, yy in zip(x, y, strict=True):
            p = logistica(sum(bi * vi for bi, vi in zip(b, f, strict=True)))
            for i in range(k):
                g[i] += (yy - p) * f[i]
                for j in range(k):
                    h[i][j] += p * (1 - p) * f[i] * f[j]
        m = [h[i][:] + [g[i]] for i in range(k)]
        for i in range(k):
            piv = max(range(i, k), key=lambda r: abs(m[r][i]))
            m[i], m[piv] = m[piv], m[i]
            for r in range(k):
                if r != i:
                    f2 = m[r][i] / m[i][i]
                    m[r] = [a - f2 * c for a, c in zip(m[r], m[i], strict=True)]
        b = [bi + m[i][k] / m[i][i] for i, bi in enumerate(b)]
    ll = 0.0
    for f, yy in zip(x, y, strict=True):
        p = min(max(logistica(sum(bi * vi for bi, vi in zip(b, f, strict=True))), 1e-12), 1 - 1e-12)
        ll += math.log(p if yy else 1 - p)
    return ll


def replica(escenario: str, rng: random.Random) -> tuple[float, float]:
    bs = [-1.5 + 3.0 * i / (K - 1) for i in range(K)]
    filas = []
    for grupo in (0, 1):
        for _ in range(N):
            t = rng.gauss(0, 1)
            resp = []
            for j, b in enumerate(bs):
                a, shift = 1.0, 0.0
                if j == 9 and grupo == 1:
                    if escenario == "uniforme":
                        shift = 0.8
                    elif escenario == "no uniforme":
                        a = 0.3
                resp.append(int(rng.random() < logistica(a * (t - b - shift))))
            filas.append((grupo, resp))
    obs = [(sum(r) - r[9], g, r[9]) for g, r in filas]           # total sin el item (criterio interno)
    chi_mh = mh_chi2(obs)
    tot = [(t - 9.5) / 3 for t, _, _ in obs]
    y = [r for _, _, r in obs]
    g = [gg for _, gg, _ in obs]
    x0 = [[1.0, t] for t in tot]
    x1 = [[1.0, t, gg] for t, gg in zip(tot, g, strict=True)]
    x2 = [[1.0, t, gg, t * gg] for t, gg in zip(tot, g, strict=True)]
    ll0, ll2 = loglik(x0, y), loglik(x2, y)
    return chi_mh, 2 * (ll2 - ll0), 2 * (loglik(x1, y) - ll0)       # type: ignore[return-value]


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'escenario':<14} {'MH detecta (1 gl)':>19} {'LR 2 gl detecta':>17} {'LR solo grupo':>15}")
    print("=" * 70)
    for esc in ("sin DIF", "uniforme", "no uniforme"):
        mh = lr2 = lrg = 0
        reps = 40
        for _ in range(reps):
            c_mh, c_lr2, c_g = replica(esc, rng)
            mh += c_mh > 3.84
            lr2 += c_lr2 > 5.99
            lrg += c_g > 3.84
        print(f"{esc:<14} {mh / reps:19.0%} {lr2 / reps:17.0%} {lrg / reps:15.0%}")
    print()
    print("Lectura: MH y la prueba de grupo detectan el DIF uniforme y casi no ven el no uniforme (curvas que")
    print("se cruzan); la regresion con interaccion lo detecta. Elegir el metodo segun el tipo de DIF que")
    print("se teme. En 'sin DIF' la tasa de deteccion debe rondar 5 % (falsos positivos).")


if __name__ == "__main__":
    main()
