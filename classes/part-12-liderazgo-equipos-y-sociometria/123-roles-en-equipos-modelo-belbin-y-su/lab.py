"""Laboratorio 123 - Roles de equipo: el riesgo de hallazgos por azar.

Se simula un estudio donde NO existe ningun efecto de la composicion de roles. 40 equipos,
9 roles (presente/ausente segun el perfil de sus integrantes) y un desempeno de equipo
aleatorio. Para cada rol se compara el desempeno de equipos con y sin ese rol (prueba z
aproximada). Se repite el estudio 2 000 veces y se cuentan:
  - estudios con al menos un rol "significativo" (p < .05) -> falsos positivos por comparaciones multiples,
  - el mismo conteo con la correccion de Bonferroni.
El modelo de roles de Belbin es propietario y su evidencia de validez es debatida; aqui solo
se usa la estructura "9 roles" como ejemplo estadistico.
"""
from __future__ import annotations

import math
import random
import statistics
from statistics import NormalDist

SEMILLA = 20260819
EQUIPOS, ROLES, REPS = 40, 9, 2000
ND = NormalDist()


def p_dos_colas(a: list[float], b: list[float]) -> float:
    if len(a) < 3 or len(b) < 3:
        return 1.0
    se = math.sqrt(statistics.variance(a) / len(a) + statistics.variance(b) / len(b))
    z = (statistics.fmean(a) - statistics.fmean(b)) / se
    return 2 * (1 - ND.cdf(abs(z)))


def main() -> None:
    rng = random.Random(SEMILLA)
    con_hallazgo = con_hallazgo_bonf = 0
    for _ in range(REPS):
        desempeno = [rng.gauss(0, 1) for _ in range(EQUIPOS)]
        sig = bonf = False
        for _ in range(ROLES):
            presente = [rng.random() < 0.5 for _ in range(EQUIPOS)]
            a = [d for d, p in zip(desempeno, presente, strict=True) if p]
            b = [d for d, p in zip(desempeno, presente, strict=True) if not p]
            p = p_dos_colas(a, b)
            sig |= p < 0.05
            bonf |= p < 0.05 / ROLES
        con_hallazgo += sig
        con_hallazgo_bonf += bonf
    print(f"Equipos por estudio: {EQUIPOS}; roles evaluados: {ROLES}; estudios simulados: {REPS}")
    print(f"Sin ningun efecto real, estudios con >= 1 rol 'significativo' (p < .05): {con_hallazgo / REPS:.1%}")
    print(f"  esperado teorico 1 - 0.95^9 = {1 - 0.95 ** 9:.1%} (el excedente viene de la aproximacion normal con muestras chicas)")
    print(f"Con correccion de Bonferroni (p < .05/9): {con_hallazgo_bonf / REPS:.1%}")
    print()
    print("Lectura: al probar 9 roles, cuatro de cada diez estudios 'encuentran' un rol decisivo")
    print("aunque no exista ningun efecto. Un modelo de roles necesita hipotesis previas, replicacion y")
    print("correccion por comparaciones multiples. 'Equipos equilibrados' es una idea plausible, no")
    print("una consecuencia demostrada de un test; el modelo no debe usarse para decidir sobre personas.")


if __name__ == "__main__":
    main()
