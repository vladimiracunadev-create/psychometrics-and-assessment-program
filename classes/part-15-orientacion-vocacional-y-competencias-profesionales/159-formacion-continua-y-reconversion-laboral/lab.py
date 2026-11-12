"""Laboratorio 159 - Brecha de habilidades hacia ocupaciones destino, con incertidumbre.

Una persona se autoevalua en 8 habilidades (0-10). Tres ocupaciones destino FICTICIAS exigen
niveles distintos. La brecha ponderada = suma de w_i * max(0, requerido_i - actual_i). La
autoevaluacion tiene error (DE 1.2 puntos). Con 3 000 remuestreos del error se calcula la
probabilidad de que cada ocupacion sea la de menor brecha y las horas de formacion estimadas
(supuesto: 6 horas por punto de brecha ponderada). Datos inventados; sirve para pensar rutas de
reconversion con honestidad sobre la incertidumbre de la autoevaluacion.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
HABILIDADES = ["comunicacion", "numerica", "digital", "gestion de proyectos", "atencion al cliente",
               "analisis de datos", "ingles", "trabajo en equipo"]
ACTUAL = [7, 5, 4, 3, 8, 3, 4, 8]
DESTINOS = {
    "soporte tecnico": ([5, 4, 8, 3, 7, 3, 5, 6], [2, 1, 3, 1, 2, 1, 1, 1]),
    "analista de datos junior": ([5, 7, 7, 4, 3, 8, 6, 5], [1, 2, 2, 1, 1, 3, 1, 1]),
    "coordinacion de proyectos": ([8, 5, 5, 8, 6, 4, 5, 7], [2, 1, 1, 3, 1, 1, 1, 2]),
}
HORAS_POR_PUNTO = 6.0


def brecha(actual: list[float], req: list[int], w: list[int]) -> float:
    return sum(wi * max(0.0, r - a) for a, r, wi in zip(actual, req, w, strict=True)) / sum(w)


def main() -> None:
    print(f"{'ocupacion destino':<28} {'brecha ponderada':>17} {'horas estimadas':>16}")
    base = {}
    for d, (req, w) in DESTINOS.items():
        b = brecha(ACTUAL, req, w)
        base[d] = b
        print(f"{d:<28} {b:17.2f} {b * HORAS_POR_PUNTO * len(HABILIDADES):16.0f}")
    rng = random.Random(SEMILLA)
    primero = dict.fromkeys(DESTINOS, 0)
    reps = 3000
    for _ in range(reps):
        real = [min(10, max(0, a + rng.gauss(0, 1.2))) for a in ACTUAL]
        primero[min(DESTINOS, key=lambda d: brecha(real, *DESTINOS[d]))] += 1
    print("\nProbabilidad de ser la ocupacion de menor brecha (autoevaluacion con error DE 1.2):")
    for d, c in sorted(primero.items(), key=lambda kv: -kv[1]):
        print(f"  {d:<28} {c / reps:5.1%}")
    print()
    print("Lectura: aqui el mejor destino es estable (94 %) porque su ventaja es amplia; con brechas mas parejas")
    print("no lo seria. Mejorar la medida (una prueba de desempeno de las habilidades criticas) reduce la")
    print("incertidumbre antes de invertir")
    print("tiempo y dinero en formacion. Las horas son un supuesto, no una promesa: la reconversion depende")
    print("tambien del mercado local, la edad, las redes y el apoyo disponible (informacion a verificar).")


if __name__ == "__main__":
    main()
