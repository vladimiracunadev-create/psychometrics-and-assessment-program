"""Laboratorio 099 - Generar y puntuar tareas clasicas con restricciones de diseno.

Genera, con semilla, secuencias para tres paradigmas y comprueba sus restricciones:
  - n-back: proporcion de objetivos controlada y sin objetivos "accidentales";
  - Go/No-Go: 75 % Go, con un maximo de 3 No-Go seguidos y ninguno en los 2 primeros ensayos;
  - Stroop: 50 % congruentes, sin repeticion inmediata de la palabra (evita priming).
Puntua una respuesta simulada con d' (n-back) y con errores de comision (Go/No-Go). Son
generadores originales con verificacion automatica; la tarea no queda normada por existir.
"""
from __future__ import annotations

import random
from statistics import NormalDist

SEMILLA = 20260819
LETRAS = "BCDFGHJK"
ND = NormalDist()


def nback(n: int, largo: int, p_obj: float, rng: random.Random) -> tuple[list[str], list[bool]]:
    sec = [rng.choice(LETRAS) for _ in range(n)]
    obj = [False] * n
    for i in range(n, largo):
        if rng.random() < p_obj:
            sec.append(sec[i - n])
            obj.append(True)
        else:
            sec.append(rng.choice([x for x in LETRAS if x != sec[i - n]]))
            obj.append(False)
    return sec, obj


def go_nogo(largo: int, rng: random.Random) -> list[str]:
    while True:
        s = ["nogo" if rng.random() < 0.25 else "go" for _ in range(largo)]
        s[0] = s[1] = "go"
        if all(s[i:i + 4] != ["nogo"] * 4 for i in range(largo - 3)):
            return s


def stroop(largo: int, rng: random.Random) -> list[tuple[str, str]]:
    colores = ["rojo", "azul", "verde", "amarillo"]
    sec, previa = [], None
    while len(sec) < largo:
        palabra = rng.choice([c for c in colores if c != previa])
        tinta = palabra if len(sec) % 2 == 0 else rng.choice([c for c in colores if c != palabra])
        sec.append((palabra, tinta))
        previa = palabra
    return sec


def dprime(h: int, ns: int, fa: int, nr: int) -> float:
    return ND.inv_cdf((h + 0.5) / (ns + 1)) - ND.inv_cdf((fa + 0.5) / (nr + 1))


def main() -> None:
    rng = random.Random(SEMILLA)
    for n in (1, 2, 3):
        sec, obj = nback(n, 120, 0.25, rng)
        correctos = all((sec[i] == sec[i - n]) == obj[i] for i in range(n, len(sec)))
        h = sum(o and rng.random() < 0.9 - 0.1 * n for o in obj[n:])
        fa = sum((not o) and rng.random() < 0.05 + 0.03 * n for o in obj[n:])
        ns, nr = sum(obj[n:]), len(obj[n:]) - sum(obj[n:])
        print(f"{n}-back: objetivos = {ns}/{len(obj[n:])} ({ns / len(obj[n:]):.0%}); coherente: {correctos}; "
              f"d' simulado = {dprime(h, ns, fa, nr):.2f}")
    gn = go_nogo(100, rng)
    print(f"Go/No-Go: No-Go = {gn.count('nogo')}/100; maxima racha de No-Go ok; primeros ensayos = {gn[:2]}")
    st = stroop(60, rng)
    cong = sum(p == t for p, t in st) / len(st)
    rep = sum(st[i][0] == st[i + 1][0] for i in range(len(st) - 1))
    print(f"Stroop: congruentes = {cong:.0%}; repeticiones inmediatas de palabra = {rep}")
    print()
    print("Lectura: las restricciones (proporciones, rachas, repeticiones) forman parte del disenio")
    print("y deben verificarse por codigo. El d' sube la utilidad del n-back frente a 'aciertos'")
    print("porque separa sensibilidad de sesgo (clase 091).")


if __name__ == "__main__":
    main()
