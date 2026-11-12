"""Laboratorio 144 - Items de calculo ORIGINALES con dificultad por "reagrupaciones".

Generador de restas de dos o tres cifras con un numero controlado de reagrupaciones (prestamos).
Cada item se resuelve con el algoritmo escrito y se verifica con la resta de Python. La
probabilidad de error de un estudiante crece con el numero de reagrupaciones (supuesto del
laboratorio, que debe comprobarse con datos). Se simula un grupo y se muestra:
  - la tabla de dificultad observada por numero de reagrupaciones,
  - el diagnostico de un error tipico: restar "el menor del mayor" en cada columna (sin reagrupar).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819


def reagrupaciones(a: int, b: int) -> int:
    n, prestamo = 0, 0
    while a or b:
        da, db = a % 10, b % 10
        if da - prestamo < db:
            n += 1
            prestamo = 1
        else:
            prestamo = 0
        a //= 10
        b //= 10
    return n


def resta_columna(a: int, b: int) -> int:
    """Algoritmo escrito con prestamos; devuelve a - b."""
    da, db, res, prestamo, pos = list(map(int, str(a)))[::-1], list(map(int, str(b)))[::-1], 0, 0, 0
    for i in range(len(da)):
        x = da[i] - prestamo - (db[i] if i < len(db) else 0)
        prestamo = 1 if x < 0 else 0
        res += (x + 10 * prestamo) * 10**pos
        pos += 1
    return res


def error_tipico(a: int, b: int) -> int:
    """Resta la cifra menor de la mayor en cada columna (no reagrupa)."""
    da, db, res = list(map(int, str(a)))[::-1], list(map(int, str(b)))[::-1], 0
    for i, x in enumerate(da):
        y = db[i] if i < len(db) else 0
        res += abs(x - y) * 10**i
    return res


def main() -> None:
    rng = random.Random(SEMILLA)
    items = []
    while len(items) < 600:
        a, b = rng.randint(100, 999), rng.randint(10, 899)
        if a > b:
            items.append((a, b))
    ok = all(resta_columna(a, b) == a - b for a, b in items)
    print(f"Algoritmo escrito concuerda con la resta de Python en {len(items)} items: {ok}")
    por_n = {k: [(a, b) for a, b in items if reagrupaciones(a, b) == k] for k in (0, 1, 2)}
    print(f"\n{'reagrupaciones':>15} {'items':>6} {'P(error) supuesta':>19} {'% error simulado':>18}")
    estudiantes = [rng.gauss(0, 1) for _ in range(300)]
    for k, lst in por_n.items():
        p_err = 0.05 + 0.18 * k
        errores = statistics.fmean(rng.random() < min(0.95, p_err - 0.04 * t) for t in estudiantes for _ in range(4))
        print(f"{k:15d} {len(lst):6d} {p_err:19.2f} {errores:18.1%}")
    a, b = 534, 278
    print(f"\nEjemplo {a} - {b} = {a - b} ({reagrupaciones(a, b)} reagrupaciones); respuesta de un error tipico: {error_tipico(a, b)}")
    print()
    print("Lectura: la dificultad de un item de calculo se puede explicar y controlar por diseno, y un")
    print("error sistematico (restar la cifra menor de la mayor) es identificable por su respuesta, lo que")
    print("orienta la ensenanza. Las probabilidades de error del laboratorio son supuestas: la relacion")
    print("dificultad-reagrupaciones se comprueba con datos reales antes de usarla.")


if __name__ == "__main__":
    main()
