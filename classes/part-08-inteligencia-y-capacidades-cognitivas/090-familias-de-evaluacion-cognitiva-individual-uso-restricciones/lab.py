"""Laboratorio 090 - Puntajes compuestos: fiabilidad de un indice y catalogo de restricciones.

Parte 1: la fiabilidad de un puntaje COMPUESTO (suma de subpruebas estandarizadas) es mayor
que la de cada subprueba si estas correlacionan entre si. Formula:
    rho_c = 1 - suma(sigma_i^2 * (1 - rho_i)) / sigma_c^2,   sigma_c^2 = suma de la matriz de covarianza
Parte 2: del catalogo ampliado (catalogo/fichas.yaml), lista las fichas de familia A (cognitivas)
con sus restricciones declaradas y si existe una alternativa abierta implementada o fichada.
Las baterias comerciales NO se reproducen: solo se documentan (licencia propietaria).
"""
from __future__ import annotations

import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]


def fiabilidad_compuesto(rhos: list[float], r_entre: float) -> float:
    k = len(rhos)
    var_c = k + k * (k - 1) * r_entre                 # subpruebas con DE = 1
    return 1 - sum(1 - r for r in rhos) / var_c


def main() -> None:
    print("Parte 1 - fiabilidad del compuesto (subpruebas con fiabilidad 0.80)")
    print(f"{'r entre subpruebas':>19} {'2 subpruebas':>13} {'4 subpruebas':>13} {'6 subpruebas':>13}")
    for r in (0.0, 0.3, 0.5):
        print(f"{r:19.1f} " + " ".join(f"{fiabilidad_compuesto([0.8] * k, r):13.3f}" for k in (2, 4, 6)))
    print("\nParte 2 - fichas de familia A (inteligencia y razonamiento)")
    crudo = yaml.safe_load((RAIZ / "catalogo" / "fichas.yaml").read_text(encoding="utf-8"))
    base = crudo.get("defaults", {})
    fichas = [{**base, **f} for f in crudo["fichas"] if f["familia"] == "A"]
    print(f"{'ficha':<52} {'licencia':<14} {'uso':<24}")
    for f in fichas[:12]:
        print(f"{f['nombre'][:50]:<52} {f['licencia']:<14} {','.join(f['uso']):<24}")
    print(f"... ({len(fichas)} fichas de familia A en total)")
    prop = [f for f in fichas if f["licencia"] == "propietaria"]
    print(f"\nPropietarias de uso clinico/educativo individual: {len(prop)}. Se estudian sus fundamentos y")
    print("se usan alternativas abiertas u originales para practicar; no se reproducen sus items ni claves.")
    print()
    print("Lectura: un indice compuesto es mas fiable que sus partes, pero la interpretacion de una")
    print("bateria individual (diagnostico, elegibilidad para apoyos) exige un profesional habilitado.")


if __name__ == "__main__":
    main()
