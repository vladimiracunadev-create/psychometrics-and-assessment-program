"""Laboratorio 163 - Trayectorias tras la adversidad: la resiliencia como resultado, no como rasgo.

Cuatro trayectorias de malestar (0-10) en 4 momentos tras un evento adverso (T0 antes, T1 a T3
despues), con proporciones supuestas: resiliente (65 %), recuperacion (20 %), cronica (10 %),
tardia (5 %). Se clasifica a cada persona con reglas simples sobre sus 4 puntajes (con ruido de
medida) y se mide la exactitud de clasificacion. Ensena que:
  - la trayectoria mas comun es la estabilidad (la mayoria NO desarrolla malestar persistente),
  - clasificar con pocas mediciones ruidosas confunde trayectorias,
  - decir "resiliencia" de una persona en base a un cuestionario de rasgo no equivale a observarla
    en el tiempo.
"""
from __future__ import annotations

import collections
import random

SEMILLA = 20260819
N = 8000
PERFILES = {
    "resiliente": ((2, 3, 2, 2), 0.65),
    "recuperacion": ((2, 7, 5, 3), 0.20),
    "cronica": ((3, 7, 7, 7), 0.10),
    "tardia": ((2, 3, 5, 7), 0.05),
}


def clasifica(p: list[float]) -> str:
    t0, t1, t2, t3 = p
    if max(t1, t2, t3) - t0 < 2.5:
        return "resiliente"
    if t3 - t0 < 2.5:
        return "recuperacion"
    if t1 - t0 >= 2.5:
        return "cronica"
    return "tardia"


def main() -> None:
    rng = random.Random(SEMILLA)
    nombres = list(PERFILES)
    pesos = [PERFILES[n][1] for n in nombres]
    conf = collections.Counter()
    for _ in range(N):
        real = rng.choices(nombres, weights=pesos)[0]
        medidas = [max(0.0, min(10.0, m + rng.gauss(0, 1.2))) for m in PERFILES[real][0]]
        conf[(real, clasifica(medidas))] += 1
    print(f"{'trayectoria real':<14} " + " ".join(f"{n[:10]:>11}" for n in nombres) + "   exactitud")
    for r in nombres:
        tot = sum(conf[(r, c)] for c in nombres)
        print(f"{r:<14} " + " ".join(f"{conf[(r, c)] / tot:11.1%}" for c in nombres) + f"   {conf[(r, r)] / tot:8.1%}")
    exacta = sum(conf[(r, r)] for r in nombres) / N
    print(f"\nExactitud global = {exacta:.1%}")
    print()
    print("Lectura: lo habitual es no desarrollar malestar persistente (65 % en este modelo). Con 4")
    print("mediciones ruidosas, las trayectorias menos frecuentes (cronica, tardia) se confunden mas. La")
    print("resiliencia se observa como resultado a lo largo del tiempo; no se infiere de un cuestionario y no")
    print("es una virtud individual: depende del apoyo y los recursos. Quien muestra malestar persistente")
    print("necesita apoyo profesional, no una etiqueta de 'poco resiliente'. Proporciones supuestas.")


if __name__ == "__main__":
    main()
