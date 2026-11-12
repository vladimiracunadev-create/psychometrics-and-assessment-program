"""Laboratorio 155 - Evidencia acumulada sobre una competencia: actualizacion bayesiana.

Una competencia tiene 3 niveles latentes (basico, intermedio, avanzado). Cada tarea de
evaluacion se resuelve "bien" con probabilidades dependientes del nivel (0.30, 0.60, 0.90; son
SUPUESTOS del laboratorio). Con una distribucion previa uniforme, se actualiza la probabilidad de
cada nivel tras observar 1 a 8 tareas, para un estudiante simulado de nivel intermedio. Se muestra:
  - la distribucion posterior tras cada tarea,
  - cuantas tareas hacen falta, en promedio, para que un nivel supere 90 % de probabilidad,
  - la proporcion de estudiantes que quedan clasificados en un nivel equivocado con ese criterio.
Un enfoque tipo "diseno centrado en la evidencia": la conclusion depende de cuanta evidencia hay.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
P_BIEN = {"basico": 0.30, "intermedio": 0.60, "avanzado": 0.90}
NIVELES = list(P_BIEN)


def actualiza(post: dict[str, float], bien: bool) -> dict[str, float]:
    nuevo = {n: post[n] * (P_BIEN[n] if bien else 1 - P_BIEN[n]) for n in NIVELES}
    s = sum(nuevo.values())
    return {n: v / s for n, v in nuevo.items()}


def main() -> None:
    rng = random.Random(SEMILLA)
    post = dict.fromkeys(NIVELES, 1 / 3)
    print("Estudiante simulado de nivel INTERMEDIO: posterior tras cada tarea")
    print(f"{'tareas':>6} {'resultado':>10} " + " ".join(f"{n:>11}" for n in NIVELES))
    for t in range(1, 9):
        bien = rng.random() < P_BIEN["intermedio"]
        post = actualiza(post, bien)
        print(f"{t:6d} {'bien' if bien else 'mal':>10} " + " ".join(f"{post[n]:11.2f}" for n in NIVELES))

    total, tareas_media, errores, sin_decision = 3000, [], 0, 0
    for _ in range(total):
        real = rng.choice(NIVELES)
        post = dict.fromkeys(NIVELES, 1 / 3)
        decidido = None
        for t in range(1, 21):
            post = actualiza(post, rng.random() < P_BIEN[real])
            mejor = max(post, key=post.get)
            if post[mejor] >= 0.90:
                decidido = (mejor, t)
                break
        if decidido is None:
            sin_decision += 1
        else:
            tareas_media.append(decidido[1])
            errores += decidido[0] != real
    print(f"\nCriterio: decidir cuando un nivel supera 90 % (hasta 20 tareas), {total} estudiantes")
    print(f"  tareas necesarias en promedio: {sum(tareas_media) / len(tareas_media):.1f}")
    print(f"  clasificados en un nivel equivocado: {errores / len(tareas_media):.1%}")
    print(f"  sin decision tras 20 tareas: {sin_decision / total:.1%}")
    print()
    print("Lectura: un 90 % de probabilidad posterior no es un 90 % de acierto garantizado (depende del")
    print("modelo supuesto). Con tareas poco discriminantes (0.60 vs 0.30) hacen falta muchas tareas para")
    print("separar niveles contiguos: las 'insignias' de competencias exigen evidencia suficiente y")
    print("declarar el criterio. Las competencias transversales se evidencian en situaciones, no en un cuestionario.")


if __name__ == "__main__":
    main()
