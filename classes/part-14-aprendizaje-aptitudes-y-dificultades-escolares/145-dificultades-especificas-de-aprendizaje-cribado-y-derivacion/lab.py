"""Laboratorio 145 - Respuesta a la intervencion: pendiente de progreso y falsos positivos.

Monitoreo semanal de PCM (palabras correctas por minuto) con ruido de medicion. Un estudiante
"responde" si su pendiente real es >= 1.5 PCM/semana. Se simula a 400 estudiantes con pendientes
reales distintas y se estima la pendiente por regresion con 4, 8 y 12 semanas de datos. Se mide:
  - la precision de la pendiente (error tipico),
  - la proporcion de clasificaciones erradas (responde / no responde) segun la duracion.
Con pocas semanas, la decision de "no responde" (y con ello la derivacion) es poco confiable.
Parametros supuestos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, UMBRAL, RUIDO = 400, 1.5, 8.0


def pendiente(y: list[float]) -> float:
    x = list(range(len(y)))
    return statistics.covariance(x, y) / statistics.variance(x)


def main() -> None:
    rng = random.Random(SEMILLA)
    reales = [max(0.0, rng.gauss(1.5, 0.8)) for _ in range(N)]
    print(f"{'semanas':>8} {'error tipico de la pendiente':>29} {'clasificacion errada':>22} {'falsos \"no responde\"':>23}")
    print("=" * 86)
    for semanas in (4, 8, 12, 16):
        errs, malas, falsos_no = [], 0, 0
        for b in reales:
            y = [40 + b * t + rng.gauss(0, RUIDO) for t in range(semanas)]
            est = pendiente(y)
            errs.append(est - b)
            malas += (est >= UMBRAL) != (b >= UMBRAL)
            falsos_no += (b >= UMBRAL) and (est < UMBRAL)
        print(f"{semanas:8d} {statistics.pstdev(errs):29.2f} {malas / N:22.1%} {falsos_no / sum(b >= UMBRAL for b in reales):23.1%}")
    print()
    print("Lectura: con 4 semanas el error de la pendiente es mayor que la propia pendiente que se quiere")
    print("juzgar: muchos estudiantes que si responden parecen no hacerlo. Un monitoreo breve no sustenta")
    print("una derivacion; requiere mas semanas, mediciones mas fiables (clase 142) y un cribado")
    print("escalonado. La evaluacion de una dificultad especifica de aprendizaje es un proceso profesional.")


if __name__ == "__main__":
    main()
