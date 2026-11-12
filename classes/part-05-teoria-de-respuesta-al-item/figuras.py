"""Figuras de las clases 051 a 060 (parte 05). Valores tomados de la ejecucion de cada lab.py o de las formulas del modelo."""
from __future__ import annotations

import math
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402

NARANJA = "#a4561b"


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


def logistica(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def barras(n, titulo, desc, xl, yl, yr, xs, ys, etiquetas, color=AZUL, ancho=0.6):
    lz = Lienzo(titulo, desc, xl, yl, (0.4, len(xs) + 0.6), yr)
    lz.ejes()
    lz.barras(xs, ys, ancho, color)
    for x, y, t in zip(xs, ys, etiquetas, strict=True):
        lz.texto(x - 0.3, y + (yr[1] - yr[0]) * 0.03, t)
    guardar(carpeta(n) / "figura-1.svg", lz)


b = [-1.8, -1.2, -0.7, -0.3, 0.0, 0.3, 0.7, 1.2, 1.8, 2.4]
p_baja = [0.67, 0.54, 0.45, 0.37, 0.30, 0.25, 0.20, 0.13, 0.08, 0.05]
p_alta = [0.93, 0.87, 0.80, 0.75, 0.70, 0.64, 0.57, 0.45, 0.34, 0.24]
lz = Lienzo("La proporción de aciertos cambia con el grupo", "Proporcion de aciertos (p) de 10 items en un grupo de habilidad baja y en uno alto; el parametro b estimado es el mismo en ambos.",
            "Dificultad real del ítem (b)", "Proporción de aciertos (p)", (-2, 2.6), (0, 1))
lz.ejes()
lz.linea(b, p_baja, ROJO, "grupo bajo")
lz.puntos(b, p_baja, ROJO, r=4, opacidad=1)
lz.linea(b, p_alta, AZUL, "grupo alto")
lz.puntos(b, p_alta, AZUL, r=4, opacidad=1)
guardar(carpeta("051") / "figura-1.svg", lz)

real = [-2.00, -1.71, -1.43, -1.14, -0.86, -0.57, -0.29, 0.00, 0.29, 0.57, 0.86, 1.14, 1.43, 1.71, 2.00]
est = [-2.07, -1.63, -1.66, -1.12, -0.83, -0.52, -0.16, -0.03, 0.15, 0.65, 0.81, 1.29, 1.44, 1.73, 1.95]
lz = Lienzo("Dificultades reales y estimadas (Rasch)", "Quince items: las dificultades estimadas quedan casi sobre la diagonal (r = 0,997).",
            "Dificultad real (logits)", "Dificultad estimada (logits)", (-2.5, 2.5), (-2.5, 2.5))
lz.ejes()
lz.linea([-2.5, 2.5], [-2.5, 2.5], ROJO, "igualdad", punteada=True)
lz.puntos(real, est, AZUL, r=5, opacidad=0.9)
guardar(carpeta("052") / "figura-1.svg", lz)

ths = [-4 + 0.1 * i for i in range(81)]
lz = Lienzo("Curvas características de tres ítems", "Un item con a=2 es mas empinado; con c=0,2 la curva parte de 0,2.", "Habilidad (θ)", "Probabilidad de acierto", (-4, 4), (0, 1))
lz.ejes()
lz.linea(ths, [logistica(1 * (t - 0)) for t in ths], AZUL, "a=1, c=0")
lz.linea(ths, [logistica(2 * (t - 0)) for t in ths], ROJO, "a=2, c=0")
lz.linea(ths, [0.2 + 0.8 * logistica(1 * (t - 0)) for t in ths], VERDE, "a=1, c=0,2")
guardar(carpeta("053") / "figura-1.svg", lz)

items = {"A": (0.6, -2), "B": (1.0, 0), "C": (2.0, 0), "D": (1.5, 1.5), "E": (2.0, -1)}
ths = [-3 + 0.1 * i for i in range(61)]
total = [sum(a * a * logistica(a * (t - bb)) * (1 - logistica(a * (t - bb))) for a, bb in items.values()) for t in ths]
lz = Lienzo("Información del test", "La informacion del test suma la de cinco items y es maxima entre -1 y 1.", "Habilidad (θ)", "Información", (-3, 3), (0, 2.2))
lz.ejes()
for nombre, (a, bb), col in zip(items, items.values(), [AZUL, VERDE, ROJO, NARANJA, "#5a3d99"], strict=True):
    lz.linea(ths, [a * a * logistica(a * (t - bb)) * (1 - logistica(a * (t - bb))) for t in ths], col, nombre)
lz.linea(ths, total, "#111111", "test")
guardar(carpeta("054") / "figura-1.svg", lz)

barras("055", "CAT frente a test fijo", "RMSE de theta: 0,295 con CAT (14,7 items) y 0,438 con un test fijo de 20 items.",
       "1 = CAT (14,7 ítems) · 2 = fijo (20 ítems)", "RMSE de θ (menor es mejor)", (0, 0.5), [1, 2], [0.295, 0.438], ["0,295", "0,438"], VERDE, 0.5)

lz = Lienzo("Estimadores ML y EAP según el patrón", "Con patrones extremos el EAP se acerca a 0 mas que el ML; con puntajes perfectos o nulos el ML no existe.",
            "Patrón (1 un acierto, 2 cinco aciertos, 3 nueve aciertos)", "θ estimado", (0.8, 3.2), (-3, 3))
lz.ejes()
lz.linea([1, 2, 3], [-2.35, 0.08, 2.45], ROJO, "ML")
lz.puntos([1, 2, 3], [-2.35, 0.08, 2.45], ROJO, r=4, opacidad=1)
lz.linea([1, 2, 3], [-1.46, 0.06, 1.49], AZUL, "EAP")
lz.puntos([1, 2, 3], [-1.46, 0.06, 1.49], AZUL, r=4, opacidad=1)
guardar(carpeta("056") / "figura-1.svg", lz)

lz = Lienzo("Fiabilidad condicional de dos diseños", "El test concentrado es mas fiable en el centro (0,87) y cae a 0,44 en los extremos; el amplio conserva 0,64.",
            "Habilidad (θ)", "Fiabilidad condicional", (-3, 3), (0.3, 1))
lz.ejes()
xs = [-3, -2, -1, 0, 1, 2, 3]
lz.linea(xs, [0.64, 0.76, 0.80, 0.81, 0.80, 0.76, 0.64], AZUL, "amplio")
lz.linea(xs, [0.44, 0.69, 0.84, 0.87, 0.84, 0.69, 0.44], ROJO, "concentrado")
guardar(carpeta("057") / "figura-1.svg", lz)

umbrales = [-1.5, -0.5, 0.5, 1.5]
ths = [-3.5 + 0.1 * i for i in range(71)]


def prob_cat(t, k):
    acum = [1.0] + [logistica(1.5 * (t - u)) for u in umbrales] + [0.0]
    return acum[k] - acum[k + 1]


lz = Lienzo("Probabilidad de cada categoría (respuesta graduada)", "Cada una de las cinco categorias es la mas probable en un tramo de theta.",
            "Habilidad (θ)", "Probabilidad", (-3.5, 3.5), (0, 1))
lz.ejes()
for k, col in zip(range(5), [ROJO, NARANJA, VERDE, AZUL, "#5a3d99"], strict=True):
    lz.linea(ths, [prob_cat(t, k) for t in ths], col, f"cat {k + 1}")
guardar(carpeta("058") / "figura-1.svg", lz)

barras("059", "Porcentaje de aprobados según el método", "Sin equiparar aprueba 6,8 por ciento; la media y la lineal, 20,9; el equipercentil, 32,5; la referencia es 30,3.",
       "1 ref. · 2 sin equiparar · 3 media · 4 lineal · 5 equipercentil", "Aprobados", (0, 0.4), [1, 2, 3, 4, 5], [0.303, 0.068, 0.209, 0.209, 0.325],
       ["30,3 %", "6,8 %", "20,9 %", "20,9 %", "32,5 %"])

barras("060", "Precisión en las colas según banco y regla", "RMSE en las colas: 0,420 y 0,436 con banco amplio; 0,530 y 0,531 con banco estrecho.",
       "1 amplio/info · 2 amplio/random · 3 estrecho/info · 4 estrecho/random", "RMSE en las colas", (0, 0.65), [1, 2, 3, 4], [0.420, 0.436, 0.530, 0.531],
       ["0,420", "0,436", "0,530", "0,531"], ROJO)
print("figuras de la parte 05 generadas")
