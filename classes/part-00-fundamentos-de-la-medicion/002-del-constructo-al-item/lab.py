"""Laboratorio 002 - Auditoria automatica de redaccion de items.

Revisa los items del catalogo contra los defectos que un programa SI puede
detectar. Los que exigen criterio humano (deseabilidad social, ambiguedad
semantica) quedan fuera a proposito y se declaran al final.
"""
from __future__ import annotations

import re
import sys

sys.path.insert(0, "src")

from psychometrics.motor import catalogo  # noqa: E402

LARGO_MAXIMO = 90  # caracteres; por encima, la carga de lectura sube

# Conjunciones que suelen indicar dos afirmaciones en un mismo item.
DOBLE_CANON = re.compile(r"\b(y tambien|y ademas|pero tambien|asi como)\b", re.I)

NEGACIONES = re.compile(r"\b(no|nunca|nadie|ni|jamas|tampoco|sin)\b", re.I)


def audita(texto: str) -> list[str]:
    problemas = []
    if len(texto) > LARGO_MAXIMO:
        problemas.append(f"largo ({len(texto)} car.)")
    if DOBLE_CANON.search(texto):
        problemas.append("posible doble canon")
    if len(NEGACIONES.findall(texto)) >= 2:
        problemas.append("negaciones acumuladas")
    return problemas


def main() -> None:
    print("Auditoria de redaccion sobre el catalogo completo")
    print("=" * 72)
    total = marcados = 0
    for ins in catalogo():
        hallazgos = []
        for item in ins.items:
            total += 1
            texto = item.texto.get("es", "")
            if problemas := audita(texto):
                marcados += 1
                hallazgos.append((item.id, texto, problemas))
        estado = f"{len(hallazgos)} marcados" if hallazgos else "sin hallazgos"
        print(f"\n{ins.codigo}  ({len(ins.items)} items) - {estado}")
        for iid, texto, problemas in hallazgos:
            print(f"   {iid}  {', '.join(problemas)}")
            print(f"        {texto}")

    print()
    print("=" * 72)
    print(f"{marcados} de {total} items marcados "
          f"({marcados / total:.1%})" if total else "sin items")
    print()
    print("Lo que esta auditoria NO puede ver")
    print("  - deseabilidad social: exige saber que respuesta queda bien")
    print("  - ambiguedad de frecuencia: exige entender el significado")
    print("  - deficiencia del dominio: exige la tabla de especificaciones")
    print("  Esos tres requieren juicio experto. Ver parte 03, clase 17.")


if __name__ == "__main__":
    main()
