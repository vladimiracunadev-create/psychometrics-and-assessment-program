"""Figuras de las clases 131 a 140 (parte 13). Valores tomados de la ejecucion de cada lab.py."""
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
    """Barras agrupadas: series es una lista de listas (una por serie) con un valor por categoria."""
    k = len(series)
    ancho = 0.8 / (k + 1)
    lz = Lienzo(titulo, desc, xl, yl, (0.4, len(cats) + 0.6), yr)
    lz.ejes()
    for j, (vals, col) in enumerate(zip(series, colores, strict=True)):
        xs = [i + 1 + (j - (k - 1) / 2) * ancho * 1.1 for i in range(len(cats))]
        lz.barras(xs, vals, ancho, col)
    lz.texto(0.5, yr[1] * 0.97, leyenda)
    guardar(carpeta(n) / "figura-1.svg", lz)


barras("131", "Niños sanos que aún no logran el hito", "A los 12 meses 50,1 por ciento, a los 14 meses 15,4, a los 16 meses 2,8 y a los 18 meses 0,4.",
       "1 = 12 meses · 2 = 14 meses · 3 = 16 meses · 4 = 18 meses", "% que aún no lo logra", (0, 60), [1, 2, 3, 4], [50.1, 15.4, 2.8, 0.4],
       ["50,1 %", "15,4 %", "2,8 %", "0,4 %"], AZUL)

lz = Lienzo("Aciertos en tareas de conservación según la edad", "A los 7 años acierta 98 por ciento en número, 89 en líquido y 50 en peso.",
            "Edad (años)", "Proporción de aciertos", (4, 9), (0, 1.05))
lz.ejes()
edades = [4, 5, 6, 7, 8, 9]
lz.linea(edades, [0.33, 0.66, 0.88, 0.98, 1.0, 1.0], AZUL, "número")
lz.linea(edades, [0.09, 0.35, 0.67, 0.89, 0.97, 1.0], VERDE, "líquido")
lz.linea(edades, [0.01, 0.05, 0.21, 0.50, 0.79, 0.95], ROJO, "peso")
guardar(carpeta("132") / "figura-1.svg", lz)

barras("133", "Hablantes tardíos a los 36 meses sin intervención", "El 32,9 por ciento sigue bajo el P10 y el 67,1 por ciento sale de ese rango.",
       "1 = sigue bajo el P10 · 2 = sale del rango", "% de los hablantes tardíos", (0, 90), [1, 2], [32.9, 67.1],
       ["32,9 %", "67,1 %"], ROJO, 0.5)

lz = Lienzo("Fiabilidad entre sesiones según el tiempo observado", "La fiabilidad sube de 0,17 con 5 minutos a 0,72 con 120 minutos.",
            "Minutos observados", "Fiabilidad entre sesiones", (5, 120), (0, 1.0))
lz.ejes()
lz.linea([5, 15, 30, 60, 120], [0.17, 0.32, 0.42, 0.60, 0.72], AZUL)
lz.puntos([5, 15, 30, 60, 120], [0.17, 0.32, 0.42, 0.60, 0.72], AZUL, r=4, opacidad=1)
guardar(carpeta("134") / "figura-1.svg", lz)

cs = [-0.5, 0.0, 0.25, 0.5, 0.75, 1.0, 1.5]
lz = Lienzo("Sensibilidad, especificidad y VPP según el corte", "La sensibilidad sube de 0,30 a 0,93; la especificidad baja de 0,98 a 0,50; el VPP baja de 0,41 a 0,09.",
            "Corte del cribado", "Valor", (-0.5, 1.5), (0, 1.05))
lz.ejes()
lz.linea(cs, [0.30, 0.50, 0.60, 0.69, 0.77, 0.84, 0.93], ROJO, "sensibilidad")
lz.linea(cs, [0.98, 0.93, 0.89, 0.84, 0.77, 0.69, 0.50], AZUL, "especificidad")
lz.linea(cs, [0.41, 0.28, 0.23, 0.19, 0.15, 0.13, 0.09], VERDE, "VPP")
guardar(carpeta("135") / "figura-1.svg", lz)

grupos("136", "Sensibilidad y especificidad por regla de combinación", "Solo familia 0,75 y 0,92; solo docente 0,58 y 0,94; cualquiera 0,90 y 0,86; ambos 0,43 y 1,00.",
       "1 familia · 2 docente · 3 cualquiera · 4 ambos", "Valor", (0, 1.15), ["f", "d", "c", "a"],
       [[0.75, 0.58, 0.90, 0.43], [0.92, 0.94, 0.86, 1.00]], [ROJO, AZUL], "rojo: sensibilidad · azul: especificidad")

barras("137", "NAP medio en tres escenarios", "NAP 0,92 con efecto real, 0,50 sin efecto y 0,93 sin efecto pero con tendencia previa.",
       "1 = efecto real · 2 = sin efecto · 3 = sin efecto con tendencia previa", "NAP medio", (0, 1.1), [1, 2, 3], [0.92, 0.50, 0.93],
       ["0,92", "0,50", "0,93"], VERDE, ref=0.5)

grupos("138", "Kappa simple y ponderado según la rúbrica", "Ambiguos 0,14 y 0,33; observables 0,46 y 0,73; observables con una educadora indulgente 0,30 y 0,65.",
       "1 ambiguos · 2 observables · 3 observables + indulgencia", "Kappa", (0, 0.9), ["a", "o", "i"],
       [[0.14, 0.46, 0.30], [0.33, 0.73, 0.65]], [ROJO, AZUL], "rojo: kappa simple · azul: kappa ponderado")

barras("139", "VPP tras dos etapas según el error compartido", "VPP 0,59 con error compartido 0, 0,44 con 0,5 y 0,26 con 0,9; si fueran independientes sería 0,57.",
       "error compartido: 1 = 0,0 · 2 = 0,5 · 3 = 0,9", "VPP tras 2 etapas", (0, 0.8), [1, 2, 3], [0.59, 0.44, 0.26],
       ["0,59", "0,44", "0,26"], AZUL, ref=0.57)

lz = Lienzo("En riesgo con norma importada o local", "Con norma importada el porcentaje en riesgo sube de 6,7 a 22,7 por ciento al desplazar la población 0,75 DE; con norma local queda en 6,7.",
            "Diferencia local respecto de la norma (DE)", "% en riesgo", (-0.75, 0), (0, 26))
lz.ejes()
lz.linea([-0.75, -0.5, -0.25, 0.0], [22.7, 15.9, 10.6, 6.7], ROJO, "norma importada")
lz.puntos([-0.75, -0.5, -0.25, 0.0], [22.7, 15.9, 10.6, 6.7], ROJO, r=4, opacidad=1)
lz.linea([-0.75, 0.0], [6.7, 6.7], AZUL, "norma local")
guardar(carpeta("140") / "figura-1.svg", lz)
print("figuras de la parte 13 generadas")
