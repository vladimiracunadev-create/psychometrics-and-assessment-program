"""Figuras de las clases 101 a 110 (parte 10). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

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


barras("101", "Predicción de un criterio según el nivel de medida", "r con el criterio: dominio 0,295; faceta relevante 0,392; seis facetas 0,380.",
       "1 dominio · 2 faceta relevante · 3 seis facetas", "r con el criterio", (0, 0.5), [1, 2, 3], [0.295, 0.392, 0.380], ["0,295", "0,392", "0,380"])

barras("102", "Puntaje de facetas ante «todo 5»", "Una persona que marca siempre 5 obtiene 4,00 en A1, 1,00 en A2, 5,00 en C1, 2,00 en C2, 3,00 en E1 y 5,00 en N1: la clave no esta equilibrada por faceta.",
       "1 A1 · 2 A2 · 3 C1 · 4 C2 · 5 E1 · 6 N1", "Puntaje de la faceta", (0, 6), [1, 2, 3, 4, 5, 6], [4.0, 1.0, 5.0, 2.0, 3.0, 5.0], ["4", "1", "5", "2", "3", "5"], ROJO)

barras("103", "Cambio de tipo entre dos aplicaciones", "Cambian de tipo 17,2 por ciento; entre los cercanos al corte, 38,9 por ciento; con cuatro dimensiones, 54,1 por ciento.",
       "1 = cualquiera · 2 = cerca del corte · 3 = tipo de 4 letras", "% que cambia", (0, 70), [1, 2, 3], [17.2, 38.9, 54.1], ["17,2 %", "38,9 %", "54,1 %"], ROJO)

lz = Lienzo("Estilo dominante estable según la fiabilidad", "El porcentaje que mantiene su estilo dominante sube de 51,2 a 75,0 con fiabilidad de 0,6 a 0,9; el azar es 25 por ciento.",
            "Fiabilidad de cada escala", "% con el mismo estilo dominante", (0.6, 0.9), (0, 100))
lz.ejes()
lz.linea([0.6, 0.7, 0.8, 0.9], [51.2, 57.1, 64.7, 75.0], AZUL)
lz.puntos([0.6, 0.7, 0.8, 0.9], [51.2, 57.1, 64.7, 75.0], AZUL, r=4, opacidad=1)
lz.linea([0.6, 0.9], [25, 25], ROJO, "azar", punteada=True)
guardar(carpeta("104") / "figura-1.svg", lz)

lz = Lienzo("Estabilidad del temperamento según la distancia", "La correlacion observada cae de 0,683 a 0,400; la verdadera, de 0,850 a 0,522; la corregida la recupera.",
            "Distancia entre mediciones (pasos de 2 años)", "Correlación", (1, 4), (0.3, 0.95))
lz.ejes()
lz.linea([1, 2, 3, 4], [0.683, 0.572, 0.470, 0.400], ROJO, "observada")
lz.linea([1, 2, 3, 4], [0.850, 0.722, 0.614, 0.522], AZUL, "verdadera")
lz.linea([1, 2, 3, 4], [0.853, 0.714, 0.587, 0.500], VERDE, "corregida")
guardar(carpeta("105") / "figura-1.svg", lz)

barras("106", "Recuperación de k y relación con el autoinforme", "La tarea recupera k con r = 0,946, pero se relaciona con el autoinforme con r = 0,090.",
       "1 = log k verdadera vs estimada · 2 = log k vs autoinforme", "Correlación", (0, 1.1), [1, 2], [0.946, 0.090], ["0,946", "0,090"], AZUL, 0.5)

lz = Lienzo("Correlación entre valores según la distancia en el círculo", "Sin corregir, todas las correlaciones son positivas; centrado por persona, los opuestos correlacionan -0,69.",
            "Distancia en el círculo (1 cercano, 3 opuesto)", "Correlación media", (1, 3), (-0.9, 1))
lz.ejes()
lz.linea([1, 2, 3], [0.80, 0.64, 0.56], ROJO, "sin corregir")
lz.puntos([1, 2, 3], [0.80, 0.64, 0.56], ROJO, r=4, opacidad=1)
lz.linea([1, 2, 3], [0.22, -0.38, -0.69], AZUL, "centrado")
lz.puntos([1, 2, 3], [0.22, -0.38, -0.69], AZUL, r=4, opacidad=1)
guardar(carpeta("107") / "figura-1.svg", lz)

barras("108", "Coincidencia del top-5 entre dos aplicaciones", "Coinciden 2,54 de 5 fortalezas, frente a 1,04 esperado por puro azar.",
       "1 = observada · 2 = azar puro", "Fortalezas coincidentes (de 5)", (0, 5), [1, 2], [2.54, 1.04], ["2,54", "1,04"], VERDE, 0.5)

lz = Lienzo("CCI y fiabilidad del promedio de 20 días", "Extraversion (rasgo): CCI 0,81 y fiabilidad del promedio 0,99; animo (estado): CCI 0,08 y fiabilidad del promedio 0,64.",
            "Variable (1 = extraversión, 2 = ánimo)", "Valor", (0.4, 2.6), (0, 1.1))
lz.ejes()
lz.barras([0.85, 1.85], [0.81, 0.08], 0.3, AZUL)
lz.barras([1.15, 2.15], [0.99, 0.64], 0.3, VERDE)
lz.texto(0.5, 1.05, "azul: CCI · verde: fiabilidad del promedio de 20 días")
guardar(carpeta("109") / "figura-1.svg", lz)

lz = Lienzo("Sensibilidad y especificidad según el corte", "La sensibilidad baja de 0,81 a 0,21 y la especificidad sube de 0,69 a 0,99 al subir el corte.",
            "Corte de la escala de validez", "Valor", (1.5, 3.5), (0, 1.05))
lz.ejes()
cs = [1.5, 2.0, 2.5, 3.0, 3.5]
lz.linea(cs, [0.81, 0.67, 0.51, 0.34, 0.21], ROJO, "sensibilidad")
lz.linea(cs, [0.69, 0.83, 0.93, 0.97, 0.99], AZUL, "especificidad")
guardar(carpeta("110") / "figura-1.svg", lz)
print("figuras de la parte 10 generadas")
