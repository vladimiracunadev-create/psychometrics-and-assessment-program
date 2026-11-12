"""Laboratorio 036 - Matriz multirrasgo-multimetodo (Campbell y Fiske, 1959).

3 rasgos (T1, T2, T3) medidos con 2 metodos (autoinforme, informante). Cada medida =
rasgo + varianza de metodo + error. Se construye la matriz de correlaciones y se evaluan
los criterios de Campbell-Fiske:
  1. diagonal de validez (mismo rasgo, distinto metodo) significativamente > 0;
  2. validez > heterorrasgo-heterometodo;
  3. validez > heterorrasgo-monometodo (si no, domina el metodo).
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N = 5000
RASGOS, METODOS = ("T1", "T2", "T3"), ("auto", "info")


def simula(peso_metodo: float, rng: random.Random) -> dict[str, list[float]]:
    # Rasgos con correlacion verdadera 0.2 entre si.
    base = [rng.gauss(0, 1) for _ in range(N)]
    rasgos = [[math.sqrt(0.2) * b + math.sqrt(0.8) * rng.gauss(0, 1) for b in base] for _ in RASGOS]
    metodos = {m: [rng.gauss(0, 1) for _ in range(N)] for m in METODOS}
    return {f"{r}-{m}": [0.7 * t + peso_metodo * v + rng.gauss(0, 0.5)
                         for t, v in zip(rasgos[i], metodos[m], strict=True)]
            for i, r in enumerate(RASGOS) for m in METODOS}


def analiza(medidas: dict[str, list[float]]) -> None:
    nombres = list(medidas)
    validez, hetero_mono, hetero_hetero = [], [], []
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            ra, ma = a.split("-")
            rb, mb = b.split("-")
            r = statistics.correlation(medidas[a], medidas[b])
            if ra == rb:
                validez.append(r)
            elif ma == mb:
                hetero_mono.append(r)
            else:
                hetero_hetero.append(r)
    f = statistics.fmean
    print(f"  validez (mismo rasgo, otro metodo)     media = {f(validez):.3f}")
    print(f"  heterorrasgo-monometodo                media = {f(hetero_mono):.3f}")
    print(f"  heterorrasgo-heterometodo              media = {f(hetero_hetero):.3f}")
    c2 = f(validez) > f(hetero_hetero)
    c3 = f(validez) > f(hetero_mono)
    print(f"  criterio 2 (validez > hetero-hetero): {'cumple' if c2 else 'NO cumple'}"
          f" | criterio 3 (validez > hetero-mono): {'cumple' if c3 else 'NO cumple'}")


def main() -> None:
    rng = random.Random(SEMILLA)
    for titulo, w in (("Poca varianza de metodo (0.2)", 0.2), ("Mucha varianza de metodo (1.0)", 1.0)):
        print(titulo)
        analiza(simula(w, rng))
        print()
    print("Lectura: con mucho metodo comun la correlacion entre rasgos DISTINTOS medidos")
    print("con el mismo metodo supera a la de un MISMO rasgo medido con metodos distintos:")
    print("lo que se mide es el formato. Eso solo se ve con un diseno multimetodo.")


if __name__ == "__main__":
    main()
