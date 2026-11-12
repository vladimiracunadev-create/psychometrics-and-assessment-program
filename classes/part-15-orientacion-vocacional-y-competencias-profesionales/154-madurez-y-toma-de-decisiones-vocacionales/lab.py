"""Laboratorio 154 - Decidir entre alternativas: analisis multicriterio y sensibilidad a los pesos.

Cuatro opciones FICTICIAS de estudio (A, B, C, D) valoradas en 5 criterios (interes, empleabilidad
esperada, costo, cercania, duracion) con puntajes 0-10 (mas = mejor). La persona asigna pesos a
los criterios, pero esos pesos son inciertos. Se calcula el puntaje ponderado y, con 5 000
perturbaciones aleatorias de los pesos (+-30 %), la probabilidad de que cada opcion quede primera.
Ensena que una decision puede ser fragil frente a pequenos cambios de preferencia. No contiene datos
reales de carreras: son numeros inventados.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
CRITERIOS = ["interes", "empleabilidad", "costo", "cercania", "duracion"]
PESOS = [0.35, 0.25, 0.15, 0.15, 0.10]
OPCIONES = {
    "A": [9, 5, 4, 6, 6],
    "B": [7, 9, 4, 5, 7],
    "C": [6, 9, 3, 4, 5],
    "D": [8, 6, 6, 7, 7],
}


def puntaje(valores: list[int], pesos: list[float]) -> float:
    return sum(v * w for v, w in zip(valores, pesos, strict=True)) / sum(pesos)


def main() -> None:
    print(f"{'opcion':<8} {'puntaje con los pesos declarados':>34}")
    for o, v in sorted(OPCIONES.items(), key=lambda kv: -puntaje(kv[1], PESOS)):
        print(f"{o:<8} {puntaje(v, PESOS):34.2f}")
    rng = random.Random(SEMILLA)
    primero = dict.fromkeys(OPCIONES, 0)
    reps = 5000
    for _ in range(reps):
        w = [p * rng.uniform(0.7, 1.3) for p in PESOS]
        mejor = max(OPCIONES, key=lambda o: puntaje(OPCIONES[o], w))
        primero[mejor] += 1
    print(f"\nProbabilidad de quedar primera si los pesos varian +-30 % ({reps} simulaciones):")
    for o, c in sorted(primero.items(), key=lambda kv: -kv[1]):
        print(f"  {o}: {c / reps:5.1%}")
    margen = sorted((puntaje(v, PESOS) for v in OPCIONES.values()), reverse=True)
    print(f"\nDiferencia entre la 1.a y la 2.a opcion: {margen[0] - margen[1]:.2f} puntos de 10")
    print()
    print("Lectura: cuando dos opciones quedan cerca, el 'ganador' cambia con pequenas variaciones de")
    print("pesos: la decision es fragil, y eso es informacion util. El analisis multicriterio ordena la")
    print("conversacion, no decide por la persona. Los puntajes de empleabilidad o costo deben salir de")
    print("fuentes verificables, no de intuiciones; aqui son inventados.")


if __name__ == "__main__":
    main()
