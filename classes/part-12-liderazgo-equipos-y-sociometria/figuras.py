"""Figuras de las clases 121 a 130 (parte 12). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


def barras(n, titulo, desc, xl, yl, yr, xs, ys, etiquetas, color=AZUL, ancho=0.6, ref=None):
    lz = Lienzo(titulo, desc, xl, yl, (0.4, len(xs) + 0.6), yr)
    lz.ejes()
    lz.barras(xs, ys, ancho, color)
    if ref is not None:
        lz.linea([0.4, len(xs) + 0.6], [ref, ref], ROJO, "referencia", punteada=True)
    for x, y, t in zip(xs, ys, etiquetas, strict=True):
        lz.texto(x - 0.3, y + (yr[1] - yr[0]) * 0.03, t)
    guardar(carpeta(n) / "figura-1.svg", lz)


barras("121", "Líderes que mantienen su cuadrante", "Mantienen su cuadrante 63,3 por ciento (bajo-bajo), 64,2 (bajo tarea alto personas), 63,2 (alto tarea bajo personas) y 62,9 (alto-alto).",
       "1 bajo-bajo · 2 bajo tarea/alto personas · 3 alto tarea/bajo personas · 4 alto-alto", "% que mantiene el cuadrante", (0, 100),
       [1, 2, 3, 4], [63.3, 64.2, 63.2, 62.9], ["63,3 %", "64,2 %", "63,2 %", "62,9 %"], AZUL)

lz = Lienzo("rwg y CCI en dos condiciones", "Con líderes distintos: rwg 0,86, CCI(1) 0,72, CCI(2) 0,94. Con líderes iguales: rwg 0,42, CCI(1) 0,00, CCI(2) -0,01.",
            "Condición (1 = líderes distintos · 2 = líderes iguales)", "Valor", (0.4, 2.6), (-0.1, 1.1))
lz.ejes()
lz.barras([0.75, 1.75], [0.86, 0.42], 0.2, AZUL)
lz.barras([1.0, 2.0], [0.72, 0.0], 0.2, VERDE)
lz.barras([1.25, 2.25], [0.94, -0.01], 0.2, ROJO)
lz.texto(0.5, 1.05, "azul: rwg · verde: CCI(1) · rojo: CCI(2)")
guardar(carpeta("122") / "figura-1.svg", lz)

barras("123", "Estudios con al menos un rol «significativo» sin efecto real", "43,3 por ciento sin corrección, 37,0 por ciento teórico y 8,6 por ciento con Bonferroni.",
       "1 = sin corrección · 2 = teórico · 3 = con Bonferroni", "% de estudios", (0, 60), [1, 2, 3], [43.3, 37.0, 8.6], ["43,3 %", "37,0 %", "8,6 %"], ROJO, ref=5)

barras("124", "Efecto indirecto y efecto total", "Indirecto verdadero 0,300; estimado 0,288 (intervalo 0,122 a 0,491); efecto total 0,202.",
       "1 = verdadero · 2 = estimado · 3 = total de X sobre Y", "Efecto", (0, 0.6), [1, 2, 3], [0.300, 0.288, 0.202], ["0,300", "0,288", "0,202"], VERDE)

barras("125", "Estatus sociométrico en un curso de 30", "Promedio 20, ignorado 4, popular 3 y rechazado 3 estudiantes.",
       "1 = promedio · 2 = ignorado · 3 = popular · 4 = rechazado", "Estudiantes", (0, 25), [1, 2, 3, 4], [20, 4, 3, 3], ["20", "4", "3", "3"], AZUL)

barras("126", "Reciprocidad y elecciones dentro del grupo", "Reciprocidad: 0,111 al azar y 0,389 con subgrupos. Elecciones dentro del grupo: 0,458 y 0,972.",
       "1 = reciprocidad (azar) · 2 = reciprocidad (subgrupos) · 3 = dentro del grupo (azar) · 4 = dentro del grupo (subgrupos)", "Proporción", (0, 1.1),
       [1, 2, 3, 4], [0.111, 0.389, 0.458, 0.972], ["0,111", "0,389", "0,458", "0,972"], AZUL)

barras("127", "Persistencia del aislamiento y del liderazgo informal", "Siguen sin ser elegidos 40,3 por ciento; el solapamiento del 10 por ciento con más elecciones es 56,4 por ciento.",
       "1 = aislados que persisten · 2 = líderes que se mantienen", "%", (0, 80), [1, 2], [40.3, 56.4], ["40,3 %", "56,4 %"], VERDE, 0.5)

barras("128", "ICC del clima", "ICC(1) = 0,084 e ICC(2) = 0,530.",
       "1 = ICC(1) · 2 = ICC(2)", "ICC", (0, 0.8), [1, 2], [0.084, 0.530], ["0,084", "0,530"], AZUL, 0.5)

lz = Lienzo("Fiabilidad del promedio según el número de pares", "La fiabilidad sube de 0,57 con 1 par a 0,93 con 10; r con la verdad sube de 0,74 a 0,96.",
            "Número de pares", "Valor", (1, 10), (0.4, 1.0))
lz.ejes()
lz.linea([1, 3, 6, 10], [0.57, 0.80, 0.89, 0.93], AZUL, "fiabilidad")
lz.puntos([1, 3, 6, 10], [0.57, 0.80, 0.89, 0.93], AZUL, r=4, opacidad=1)
lz.linea([1, 3, 6, 10], [0.74, 0.88, 0.93, 0.96], VERDE, "r con la verdad")
lz.puntos([1, 3, 6, 10], [0.74, 0.88, 0.93, 0.96], VERDE, r=4, opacidad=1)
guardar(carpeta("129") / "figura-1.svg", lz)

barras("130", "Error colectivo según la independencia de los juicios", "MSE de 45,7 con juicios independientes y de 325,9 con influencia de un líder sesgado.",
       "1 = independientes · 2 = influidos por el líder", "Error colectivo (MSE)", (0, 400), [1, 2], [45.7, 325.9], ["45,7", "325,9"], ROJO, 0.5)
print("figuras de la parte 12 generadas")
