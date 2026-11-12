"""Laboratorio 084 - Legibilidad de instrucciones: indice de Szigriszt-Pazos (INFLESZ).

    IFSZ = 206.835 - 62.3 * (silabas / palabras) - (palabras / frases)
Se aplica a tres versiones de una misma instruccion y a una instruccion enrevesada, con un
contador de silabas heuristico (aproximado: no maneja todos los diptongos ni hiatos). Sirve
para decidir cual redaccion es mas accesible, no para fijar la dificultad cognitiva.
"""
from __future__ import annotations

import re

VOCALES = "aeiouáéíóúü"
FUERTES = "aeoáéó"


def silabas(palabra: str) -> int:
    p = palabra.lower()
    grupos = re.findall(rf"[{VOCALES}]+", p)
    n = 0
    for g in grupos:
        # un grupo con dos vocales fuertes consecutivas es hiato (2 silabas); el resto, diptongo/triptongo
        fuertes = sum(c in FUERTES for c in g)
        n += max(1, fuertes) if len(g) > 1 else 1
    return max(n, 1)


def szigriszt(texto: str) -> float:
    palabras = re.findall(r"[A-Za-zÁÉÍÓÚáéíóúüÑñ]+", texto)
    frases = max(1, len(re.findall(r"[.!?]+", texto)))
    return 206.835 - 62.3 * sum(silabas(w) for w in palabras) / len(palabras) - len(palabras) / frases


TEXTOS = {
    "A. simple": "Lea cada pregunta. Elija una respuesta. Marque la letra que corresponde.",
    "B. intermedia": ("Lea con atencion cada una de las preguntas y seleccione la alternativa "
                      "que considere correcta. Luego marque la letra en la hoja de respuestas."),
    "C. enrevesada": ("Previamente a la consignacion de la alternativa seleccionada, el postulante "
                      "debera cerciorarse de que la interpretacion efectuada de los enunciados "
                      "correspondientes resulte plenamente congruente con lo solicitado.")
}


def main() -> None:
    print(f"{'version':<16} {'IFSZ':>7}  lectura aproximada (escala INFLESZ)")
    print("=" * 62)
    for nombre, t in TEXTOS.items():
        v = szigriszt(t)
        if v > 80:
            nivel = "muy facil"
        elif v > 65:
            nivel = "bastante facil"
        elif v > 55:
            nivel = "normal"
        elif v > 40:
            nivel = "algo dificil"
        else:
            nivel = "muy dificil"
        print(f"{nombre:<16} {v:7.1f}  {nivel}")
    print()
    print("Lectura: la version C exige mas lectura que razonamiento: si el objetivo es medir")
    print("comprension de instrucciones o razonamiento, una redaccion innecesariamente compleja")
    print("agrega varianza irrelevante al constructo (clase 031). El indice es una guia (y el contador de silabas es aproximado): un texto")
    print("corto con terminos tecnicos puede ser dificil aunque su indice sea alto.")


if __name__ == "__main__":
    main()
