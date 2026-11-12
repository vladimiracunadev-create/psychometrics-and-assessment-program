"""Figuras de las clases 041 a 050 (parte 04). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

import math
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


def barras(n, titulo, desc, xl, yl, yr, xs, ys, etiquetas, color=AZUL, ancho=0.6):
    lz = Lienzo(titulo, desc, xl, yl, (0.4, len(xs) + 0.6), yr)
    lz.ejes()
    lz.barras(xs, ys, ancho, color)
    for x, y, t in zip(xs, ys, etiquetas, strict=True):
        lz.texto(x - 0.3, y + (yr[1] - yr[0]) * 0.03, t)
    guardar(carpeta(n) / "figura-1.svg", lz)


barras("041", "Autovalores de una matriz de seis ítems", "Autovalores 2,42; 1,44; 0,56; 0,54; 0,53 y 0,51: dos dimensiones sobre 1.",
       "Posición del autovalor", "Autovalor", (0, 3), [1, 2, 3, 4, 5, 6], [2.42, 1.44, 0.56, 0.54, 0.53, 0.51], ["2,42", "1,44", "0,56", "0,54", "0,53", "0,51"])

lz = Lienzo("Autovalores reales frente al azar (p95)", "Solo los dos primeros autovalores superan la linea del azar; los demas quedan debajo.",
            "Posición del autovalor", "Autovalor", (0.4, 6.6), (0, 3.2))
lz.ejes()
lz.barras([1, 2, 3, 4, 5, 6], [2.81, 2.67, 0.83, 0.77, 0.74, 0.70], 0.55, AZUL)
lz.linea([1, 2, 3, 4, 5, 6], [1.38, 1.25, 1.19, 1.13, 1.10, 1.05], ROJO, "azar p95", punteada=True)
guardar(carpeta("042") / "figura-1.svg", lz)

barras("043", "Residuo del modelo de un factor (SRMR)", "SRMR de 0,016 si los datos tienen un factor y de 0,198 si tienen dos factores.",
       "Datos generados por (1 un factor, 2 dos factores)", "SRMR", (0, 0.25), [1, 2], [0.016, 0.198], ["0,016", "0,198"], ROJO, 0.5)

barras("044", "Predicciones del hexágono cumplidas", "72 de 72 predicciones con estructura circular frente a 41 de 72 con seis variables independientes.",
       "Datos (1 circulares, 2 independientes)", "Proporción cumplida", (0, 1.1), [1, 2], [1.0, 0.57], ["72/72", "41/72"], VERDE, 0.5)

lz = Lienzo("Fiabilidad y validez en dos grupos", "Alfa 0,858 en el grupo A y 0,808 en el B; la correlacion con el criterio es casi igual (0,459 y 0,462).",
            "Grupo (1 = A, 2 = B)", "Valor", (0.4, 2.6), (0, 1))
lz.ejes()
lz.barras([0.85, 1.85], [0.858, 0.808], 0.3, AZUL)
lz.barras([1.15, 2.15], [0.459, 0.462], 0.3, ROJO)
lz.texto(0.5, 0.95, "azul: alfa · rojo: r con el criterio")
guardar(carpeta("045") / "figura-1.svg", lz)

sin_rotar = [(0.23, 0.75), (0.26, 0.75), (0.20, 0.75), (0.22, 0.75), (0.76, -0.23), (0.76, -0.25), (0.76, -0.20), (0.76, -0.22)]
varimax = [(0.01, 0.78), (0.04, 0.79), (-0.03, 0.77), (-0.01, 0.78), (0.79, 0.00), (0.80, -0.02), (0.78, 0.02), (0.79, 0.01)]
lz = Lienzo("Cargas antes y después de rotar", "Antes de rotar cada item carga en ambos factores; tras varimax cada item carga en uno solo.",
            "Carga en el factor 1", "Carga en el factor 2", (-0.4, 1), (-0.4, 1))
lz.ejes()
lz.puntos([p[0] for p in sin_rotar], [p[1] for p in sin_rotar], AZUL, r=5, opacidad=0.8)
lz.puntos([p[0] for p in varimax], [p[1] for p in varimax], ROJO, r=5, opacidad=0.9)
lz.texto(-0.35, 0.95, "azul: sin rotar · rojo: varimax")
guardar(carpeta("046") / "figura-1.svg", lz)

ns = [100, 200, 500, 1000, 5000, 20000]
lz = Lienzo("El RMSEA se estabiliza con el tamaño muestral", "Con el mismo desajuste, el RMSEA sube de 0 con N = 500 a 0,038 con N = 20000 y queda bajo 0,06.",
            "log10 del tamaño muestral (N)", "RMSEA", (2, 4.5), (0, 0.08))
lz.ejes()
lz.linea([math.log10(n) for n in ns], [0, 0, 0, 0.022, 0.036, 0.038], AZUL)
lz.puntos([math.log10(n) for n in ns], [0, 0, 0, 0.022, 0.036, 0.038], AZUL, r=4, opacidad=1)
lz.linea([2, 4.5], [0.06, 0.06], ROJO, "referencia 0,06", punteada=True)
guardar(carpeta("047") / "figura-1.svg", lz)

lz = Lienzo("Omega total, omega jerárquico y ECV", "Con factor general debil (0,3) el omega total sigue alto (0,775) pero el omega jerarquico cae a 0,332.",
            "Caso (1 general 0,7; 2 general 0,5; 3 general 0,3)", "Valor", (0.4, 3.6), (0, 1))
lz.ejes()
lz.barras([0.8, 1.8, 2.8], [0.906, 0.857, 0.775], 0.22, AZUL)
lz.barras([1.0, 2.0, 3.0], [0.882, 0.643, 0.332], 0.22, ROJO)
lz.barras([1.2, 2.2, 3.2], [0.925, 0.500, 0.200], 0.22, VERDE)
lz.texto(0.5, 0.95, "azul: ω total · rojo: ω jerárquico · verde: ECV")
guardar(carpeta("048") / "figura-1.svg", lz)

lz = Lienzo("Correlación marginal frente a parcial", "En una cadena A-B-C-D las parciales de pares no adyacentes son casi 0, mientras las marginales sugieren relaciones.",
            "Par (1 AB, 2 AC, 3 AD, 4 BC, 5 BD, 6 CD)", "Correlación", (0.4, 6.6), (-0.1, 0.7))
lz.ejes()
lz.barras([0.85, 1.85, 2.85, 3.85, 4.85, 5.85], [0.61, 0.36, 0.19, 0.59, 0.32, 0.59], 0.3, AZUL)
lz.barras([1.15, 2.15, 3.15, 4.15, 5.15, 6.15], [0.53, 0.0, -0.01, 0.44, -0.03, 0.53], 0.3, ROJO)
lz.texto(0.5, 0.65, "azul: marginal · rojo: parcial")
guardar(carpeta("049") / "figura-1.svg", lz)

cortes = [0.0, 0.5, 1.0, 1.5, 2.0]
lz = Lienzo("Pearson subestima con ítems asimétricos", "Con correlacion latente 0,6, el phi baja de 0,41 a 0,25 cuando el corte es extremo; la tetracorica se acerca a 0,6 solo con cortes centrales.",
            "Corte (z): mayor corte, ítem más difícil", "Correlación", (0, 2), (0.2, 0.9))
lz.ejes()
lz.linea(cortes, [0.406, 0.401, 0.358, 0.293, 0.249], ROJO, "Pearson / phi")
lz.linea(cortes, [0.595, 0.622, 0.666, 0.734, 0.839], AZUL, "tetracórica (aprox.)")
lz.linea([0, 2], [0.6, 0.6], "#888888", None, punteada=True)
guardar(carpeta("050") / "figura-1.svg", lz)
print("figuras de la parte 04 generadas")
