"""Laboratorio 167 - Escalas de sintomas: un cribado no diagnostica, y los items de seguridad no se promedian.

Parte 1: una escala de 9 items (0-3) de sintomas, sintetica. Con corte >= 10 se calcula, segun
la prevalencia real, cuantos "positivos" son verdaderos (VPP).
Parte 2: REGLA DE SEGURIDAD. El item 9 (de riesgo) se trata aparte: CUALQUIER respuesta > 0
dispara contacto humano inmediato, sin importar el puntaje total. Se verifica por simulacion que
la regla nunca deja pasar una respuesta de riesgo (propiedad que se prueba, no se supone).
Este laboratorio NO es una escala real ni un protocolo clinico: ilustra el diseno de software y las
tasas base. Los protocolos reales los definen profesionales de salud mental.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N = 100000


def clasifica(resp: list[int]) -> dict[str, bool]:
    total = sum(resp)
    return {"positivo_cribado": total >= 10, "alerta_seguridad": resp[8] > 0}


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'prevalencia':>12} {'positivos':>10} {'VPP':>6}")
    for prev in (0.02, 0.05, 0.10, 0.20):
        tp = fp = 0
        for _ in range(N // 4):
            caso = rng.random() < prev
            resp = [min(3, max(0, round(rng.gauss(1.7 if caso else 0.6, 0.9)))) for _ in range(9)]
            if clasifica(resp)["positivo_cribado"]:
                tp += caso
                fp += not caso
        print(f"{prev:12.0%} {tp + fp:10d} {tp / max(tp + fp, 1):6.2f}")
    # Propiedad de seguridad: ninguna respuesta de riesgo debe quedar sin alerta.
    fallas = 0
    for _ in range(N):
        resp = [rng.randint(0, 3) if rng.random() < 0.3 else 0 for _ in range(9)]
        if resp[8] > 0 and not clasifica(resp)["alerta_seguridad"]:
            fallas += 1
    print(f"\nRespuestas con item de riesgo > 0 sin alerta de seguridad, en {N} protocolos: {fallas} (debe ser 0)")
    print()
    print("Lectura: con prevalencias bajas, la mayoria de los positivos de un cribado son falsos positivos, asi")
    print("que 'positivo' significa 'conversar y evaluar', nunca 'tiene el trastorno'. La alerta de seguridad es")
    print("independiente del puntaje total y debe llevar a contacto humano inmediato segun un protocolo")
    print("(clase 168). Interpretar o aplicar escalas de sintomas clinicos exige un profesional competente.")


if __name__ == "__main__":
    main()
