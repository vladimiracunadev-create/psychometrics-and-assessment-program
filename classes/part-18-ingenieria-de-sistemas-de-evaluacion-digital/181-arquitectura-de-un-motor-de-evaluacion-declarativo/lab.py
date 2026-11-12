"""Laboratorio 181 - Un instrumento es DATO: agregar un test sin tocar el codigo.

Se carga el catalogo real y se resume su estructura (tipo de respuesta, escalas, items, proporcion
de invertidos). Luego se declara un instrumento NUEVO de tres items como texto YAML, se carga con
`cargar_desde_texto` y se puntua con el mismo motor, sin modificar ninguna linea de Python. Es la
decision arquitectonica central del repositorio: separar el catalogo, el motor de administracion,
el de puntuacion y los datos normativos.
"""
from __future__ import annotations

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import Respuesta, cargar_desde_texto, catalogo, puntuar  # noqa: E402

YAML_NUEVO = """
codigo: demo-mini
version: "0.1.0"
nombre: {es: Demostracion de tres items}
descripcion: {es: Instrumento minimo para ensenar el motor. No mide nada real.}
tipo_respuesta: likert
ipsativo: false
procedencia:
  autores: psychometrics-and-assessment-program (demostracion)
  anio: 2026
  fuente: https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program
  licencia: autoria-propia
  notas: {estado: "SIN VALIDAR. Demostracion tecnica, no usar para decidir sobre personas."}
opciones:
  - {valor: 1, etiqueta: {es: En desacuerdo}}
  - {valor: 2, etiqueta: {es: Neutral}}
  - {valor: 3, etiqueta: {es: De acuerdo}}
escalas:
  - {codigo: A, nombre: {es: Escala A}}
items:
  - {id: d1, escala: A, clave: 1, texto: {es: Me gusta organizar mis tareas.}}
  - {id: d2, escala: A, clave: -1, texto: {es: Dejo todo para el ultimo minuto.}}
  - {id: d3, escala: A, clave: 1, texto: {es: Reviso mi trabajo antes de entregarlo.}}
"""


def main() -> None:
    print(f"{'instrumento':<20} {'tipo':<8} {'escalas':>8} {'items':>6} {'invertidos':>11} {'licencia':<22}")
    print("=" * 80)
    for i in catalogo():
        inv = sum(it.clave == -1 for it in i.items) / len(i.items)
        print(f"{i.codigo:<20} {i.tipo_respuesta.value:<8} {len(i.escalas):8d} {len(i.items):6d} "
              f"{inv:11.0%} {i.procedencia.licencia.value:<22}")
    nuevo = cargar_desde_texto(YAML_NUEVO, "demo-mini")
    res = puntuar(nuevo, [Respuesta("d1", 3), Respuesta("d2", 1), Respuesta("d3", 3)])
    print(f"\nInstrumento nuevo declarado como texto: {nuevo.codigo} ({len(nuevo.items)} items)")
    print(f"  respuestas (3, 1, 3) con el item 2 invertido -> media de la escala A = {res['A'].media_item}")
    print()
    print("Lectura: agregar un test es escribir un archivo de datos validado, no programar. Esa decision")
    print("reduce errores (el cargador rechaza lo mal declarado) y permite que un especialista contribuya")
    print("sin tocar Python. Cada capa tiene su responsabilidad y sus pruebas.")


if __name__ == "__main__":
    main()
