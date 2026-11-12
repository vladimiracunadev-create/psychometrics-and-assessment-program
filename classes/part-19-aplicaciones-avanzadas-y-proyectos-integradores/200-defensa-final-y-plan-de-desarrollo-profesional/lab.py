"""Laboratorio 200 - Defensa final: panel de cobertura del programa y plan de desarrollo.

Lee `curriculum.yaml` y cuenta, por parte, las clases escritas y planificadas, y cuantas tienen
laboratorio ejecutable. Luego imprime una rubrica de defensa con criterios de logro y un plan de
desarrollo profesional en tres horizontes. El panel se calcula del repositorio real: si hay clases
planificadas, el panel las muestra (el programa no puede declararse completo sin estarlo).
"""
from __future__ import annotations

import collections
import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]

RUBRICA = [
    ("Fundamentos", "Explica error de medida, fiabilidad y validez como evidencia, no como propiedades del test"),
    ("Evidencia", "Disena un estudio de validacion con tamano, instrumentos y criterios fijados antes"),
    ("Equidad", "Detecta y discute sesgo y DIF sin concluir causas sin evidencia"),
    ("Uso responsable", "Distingue cribado, diagnostico y decision; declara limites y protege datos"),
    ("Comunicacion", "Redacta informes cualificados para familias, docentes y organizaciones"),
    ("Reproducibilidad", "Entrega codigo, semilla, datos sinteticos y registro de versiones"),
]
PLAN = [
    ("0-6 meses", "repetir los laboratorios con datos propios autorizados y leer las fuentes primarias de la bibliografia"),
    ("6-18 meses", "participar en un estudio real con supervision; cursar formacion en el instrumento que se vaya a usar"),
    ("18 meses en adelante", "especializarse (educacional, laboral, clinica) con la certificacion y supervision que exija la normativa"),
]


def main() -> None:
    d = yaml.safe_load((RAIZ / "curriculum.yaml").read_text(encoding="utf-8"))
    print(f"{'parte':<7} {'titulo':<52} {'escritas':>9} {'planificadas':>13} {'con lab':>8}")
    print("=" * 94)
    tot = collections.Counter()
    for p in d["temario"]:
        c = collections.Counter(x["estado"] for x in p["clases"])
        labs = sum((RAIZ / x["ruta"] / "lab.py").exists() for x in p["clases"])
        print(f"{p['id']:<7} {p['titulo'][:50]:<52} {c['escrita']:9d} {c['planificada']:13d} {labs:8d}")
        tot.update(c)
        tot["labs"] += labs
    print("-" * 94)
    print(f"{'TOTAL':<60} {tot['escrita']:9d} {tot['planificada']:13d} {tot['labs']:8d}")
    print("\nRubrica de defensa final (logrado / en proceso / no logrado, con evidencia):")
    for c, d_ in RUBRICA:
        print(f"  - {c:<17} {d_}")
    print("\nPlan de desarrollo profesional:")
    for h, t in PLAN:
        print(f"  {h:<22} {t}")
    print()
    print("Lectura: el panel sale del repositorio; si queda alguna clase planificada, se muestra. Completar el")
    print("programa no habilita a ejercer: la practica profesional exige formacion, supervision y las")
    print("autorizaciones que fije la normativa. La defensa evalua criterio y honestidad, no memoria.")


if __name__ == "__main__":
    main()
