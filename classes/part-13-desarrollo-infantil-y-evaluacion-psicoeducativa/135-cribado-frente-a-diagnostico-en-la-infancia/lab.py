"""Laboratorio 135 - Curva ROC de un cribado infantil y eleccion del punto de corte.

Un cribado produce un puntaje continuo. Ninos con la condicion: media 0.0 y DE 1.0 (puntaje mas
bajo = mas riesgo, escala invertida); ninos sin la condicion: media 1.5, DE 1.0. Prevalencia 5 %.
Para distintos cortes se calculan sensibilidad, especificidad, VPP, "ninos a derivar por cada 100
evaluados" y "numero necesario a derivar por caso verdadero". Tambien el AUC (aproximado por
pares). El corte "optimo" (Youden) no es el mismo que el corte aceptable segun la capacidad de la
red de derivacion.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N, PREV = 100000, 0.05


def main() -> None:
    rng = random.Random(SEMILLA)
    caso = [rng.gauss(0.0, 1.0) for _ in range(int(N * PREV))]
    sano = [rng.gauss(1.5, 1.0) for _ in range(int(N * (1 - PREV)))]
    print(f"{'corte (<=)':>10} {'sens.':>6} {'espec.':>7} {'VPP':>6} {'derivar x100':>13} {'derivados/caso':>15} {'Youden':>7}")
    print("=" * 72)
    mejor = (0.0, 0.0)
    for corte in (-0.5, 0.0, 0.25, 0.5, 0.75, 1.0, 1.5):
        tp = sum(x <= corte for x in caso)
        fp = sum(x <= corte for x in sano)
        sens, esp = tp / len(caso), 1 - fp / len(sano)
        vpp = tp / (tp + fp) if tp + fp else 0.0
        y = sens + esp - 1
        if y > mejor[0]:
            mejor = (y, corte)
        print(f"{corte:10.2f} {sens:6.2f} {esp:7.2f} {vpp:6.2f} {100 * (tp + fp) / N:13.1f} "
              f"{(tp + fp) / max(tp, 1):15.1f} {y:7.2f}")
    muestra = 4000
    a, b = rng.sample(caso, muestra), rng.sample(sano, muestra)
    auc = sum(x < y for x, y in zip(a, b, strict=True)) / muestra
    print(f"\nAUC aproximado = {auc:.2f}; corte de Youden = {mejor[1]:.2f}")
    print()
    print("Lectura: aun con un cribado razonable (AUC ~0.86) y 5 % de prevalencia, la mayoria de los")
    print("derivados no tiene la condicion (VPP bajo). Un cribado reparte la atencion: el corte se elige")
    print("segun la capacidad de evaluacion posterior y el costo de no detectar, y el resultado")
    print("positivo se llama 'riesgo', nunca 'diagnostico'. El diagnostico es un proceso profesional.")


if __name__ == "__main__":
    main()
