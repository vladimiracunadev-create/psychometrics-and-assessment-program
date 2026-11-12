"""Laboratorio 083 - Un generador ORIGINAL de series numericas con solucion verificable.

Reglas de generacion (todas propias, sin copiar ninguna prueba): aritmetica (+d), geometrica
(*r), alternada (dos reglas entrelazadas) y de segundo orden (la diferencia crece). Para cada
item se calcula la respuesta y se comprueba con un resolutor independiente que SOLO una de las
reglas candidatas explica la serie (solucion unica). Los distractores se construyen a partir de
errores tipicos. La dificultad esperada crece con el numero de reglas.
"""
from __future__ import annotations

import random

SEMILLA = 20260819


def genera(tipo: str, rng: random.Random) -> list[int]:
    a = rng.randint(2, 9)
    if tipo == "aritmetica":
        d = rng.randint(2, 7)
        return [a + d * i for i in range(7)]
    if tipo == "geometrica":
        r = rng.choice([2, 3])
        return [a * r**i for i in range(6)]
    if tipo == "alternada":
        d1, d2 = rng.randint(2, 5), rng.randint(2, 5)
        return [a + d1 * (i // 2) if i % 2 == 0 else 50 + d2 * (i // 2) for i in range(8)]
    d = rng.randint(1, 3)                      # segundo orden: diferencias d, 2d, 3d...
    s = [a]
    for i in range(1, 7):
        s.append(s[-1] + d * i)
    return s


def candidatas(visible: list[int]) -> set[int]:
    """Siguientes valores que producen las reglas candidatas; unica => item bien formado."""
    sig = set()
    if len({visible[i + 1] - visible[i] for i in range(len(visible) - 1)}) == 1:
        sig.add(visible[-1] + visible[1] - visible[0])
    if visible[0] != 0 and all(visible[i] * (visible[1] // visible[0]) == visible[i + 1] for i in range(len(visible) - 1)) \
            and visible[1] % visible[0] == 0:
        sig.add(visible[-1] * (visible[1] // visible[0]))
    d2 = [visible[i + 1] - visible[i] for i in range(len(visible) - 1)]
    if len(d2) > 2 and len({d2[i + 1] - d2[i] for i in range(len(d2) - 1)}) == 1:
        sig.add(visible[-1] + d2[-1] + (d2[1] - d2[0]))
    if len(visible) >= 6:
        par, impar = visible[0::2], visible[1::2]
        if len({par[i + 1] - par[i] for i in range(len(par) - 1)}) == 1 and \
           len({impar[i + 1] - impar[i] for i in range(len(impar) - 1)}) == 1:
            seq = impar if len(visible) % 2 else par
            sig.add(seq[-1] + seq[1] - seq[0])
    return sig


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'tipo':<12} {'serie visible':<34} {'respuesta':>9} {'unica':>6}  distractores")
    print("=" * 96)
    bien = 0
    for tipo in ("aritmetica", "geometrica", "alternada", "segundo orden"):
        for _ in range(3):
            serie = genera(tipo, rng)
            visible, respuesta = serie[:-1], serie[-1]
            cand = candidatas(visible)
            unica = cand == {respuesta}
            bien += unica
            distr = sorted({visible[-1] + (visible[-1] - visible[-2]), respuesta + 1, respuesta - 2,
                            visible[-1] * 2} - {respuesta})[:3]
            print(f"{tipo:<12} {str(visible):<34} {respuesta:9d} {'si' if unica else 'NO':>6}  {distr}")
    print(f"\nItems con solucion unica verificada por el resolutor: {bien} de 12")
    print()
    print("Lectura: generar items con semilla permite bancos originales y auditables, pero la")
    print("dificultad real y la calidad de los distractores se estiman con datos (clase 015). Un")
    print("item con dos explicaciones validas es un item defectuoso: el resolutor lo detecta.")


if __name__ == "__main__":
    main()
