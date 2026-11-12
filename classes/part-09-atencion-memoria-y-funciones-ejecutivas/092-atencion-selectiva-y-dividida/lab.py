"""Laboratorio 092 - Busqueda visual (selectiva) y costo de doble tarea (dividida).

Parte 1: busqueda de rasgo (pendiente ~0 ms por elemento) frente a busqueda de conjuncion
(pendiente de ~10 ms o mas por elemento). Se simulan 100 personas y se ajusta la pendiente
tiempo ~ tamano del conjunto (Treisman y Gelade, 1980).
Parte 2: costo de doble tarea = (RT en doble tarea - RT en tarea simple) / RT simple, con y
sin competencia por el mismo recurso. Datos sinteticos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, TAMANOS, REPS = 100, (4, 8, 16, 32), 20


def pendiente(xs: list[float], ys: list[float]) -> float:
    return statistics.covariance(xs, ys) / statistics.variance(xs)


def main() -> None:
    rng = random.Random(SEMILLA)
    pend = {"rasgo": [], "conjuncion": []}
    for _ in range(N):
        base = rng.gauss(500, 60)
        for tipo, costo in (("rasgo", 0.5), ("conjuncion", 25.0)):
            xs, ys = [], []
            for n in TAMANOS:
                for _ in range(REPS):
                    xs.append(float(n))
                    ys.append(base + rng.gauss(costo, 3) * n / 2 + rng.gauss(0, 60))
            pend[tipo].append(pendiente(xs, ys))
    print("Parte 1 - pendiente de la busqueda (ms por elemento)")
    for tipo, v in pend.items():
        print(f"  {tipo:<11} media = {statistics.fmean(v):6.2f}  DE entre personas = {statistics.pstdev(v):5.2f}")

    print("\nParte 2 - costo de doble tarea")
    for nombre, extra in (("recursos distintos", 0.05), ("mismo recurso", 0.35)):
        costos = []
        for _ in range(N):
            simple = rng.gauss(600, 70)
            doble = simple * (1 + extra) + rng.gauss(0, 40)
            costos.append((doble - simple) / simple)
        print(f"  {nombre:<20} costo medio = {statistics.fmean(costos):5.1%}")
    print()
    print("Lectura: 'atencion' no es una sola cosa. La busqueda de rasgo es casi paralela; la de")
    print("conjuncion exige atencion serial. El costo de doble tarea depende de si las tareas compiten")
    print("por el mismo recurso. Un 'test de atencion' mide la combinacion especifica que pide la tarea.")


if __name__ == "__main__":
    main()
