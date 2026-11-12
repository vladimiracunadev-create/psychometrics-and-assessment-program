"""Laboratorio 139 - Cribado en dos etapas: el valor predictivo cuando las pruebas se parecen.

Etapa 1: cuestionario a la familia. Etapa 2: prueba directa a quienes salieron positivos. Si las
dos pruebas fueran independientes (dado el estado real), el valor predictivo se calcula
multiplicando razones de verosimilitud. Pero si comparten error (ambas se ven afectadas por la
misma variable, p. ej. el sueno o la timidez), el segundo positivo agrega menos informacion.
Se simula una variable comun de error y se compara el VPP de la secuencia con el de independencia.
Prevalencia 4 %. Parametros supuestos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N, PREV = 300000, 0.04


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'peso del error compartido':>26} {'VPP etapa 1':>12} {'VPP tras 2 etapas':>19} {'VPP si independientes':>23}")
    print("=" * 84)
    for w in (0.0, 0.5, 0.9):
        tp1 = fp1 = tp2 = fp2 = 0
        for _ in range(N):
            caso = rng.random() < PREV
            comun = rng.gauss(0, 1)                                 # fuente de error compartida
            s = (1.6 if caso else 0.0) + w * comun
            e1 = s + math.sqrt(1 - w * w) * rng.gauss(0, 1)
            e2 = s + math.sqrt(1 - w * w) * rng.gauss(0, 1)
            pos1 = e1 > 1.2
            if pos1:
                tp1 += caso
                fp1 += not caso
                if e2 > 1.2:
                    tp2 += caso
                    fp2 += not caso
        vpp1 = tp1 / (tp1 + fp1)
        vpp2 = tp2 / max(tp2 + fp2, 1)
        # Referencia: independencia (w = 0) con los mismos cortes.
        sens = 1 - 0.5 * (1 + math.erf((1.2 - 1.6) / math.sqrt(2)))
        fpr = 1 - 0.5 * (1 + math.erf(1.2 / math.sqrt(2)))
        odds = (PREV / (1 - PREV)) * (sens / fpr) ** 2
        print(f"{w:26.1f} {vpp1:12.2f} {vpp2:19.2f} {odds / (1 + odds):23.2f}")
    print()
    print("Lectura: un segundo cribado mejora el valor predictivo, pero menos de lo que sugiere el calculo")
    print("independiente cuando las pruebas comparten error. Un cribado de dos etapas reduce derivaciones")
    print("innecesarias; el resultado sigue siendo 'riesgo', y la derivacion a evaluacion diagnostica la")
    print("hace un equipo habilitado, con consentimiento de la familia y apoyos mientras se espera.")


if __name__ == "__main__":
    main()
