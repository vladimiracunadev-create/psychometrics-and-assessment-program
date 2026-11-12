"""Laboratorio 113 - Items ORIGINALES de comprension de instrucciones con respuesta calculada.

Cada item es un programa de instrucciones sobre una cifra ("Parta con 7. Si el numero es impar,
sumele 4; si no, restele 2. Luego multipliquelo por 3."). La respuesta se obtiene ejecutando
las instrucciones con un interprete propio, y se verifica con un segundo calculo independiente.
La dificultad se controla por el numero de pasos y de condicionales. Es un generador propio:
no replica ninguna prueba comercial de comprension de instrucciones.
"""
from __future__ import annotations

import random

SEMILLA = 20260819


def genera(pasos: int, condicionales: int, rng: random.Random):
    n0 = rng.randint(2, 12)
    programa, texto = [], [f"Parta con {n0}."]
    posiciones = set(rng.sample(range(pasos), condicionales)) if condicionales else set()
    for i in range(pasos):
        if i in posiciones:
            a, b = rng.randint(2, 6), rng.randint(2, 6)
            programa.append(("si_impar", a, b))
            texto.append(f"Si el numero es impar, sumele {a}; si es par, restele {b}.")
        else:
            op = rng.choice(["suma", "resta", "multiplica"])
            v = rng.randint(2, 4) if op == "multiplica" else rng.randint(1, 9)
            programa.append((op, v, 0))
            verbo = {"suma": "Sumele", "resta": "Restele", "multiplica": "Multipliquelo por"}[op]
            texto.append(f"{verbo} {v}.")
    return n0, programa, " ".join(texto)


def ejecuta(n0: int, programa) -> int:
    n = n0
    for op, a, b in programa:
        if op == "suma":
            n += a
        elif op == "resta":
            n -= a
        elif op == "multiplica":
            n *= a
        else:
            n = n + a if n % 2 else n - b
    return n


def verifica(n0: int, programa) -> int:
    """Segunda implementacion (recursiva) para contrastar el interprete."""
    if not programa:
        return n0
    (op, a, b), *resto = programa
    if op == "suma":
        return verifica(n0 + a, resto)
    if op == "resta":
        return verifica(n0 - a, resto)
    if op == "multiplica":
        return verifica(n0 * a, resto)
    return verifica(n0 + a if n0 % 2 else n0 - b, resto)


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'pasos':>5} {'cond.':>5}  item -> respuesta")
    print("=" * 100)
    coinciden = 0
    total = 0
    for pasos, cond in ((2, 0), (3, 1), (4, 2), (5, 3)):
        for _ in range(2):
            n0, prog, texto = genera(pasos, cond, rng)
            r1, r2 = ejecuta(n0, prog), verifica(n0, prog)
            coinciden += r1 == r2
            total += 1
            print(f"{pasos:5d} {cond:5d}  {texto}  -> {r1}")
    print(f"\nConcordancia entre interprete y verificador: {coinciden}/{total}")
    print()
    print("Lectura: la dificultad (pasos y condicionales) se controla por diseno, y la clave se calcula")
    print("y se verifica por codigo, sin errores de transcripcion. Esa dificultad 'de diseno' debe")
    print("contrastarse con datos (clase 015) y vigilar que no mida solo memoria de trabajo (clase 095)")
    print("o lectura (clase 084). Un instrumento laboral requiere ademas evidencia de validez para el puesto.")


if __name__ == "__main__":
    main()
