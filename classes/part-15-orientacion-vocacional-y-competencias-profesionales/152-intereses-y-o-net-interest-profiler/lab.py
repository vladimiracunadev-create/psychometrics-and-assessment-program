"""Laboratorio 152 - Del perfil de intereses a ocupaciones: estabilidad del ranking.

Parte 1: lee la ficha de procedencia de `onet-riasec-sf` (adaptacion de un instrumento de la
herramienta oficial O*NET) y muestra licencia, cita y la obligacion de validacion pendiente.
Parte 2: con un mini-catalogo FICTICIO de 12 ocupaciones (perfiles RIASEC inventados, NO datos de
O*NET), se ordenan por la correlacion entre el perfil de la persona y el de la ocupacion. Se
perturba el perfil con el error de medida de una escala de 10 items y se mide la estabilidad del
"top 3" de ocupaciones.
"""
from __future__ import annotations

import pathlib
import random
import statistics
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import cargar  # noqa: E402

SEMILLA = 20260819
OCUPACIONES = {  # perfiles R I A S E C ficticios (escala 0-1), solo para ensenar el calculo
    "tecnico/a en mantencion": (0.9, 0.5, 0.1, 0.2, 0.3, 0.4),
    "laboratorista": (0.4, 0.9, 0.2, 0.2, 0.1, 0.5),
    "disenador/a grafico/a": (0.2, 0.3, 0.9, 0.3, 0.3, 0.2),
    "docente basico": (0.1, 0.3, 0.4, 0.9, 0.4, 0.3),
    "vendedor/a tecnico/a": (0.3, 0.3, 0.2, 0.5, 0.9, 0.4),
    "contador/a": (0.1, 0.4, 0.1, 0.2, 0.4, 0.9),
    "enfermero/a": (0.4, 0.6, 0.2, 0.9, 0.3, 0.4),
    "programador/a": (0.3, 0.8, 0.4, 0.2, 0.2, 0.5),
    "chef": (0.6, 0.3, 0.7, 0.4, 0.5, 0.3),
    "administrador/a": (0.2, 0.3, 0.2, 0.5, 0.8, 0.8),
    "arquitecto/a": (0.5, 0.6, 0.8, 0.3, 0.3, 0.3),
    "orientador/a": (0.1, 0.3, 0.4, 0.9, 0.3, 0.2),
}


def top3(perfil, ocup) -> tuple[str, ...]:
    pares = sorted(ocup, key=lambda o: -statistics.correlation(perfil, ocup[o]))
    return tuple(pares[:3])


def main() -> None:
    inst = cargar("onet-riasec-sf")
    p = inst.procedencia
    print(f"Instrumento: {inst.codigo} | licencia: {p.licencia.value}")
    print(f"Fuente: {p.fuente}")
    for k, v in p.notas.items():
        print(f"  nota [{k}]: {' '.join(str(v).split())[:150]}...")
    print("\nParte 2 - estabilidad del 'top 3' de ocupaciones ante el error de medida de 10 items por escala")
    rng = random.Random(SEMILLA)
    estables = coincide_dos = 0
    reps = 800
    for _ in range(reps):
        base = [rng.uniform(0, 1) for _ in range(6)]
        a = [b + rng.gauss(0, 0.20) for b in base]
        b2 = [b + rng.gauss(0, 0.20) for b in base]
        t1, t2 = top3(a, OCUPACIONES), top3(b2, OCUPACIONES)
        estables += t1[0] == t2[0]
        coincide_dos += len(set(t1) & set(t2)) >= 2
    print(f"  misma ocupacion en el 1.er lugar entre dos aplicaciones : {estables / reps:.1%}")
    print(f"  al menos 2 de 3 ocupaciones en comun                    : {coincide_dos / reps:.1%}")
    print()
    print("Lectura: el ranking exacto de ocupaciones es inestable; un listado de 'opciones a explorar' es mas")
    print("honesto que un 'ocupacion ideal'. La adaptacion usada aqui tiene una obligacion de validacion")
    print("pendiente declarada en su ficha: no se usa para decidir. Las ocupaciones son ficticias.")


if __name__ == "__main__":
    main()
