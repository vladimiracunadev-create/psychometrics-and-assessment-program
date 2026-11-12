"""Figuras de las clases 091 a 100 (parte 09). Valores tomados de la ejecucion de cada lab.py."""
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


lz = Lienzo("Sensibilidad (d′) y criterio (c) por bloque", "d' baja de 2,04 a 1,64 mientras el criterio c sube de -0,03 a 0,46: el decremento es en buena parte cautela.",
            "Bloque", "Valor", (1, 4), (-0.5, 2.5))
lz.ejes()
lz.linea([1, 2, 3, 4], [2.04, 1.94, 1.79, 1.64], AZUL, "d′")
lz.puntos([1, 2, 3, 4], [2.04, 1.94, 1.79, 1.64], AZUL, r=4, opacidad=1)
lz.linea([1, 2, 3, 4], [-0.03, 0.15, 0.32, 0.46], ROJO, "c")
lz.puntos([1, 2, 3, 4], [-0.03, 0.15, 0.32, 0.46], ROJO, r=4, opacidad=1)
guardar(carpeta("091") / "figura-1.svg", lz)

barras("092", "Pendiente de búsqueda visual", "Pendiente de 0,40 ms por elemento en busqueda de rasgo y de 12,45 en busqueda de conjuncion.",
       "1 = rasgo · 2 = conjunción", "ms por elemento", (0, 15), [1, 2], [0.40, 12.45], ["0,40", "12,45"], AZUL, 0.5)

lz = Lienzo("Fiabilidad por resumen de tiempos de reacción", "La mediana y la media recortada tienen mas fiabilidad que la media en un dispositivo ideal y en uno ruidoso.",
            "Resumen (1 media, 2 mediana, 3 media recortada)", "Fiabilidad (SB)", (0.4, 3.6), (0.7, 0.9))
lz.ejes()
lz.barras([0.85, 1.85, 2.85], [0.818, 0.864, 0.852], 0.3, AZUL)
lz.barras([1.15, 2.15, 3.15], [0.830, 0.861, 0.861], 0.3, ROJO)
lz.texto(0.5, 0.885, "azul: ideal · rojo: ruidoso")
guardar(carpeta("093") / "figura-1.svg", lz)

pos = list(range(1, 16))
vis = [0.62, 0.57, 0.53, 0.47, 0.45, 0.46, 0.41, 0.38, 0.40, 0.31, 0.33, 0.54, 0.56, 0.57, 0.56]
aud = [0.60, 0.52, 0.52, 0.50, 0.43, 0.42, 0.39, 0.40, 0.35, 0.35, 0.34, 0.65, 0.67, 0.72, 0.75]
lz = Lienzo("Curva de posición serial", "Probabilidad de recuerdo por posicion: forma de U, con mayor recencia en la modalidad auditiva.",
            "Posición en la lista", "Probabilidad de recuerdo", (1, 15), (0.2, 0.85))
lz.ejes()
lz.linea(pos, vis, AZUL, "visual")
lz.linea(pos, aud, ROJO, "auditiva")
guardar(carpeta("094") / "figura-1.svg", lz)

lz = Lienzo("Regla de puntuación de la memoria de trabajo", "Fiabilidad por mitades y correlacion con la capacidad verdadera segun la regla: todo-o-nada, credito parcial y amplitud maxima.",
            "Regla (1 todo-o-nada, 2 crédito parcial, 3 amplitud máxima)", "Valor", (0.4, 3.6), (0, 1))
lz.ejes()
lz.barras([0.85, 1.85, 2.85], [0.686, 0.787, 0.652], 0.3, AZUL)
lz.barras([1.15, 2.15, 3.15], [0.849, 0.816, 0.748], 0.3, VERDE)
lz.texto(0.5, 0.95, "azul: fiabilidad · verde: r con la capacidad")
guardar(carpeta("095") / "figura-1.svg", lz)

barras("096", "Fiabilidad entre formas de cada índice", "Aprendizaje total 0,934, ganancia 0,543, retencion 0,077 e intrusiones -0,056.",
       "1 total · 2 ganancia · 3 retención · 4 intrusiones (−0,056)", "Fiabilidad entre formas", (0, 1), [1, 2, 3, 4], [0.934, 0.543, 0.077, 0.0], ["0,934", "0,543", "0,077", "−0,056"])

lz = Lienzo("Fiabilidad según los ensayos por condición", "El tiempo medio es fiable con pocos ensayos; el efecto necesita cientos.", "Ensayos por condición", "Fiabilidad", (0, 200), (0, 1))
lz.ejes()
lz.linea([20, 60, 200], [0.938, 0.975, 0.986], AZUL, "RT medio")
lz.puntos([20, 60, 200], [0.938, 0.975, 0.986], AZUL, r=4, opacidad=1)
lz.linea([20, 60, 200], [0.109, 0.324, 0.620], ROJO, "efecto")
lz.puntos([20, 60, 200], [0.109, 0.324, 0.620], ROJO, r=4, opacidad=1)
guardar(carpeta("097") / "figura-1.svg", lz)

lz = Lienzo("Exceso medio de movimientos según el horizonte", "Con 3 discos el exceso cae de 92,9 (h=1) a 0,5 (h=6); con 4 discos, de 238,4 a 115,0.",
            "Horizonte de planificación (movimientos que ve el planificador)", "Exceso medio de movimientos", (0.5, 6.5), (0, 260))
lz.ejes()
lz.linea([1, 3, 6], [92.9, 22.5, 0.5], AZUL, "3 discos")
lz.puntos([1, 3, 6], [92.9, 22.5, 0.5], AZUL, r=4, opacidad=1)
lz.linea([1, 3, 6], [238.4, 203.1, 115.0], ROJO, "4 discos")
lz.puntos([1, 3, 6], [238.4, 203.1, 115.0], ROJO, r=4, opacidad=1)
guardar(carpeta("098") / "figura-1.svg", lz)

barras("099", "Proporción de objetivos en cada secuencia n-back", "Las secuencias de 1, 2 y 3-back tienen 29, 23 y 26 por ciento de objetivos.",
       "1 = 1-back · 2 = 2-back · 3 = 3-back", "% de objetivos", (0, 40), [1, 2, 3], [29, 23, 26], ["29 %", "23 %", "26 %"], VERDE)

lz = Lienzo("VPP según la prevalencia", "Con sensibilidad 0,85 y especificidad 0,90, el VPP es 7,9 por ciento con prevalencia de 1 por ciento y 78,5 por ciento con 30 por ciento.",
            "Prevalencia (%)", "VPP (%)", (0, 30), (0, 100))
lz.ejes()
lz.linea([1, 5, 10, 30], [7.9, 30.9, 48.6, 78.5], ROJO)
lz.puntos([1, 5, 10, 30], [7.9, 30.9, 48.6, 78.5], ROJO, r=4, opacidad=1)
guardar(carpeta("100") / "figura-1.svg", lz)
print("figuras de la parte 09 generadas")
