"""Laboratorio 056 - Estimar la habilidad: maxima verosimilitud (ML) frente a EAP.

Prueba de 10 items 2PL con parametros conocidos. Para varios patrones de respuesta se
calcula theta por ML (Newton, acotado a [-4, 4]) y por EAP con prior N(0, 1).
  - ML no existe (diverge) con puntaje 0 o perfecto;
  - EAP siempre existe pero "encoge" hacia la media del prior (sesgo a los extremos).
Luego, sobre 3000 personas simuladas, se compara el error de ambos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
ITEMS = [(1.2, -1.8), (1.0, -1.4), (1.5, -1.0), (1.0, -0.5), (1.3, -0.1),
         (1.1, 0.3), (1.4, 0.7), (1.0, 1.1), (1.2, 1.5), (1.0, 1.9)]
GRID = [-4 + 0.05 * i for i in range(161)]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def ml(u: list[int]) -> float | None:
    if sum(u) in (0, len(u)):
        return None
    t = 0.0
    for _ in range(50):
        p = [logistica(a * (t - b)) for a, b in ITEMS]
        g = sum(a * (x - q) for (a, _), x, q in zip(ITEMS, u, p, strict=True))
        h = -sum(a * a * q * (1 - q) for (a, _), q in zip(ITEMS, p, strict=True))
        t = max(-4.0, min(4.0, t - g / h))
    return t


def eap(u: list[int]) -> float:
    num = den = 0.0
    for g in GRID:
        w = math.exp(-0.5 * g * g)
        for (a, b), x in zip(ITEMS, u, strict=True):
            p = logistica(a * (g - b))
            w *= p if x else 1 - p
        num += g * w
        den += w
    return num / den


def main() -> None:
    patrones = {"todo mal": [0] * 10, "1 acierto (el mas facil)": [1] + [0] * 9,
                "5 aciertos (los 5 faciles)": [1] * 5 + [0] * 5,
                "9 aciertos (falla el mas facil)": [0] + [1] * 9, "todo bien": [1] * 10}
    print(f"{'patron':<34} {'ML':>7} {'EAP':>7}")
    print("=" * 50)
    for nombre, u in patrones.items():
        m = ml(u)
        print(f"{nombre:<34} {('indef.' if m is None else f'{m:7.2f}'):>7} {eap(u):7.2f}")

    rng = random.Random(SEMILLA)
    e_ml, e_eap = [], []
    for _ in range(3000):
        t = rng.gauss(0, 1)
        u = [int(rng.random() < logistica(a * (t - b))) for a, b in ITEMS]
        e_eap.append(eap(u) - t)
        m = ml(u)
        if m is not None:
            e_ml.append(m - t)
    rm = lambda e: math.sqrt(sum(x * x for x in e) / len(e))  # noqa: E731
    print(f"\nRMSE sobre 3000 personas: EAP = {rm(e_eap):.3f} (todas) | "
          f"ML = {rm(e_ml):.3f} (solo {len(e_ml)} con estimacion finita)")
    print()
    print("Lectura: ML es insesgado en teoria pero indefinido para puntajes extremos y ruidoso")
    print("con pocos items; EAP incorpora un prior y reduce el error, a costa de acercar a todos")
    print("hacia 0. Elegir estimador es elegir un sesgo: se declara y se justifica.")


if __name__ == "__main__":
    main()
