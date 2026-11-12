"""Laboratorio 024 - Test-retest: que captura la correlacion y que no.

Cada persona tiene un rasgo estable mas un componente transitorio por ocasion.
  X1 = T + U1 + E1,   X2 = T + U2 + E2
La correlacion test-retest baja cuando el rasgo cambia entre ocasiones o hay mas
variacion transitoria. Y hay algo que la correlacion NO ve: un cambio medio del
grupo (efecto de practica). Se muestran ambos hechos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 10000


def simula(sd_transitorio: float, sd_cambio: float, practica: float, rng: random.Random):
    t = [rng.gauss(0, 1) for _ in range(N)]
    x1 = [a + rng.gauss(0, sd_transitorio) for a in t]
    t2 = [a + rng.gauss(0, sd_cambio) for a in t]                  # el rasgo cambia un poco
    x2 = [a + practica + rng.gauss(0, sd_transitorio) for a in t2]  # + mejora media
    return x1, x2


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'caso':<44} {'r test-retest':>13} {'dif. de medias':>15}")
    print("=" * 76)
    casos = [
        ("estable, poco ruido transitorio", 0.3, 0.0, 0.0),
        ("estable, mucho ruido transitorio", 1.0, 0.0, 0.0),
        ("rasgo que cambia entre ocasiones", 0.3, 0.8, 0.0),
        ("estable, pero con efecto de practica (+1 DE)", 0.3, 0.0, 1.0),
    ]
    for nombre, st, sc, pr in casos:
        x1, x2 = simula(st, sc, pr, rng)
        d = statistics.fmean(x2) - statistics.fmean(x1)
        print(f"{nombre:<44} {statistics.correlation(x1, x2):13.3f} {d:15.3f}")
    print()
    print("Lectura")
    print("  - Mas ruido transitorio o cambio real del rasgo -> r baja, y la")
    print("    correlacion no distingue cual de los dos causo la caida.")
    print("  - El efecto de practica deja r casi intacta (misma ordenacion de")
    print("    personas) aunque todo el grupo suba 1 DE: r no es acuerdo absoluto.")
    print("    Para acuerdo hace falta ademas comparar medias o usar un CCI.")


if __name__ == "__main__":
    main()
