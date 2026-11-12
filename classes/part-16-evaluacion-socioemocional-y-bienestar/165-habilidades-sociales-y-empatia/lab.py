"""Laboratorio 165 - Reconocimiento de emociones: precision cruda frente a tasa de acierto no sesgada.

Prueba con 6 emociones (alegria, tristeza, enojo, miedo, sorpresa, asco), 12 estimulos cada una.
Dos personas con la MISMA capacidad de discriminar pero distinto sesgo de respuesta: B responde
"enojo" con mucha frecuencia. La precision cruda (aciertos/72) favorece o perjudica por sesgo; la
tasa de acierto no sesgada de Wagner (1993), Hu = (aciertos_i^2) / (n_estimulos_i * n_respuestas_i),
promediada entre emociones, corrige parte del sesgo. Se simula la matriz de confusion y se
comparan ambos indices. Datos sinteticos; no usa imagenes de personas.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
EMO = ["alegria", "tristeza", "enojo", "miedo", "sorpresa", "asco"]
POR_EMO = 12
REPS = 400


def responde(verdadera: int, nitidez: float, sesgo_enojo: float, rng: random.Random) -> int:
    pesos = [0.0] * 6
    pesos[verdadera] = nitidez
    for j in range(6):
        pesos[j] += (1 - nitidez) / 6
    pesos[2] += sesgo_enojo
    return rng.choices(range(6), weights=pesos)[0]


def indices(conf: list[list[int]]) -> tuple[float, float]:
    total = sum(conf[i][i] for i in range(6)) / (6 * POR_EMO)
    hu = 0.0
    for i in range(6):
        n_resp = sum(conf[j][i] for j in range(6))
        hu += (conf[i][i] ** 2) / (POR_EMO * n_resp) if n_resp else 0.0
    return total, hu / 6


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'persona':<26} {'precision cruda':>16} {'Hu (no sesgada)':>16}")
    print("=" * 62)
    for nombre, sesgo in (("sin sesgo de respuesta", 0.0), ("sesgo a responder 'enojo'", 0.45)):
        crudo = hu = 0.0
        for _ in range(REPS):
            conf = [[0] * 6 for _ in range(6)]
            for e in range(6):
                for _ in range(POR_EMO):
                    conf[e][responde(e, 0.7, sesgo, rng)] += 1
            c, h = indices(conf)
            crudo += c / REPS
            hu += h / REPS
        print(f"{nombre:<26} {crudo:16.2f} {hu:16.2f}")
    print()
    print("Lectura: con la misma nitidez de percepcion, el sesgo a una respuesta cambia la precision cruda y")
    print("tambien (menos) la tasa no sesgada. Las pruebas de reconocimiento de emociones mezclan percepcion,")
    print("vocabulario y sesgo; las escalas autoinformadas de empatia miden otra cosa (autoconcepto). Ni una ni")
    print("otra diagnostican 'falta de empatia' ni 'dificultades sociales': se interpretan con observacion y contexto.")


if __name__ == "__main__":
    main()
