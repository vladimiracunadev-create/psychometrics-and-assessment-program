"""Laboratorio 076 - Inventario de datos de una evaluacion y minimizacion.

Dado el registro de una evaluacion, clasifica cada campo (identificador directo, cuasi-
identificador, dato sensible, resultado, tecnico) segun una taxonomia didactica y exige que
cada dato tenga FINALIDAD. Los campos sin finalidad se marcan para eliminar (minimizacion). La
taxonomia es una herramienta de estudio basada en categorias generales de la normativa de
proteccion de datos; NO es asesoria juridica ni reproduce el texto de la ley.
"""
from __future__ import annotations

CAMPOS = {
    # campo: (categoria, finalidad)
    "rut": ("identificador directo", "vincular con el expediente del colegio"),
    "nombre": ("identificador directo", "entregar el informe"),
    "fecha_nacimiento": ("cuasi-identificador", "elegir el baremo por edad"),
    "comuna": ("cuasi-identificador", ""),
    "diagnostico_previo": ("dato sensible", ""),
    "pertenencia_etnica": ("dato sensible", ""),
    "puntaje_bruto": ("resultado", "calcular el puntaje tipificado"),
    "tiempo_por_item": ("dato tecnico", "detectar respuestas sin esfuerzo"),
    "ip_origen": ("dato tecnico", ""),
}


def main() -> None:
    print(f"{'campo':<20} {'categoria':<24} {'finalidad':<42} accion")
    print("=" * 100)
    eliminar = 0
    for campo, (cat, fin) in CAMPOS.items():
        if not fin:
            accion = "ELIMINAR (sin finalidad)"
            eliminar += 1
        elif cat == "dato sensible":
            accion = "base reforzada + proteccion especial"
        elif cat == "identificador directo":
            accion = "separar del resultado (seudonimizar)"
        else:
            accion = "conservar"
        print(f"{campo:<20} {cat:<24} {fin or '-':<42} {accion}")
    print(f"\nCampos a eliminar por no tener finalidad: {eliminar} de {len(CAMPOS)}")
    print()
    print("Lectura: el principio de minimizacion pregunta, campo por campo, 'para que lo necesito'.")
    print("Los datos sensibles exigen condiciones reforzadas. La ley 21.719 reemplaza el regimen de la")
    print("19.628; su vigencia y detalle se verifican en la fuente oficial (bcn.cl) antes de aplicar.")


if __name__ == "__main__":
    main()
