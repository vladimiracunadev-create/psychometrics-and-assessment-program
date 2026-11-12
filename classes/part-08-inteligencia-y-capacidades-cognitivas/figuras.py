"""Figuras de las clases 081 a 090 (parte 08). Valores tomados de la ejecucion de cada lab.py."""
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


barras("081", "Tetrada media según el modelo", "Tetrada media de 0,0047 con un factor general y de 0,0790 con dos factores de grupo.",
       "1 = un factor general · 2 = dos factores de grupo", "|tetrada| media", (0, 0.1), [1, 2], [0.0047, 0.0790], ["0,0047", "0,0790"], AZUL, 0.5)

ed = [20, 30, 40, 50, 60, 70]
lz = Lienzo("Fluida y cristalizada según la edad", "Gf transversal cae de 1,41 a -1,01; Gf longitudinal de la cohorte 1966, de 0,21 a -0,51; Gc transversal baja poco.",
            "Edad (años)", "Puntaje (DE)", (20, 70), (-1.5, 1.8))
lz.ejes()
lz.linea(ed, [1.41, 0.99, 0.52, 0.0, -0.54, -1.01], ROJO, "Gf transversal")
lz.linea(ed, [1.36, 1.27, 1.18, 1.06, 0.96, 0.88], VERDE, "Gc transversal")
lz.linea([20, 30, 40, 50, 60], [0.21, 0.08, -0.12, -0.31, -0.51], AZUL, "Gf longitudinal")
guardar(carpeta("082") / "figura-1.svg", lz)

barras("083", "Ítems generados por regla", "Tres items por cada una de las cuatro reglas: aritmetica, geometrica, alternada y de segundo orden; todos con solucion unica.",
       "1 aritmética · 2 geométrica · 3 alternada · 4 segundo orden", "Ítems con solución única", (0, 4), [1, 2, 3, 4], [3, 3, 3, 3], ["3", "3", "3", "3"], VERDE)

lz = Lienzo("Legibilidad de tres versiones de una instrucción", "IFSZ de 61,6 (normal), 67,6 (bastante facil) y 9,1 (muy dificil).", "Versión (1 simple, 2 intermedia, 3 enrevesada)", "IFSZ", (0.4, 3.6), (0, 90))
lz.ejes()
lz.barras([1, 2, 3], [61.6, 67.6, 9.1], 0.55, AZUL)
lz.linea([0.4, 3.6], [40, 40], ROJO, "debajo de 40: muy difícil", punteada=True)
guardar(carpeta("084") / "figura-1.svg", lz)

barras("085", "Proporción en la opción más elegida", "Perfil que domina: 0,92 en la correcta; perfiles con error: 0,77 a 0,78 en su distractor tipico.",
       "1 domina · 2 divide · 3 suma · 4 decimal", "Proporción", (0, 1), [1, 2, 3, 4], [0.92, 0.77, 0.78, 0.78], ["0,92", "0,77", "0,78", "0,78"], AZUL)

lz = Lienzo("Errores según el ángulo de rotación", "La tasa de error sube de 0,045 a 0 grados a 0,169 a 180 grados.", "Ángulo (grados)", "Tasa de error", (0, 180), (0, 0.2))
lz.ejes()
lz.linea([0, 45, 90, 135, 180], [0.045, 0.079, 0.117, 0.131, 0.169], ROJO)
lz.puntos([0, 45, 90, 135, 180], [0.045, 0.079, 0.117, 0.131, 0.169], ROJO, r=4, opacidad=1)
guardar(carpeta("086") / "figura-1.svg", lz)

lz = Lienzo("Fiabilidad de la ganancia", "La fiabilidad de la ganancia baja de 0,88 a 0,67 cuando la correlacion pre-post sube de 0,19 a 0,70, con fiabilidad 0,90 en ambas.",
            "Correlación entre pre y post", "Fiabilidad de la ganancia", (0.1, 0.8), (0.5, 1))
lz.ejes()
lz.linea([0.19, 0.50, 0.70], [0.876, 0.801, 0.670], AZUL, "fórmula")
lz.puntos([0.19, 0.50, 0.70], [0.879, 0.804, 0.672], ROJO, r=5, opacidad=1)
guardar(carpeta("087") / "figura-1.svg", lz)

barras("088", "Perfiles planos con diferencias aparentes", "En personas con perfil verdaderamente plano, el 74,2 por ciento muestra alguna diferencia de 10 puntos o mas y el 28,8 por ciento supera el umbral fiable.",
       "1 = alguna diferencia ≥ 10 · 2 = supera el umbral fiable (16,1)", "% de personas", (0, 90), [1, 2], [74.2, 28.8], ["74,2 %", "28,8 %"], ROJO, 0.5)

barras("089", "IES según capacidad y cautela", "El indicador IES vale 1,468; 0,757; 0,582 y 2,165 en los cuatro casos; con la misma capacidad varia casi a la mitad.",
       "1 media-cauto · 2 media-apurado · 3 alta-apurado · 4 baja-cauto", "IES (menor es mejor)", (0, 2.6), [1, 2, 3, 4], [1.468, 0.757, 0.582, 2.165], ["1,468", "0,757", "0,582", "2,165"], AZUL)

lz = Lienzo("Fiabilidad de un compuesto", "La fiabilidad del compuesto crece con el numero de subpruebas y con su correlacion (subpruebas con fiabilidad 0,80).",
            "Número de subpruebas", "Fiabilidad del compuesto", (2, 6), (0.75, 1))
lz.ejes()
lz.linea([2, 4, 6], [0.800, 0.800, 0.800], "#888888", "r = 0,0")
lz.linea([2, 4, 6], [0.846, 0.895, 0.920], AZUL, "r = 0,3")
lz.linea([2, 4, 6], [0.867, 0.920, 0.943], VERDE, "r = 0,5")
guardar(carpeta("090") / "figura-1.svg", lz)
print("figuras de la parte 08 generadas")
