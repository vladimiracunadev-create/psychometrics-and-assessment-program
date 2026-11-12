"""Laboratorio 082 - Gf y Gc por edad: por que un estudio transversal exagera el declive.

Modelo ilustrativo (los parametros son supuestos del laboratorio, no resultados empiricos):
  Gf (fluida): sube hasta ~25 anos y baja despues, ~0.02 DE por ano.
  Gc (cristalizada): sigue subiendo con la edad.
  EFECTO DE COHORTE: cada cohorte mas joven rinde mas (+0.3 DE por decada; efecto Flynn).
Se compara (1) un estudio TRANSVERSAL (distintas personas de 20 a 70 anos medidas hoy) con
(2) un estudio LONGITUDINAL (las mismas personas medidas a lo largo de 30 anos).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 3000
ANIO = 2026
COHORTE_POR_DECADA = 0.3


def gf_verdadero(edad: float) -> float:
    return 0.0 if edad <= 25 else -0.02 * (edad - 25)


def gc_verdadero(edad: float) -> float:
    return 0.02 * (edad - 20)


def cohorte(nacimiento: float) -> float:
    return COHORTE_POR_DECADA * (nacimiento - 1960) / 10


def main() -> None:
    rng = random.Random(SEMILLA)
    print("Estudio TRANSVERSAL (hoy): media por grupo de edad")
    print(f"{'edad':>5} {'Gf':>8} {'Gc':>8}")
    gf0 = None
    for edad in (20, 30, 40, 50, 60, 70):
        nac = ANIO - edad
        gf = statistics.fmean(gf_verdadero(edad) + cohorte(nac) + rng.gauss(0, 1) for _ in range(N))
        gc = statistics.fmean(gc_verdadero(edad) + cohorte(nac) + rng.gauss(0, 1) for _ in range(N))
        gf0 = gf if gf0 is None else gf0
        print(f"{edad:5d} {gf:8.2f} {gc:8.2f}")
    print("\nEstudio LONGITUDINAL: la misma cohorte (nacida en 1966) entre los 20 y los 60 anos")
    print(f"{'edad':>5} {'Gf':>8}")
    for edad in (20, 30, 40, 50, 60):
        gf = statistics.fmean(gf_verdadero(edad) + cohorte(1966) + rng.gauss(0, 1) for _ in range(N))
        print(f"{edad:5d} {gf:8.2f}")
    print()
    print("Lectura: en el transversal, los de 60 estan ~2 DE bajo los de 20, pero en gran parte")
    print("porque nacieron en otra cohorte; el declive 'propio' (longitudinal) es ~0.7 DE. Las")
    print("comparaciones entre edades confunden edad, cohorte y periodo. Y los parametros aqui son")
    print("supuestos: la trayectoria real varia por dominio, persona y contexto.")


if __name__ == "__main__":
    main()
