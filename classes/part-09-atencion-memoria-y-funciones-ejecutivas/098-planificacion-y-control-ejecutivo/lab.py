"""Laboratorio 098 - Planificacion: problemas tipo Torre de Hanoi con solucion optima exacta.

Se resuelve por busqueda en anchura (BFS) el numero minimo de movimientos de configuraciones
aleatorias de 3 y 4 discos en 3 varillas. Con eso:
  - se tabula la dificultad objetiva (movimientos optimos) de un banco generado;
  - se simula un planificador que mira `h` pasos hacia adelante y se mide su exceso de
    movimientos respecto del optimo (un indicador de planificacion).
Es un ejemplo ORIGINAL de generacion y calificacion automatica, no una prueba normada.
"""
from __future__ import annotations

import collections
import itertools
import random
import statistics

SEMILLA = 20260819


def vecinos(estado: tuple[int, ...]):
    n = len(estado)
    for i in range(n):
        if all(estado[j] != estado[i] for j in range(i)):     # disco i libre por arriba
            for v in range(3):
                if v != estado[i] and all(estado[j] != v for j in range(i)):
                    yield estado[:i] + (v,) + estado[i + 1:]


def distancias_desde(meta: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    d = {meta: 0}
    cola = collections.deque([meta])
    while cola:
        s = cola.popleft()
        for t in vecinos(s):
            if t not in d:
                d[t] = d[s] + 1
                cola.append(t)
    return d


def planificador(inicio, meta, dist, h, rng):
    """Planificador miope: solo 've' la solucion si esta a h movimientos o menos.

    Si la meta esta lejos (dist > h), se mueve al azar; si esta a la vista, sigue el camino
    optimo. Devuelve el numero de movimientos hasta resolver (tope 400)."""
    s, pasos = inicio, 0
    while s != meta and pasos < 400:
        if dist[s] <= h:
            s = min(vecinos(s), key=lambda t: dist[t])
        else:
            s = rng.choice(list(vecinos(s)))
        pasos += 1
    return pasos


def main() -> None:
    rng = random.Random(SEMILLA)
    for n in (3, 4):
        meta = (2,) * n
        dist = distancias_desde(meta)
        todos = list(itertools.product(range(3), repeat=n))
        optimos = [dist[s] for s in todos]
        cuenta = collections.Counter(optimos)
        print(f"{n} discos: {len(todos)} configuraciones; movimientos optimos maximos = {max(optimos)}")
        print("  distribucion de la dificultad:", dict(sorted(cuenta.items())))
        exceso = {}
        for h in (1, 3, 6):
            ex = []
            for _ in range(60):
                ini = rng.choice(todos)
                if ini == meta:
                    continue
                ex.append(planificador(ini, meta, dist, h, rng) - dist[ini])
            exceso[h] = statistics.fmean(ex)
        print("  exceso medio de movimientos segun horizonte de planificacion h:",
              {h: round(v, 1) for h, v in exceso.items()})
    print()
    print("Lectura: la dificultad de un problema de planificacion se puede calcular, no suponer. El")
    print("exceso de movimientos mide la calidad del plan, pero depende de la estrategia y la regla")
    print("de puntuacion; ademas la tarea sola no es un diagnostico de 'funcion ejecutiva'.")


if __name__ == "__main__":
    main()
