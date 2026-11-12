"""Laboratorio 197 - Proyecto: auditoria etica del propio catalogo.

Se audita `catalogo/fichas.yaml` y los instrumentos implementados con una lista de control:
  A. consistencia: el validador de fichas no reporta problemas,
  B. honestidad de estado: ninguna ficha dice 'validado-uso-especifico' sin evidencia,
  C. propiedad intelectual: ninguna ficha propietaria es redistribuible y ningun instrumento
     propietario contiene items,
  D. verificacion: cuantas fichas siguen sin contrastarse con fuente primaria (se informa, no se oculta),
  E. instrumentos propios: los de autoria propia declaran 'sin_validar' en sus notas.
El resultado es un informe de hallazgos: la auditoria sirve si puede fallar y se muestra el hallazgo.
"""
from __future__ import annotations

import collections
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.fichas import cargar_fichas, validar_fichas  # noqa: E402
from psychometrics.motor import Licencia, catalogo  # noqa: E402


def main() -> None:
    fichas = cargar_fichas()
    ins = catalogo()
    codigos = {i.codigo for i in ins}
    hallazgos = []
    problemas = validar_fichas(fichas, codigos)
    hallazgos.append(("A consistencia de fichas", not problemas, f"{len(problemas)} problemas"))
    sin_ev = [f["id"] for f in fichas if f["estado"] == "validado-uso-especifico" and not f.get("evidencia")]
    hallazgos.append(("B validado sin evidencia", not sin_ev, f"{len(sin_ev)} fichas"))
    prop_redis = [f["id"] for f in fichas if f["licencia"] == "propietaria" and f.get("redistribuible") == "si"]
    prop_items = [i.codigo for i in ins if i.procedencia.licencia == Licencia.PROPIETARIA and i.items]
    hallazgos.append(("C propietarias redistribuibles o con items", not prop_redis and not prop_items,
                      f"{len(prop_redis)} fichas, {len(prop_items)} instrumentos"))
    propios = [i for i in ins if i.procedencia.licencia.value == "autoria-propia"]
    sin_marca = [i.codigo for i in propios if "sin_validar" not in (i.procedencia.notas or {})]
    hallazgos.append(("E propios sin marca 'sin_validar'", not sin_marca, f"{sin_marca or 'ninguno'}"))
    print(f"{'control':<46} {'resultado':<10} detalle")
    print("=" * 84)
    for n, ok, det in hallazgos:
        print(f"{n:<46} {'cumple' if ok else 'FALLA':<10} {det}")
    ver = collections.Counter(f["verificado"] for f in fichas)
    est = collections.Counter(f["estado"] for f in fichas)
    print(f"\nD verificacion: {ver[True]} fichas verificadas y {ver[False]} SIN verificar de {len(fichas)} (hallazgo informado, no corregible por script)")
    print(f"Estados: {dict(est)}")
    print("\nHallazgo principal: el catalogo es honesto sobre lo que NO sabe; el riesgo principal es que alguien lea")
    print("una ficha documentada como si fuera un instrumento validado. Mitigacion: estados separados y el campo")
    print("'verificado'. Prioridad siguiente: contrastar fichas contra fuente primaria, de a una familia por vez.")


if __name__ == "__main__":
    main()
