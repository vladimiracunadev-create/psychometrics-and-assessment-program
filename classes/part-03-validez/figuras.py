"""Figuras de las clases 031 a 040 (parte 03). Valores tomados de la ejecucion de cada lab.py."""
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


lz = Lienzo("Fiable no es lo mismo que válido", "Vocabulario: fiabilidad 0,95 pero r con el criterio 0,09; razonamiento numerico: fiabilidad 0,80 y r 0,58.",
            "Prueba (1 vocabulario, 2 razonamiento numérico)", "Valor", (0.4, 2.6), (0, 1))
lz.ejes()
lz.barras([0.85, 1.85], [0.95, 0.80], 0.3, AZUL)
lz.barras([1.15, 2.15], [0.090, 0.584], 0.3, ROJO)
lz.texto(0.5, 0.97, "azul: fiabilidad · rojo: r con el criterio")
guardar(carpeta("031") / "figura-1.svg", lz)

icvi = [1, 1, 1, 1, 0.83, 0.83, 0.83, 0.83, 1, 1, 0.17, 0.0]
lz = Lienzo("I-CVI de 12 ítems", "Diez items superan el umbral 0,78; los items 11 (0,17) y 12 (0,00) quedan muy por debajo.", "Ítem", "I-CVI", (0.4, 12.6), (0, 1.1))
lz.ejes(n=5)
lz.barras(list(range(1, 13)), icvi, 0.6, AZUL)
lz.linea([0.4, 12.6], [0.78, 0.78], ROJO, "umbral 0,78", punteada=True)
guardar(carpeta("032") / "figura-1.svg", lz)

lz = Lienzo("El método compartido infla la correlación", "Con formato compartido, r(A,C) sube de 0,21 a 0,42 mientras r(B,C) baja a 0,18.",
            "Condición (1 sin método común, 2 A y C comparten formato)", "Correlación", (0.4, 2.6), (0, 0.6))
lz.ejes(n=6)
lz.barras([0.85, 1.85], [0.211, 0.421], 0.3, ROJO)
lz.barras([1.15, 2.15], [0.212, 0.181], 0.3, AZUL)
lz.texto(0.5, 0.56, "rojo: r(A,C) · azul: r(B,C)")
guardar(carpeta("033") / "figura-1.svg", lz)

lz = Lienzo("Qué tan bien selecciona un test", "Tasa de buen desempeno entre contratados segun la validez: 0,50 sin validez y 0,79 con validez 0,6.",
            "Validez del test (r)", "Tasa de buen desempeño", (0, 0.65), (0.4, 0.9))
lz.ejes()
lz.linea([0, 0.2, 0.4, 0.6], [0.498, 0.592, 0.685, 0.793], AZUL)
lz.puntos([0, 0.2, 0.4, 0.6], [0.498, 0.592, 0.685, 0.793], AZUL, r=4, opacidad=1)
lz.linea([0, 0.65], [0.5, 0.5], ROJO, "azar", punteada=True)
guardar(carpeta("034") / "figura-1.svg", lz)

lz = Lienzo("El impacto adverso crece con la selectividad", "Razon de tasas entre dos grupos (d = 0,5) segun el corte: 0,91 con corte 10 y 0,32 con corte 97.",
            "Corte (percentil global)", "Razón de tasas G2 / G1", (0, 100), (0, 1))
lz.ejes()
lz.linea([10, 30, 50, 70, 90, 97], [0.91, 0.78, 0.67, 0.56, 0.40, 0.32], ROJO)
lz.puntos([10, 30, 50, 70, 90, 97], [0.91, 0.78, 0.67, 0.56, 0.40, 0.32], ROJO, r=4, opacidad=1)
lz.linea([0, 100], [0.8, 0.8], AZUL, "alerta 0,80", punteada=True)
guardar(carpeta("035") / "figura-1.svg", lz)

lz = Lienzo("Matriz multirrasgo-multimétodo: poco y mucho método", "Con poco metodo la correlacion de validez (0,63) supera a las otras; con mucho metodo la hetero-mono (0,63) supera a la de validez (0,29).",
            "Condición (1 poco método, 2 mucho método)", "Correlación media", (0.4, 2.6), (0, 0.8))
lz.ejes()
lz.barras([0.8, 1.8], [0.630, 0.288], 0.22, VERDE)
lz.barras([1.0, 2.0], [0.167, 0.632], 0.22, ROJO)
lz.barras([1.2, 2.2], [0.115, 0.064], 0.22, AZUL)
lz.texto(0.5, 0.75, "verde: validez · rojo: hetero-mono · azul: hetero-hetero")
guardar(carpeta("036") / "figura-1.svg", lz)

lz = Lienzo("Generalizabilidad según el número de tareas", "G sube de 0,39 con una tarea a 0,89 con doce.", "Número de tareas", "Coeficiente G", (0, 12), (0, 1))
lz.ejes()
lz.linea([1, 2, 4, 8, 12], [0.394, 0.566, 0.723, 0.839, 0.887], AZUL)
lz.puntos([1, 2, 4, 8, 12], [0.394, 0.566, 0.723, 0.839, 0.887], AZUL, r=4, opacidad=1)
guardar(carpeta("037") / "figura-1.svg", lz)

barras("038", "Filtrar respuestas sin esfuerzo acerca el puntaje a la habilidad", "r con la habilidad: 0,882 con el puntaje bruto y 0,930 sin respuestas rapidas; aciertos 0,257 en rapidas y 0,508 en normales.",
       "1 r bruto · 2 r sin rápidas · 3 aciertos rápidas · 4 aciertos normales", "Valor", (0, 1), [1, 2, 3, 4], [0.882, 0.930, 0.257, 0.508], ["0,882", "0,930", "0,257", "0,508"])

barras("039", "Metaanálisis: observada, esperada y corregida", "r observada 0,358, esperada 0,346, corregida por atenuacion 0,516 y verdadera 0,50.",
       "1 observada · 2 esperada · 3 corregida · 4 verdadera", "Correlación", (0, 0.7), [1, 2, 3, 4], [0.358, 0.346, 0.516, 0.50], ["0,358", "0,346", "0,516", "0,50"])

lz = Lienzo("Falseamiento y quiénes quedan seleccionados", "Porcentaje de falseadores en el 10 por ciento superior: de 27 por ciento sin desplazamiento a 77 por ciento con desplazamiento de 1,5 DE.",
            "Desplazamiento medio de los falseadores (DE)", "% de falseadores en el top 10 %", (0, 1.5), (0, 100))
lz.ejes()
lz.linea([0, 0.5, 1.0, 1.5], [27.2, 43.3, 61.4, 76.9], ROJO)
lz.puntos([0, 0.5, 1.0, 1.5], [27.2, 43.3, 61.4, 76.9], ROJO, r=4, opacidad=1)
lz.linea([0, 1.5], [25, 25], AZUL, "25 % de la población", punteada=True)
guardar(carpeta("040") / "figura-1.svg", lz)
print("figuras de la parte 03 generadas")
