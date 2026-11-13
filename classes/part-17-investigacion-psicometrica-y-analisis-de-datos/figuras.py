"""Figuras de las clases 171 a 180 (parte 17). Valores tomados de la ejecucion de cada lab.py."""
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


barras("171", "N mínimo de cada componente de un estudio de validación", "Fiabilidad alfa 0,80: 137; alfa 0,90: 36; correlación con criterio: 85; convergente frente a discriminante: 280; grupos conocidos: 350; AFC: 250.",
       "1 alfa .80 · 2 alfa .90 · 3 criterio · 4 conv/disc · 5 grupos · 6 AFC", "N mínimo", (0, 420), [1, 2, 3, 4, 5, 6],
       [137, 36, 85, 280, 350, 250], ["137", "36", "85", "280", "350", "250"], AZUL)

lz = Lienzo("RMSE de las cargas factoriales según N", "El RMSE baja de 0,094 con N 50 a 0,022 con N 1 000.",
            "N", "RMSE de las cargas", (50, 1000), (0, 0.11))
lz.ejes()
lz.linea([50, 100, 200, 500, 1000], [0.094, 0.071, 0.047, 0.032, 0.022], AZUL)
lz.puntos([50, 100, 200, 500, 1000], [0.094, 0.071, 0.047, 0.032, 0.022], AZUL, r=4, opacidad=1)
guardar(carpeta("172") / "figura-1.svg", lz)

lz = Lienzo("Cobertura real de un intervalo del 95 % según la distribución", "Con datos normales la cobertura es cerca de 95 por ciento; con asimetría baja a 78-87 y con extremos a 68-71.",
            "n", "Cobertura (%)", (30, 200), (60, 100))
lz.ejes()
lz.linea([30, 60, 200], [95.5, 94.5, 95.3], AZUL, "normal")
lz.linea([30, 60, 200], [86.7, 83.9, 78.5], ROJO, "asimétrica")
lz.linea([30, 60, 200], [70.7, 68.0, 67.8], VERDE, "con extremos")
lz.linea([30, 200], [95, 95], AZUL, "nominal 95 %", punteada=True)
guardar(carpeta("173") / "figura-1.svg", lz)

grupos("174", "Sesgo de la media de Y según mecanismo y método", "Sesgo de la media: MCAR cero con cualquier método; MAR +0,161 con completos o media y +0,005 con regresión; MNAR +0,314 con completos o media y +0,249 con regresión.",
       "1 = MCAR · 2 = MAR · 3 = MNAR", "Sesgo de la media", (-0.05, 0.4), ["a", "b", "c"],
       [[-0.001, 0.161, 0.314], [-0.000, 0.005, 0.249]], [ROJO, VERDE], "rojo: casos completos · verde: regresión estocástica")

grupos("175", "Porcentaje que «mejoró» según el RCI", "Sin cambio real: 10,0 por ciento con RCI ingenuo y 2,6 con RCI corregido. Con cambio real de +6: 51,8 y 27,0.",
       "1 = sin cambio real (solo práctica) · 2 = cambio real de +6", "% que «mejoró»", (0, 65), ["a", "b"],
       [[10.0, 51.8], [2.6, 27.0]], [ROJO, AZUL], "rojo: RCI ingenuo · azul: RCI corregido por práctica")

barras("176", "Ancho medio del intervalo bootstrap según n", "El ancho medio baja de 0,258 con n 40 a 0,170 con n 80 y 0,100 con n 200.",
       "1 = n 40 · 2 = n 80 · 3 = n 200", "Ancho medio", (0, 0.32), [1, 2, 3], [0.258, 0.170, 0.100], ["0,258", "0,170", "0,100"], AZUL)

grupos("177", "Detección de DIF según el método", "Sin DIF: MH 0, RL con interacción 5, RL solo grupo 0 por ciento. Uniforme: 100 con los tres. No uniforme: MH 10, RL con interacción 95, RL solo grupo 10.",
       "1 = sin DIF · 2 = uniforme · 3 = no uniforme", "% de detección", (0, 120), ["a", "b", "c"],
       [[0, 100, 10], [5, 100, 95], [0, 100, 10]], [AZUL, ROJO, VERDE], "azul: MH · rojo: RL con interacción · verde: RL solo grupo")

barras("178", "Huellas distintas en tres ejecuciones", "Con semilla fija las tres ejecuciones dan una sola huella; sin semilla dan tres huellas distintas.",
       "1 = semilla fija y estructuras ordenadas · 2 = sin semilla", "Huellas distintas (de 3)", (0, 4), [1, 2], [1, 3], ["1", "3"], VERDE, 0.5)

lz = Lienzo("Alfa agrupado con su intervalo y su intervalo de predicción", "Alfa agrupado 0,803 con intervalo de confianza de 0,779 a 0,824 e intervalo de predicción de 0,665 a 0,884.",
            "Alfa de Cronbach", "1 = intervalo del promedio · 2 = intervalo de predicción", (0.6, 0.92), (0.5, 2.5))
lz.ejes()
lz.linea([0.779, 0.824], [1, 1], AZUL, "IC 95 % del promedio")
lz.linea([0.665, 0.884], [2, 2], ROJO, "intervalo de predicción")
lz.puntos([0.803, 0.803], [1, 2], VERDE, r=5, opacidad=1)
guardar(carpeta("179") / "figura-1.svg", lz)

barras("180", "Criterios cumplidos por cada informe", "El Informe A cumple 4 de 4 criterios; el Informe B, 0 de 4.",
       "1 = Informe A · 2 = Informe B", "Criterios cumplidos (de 4)", (0, 5), [1, 2], [4, 0], ["4/4", "0/4"], VERDE, 0.5)
print("figuras de la parte 17 generadas")
