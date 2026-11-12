"""Laboratorio 130 - Decisiones de grupo: el teorema de la prediccion de la diversidad.

Para estimaciones numericas: error colectivo = error medio individual - diversidad, donde
    error colectivo   = (media de estimaciones - verdad)^2
    error individual  = media de (estimacion_i - verdad)^2
    diversidad        = varianza de las estimaciones          (Page, 2007)
Se verifica la igualdad numericamente y se compara el error del grupo en dos condiciones:
  - INDEPENDIENTES: cada integrante estima solo;
  - INFLUIDOS: tras una discusion, cada uno se acerca al lider (que tiene un sesgo), lo que reduce la
    diversidad y propaga el sesgo.
Es un modelo simple de por que la discusion no siempre mejora la decision (pensamiento de grupo).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
VERDAD, N, REPS = 100.0, 9, 4000


def descompone(est: list[float]) -> tuple[float, float, float]:
    colectivo = (statistics.fmean(est) - VERDAD) ** 2
    individual = statistics.fmean((e - VERDAD) ** 2 for e in est)
    diversidad = statistics.pvariance(est)
    return colectivo, individual, diversidad


def main() -> None:
    rng = random.Random(SEMILLA)
    colec = {"independientes": [], "influidos": []}
    chequeo = 0.0
    for _ in range(REPS):
        indep = [VERDAD + rng.gauss(0, 20) for _ in range(N)]
        lider = VERDAD + 25.0 + rng.gauss(0, 5)                    # el lider tiene un sesgo de +25
        influ = [e + 0.7 * (lider - e) for e in indep]
        for nombre, est in (("independientes", indep), ("influidos", influ)):
            c, i, d = descompone(est)
            colec[nombre].append(c)
            if nombre == "independientes":
                chequeo = max(chequeo, abs(c - (i - d)))
    print(f"Verificacion del teorema: max |error colectivo - (error individual - diversidad)| = {chequeo:.1e}")
    print(f"\n{'condicion':<16} {'error colectivo (MSE)':>22} {'RMSE':>7}")
    for nombre, v in colec.items():
        m = statistics.fmean(v)
        print(f"{nombre:<16} {m:22.1f} {m ** 0.5:7.1f}")
    print()
    print("Lectura: con juicios independientes el promedio es mucho mas exacto que el individuo, porque")
    print("los errores se cancelan. Cuando la discusion alinea al grupo con un lider sesgado, baja la")
    print("diversidad y se hereda el sesgo. Procedimientos como estimaciones independientes antes de")
    print("discutir (tipo Delphi) conservan la diversidad. En conflictos interpersonales, ademas, los")
    print("cuestionarios de 'estilo de manejo de conflictos' son autoinformes con evidencia limitada.")


if __name__ == "__main__":
    main()
