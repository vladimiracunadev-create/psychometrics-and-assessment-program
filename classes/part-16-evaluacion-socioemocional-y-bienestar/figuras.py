"""Figuras de las clases 161 a 170 (parte 16). Valores tomados de la ejecucion de cada lab.py."""
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


barras("161", "Tamaño de muestra para 80 % de potencia", "Con un ítem se necesitan 84 personas; con la escala de 5 ítems, 59.",
       "1 = un ítem (fiabilidad 0,60) · 2 = escala de 5 ítems (0,85)", "n necesario", (0, 100), [1, 2], [84, 59], ["84", "59"], AZUL, 0.5)

barras("162", "Falsos cambios según el criterio", "Sin cambio real, parecen haber cambiado 35,8 por ciento con 0,5 DE, 47,6 con 1 ETM y 5,1 con el cambio fiable.",
       "1 = 0,5 DE · 2 = 1 ETM · 3 = cambio fiable", "% de falsos cambios", (0, 60), [1, 2, 3], [35.8, 47.6, 5.1],
       ["35,8 %", "47,6 %", "5,1 %"], ROJO)

barras("163", "Exactitud al clasificar cada trayectoria", "Resiliente 74,6 por ciento, recuperación 77,6, crónica 71,3 y tardía 76,9.",
       "1 resiliente · 2 recuperación · 3 crónica · 4 tardía", "% clasificado correctamente", (0, 100), [1, 2, 3, 4],
       [74.6, 77.6, 71.3, 76.9], ["74,6 %", "77,6 %", "71,3 %", "76,9 %"], VERDE)

barras("164", "Correlación según el nivel de análisis", "Entre personas 0,96; agrupada ingenua 0,15; dentro de la persona -0,58.",
       "1 = entre personas · 2 = agrupada · 3 = dentro de la persona", "Correlación", (-0.8, 1.2), [1, 2, 3], [0.96, 0.15, -0.58],
       ["0,96", "0,15", "-0,58"], AZUL)

grupos("165", "Precisión cruda y Hu según el sesgo de respuesta", "Sin sesgo: precisión cruda 0,75 y Hu 0,57. Con sesgo a enojo: 0,56 y 0,37.",
       "1 = sin sesgo · 2 = sesgo a «enojo»", "Valor", (0, 1.0), ["a", "b"],
       [[0.75, 0.56], [0.57, 0.37]], [AZUL, ROJO], "azul: precisión cruda · rojo: Hu")

barras("166", "Porcentaje favorable de unidades con la misma satisfacción real", "Con satisfacción real de 62 por ciento en todas, el puesto 1 (n 8) muestra 88, el 2 (n 20) 80, el 28 (n 8) 50 y el 30 (n 12) 33.",
       "1 = puesto 1 (n 8) · 2 = puesto 2 (n 20) · 3 = puesto 28 (n 8) · 4 = puesto 30 (n 12)", "% favorable", (0, 100), [1, 2, 3, 4],
       [88, 80, 50, 33], ["88 %", "80 %", "50 %", "33 %"], AZUL, ref=62)

barras("167", "Valor predictivo positivo según la prevalencia", "VPP de 0,17 con prevalencia de 2 por ciento, 0,34 con 5, 0,54 con 10 y 0,72 con 20.",
       "prevalencia: 1 = 2 % · 2 = 5 % · 3 = 10 % · 4 = 20 %", "VPP", (0, 0.9), [1, 2, 3, 4], [0.17, 0.34, 0.54, 0.72],
       ["0,17", "0,34", "0,54", "0,72"], ROJO)

barras("168", "Plazo de respuesta en las combinaciones mostradas", "De las ocho combinaciones de la tabla, cuatro (las que tienen riesgo) se atienden de inmediato, dos en 24 horas y dos sin acción específica; ninguna viola un invariante.",
       "1 = inmediato (con riesgo) · 2 = 24 h (alerta sin riesgo) · 3 = sin acción", "Combinaciones de la tabla", (0, 6),
       [1, 2, 3], [4, 2, 2], ["inmediato", "24 h", "sin acción"], VERDE)

grupos("169", "Estudiantes marcados por curso según la regla", "Regla relativa: 1, 1, 15, 0, 3 y 3 estudiantes en los cursos 1 a 6. Regla absoluta: 0, 0, 3, 0, 0 y 0.",
       "curso 1 a 6", "Estudiantes marcados", (0, 18), ["1", "2", "3", "4", "5", "6"],
       [[1, 1, 15, 0, 3, 3], [0, 0, 3, 0, 0, 0]], [AZUL, ROJO], "azul: relativa (≥ 9) · rojo: absoluta (≥ 12)")

barras("170", "Efecto medio según el conjunto de estudios", "La media simple de todos los estudios es 0,05 y la de los publicados 0,14.",
       "1 = todos los estudios · 2 = solo los publicados", "Media simple del efecto (d)", (0, 0.2), [1, 2], [0.05, 0.14], ["0,05", "0,14"], ROJO, 0.5)
print("figuras de la parte 16 generadas")
