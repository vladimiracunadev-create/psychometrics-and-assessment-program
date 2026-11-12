"""Figuras de las clases 141 a 150 (parte 14). Valores tomados de la ejecucion de cada lab.py."""
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


def grupos(n, titulo, desc, xl, yl, yr, cats, series, colores, leyenda):
    k = len(series)
    ancho = 0.8 / (k + 1)
    lz = Lienzo(titulo, desc, xl, yl, (0.4, len(cats) + 0.6), yr)
    lz.ejes()
    for j, (vals, col) in enumerate(zip(series, colores, strict=True)):
        xs = [i + 1 + (j - (k - 1) / 2) * ancho * 1.1 for i in range(len(cats))]
        lz.barras(xs, vals, ancho, col)
    lz.texto(0.5, yr[1] * 0.97, leyenda)
    guardar(carpeta(n) / "figura-1.svg", lz)


grupos("141", "Aciertos y alfa por nivel de comprensión", "Aciertos: literal 66,8 por ciento, inferencial 50,3, crítico 33,6, total 50,2. Alfa: 0,62, 0,63, 0,62 y 0,83.",
       "1 literal · 2 inferencial · 3 crítico · 4 total", "Proporción", (0, 1.1), ["l", "i", "c", "t"],
       [[0.668, 0.503, 0.336, 0.502], [0.62, 0.63, 0.62, 0.83]], [AZUL, ROJO], "azul: proporción de aciertos · rojo: alfa")

barras("142", "Estudiantes que cambian de lado del criterio", "Con una lectura cambian 18,6 por ciento; con la mediana de tres lecturas, 10,8 por ciento.",
       "1 = una lectura · 2 = mediana de 3 lecturas", "% que cambia de lado", (0, 25), [1, 2], [18.6, 10.8], ["18,6 %", "10,8 %"], ROJO, 0.5)

lz = Lienzo("Coeficiente G según tareas y jueces", "G sube de 0,38 (1 tarea, 1 juez) a 0,79 (6 tareas, 3 jueces); agregar tareas pesa más que agregar jueces.",
            "Número de tareas", "Coeficiente G", (1, 6), (0.3, 0.85))
lz.ejes()
tareas = [1, 2, 4, 6]
lz.linea(tareas, [0.38, 0.51, 0.62, 0.66], ROJO, "1 juez")
lz.linea(tareas, [0.45, 0.60, 0.71, 0.75], AZUL, "2 jueces")
lz.linea(tareas, [0.48, 0.63, 0.75, 0.79], VERDE, "3 jueces")
guardar(carpeta("143") / "figura-1.svg", lz)

barras("144", "Error simulado según las reagrupaciones", "Con 0 reagrupaciones el error simulado es 6,8 por ciento; con 1, 22,9; con 2, 40,2.",
       "reagrupaciones: 1 = 0 · 2 = 1 · 3 = 2", "% de error simulado", (0, 50), [1, 2, 3], [6.8, 22.9, 40.2], ["6,8 %", "22,9 %", "40,2 %"], ROJO)

lz = Lienzo("Clasificación errada según las semanas de monitoreo", "La clasificación errada baja de 44,5 por ciento con 4 semanas a 18,2 por ciento con 16 semanas.",
            "Semanas de monitoreo", "% clasificación errada", (4, 16), (0, 50))
lz.ejes()
lz.linea([4, 8, 12, 16], [44.5, 33.8, 23.5, 18.2], ROJO, "clasificación errada (%)")
lz.puntos([4, 8, 12, 16], [44.5, 33.8, 23.5, 18.2], ROJO, r=4, opacidad=1)
guardar(carpeta("145") / "figura-1.svg", lz)

grupos("146", "Recuerdo el día 14 y el día 28 según el plan", "Masivo día 13: 0,90 y 0,10; masivo día 0: 0,12 y 0,01; distribuido: 0,66 y 0,21; distribuido tardío: 0,92 y 0,29.",
       "1 masivo día 13 · 2 masivo día 0 · 3 distribuido · 4 distribuido tardío", "Recuerdo", (0, 1.1), ["a", "b", "c", "d"],
       [[0.90, 0.12, 0.66, 0.92], [0.10, 0.01, 0.21, 0.29]], [AZUL, ROJO], "azul: prueba día 14 · rojo: retención día 28")

grupos("147", "Auto − real por cuartil, sin y con sobreconfianza real", "Sin sesgo: +5,9, +1,2, -1,3 y -5,5. Con +8 de sobreconfianza real: +13,7, +9,7, +6,4 y +2,4.",
       "cuartil por puntaje observado: 1 = Q1 · 2 = Q2 · 3 = Q3 · 4 = Q4", "Auto − real (puntos)", (-8, 16), ["1", "2", "3", "4"],
       [[5.9, 1.2, -1.3, -5.5], [13.7, 9.7, 6.4, 2.4]], [AZUL, ROJO], "azul: sin sesgo real · rojo: con +8 de sobreconfianza")

grupos("148", "Estimaciones del modelo cruzado", "M1 a R2 (verdad 0,00): -0,001 sin error y 0,027 con error. R1 a M2 (verdad 0,25): 0,256 sin error y 0,318 con error.",
       "1 = M1→R2 (verdad 0,00) · 2 = R1→M2 (verdad 0,25)", "Estimación", (-0.05, 0.4), ["a", "b"],
       [[-0.001, 0.256], [0.027, 0.318]], [AZUL, ROJO], "azul: sin error de medida · rojo: con error de medida")

barras("149", "Diferencia entre grupos en autoinforme y en desempeño", "d = 1,27 en autoinforme y d = 0,81 en desempeño.",
       "1 = autoinforme · 2 = desempeño", "d de Cohen", (0, 1.6), [1, 2], [1.27, 0.81], ["1,27", "0,81"], ROJO, 0.5)

barras("150", "Puntaje T de GAS en distintos casos", "T = 54,6; 57,7; 50,0; 53,0 y 65,1 según los logros, los pesos y la cantidad de metas.",
       "1 = A pesos iguales · 2 = A peso 3 · 3 = B todas lo esperado · 4 = B +1 en una · 5 = B +1 en todas", "T", (0, 75),
       [1, 2, 3, 4, 5], [54.6, 57.7, 50.0, 53.0, 65.1], ["54,6", "57,7", "50,0", "53,0", "65,1"], VERDE, ref=50)
print("figuras de la parte 14 generadas")
