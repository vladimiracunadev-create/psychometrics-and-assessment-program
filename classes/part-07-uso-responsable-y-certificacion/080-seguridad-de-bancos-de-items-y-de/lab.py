"""Laboratorio 080 - Seguridad del banco: deteccion de filtracion e integridad de archivos.

Parte 1 (filtracion): 1 000 examinados rinden 40 items; el 25 % tuvo acceso previo a 10 items
filtrados. Se compara la proporcion de aciertos por item antes y despues de la filtracion: los
items filtrados "suben" de forma anomala respecto de los demas.
Parte 2 (integridad): se calcula la huella SHA-256 de cada instrumento de instruments/ y se
verifica contra un manifiesto; alterar un byte cambia la huella. El hash detecta cambios, no
previene el acceso indebido.
"""
from __future__ import annotations

import hashlib
import math
import pathlib
import random
import statistics

SEMILLA = 20260819
N, K, FILTRADOS = 1000, 40, set(range(10))
RAIZ = pathlib.Path(__file__).resolve().parents[3]


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def aplica(filtracion: bool, rng: random.Random) -> list[float]:
    aciertos = [0] * K
    for _ in range(N):
        t = rng.gauss(0, 1)
        sabe = filtracion and rng.random() < 0.25
        for j in range(K):
            p = 0.95 if (sabe and j in FILTRADOS) else logistica(t - (-1.5 + 3.0 * j / (K - 1)))
            aciertos[j] += rng.random() < p
    return [a / N for a in aciertos]


def main() -> None:
    rng = random.Random(SEMILLA)
    antes, despues = aplica(False, rng), aplica(True, rng)
    cambios = [d - a for a, d in zip(antes, despues, strict=True)]
    media_otros = statistics.fmean(c for j, c in enumerate(cambios) if j not in FILTRADOS)
    sd_otros = statistics.stdev(c for j, c in enumerate(cambios) if j not in FILTRADOS)
    marcados = [j + 1 for j, c in enumerate(cambios) if (c - media_otros) / sd_otros > 3]
    print(f"Cambio medio de p en items no filtrados: {media_otros:+.3f} (DE {sd_otros:.3f})")
    print(f"Cambio medio de p en los 10 items filtrados: {statistics.fmean(cambios[:10]):+.3f}")
    print(f"Items marcados (cambio > 3 DE sobre los demas): {marcados}")

    print("\nManifiesto de integridad (primeros 16 hex de SHA-256):")
    huellas = {}
    for a in sorted((RAIZ / "instruments").glob("*.yaml")):
        huellas[a.name] = hashlib.sha256(a.read_bytes()).hexdigest()
        print(f"  {a.name:<24} {huellas[a.name][:16]}")
    muestra = (RAIZ / "instruments" / "disc-abierto.yaml").read_bytes() + b" "
    print(f"  disc-abierto.yaml con 1 byte agregado -> {hashlib.sha256(muestra).hexdigest()[:16]} (cambia)")
    print()
    print("Lectura: una filtracion deja huella estadistica en los items expuestos, pero hay que")
    print("distinguirla de aprendizaje real o cambios de poblacion. El hash garantiza integridad, no")
    print("confidencialidad: un banco secreto ademas necesita control de acceso, cifrado y rotacion.")


if __name__ == "__main__":
    main()
