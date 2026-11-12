"""Laboratorio 169 - Cribado universal en una escuela: criterio relativo frente a criterio absoluto.

Informe docente (escala 0-20 de dificultades) para 6 cursos. Dos reglas para "marcar" a
estudiantes:
  RELATIVA: el 10 % mas alto de la escuela;
  ABSOLUTA: puntaje >= 12 (punto de corte fijado por un estudio, supuesto).
Los cursos difieren en su nivel real de dificultades (el curso 3 tiene un problema de clima). Se
muestra que una regla relativa marca siempre a alguien (aunque nadie necesite apoyo) y reparte
las alertas de forma distinta, y que la regla absoluta revela diferencias reales entre cursos.
Datos sinteticos.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
POR_CURSO = 30
MEDIAS = [4.0, 4.5, 8.0, 4.0, 3.5, 4.5]            # el curso 3 tiene dificultades mayores
CORTE_ABS = 12


def main() -> None:
    rng = random.Random(SEMILLA)
    puntajes = []
    for c, m in enumerate(MEDIAS):
        for _ in range(POR_CURSO):
            puntajes.append((c + 1, max(0, min(20, round(rng.gauss(m, 3.0))))))
    todos = sorted(p for _, p in puntajes)
    corte_rel = todos[int(0.90 * len(todos))]
    print(f"Corte relativo (percentil 90 de la escuela) = {corte_rel}; corte absoluto = {CORTE_ABS}")
    print(f"{'curso':>5} {'media':>6} {'marcados (relativa)':>20} {'marcados (absoluta)':>20}")
    for c in range(1, 7):
        sub = [p for k, p in puntajes if k == c]
        rel = sum(p >= corte_rel for p in sub)
        absol = sum(p >= CORTE_ABS for p in sub)
        print(f"{c:5d} {sum(sub) / len(sub):6.1f} {rel:20d} {absol:20d}")
    print(f"\nTotal marcados: relativa = {sum(p >= corte_rel for _, p in puntajes)}; "
          f"absoluta = {sum(p >= CORTE_ABS for _, p in puntajes)}")
    print()
    print("Lectura: la regla relativa marca alrededor de 10 % aunque la escuela este muy bien (aqui 15 de las 23")
    print("alertas caen en el curso 3, pero con cursos iguales marcaria igual); la absoluta depende de un corte")
    print("bien fundamentado y ve la diferencia real. Un cribado")
    print("universal informa tambien a nivel de curso (clima, convivencia): un resultado de curso puede apuntar a")
    print("una intervencion de aula, no a 'estudiantes problema'. Los resultados individuales se manejan con")
    print("confidencialidad y apoyo, con consentimiento y protocolo de derivacion (clase 168).")


if __name__ == "__main__":
    main()
