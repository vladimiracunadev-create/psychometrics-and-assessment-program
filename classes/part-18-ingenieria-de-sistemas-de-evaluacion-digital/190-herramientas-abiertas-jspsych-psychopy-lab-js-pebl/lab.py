"""Laboratorio 190 - Evaluar un recurso abierto: deteccion de licencia y compatibilidad con MIT.

Antes de incorporar un recurso (libreria, banco de items, plataforma) hay que saber con que
licencia se distribuye. Este laboratorio implementa un detector simple de familia de licencia sobre
el TEXTO de un archivo LICENSE y una tabla de compatibilidad con un proyecto cuyo CODIGO es MIT. Se
prueba con los textos de licencia de ESTE repositorio. Los recursos del mundo real mencionados en la
clase (jsPsych, PsychoPy, lab.js, PEBL, Concerto, R psych/mirt/lavaan, semopy) se evaluan leyendo su
LICENSE en la fuente primaria y su mantenimiento: esa verificacion es manual y se anota en la ficha;
aqui no se afirma la licencia de ninguno.
"""
from __future__ import annotations

import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[3]

FIRMAS = [
    ("MIT", ["permission is hereby granted, free of charge"]),
    ("Apache-2.0", ["apache license", "version 2.0"]),
    ("GPL", ["gnu general public license"]),
    ("LGPL", ["gnu lesser general public license"]),
    ("BSD", ["redistribution and use in source and binary forms"]),
    ("CC BY-NC-SA", ["noncommercial", "sharealike"]),
    ("CC BY", ["creative commons", "attribution"]),
]

# Compatibilidad para INCORPORAR (o enlazar) en un proyecto cuyo codigo es MIT. Es una guia de
# estudio, no asesoria juridica: la decision final se consulta con un profesional.
COMPAT_MIT = {
    "MIT": "si (conservar el aviso de copyright)",
    "BSD": "si (conservar el aviso)",
    "Apache-2.0": "si (conservar avisos y NOTICE; cuidado con la clausula de patentes)",
    "LGPL": "depende: enlazar dinamicamente suele permitirse; copiar codigo, no",
    "GPL": "no sin relicenciar el conjunto: obligaciones copyleft",
    "CC BY": "adecuada para contenido, no para codigo",
    "CC BY-NC-SA": "no apta para codigo; el contenido tiene restriccion no comercial",
    "desconocida": "no incorporar hasta aclarar la licencia",
}


def detecta(texto: str) -> str:
    t = " ".join(texto.lower().split())
    for nombre, claves in FIRMAS:
        if all(k in t for k in claves):
            return nombre
    return "desconocida"


def main() -> None:
    archivos = ["LICENSE"]   # LICENSE-CONTENT.md y THIRD_PARTY_NOTICES.md son documentos explicativos, no textos de licencia
    print(f"{'archivo':<26} {'familia detectada':<18} compatibilidad con codigo MIT")
    print("=" * 96)
    for a in archivos:
        ruta = RAIZ / a
        fam = detecta(ruta.read_text(encoding="utf-8")) if ruta.exists() else "desconocida"
        print(f"{a:<26} {fam:<18} {COMPAT_MIT[fam]}")
    print("\nCasos de prueba del detector:")
    for nombre, texto in (("texto MIT", "Permission is hereby granted, free of charge, to any person ..."),
                          ("texto GPL", "GNU General Public License ... version 3"),
                          ("texto Apache", "Apache License Version 2.0, January 2004"),
                          ("CC BY-NC-SA", "Attribution-NonCommercial-ShareAlike 4.0"),
                          ("texto vacio", "")):
        print(f"  {nombre:<12} -> {detecta(texto)}")
    print()
    print("Lectura: el detector solo reconoce familias por frases tipicas: la licencia exacta y sus condiciones")
    print("se leen en el archivo. Una libreria 'abierta' puede tener licencia incompatible con tu proyecto, y un")
    print("banco de items puede tener condiciones propias (clase 102). Cada recurso adoptado queda registrado")
    print("con URL, version, licencia leida, fecha de revision y estado de mantenimiento.")


if __name__ == "__main__":
    main()
