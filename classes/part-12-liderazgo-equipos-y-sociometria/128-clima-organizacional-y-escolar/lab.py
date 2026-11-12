"""Laboratorio 128 - Encuesta de clima: agregacion, ICC y proteccion del anonimato.

40 cursos/equipos de tamano variable (3 a 40 personas) responden una escala de clima (1-5) y
una pregunta delicada. Se calcula:
  - ICC(1) y ICC(2) con tamanos desiguales (media armonica),
  - la regla de supresion: no se reportan resultados de grupos con menos de 5 respuestas (un
    umbral habitual de anonimato; se declara y se ajusta segun el contexto),
  - cuantos grupos quedan suprimidos y cuanta informacion se pierde.
Datos sinteticos.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
GRUPOS, MIN_RESP = 40, 5


def main() -> None:
    rng = random.Random(SEMILLA)
    tamanos = [rng.choice([3, 4, 5, 6, 8, 10, 15, 25, 40]) for _ in range(GRUPOS)]
    grupos = []
    for n in tamanos:
        base = rng.gauss(3.3, 0.35)
        grupos.append([max(1.0, min(5.0, round(base + rng.gauss(0, 0.9)))) for _ in range(n)])
    k = len(grupos)
    n_tot = sum(tamanos)
    gm = statistics.fmean(v for g in grupos for v in g)
    ssb = sum(len(g) * (statistics.fmean(g) - gm) ** 2 for g in grupos)
    ssw = sum((v - statistics.fmean(g)) ** 2 for g in grupos for v in g)
    msb, msw = ssb / (k - 1), ssw / (n_tot - k)
    n0 = (n_tot - sum(n * n for n in tamanos) / n_tot) / (k - 1)
    icc1 = (msb - msw) / (msb + (n0 - 1) * msw)
    nh = k / sum(1 / n for n in tamanos)                       # media armonica
    icc2 = (msb - msw) / msb
    print(f"Grupos: {k}; personas: {n_tot}; tamano medio armonico = {nh:.1f}")
    print(f"ICC(1) = {icc1:.3f} (varianza del clima entre grupos) | ICC(2) = {icc2:.3f} (fiabilidad del promedio)")
    suprimidos = [n for n in tamanos if n < MIN_RESP]
    print(f"\nGrupos con menos de {MIN_RESP} respuestas (resultados NO se reportan): {len(suprimidos)} de {k}")
    print(f"Personas en grupos suprimidos: {sum(suprimidos)} ({sum(suprimidos) / n_tot:.1%} de las respuestas)")
    print("Para esos grupos se informa solo el resultado agregado a un nivel superior.")
    print()
    print("Lectura: el clima es un constructo de GRUPO: solo se interpreta si hay diferencias entre")
    print("grupos (ICC) y fiabilidad del promedio. Los grupos pequenos se suprimen para proteger a")
    print("quienes respondieron; el umbral se decide con criterios de privacidad (parte 07), no solo")
    print("estadisticos. Reportar 'clima' de un equipo de 3 personas expone a sus integrantes.")


if __name__ == "__main__":
    main()
