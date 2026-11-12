"""Figuras de las clases 111 a 120 (parte 11). Valores tomados de la ejecucion de cada lab.py."""
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


barras("111", "Criticidad media por tarea", "Las tareas 3, 1 y 4 superan el umbral de 12; las tareas 10, 11 y 6 no.",
       "1 = tarea 3 · 2 = tarea 1 · 3 = tarea 4 · 4 = tarea 10 · 5 = tarea 11 · 6 = tarea 6", "Criticidad media", (0, 18),
       [1, 2, 3, 4, 5, 6], [15.0, 13.9, 13.5, 11.2, 10.2, 9.5], ["15,0", "13,9", "13,5", "11,2", "10,2", "9,5"], AZUL, ref=12)

barras("112", "Validez del compuesto según la correlación entre predictores", "R baja de 0,495 a 0,391 cuando r12 sube de 0 a 0,6.",
       "r12: 1 = 0,0 · 2 = 0,2 · 3 = 0,4 · 4 = 0,6", "R del compuesto", (0, 0.6), [1, 2, 3, 4], [0.495, 0.452, 0.418, 0.391],
       ["0,495", "0,452", "0,418", "0,391"], VERDE)

lz = Lienzo("Pasos y condicionales de los ocho ítems", "Los ocho ítems tienen 2, 2, 3, 3, 4, 4, 5 y 5 pasos y 0, 0, 1, 1, 2, 2, 3 y 3 condicionales.",
            "Ítem", "Cantidad", (1, 8), (0, 6))
lz.ejes()
lz.linea([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 3, 4, 4, 5, 5], AZUL, "pasos")
lz.puntos([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 3, 4, 4, 5, 5], AZUL, r=4, opacidad=1)
lz.linea([1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 1, 1, 2, 2, 3, 3], ROJO, "condicionales")
lz.puntos([1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 1, 1, 2, 2, 3, 3], ROJO, r=4, opacidad=1)
guardar(carpeta("113") / "figura-1.svg", lz)

barras("114", "Correlación media entre dimensiones según el error del evaluador", "Sin errores 0,15; con halo e indulgencia 0,64; tras entrenamiento 0,47.",
       "1 = sin errores · 2 = halo e indulgencia · 3 = tras entrenamiento", "Correlación media", (0, 0.8), [1, 2, 3], [0.15, 0.64, 0.47],
       ["0,15", "0,64", "0,47"], ROJO)

barras("115", "Distancia total a la clave de expertos", "Los expertos quedan a 45,2 de la clave (puntaje -45,2) y los novatos a 55,9 (puntaje -55,9).",
       "1 = expertos · 2 = novatos", "Distancia a la clave (menor es mejor)", (0, 70), [1, 2], [45.2, 55.9], ["-45,2", "-55,9"], VERDE, 0.5)

lz = Lienzo("R² lineal y cuadrático según el peso del territorio", "El R² lineal baja de 0,255 a 0,094 y el cuadrático de 0,285 a 0,106 al subir el peso del territorio de 0 a 2.",
            "Peso del territorio en las ventas", "R²", (0, 2), (0, 0.35))
lz.ejes()
lz.linea([0, 0.5, 1.0, 2.0], [0.255, 0.237, 0.187, 0.094], ROJO, "lineal")
lz.puntos([0, 0.5, 1.0, 2.0], [0.255, 0.237, 0.187, 0.094], ROJO, r=4, opacidad=1)
lz.linea([0, 0.5, 1.0, 2.0], [0.285, 0.269, 0.215, 0.106], AZUL, "cuadrático")
lz.puntos([0, 0.5, 1.0, 2.0], [0.285, 0.269, 0.215, 0.106], AZUL, r=4, opacidad=1)
guardar(carpeta("116") / "figura-1.svg", lz)

barras("117", "Potencia para detectar la relación con accidentes", "Con N = 200 la potencia es 20 por ciento; con N = 2 000 es 87 por ciento.",
       "1 = N 200 · 2 = N 2 000", "Potencia (%)", (0, 110), [1, 2], [20, 87], ["20 %", "87 %"], AZUL, 0.5, ref=80)

lz = Lienzo("Índices de ajuste de tres candidatos", "Ana: 76, 75 y 83. Beto: 76, 88 y 88. Carla: 60, 0 y 96, según los índices A, B y C.",
            "Candidato (1 = Ana · 2 = Beto · 3 = Carla)", "Puntos de ajuste", (0.4, 3.6), (0, 110))
lz.ejes()
lz.barras([0.8, 1.8, 2.8], [76, 76, 60], 0.2, AZUL)
lz.barras([1.0, 2.0, 3.0], [75, 88, 0], 0.2, VERDE)
lz.barras([1.2, 2.2, 3.2], [83, 88, 96], 0.2, ROJO)
lz.texto(0.5, 105, "azul: A distancia · verde: B porcentaje que cumple · rojo: C correlación")
guardar(carpeta("118") / "figura-1.svg", lz)

barras("119", "Exactitud de clasificación por nivel", "Exactitud: A2 84,2 por ciento, B1 85,5 por ciento, B2 81,6 por ciento.",
       "1 = A2 · 2 = B1 · 3 = B2", "Exactitud (%)", (0, 100), [1, 2, 3], [84.2, 85.5, 81.6], ["84,2 %", "85,5 %", "81,6 %"], AZUL)

barras("120", "p de Fisher en cuatro escenarios", "p = 0,5145 con n 20; 0,0405 con n 100; 0,0001 con n 3 000; 1,0 sin diferencia. La referencia es 0,05.",
       "1 = n 20 · 2 = n 100 · 3 = n 3 000 · 4 = sin diferencia", "p (Fisher)", (0, 1.15), [1, 2, 3, 4], [0.5145, 0.0405, 0.0001, 1.0],
       ["0,51", "0,04", "0,0001", "1,00"], ROJO, ref=0.05)
print("figuras de la parte 11 generadas")
