"""Laboratorio 047 - Analisis de distractores en items de opcion multiple.

Se simulan 1.200 personas respondiendo 6 items de 4 opciones (A-D). Cada item tiene una clave y tres
distractores de calidad distinta (uno plausible, uno debil y uno que nadie elige o que atrae a los
mejores). Para cada item se calcula la proporcion que elige cada opcion en tres grupos de habilidad
(bajo, medio, alto). Un buen distractor lo elige mas el grupo bajo que el alto; la clave, al reves.
Se marcan: distractores no funcionales (< 5 %), distractores con discriminacion positiva y claves
mal asignadas. Datos sinteticos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
N = 1200
ITEMS = {
    "q1": {"clave": "B", "atractivo": {"A": 1.0, "C": 0.8, "D": 0.6}},       # bueno
    "q2": {"clave": "C", "atractivo": {"A": 1.0, "B": 0.05, "D": 0.7}},      # un distractor casi inutil
    "q3": {"clave": "A", "atractivo": {"B": 1.0, "C": 0.9, "D": 0.8}},       # bueno
    "q4": {"clave": "D", "atractivo": {"A": 0.9, "B": 0.9, "C": 0.9}},       # clave dificil
    "q5": {"clave": "B", "atractivo": {"A": 0.8, "C": 0.7, "D": 0.6}},       # bueno
    "q6": {"clave": "A", "atractivo": {"B": 0.9, "C": 0.8, "D": -1.0}},      # D atrae a los mejores
}
DIF = {"q1": -0.5, "q2": 0.0, "q3": -1.0, "q4": 1.5, "q5": 0.3, "q6": 0.0}


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def responde(theta: float, item: str, rng: random.Random) -> str:
    cfg = ITEMS[item]
    if rng.random() < logistica(1.4 * (theta - DIF[item])):
        return cfg["clave"]
    pesos = {op: math.exp(-a * theta * 0.6) * abs(a) if a != 0 else 0.0 for op, a in cfg["atractivo"].items()}
    if item == "q6":
        pesos["D"] = math.exp(0.8 * theta)               # el distractor D lo eligen los de habilidad alta
    ops, w = zip(*pesos.items(), strict=True)
    return rng.choices(ops, weights=[max(x, 1e-6) for x in w])[0]


def main() -> None:
    rng = random.Random(SEMILLA)
    theta = [rng.gauss(0, 1) for _ in range(N)]
    orden = sorted(range(N), key=lambda i: theta[i])
    grupos = {"bajo": orden[: N // 3], "medio": orden[N // 3: 2 * N // 3], "alto": orden[2 * N // 3:]}
    resp = {q: [responde(theta[i], q, rng) for i in range(N)] for q in ITEMS}
    for q, cfg in ITEMS.items():
        print(f"\n{q} (clave {cfg['clave']}): proporcion que elige cada opcion  [bajo / medio / alto]")
        hallazgos = []
        for op in "ABCD":
            p = {g: sum(resp[q][i] == op for i in idx) / len(idx) for g, idx in grupos.items()}
            total = sum(resp[q][i] == op for i in range(N)) / N
            marca = "  <- clave" if op == cfg["clave"] else ""
            print(f"   {op}: {p['bajo']:.2f} / {p['medio']:.2f} / {p['alto']:.2f}  (total {total:.2f}){marca}")
            if op != cfg["clave"]:
                if total < 0.05:
                    hallazgos.append(f"distractor {op} no funcional")
                elif p["alto"] > p["bajo"]:
                    hallazgos.append(f"distractor {op} atrae a los mejores: revisar")
            elif p["alto"] <= p["bajo"]:
                hallazgos.append(f"la clave {op} no discrimina: revisar la clave")
        print("   hallazgos:", "; ".join(hallazgos) if hallazgos else "ninguno")
    print()
    print("Lectura: un distractor util atrae mas al grupo bajo; uno que casi nadie elige no aporta; uno que atrae a")
    print("los mejores suele indicar una clave discutible o un enunciado ambiguo. El analisis de distractores")
    print("complementa el indice de dificultad y de discriminacion (clase 010). Datos sinteticos.")


if __name__ == "__main__":
    main()
