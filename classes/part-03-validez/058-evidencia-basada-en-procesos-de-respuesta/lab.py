"""Laboratorio 058 - Evidencia basada en procesos de respuesta: tiempos y adivinacion rapida.

Una prueba de 30 items donde cierto porcentaje de respuestas se da "al azar y rapido"
(adivinacion rapida, ~1.5 s) en lugar de razonada (~15 s con variacion). Se muestra:
  1. el tiempo de respuesta separa ambos procesos;
  2. los aciertos de respuestas rapidas rondan el azar (0.25 con 4 opciones);
  3. filtrar las respuestas rapidas mejora la correlacion entre habilidad y puntaje.
El umbral de 3 s es una decision explicita del laboratorio; en la practica se justifica
con la distribucion de tiempos de cada item.
"""
from __future__ import annotations

import math
import random
import statistics

SEMILLA = 20260819
N, K = 2000, 30
UMBRAL_S = 3.0


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def main() -> None:
    rng = random.Random(SEMILLA)
    hab, tiempos, aciertos = [], [], []
    for _ in range(N):
        theta = rng.gauss(0, 1)
        apurado = rng.random() < 0.3                     # 30 % de las personas se apura en algunos items
        t_p, a_p = [], []
        for _ in range(K):
            rapido = apurado and rng.random() < 0.5
            if rapido:
                t_p.append(max(0.3, rng.gauss(1.5, 0.4)))
                a_p.append(int(rng.random() < 0.25))
            else:
                t_p.append(max(2.0, rng.gauss(15, 4)))
                a_p.append(int(rng.random() < logistica(1.4 * theta)))
        hab.append(theta), tiempos.append(t_p), aciertos.append(a_p)

    rap = [(t, a) for tp, ap in zip(tiempos, aciertos, strict=True) for t, a in zip(tp, ap, strict=True)]
    ra = [a for t, a in rap if t < UMBRAL_S]
    ln = [a for t, a in rap if t >= UMBRAL_S]
    print(f"Respuestas rapidas (< {UMBRAL_S}s): {len(ra) / len(rap):.1%} del total; "
          f"aciertos = {statistics.fmean(ra):.3f} (azar = 0.25)")
    print(f"Respuestas normales: aciertos = {statistics.fmean(ln):.3f}")

    bruto = [sum(a) for a in aciertos]
    # Puntaje de respuestas normales, reescalado a 30 items para ser comparable.
    filtrado = []
    for tp, ap in zip(tiempos, aciertos, strict=True):
        v = [a for t, a in zip(tp, ap, strict=True) if t >= UMBRAL_S]
        filtrado.append(statistics.fmean(v) * K if v else K * 0.25)
    print()
    print(f"r(habilidad, puntaje bruto)               = {statistics.correlation(hab, bruto):.3f}")
    print(f"r(habilidad, puntaje sin resp. rapidas)   = {statistics.correlation(hab, filtrado):.3f}")
    print()
    print("Lectura: el puntaje mezcla habilidad con motivacion de esfuerzo. Los tiempos son")
    print("evidencia de proceso (AERA/APA/NCME 2014), pero un tiempo corto tambien puede ser")
    print("pericia: se interpreta con el contenido del item, no mecanicamente.")


if __name__ == "__main__":
    main()
