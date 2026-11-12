"""Laboratorio 095 - Puntuar la amplitud de memoria de trabajo: tres reglas, tres fiabilidades.

Tarea de amplitud: 12 ensayos (tamanos 2 a 7, dos por tamano). La capacidad verdadera de cada
persona C (items que sostiene). En un ensayo de tamano k se recuerdan correctamente
min(k, C) items menos errores aleatorios. Tres puntuaciones:
  - todo-o-nada: suma de tamanos de ensayos perfectos;
  - credito parcial por ensayo: proporcion media de items correctos;
  - amplitud maxima: mayor tamano con ensayo perfecto.
Se estima la fiabilidad por mitades (ensayos pares/impares) y la correlacion con C. La
literatura (Conway et al., 2005) discute el credito parcial; aqui se contrasta en simulacion.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, TAMANOS = 600, (2, 3, 4, 5, 6, 7) * 2


def ensayo(c: float, k: int, rng: random.Random) -> int:
    correctos = 0
    for i in range(k):
        p = 0.97 if i < c else 0.25                   # los items "sostenidos" se recuerdan bien
        correctos += rng.random() < p
    return correctos


def puntajes(ens: list[tuple[int, int]]) -> dict[str, float]:
    todo = sum(k for k, r in ens if r == k)
    parcial = statistics.fmean(r / k for k, r in ens)
    maxima = max([k for k, r in ens if r == k] or [0])
    return {"todo-o-nada": todo, "credito parcial": parcial, "amplitud maxima": maxima}


def main() -> None:
    rng = random.Random(SEMILLA)
    caps = [max(1.0, rng.gauss(4.2, 1.1)) for _ in range(N)]
    medias: dict[str, tuple[list[float], list[float]]] = {}
    totales: dict[str, list[float]] = {}
    for c in caps:
        ens = [(k, ensayo(c, k, rng)) for k in TAMANOS]
        a, b = puntajes(ens[0::2]), puntajes(ens[1::2])
        t = puntajes(ens)
        for k in a:
            medias.setdefault(k, ([], []))
            medias[k][0].append(a[k])
            medias[k][1].append(b[k])
            totales.setdefault(k, []).append(t[k])
    print(f"{'puntuacion':<18} {'fiab. mitades (SB)':>19} {'r con capacidad real':>22}")
    print("=" * 62)
    for k, (a, b) in medias.items():
        r = statistics.correlation(a, b)
        print(f"{k:<18} {2 * r / (1 + r):19.3f} {statistics.correlation(totales[k], caps):22.3f}")
    print()
    print("Lectura: la amplitud maxima aprovecha un solo ensayo y es la menos fiable; el credito parcial")
    print("es el mas fiable (usa toda la informacion). En ESTA simulacion el todo-o-nada se acerca algo")
    print("mas a la capacidad verdadera porque el recuerdo de los items sostenidos es casi deterministico:")
    print("el resultado depende del modelo de respuesta. La regla de puntuacion es una decision de")
    print("medicion, no un detalle, y se justifica con datos de la tarea real.")


if __name__ == "__main__":
    main()
