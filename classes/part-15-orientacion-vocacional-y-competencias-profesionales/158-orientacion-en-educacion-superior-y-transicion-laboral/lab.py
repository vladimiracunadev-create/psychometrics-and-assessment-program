"""Laboratorio 158 - Alerta temprana de desercion: calibracion, AUC y equidad por grupo.

Se simulan 6 000 estudiantes de primer anio con dos senales tempranas (asistencia, nota de
primer semestre) y un grupo de pertenencia (G0/G1). La desercion depende de las senales, y el
grupo G1 tiene una desercion base mayor por razones externas al desempeno (p. ej. carga
economica). Se ajusta una regresion logistica SIN usar el grupo y se evalua:
  - AUC y calibracion global (media predicha frente a observada),
  - tasa de verdaderos positivos y de falsos positivos por grupo con un mismo corte.
Sirve para discutir si un sistema de alerta ayuda a apoyar o a estigmatizar. Datos sinteticos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 6000


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def ajusta(x: list[list[float]], y: list[int]) -> list[float]:
    k = len(x[0]) + 1
    b = [0.0] * k
    for _ in range(25):
        g = [0.0] * k
        h = [[0.0] * k for _ in range(k)]
        for f, yy in zip(x, y, strict=True):
            v = [1.0, *f]
            p = logistica(sum(bi * vi for bi, vi in zip(b, v, strict=True)))
            for i in range(k):
                g[i] += (yy - p) * v[i]
                for j in range(k):
                    h[i][j] += p * (1 - p) * v[i] * v[j]
        # resolver h * d = g (eliminacion gaussiana)
        m = [h[i][:] + [g[i]] for i in range(k)]
        for i in range(k):
            piv = max(range(i, k), key=lambda r: abs(m[r][i]))
            m[i], m[piv] = m[piv], m[i]
            for r in range(k):
                if r != i:
                    f2 = m[r][i] / m[i][i]
                    m[r] = [a - f2 * c for a, c in zip(m[r], m[i], strict=True)]
        b = [bi + m[i][k] / m[i][i] for i, bi in enumerate(b)]
    return b


def main() -> None:
    rng = random.Random(SEMILLA)
    datos = []
    for _ in range(N):
        grupo = int(rng.random() < 0.4)
        asist = min(1.0, max(0.0, rng.gauss(0.80, 0.12)))
        nota = rng.gauss(4.8, 0.7) - 0.15 * grupo
        riesgo = -2.0 - 4.0 * (asist - 0.8) - 1.0 * (nota - 4.8) + 0.9 * grupo
        datos.append((grupo, asist, nota, int(rng.random() < logistica(riesgo))))
    x = [[(a - 0.8) * 5, n - 4.8] for _, a, n, _ in datos]
    y = [d for *_, d in datos]
    b = ajusta(x, y)
    pred = [logistica(b[0] + b[1] * f[0] + b[2] * f[1]) for f in x]
    pos = [p for p, yy in zip(pred, y, strict=True) if yy]
    neg = [p for p, yy in zip(pred, y, strict=True) if not yy]
    auc = sum(a > c for a, c in zip(rng.choices(pos, k=4000), rng.choices(neg, k=4000), strict=True)) / 4000
    print(f"Desercion observada = {sum(y) / N:.1%}; media predicha = {sum(pred) / N:.1%}; AUC aprox. = {auc:.2f}")
    corte = sorted(pred)[int(0.80 * N)]                      # se alerta al 20 % de mayor riesgo
    print(f"\nAlerta al 20 % de mayor riesgo (corte {corte:.2f}):")
    print(f"{'grupo':<6} {'desercion':>10} {'alertados':>10} {'TPR':>6} {'FPR':>6}")
    for g in (0, 1):
        idx = [i for i in range(N) if datos[i][0] == g]
        al = [pred[i] >= corte for i in idx]
        yy = [y[i] for i in idx]
        tpr = sum(a and v for a, v in zip(al, yy, strict=True)) / max(1, sum(yy))
        fpr = sum(a and not v for a, v in zip(al, yy, strict=True)) / max(1, len(yy) - sum(yy))
        print(f"G{g:<5} {sum(yy) / len(yy):10.1%} {sum(al) / len(al):10.1%} {tpr:6.2f} {fpr:6.2f}")
    print()
    print("Lectura: el modelo no usa el grupo y tiene TPR y FPR parecidas en ambos, pero alerta a mas")
    print("estudiantes del grupo con desercion basal mayor, y en los dos grupos detecta solo ~4 de cada 10")
    print("desertores. Un sistema de alerta temprana se usa para OFRECER apoyo, no para etiquetar; se audita por")
    print("grupo (clase 064), se informa su limite y se acompana de intervenciones con evidencia.")


if __name__ == "__main__":
    main()
