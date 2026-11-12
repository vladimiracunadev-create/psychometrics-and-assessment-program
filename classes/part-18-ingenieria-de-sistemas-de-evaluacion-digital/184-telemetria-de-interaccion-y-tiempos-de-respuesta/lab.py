"""Laboratorio 184 - Telemetria minima para detectar respuestas descuidadas.

Cada persona produce, por item, un tiempo de respuesta. Un 10 % responde de forma descuidada
(tiempos muy cortos y poco variables). Se calculan tres indicadores por persona sin guardar el
registro crudo: mediana de tiempos, proporcion de respuestas rapidas (< 1.5 s) y coeficiente de
variacion. Con ellos se evalua la deteccion (sensibilidad, especificidad y AUC) y se ensena el
principio de minimizacion: se conservan los indicadores agregados y se descarta la telemetria
detallada. Datos sinteticos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, ITEMS = 2000, 40


def persona(descuidada: bool, rng: random.Random) -> list[float]:
    if descuidada:
        base = rng.uniform(1.0, 3.2)
        return [max(0.4, rng.gauss(base, base * 0.40)) for _ in range(ITEMS)]
    base = rng.uniform(1.6, 8.0)          # incluye lectores rapidos legitimos
    return [max(0.6, rng.gauss(base, base * 0.40)) for _ in range(ITEMS)]


def indicadores(t: list[float]) -> dict[str, float]:
    return {"mediana": statistics.median(t), "rapidas": sum(x < 1.5 for x in t) / len(t),
            "cv": statistics.pstdev(t) / statistics.fmean(t)}


def main() -> None:
    rng = random.Random(SEMILLA)
    datos = []
    for _ in range(N):
        d = rng.random() < 0.10
        datos.append((d, indicadores(persona(d, rng))))
    print(f"{'regla de marcado':<42} {'sensibilidad':>13} {'especificidad':>14} {'VPP':>6}")
    print("=" * 80)
    for nombre, f in (("mediana < 2 s", lambda ind: ind["mediana"] < 2.0),
                      ("mas de 50 % de respuestas rapidas", lambda ind: ind["rapidas"] > 0.5),
                      ("mediana < 2 s Y CV < 0.5", lambda ind: ind["mediana"] < 2.0 and ind["cv"] < 0.5)):
        tp = sum(d and f(i) for d, i in datos)
        fp = sum((not d) and f(i) for d, i in datos)
        pos = sum(d for d, _ in datos)
        print(f"{nombre:<42} {tp / pos:13.2f} {1 - fp / (N - pos):14.2f} {tp / max(tp + fp, 1):6.2f}")
    # AUC de la mediana (menor = mas descuidado)
    a = [i["mediana"] for d, i in datos if d]
    b = [i["mediana"] for d, i in datos if not d]
    auc = sum(x < y for x, y in zip(rng.choices(a, k=4000), rng.choices(b, k=4000), strict=True)) / 4000
    print(f"\nAUC de la mediana de tiempos = {auc:.2f}")
    print()
    print("Lectura: los tiempos separan bien a quienes responden sin leer, pero una persona lectora rapida o un")
    print("estudiante con experiencia puede ser marcado: el indicador alerta, no condena. Se conservan solo los")
    print("indicadores agregados y se descartan los tiempos por item (minimizacion, clase 076); el uso de")
    print("telemetria se informa en el consentimiento y no se usa para decidir sin revision humana.")


if __name__ == "__main__":
    main()
