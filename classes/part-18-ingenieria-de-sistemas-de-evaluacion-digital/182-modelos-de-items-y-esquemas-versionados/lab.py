"""Laboratorio 182 - Un esquema estricto rechaza los errores antes de puntuar.

Se declaran cinco instrumentos DEFECTUOSOS (clave con tilde, licencia desconocida, items con id
repetido, escala sin items y propietaria con items) y se muestra el error con que el cargador los
rechaza. Despues se comprueba la politica de versiones: una comparacion de versiones semanticas
decide si un cambio es compatible. Es una prueba de que "fallar pronto y ruidosamente" protege a
las personas de un informe plausible pero equivocado.
"""
from __future__ import annotations

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import InstrumentoInvalido, cargar_desde_texto  # noqa: E402

BASE = """
codigo: {cod}
version: "0.1.0"
nombre: {{es: Prueba}}
descripcion: {{es: Prueba}}
tipo_respuesta: likert
procedencia: {{autores: x, anio: 2026, fuente: https://example.org, licencia: {lic}}}
opciones: [{{valor: 1, etiqueta: {{es: a}}}}, {{valor: 2, etiqueta: {{es: b}}}}]
escalas: [{escalas}]
items: [{items}]
"""

CASOS = {
    "licencia desconocida": dict(cod="c1", lic="inventada", escalas="{codigo: A, nombre: {es: A}}",
                                 items="{id: i1, escala: A, clave: 1, texto: {es: x}}"),
    "item con id repetido": dict(cod="c2", lic="autoria-propia", escalas="{codigo: A, nombre: {es: A}}",
                                 items="{id: i1, escala: A, clave: 1, texto: {es: x}}, {id: i1, escala: A, clave: 1, texto: {es: y}}"),
    "item en escala inexistente": dict(cod="c3", lic="autoria-propia", escalas="{codigo: A, nombre: {es: A}}",
                                       items="{id: i1, escala: Z, clave: 1, texto: {es: x}}"),
    "escala sin items": dict(cod="c4", lic="autoria-propia", escalas="{codigo: A, nombre: {es: A}}, {codigo: B, nombre: {es: B}}",
                             items="{id: i1, escala: A, clave: 1, texto: {es: x}}"),
    "propietaria con items": dict(cod="c5", lic="propietaria", escalas="{codigo: A, nombre: {es: A}}",
                                  items="{id: i1, escala: A, clave: 1, texto: {es: x}}"),
}


def version(v: str) -> tuple[int, int, int]:
    a, b, c = v.split(".")
    return int(a), int(b), int(c)


def compatible(antigua: str, nueva: str) -> str:
    a, n = version(antigua), version(nueva)
    if n[0] != a[0]:
        return "ruptura: cambia la version mayor (puntajes no comparables)"
    if n[1] != a[1]:
        return "cambio de contenido o puntuacion: documentar y recalcular"
    return "correccion menor: comparable"


def main() -> None:
    rechazados = 0
    for nombre, kw in CASOS.items():
        try:
            cargar_desde_texto(BASE.format(**kw), kw["cod"])
            print(f"[ACEPTADO ] {nombre}")
        except InstrumentoInvalido as e:
            rechazados += 1
            print(f"[rechazado] {nombre}: {e.errores[0][:90]}")
    print(f"\nDefectuosos rechazados: {rechazados} de {len(CASOS)}")
    print("\nPolitica de versiones (semver aplicado a instrumentos):")
    for a, b in (("1.2.0", "1.2.3"), ("1.2.0", "1.3.0"), ("1.2.0", "2.0.0")):
        print(f"  {a} -> {b}: {compatible(a, b)}")
    print()
    print("Lectura: un esquema estricto convierte errores de datos en errores inmediatos. La version de un")
    print("instrumento forma parte del resultado (el motor la registra): reportar un puntaje sin su version")
    print("impide reproducirlo. Cambiar el texto de un item es cambiar el instrumento.")


if __name__ == "__main__":
    main()
