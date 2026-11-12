"""Laboratorio 079 - Una decision automatizada que se puede explicar y revisar.

Puntaje lineal transparente: suma ponderada de tres componentes con pesos DECLARADOS. Para
cada persona se emiten (a) la decision preliminar, (b) los motivos ordenados por contribucion,
(c) una marca de REVISION HUMANA obligatoria cuando la distancia al corte es menor que el
margen de error. Datos sinteticos; los pesos son un ejemplo y no tienen validez demostrada.
"""
from __future__ import annotations

import math

PESOS = {"prueba de razonamiento": 0.5, "muestra de trabajo": 0.35, "entrevista estructurada": 0.15}
CORTE = 60.0
MARGEN = 1.96 * 5.0 * math.sqrt(sum(p * p for p in PESOS.values())) * 1.0   # ETM supuesto 5 pts/componente

PERSONAS = {
    "persona A": {"prueba de razonamiento": 80, "muestra de trabajo": 70, "entrevista estructurada": 65},
    "persona B": {"prueba de razonamiento": 50, "muestra de trabajo": 70, "entrevista estructurada": 60},
    "persona C": {"prueba de razonamiento": 40, "muestra de trabajo": 45, "entrevista estructurada": 55},
}


def main() -> None:
    print(f"Corte = {CORTE:.0f} | margen de revision humana = ±{MARGEN:.1f}")
    print("=" * 74)
    for nombre, v in PERSONAS.items():
        contrib = {k: PESOS[k] * v[k] for k in PESOS}
        total = sum(contrib.values())
        decision = "avanza" if total >= CORTE else "no avanza"
        revision = abs(total - CORTE) <= MARGEN
        print(f"{nombre}: puntaje {total:.1f} -> {decision}"
              + ("  | REVISION HUMANA OBLIGATORIA" if revision else ""))
        for k, c in sorted(contrib.items(), key=lambda kv: -kv[1]):
            print(f"    {k:<26} aporta {c:5.1f} (peso {PESOS[k]:.2f} x {v[k]})")
    print()
    print("Lectura: un puntaje con pesos declarados permite explicar la decision y rebatirla. El")
    print("derecho a explicacion y a intervencion humana (que recoge la nueva normativa de datos")
    print("personales, a verificar en la fuente oficial) exige poder hacerlo. Un modelo opaco no")
    print("puede. El margen de revision traduce la incertidumbre de la clase 025 en una regla.")


if __name__ == "__main__":
    main()
