"""Laboratorio 194 - Proyecto: informe para familias y docentes con revisor de lenguaje.

Un generador arma el informe a partir de una banda de resultado (con error de medida) y un revisor
verifica reglas: (1) sin etiquetas diagnosticas, (2) sin lenguaje deterministico, (3) incluye la
incertidumbre, (4) incluye recomendaciones accionables, (5) declara que no es diagnostico. Se prueba
con un informe correcto y con uno que incumple las reglas. Datos ficticios.
"""
from __future__ import annotations

import re

ETIQUETAS = ["dislexia", "tdah", "autismo", "discapacidad intelectual", "retrasado", "problema de aprendizaje", "padece"]
DETERMINISTAS = ["siempre", "nunca", "jamas", "no podra", "incapaz", "esta destinado"]


def informe(nombre: str, lectura: float, ee: float, curso: str) -> str:
    li, ls = lectura - 1.96 * ee, lectura + 1.96 * ee
    return (f"Informe de cribado de lectura de {nombre} ({curso}). En esta aplicacion, el rendimiento estuvo cerca "
            f"de {lectura:.0f} puntos, con un intervalo razonable entre {li:.0f} y {ls:.0f}, por lo que conviene "
            f"observar el progreso en otra medicion. Sugerimos: leer 10 minutos al dia en voz alta con apoyo, y "
            f"revisar el avance en cuatro semanas. Este informe describe una aplicacion puntual y no es un "
            f"diagnostico; cualquier decision requiere una evaluacion integral.")


MALO = "Pedro padece dislexia y siempre tendra problemas de lectura. Es incapaz de mejorar. Puntaje 38."


def revisa(texto: str) -> dict[str, bool]:
    t = texto.lower()
    return {"sin etiquetas diagnosticas": not any(e in t for e in ETIQUETAS),
            "sin lenguaje deterministico": not any(re.search(rf"\b{d}\b", t) for d in DETERMINISTAS),
            "incluye incertidumbre": "intervalo" in t,
            "incluye recomendaciones": "sugerimos" in t or "recomendamos" in t,
            "declara que no es diagnostico": "no es un diagnostico" in t or "no es diagnostico" in t}


def main() -> None:
    for nombre, texto in (("Informe generado", informe("Ana", 52, 4.0, "3.o basico")), ("Informe de contraejemplo", MALO)):
        r = revisa(texto)
        print(f"{nombre}: {sum(r.values())}/{len(r)} reglas")
        for k, v in r.items():
            print(f"   [{'ok' if v else 'FALLA'}] {k}")
    print("\nTexto del informe generado:\n  " + informe("Ana", 52, 4.0, "3.o basico")[:220] + "...")
    print()
    print("Lectura: la comunicacion a familias es una intervencion: una etiqueta o un numero sin contexto puede")
    print("fijar expectativas y danar. El informe describe lo observado, incluye la incertidumbre, propone pasos y")
    print("aclara su alcance. El revisor automatico detecta forma; la revision de un profesional evalua el fondo.")


if __name__ == "__main__":
    main()
