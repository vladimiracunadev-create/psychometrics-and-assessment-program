"""Laboratorio 037 - Auditoria del catalogo ampliado de fichas.

Las directrices internacionales sobre uso de tests (ITC) piden distinguir lo documentado de lo
verificado y respetar las restricciones de uso y de derechos. Este laboratorio audita
catalogo/fichas.yaml con ese espiritu: cuantas fichas estan verificadas, cuantas son
propietarias (no redistribuibles), cuantas piden profesional cualificado, y si algun estado se
usa de forma inflada.
"""
from __future__ import annotations

import collections
import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]


def main() -> None:
    crudo = yaml.safe_load((RAIZ / "catalogo" / "fichas.yaml").read_text(encoding="utf-8"))
    base = crudo.get("defaults", {})
    fichas = [{**base, **f} for f in crudo["fichas"]]
    n = len(fichas)

    def cuenta(clave: str) -> collections.Counter:
        return collections.Counter(str(f.get(clave)) for f in fichas)

    print(f"Fichas: {n}")
    for clave in ("estado", "licencia", "verificado", "familia"):
        print(f"  {clave:<11}", dict(sorted(cuenta(clave).items())))
    clinicos = [f for f in fichas if "clinico" in f["uso"] and f["licencia"] == "propietaria"]
    print(f"\nPropietarias de uso clinico (exigen profesional habilitado): {len(clinicos)}")
    for f in clinicos[:6]:
        print(f"  - {f['nombre']}")
    print("  ...")
    inflados = [f["id"] for f in fichas if f["estado"] == "validado-uso-especifico" and not f.get("evidencia")]
    print(f"\nValidados sin evidencia declarada (debe ser 0): {len(inflados)}")
    print(f"Verificados contra fuente primaria: {sum(bool(f['verificado']) for f in fichas)} de {n}")
    print()
    print("Lectura: el catalogo distingue documentar, implementar y validar. Una ficha")
    print("bibliografica no es una prueba implementada, y un test implementado no esta validado.")


if __name__ == "__main__":
    main()
