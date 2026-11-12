"""Laboratorio 140 - Normas extranjeras en Chile: efecto de aplicar un baremo desplazado.

Parte 1 (mapa normativo, a VERIFICAR en la fuente oficial): lista de referentes que enmarcan la
evaluacion educativa en Chile. La tabla es una guia de estudio; la vigencia y el texto exacto se
consultan en bcn.cl y mineduc.cl.
Parte 2 (calculo): si el desempeno local medio es 0.5 DE menor que el de la muestra normativa
extranjera, un baremo importado clasifica a mas ninos como "en riesgo" (< -1.5 DE de la norma).
Se calcula cuantos y cuantos serian con un baremo local.
"""
from __future__ import annotations

from statistics import NormalDist

ND = NormalDist()

MAPA = [
    ("Ley General de Educacion (Ley 20.370)", "marco general del sistema escolar"),
    ("Bases Curriculares de la Educacion Parvularia", "ambitos y nucleos de aprendizaje 0-6 anos"),
    ("Bases Curriculares 1.o a 6.o basico y 7.o a 2.o medio", "objetivos de aprendizaje por asignatura"),
    ("Ley 20.422 (igualdad de oportunidades e inclusion de personas con discapacidad)", "ajustes y no discriminacion"),
    ("Decreto 170/2009 (Necesidades Educativas Especiales)", "criterios y evaluacion diagnostica para subvencion NEE"),
    ("Decreto 83/2015 (diversificacion de la ensenanza)", "adecuaciones curriculares y DUA"),
    ("Decreto 67/2018 (evaluacion, calificacion y promocion)", "evaluacion formativa y sumativa en aula"),
    ("Ley 21.545 (inclusion y atencion integral de personas con TEA)", "derechos, deteccion y apoyos"),
    ("Ley 21.719 (datos personales)", "tratamiento de datos de estudiantes (ver clase 076)"),
]


def main() -> None:
    print("Parte 1 - mapa normativo (verificar vigencia y texto en bcn.cl / mineduc.cl)")
    for norma, ambito in MAPA:
        print(f"  - {norma}: {ambito}")
    print("\nParte 2 - baremo importado frente a baremo local")
    print(f"{'diferencia local (DE)':>22} {'en riesgo con norma importada':>31} {'con norma local':>17}")
    for delta in (0.0, -0.25, -0.5, -0.75):
        importada = ND.cdf(-1.5 - delta)                  # P(z_local < -1.5 respecto de la norma importada)
        local = ND.cdf(-1.5)
        print(f"{delta:22.2f} {importada:31.1%} {local:17.1%}")
    print()
    print("Lectura: con un desplazamiento de 0.5 DE entre la poblacion local y la normativa, una norma")
    print("importada marca como 'riesgo' a ~16 % en vez de ~7 %: mas del doble de derivaciones por una")
    print("diferencia de referencia, no de los ninos. Por eso se exige evidencia de equivalencia o un")
    print("baremo local (clases 032 y 035), y se usan instrumentos chilenos (p. ej. TEPSI o EEDP, ya")
    print("fichados en el catalogo) con la version y el baremo vigentes verificados.")


if __name__ == "__main__":
    main()
