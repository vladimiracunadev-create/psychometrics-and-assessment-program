"""Figuras de las clases 071 a 080 (parte 07). Valores tomados de la ejecucion de cada lab.py."""
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


barras("071", "Criterios de documentación cumplidos (de 8)", "Cuatro instrumentos cumplen 8 de 8; el IPIP-NEO-120 cumple 7 de 8 porque no declara su estado de validacion.",
       "1 DISC · 2 IPIP-NEO-120 · 3 IPIP-VIA-R · 4 O*NET · 5 Valores", "Criterios cumplidos", (0, 9), [1, 2, 3, 4, 5], [8, 7, 8, 8, 8], ["8", "7", "8", "8", "8"])

barras("072", "Fichas del catálogo según su licencia", "No verificada 56, no aplica 43, propietaria 36, abierta 3 y dominio publico 2.",
       "1 no verificada · 2 no aplica · 3 propietaria · 4 abierta · 5 dominio público", "Fichas", (0, 65), [1, 2, 3, 4, 5], [56, 43, 36, 3, 2], ["56", "43", "36", "3", "2"])

lz = Lienzo("Intervalos de tres resultados frente al corte", "Resultados 108, 85 y 130 con su intervalo; solo el de 108 incluye el corte de 105.",
            "Caso (1 = 108, 2 = 85, 3 = 130)", "Puntaje", (0.5, 3.5), (60, 150))
lz.ejes()
for x, lo, hi, col in [(1, 99, 117, ROJO), (2, 76, 94, AZUL), (3, 121, 139, AZUL)]:
    lz.linea([x, x], [lo, hi], col)
    lz.puntos([x, x], [lo, hi], col, r=5, opacidad=1)
lz.linea([0.5, 3.5], [105, 105], VERDE, "corte 105", punteada=True)
guardar(carpeta("073") / "figura-1.svg", lz)

barras("074", "Reglas cumplidas por dos procesos de selección", "El proceso A cumple las 8 reglas; el proceso B, que usa un cuestionario sin validar como filtro unico, solo 1.",
       "1 = A (diseño completo) · 2 = B (filtro único)", "Reglas cumplidas (de 8)", (0, 9), [1, 2], [8, 1], ["8", "1"], VERDE, 0.5)

barras("075", "Indicadores del examen de certificación", "Aprobados 65 por ciento, consistencia de clasificacion 86,7 por ciento y 38 por ciento de candidatos a menos de 4 puntos del corte.",
       "1 aprobados · 2 consistencia · 3 cerca del corte", "Proporción", (0, 1), [1, 2, 3], [0.65, 0.867, 0.38], ["65 %", "86,7 %", "38 %"])

barras("076", "Campos de una evaluación: qué se conserva y qué se elimina", "De 9 campos, 5 se conservan o se separan del resultado y 4 se eliminan por no tener finalidad.",
       "1 = conservar o separar · 2 = eliminar (sin finalidad)", "Campos", (0, 7), [1, 2], [5, 4], ["5", "4"], AZUL, 0.5)

barras("077", "Quién puede usarse según la finalidad", "Con finalidad de evaluacion se pueden usar 2 sujetos; con finalidad de investigacion, solo 1.",
       "1 = evaluación · 2 = investigación", "Sujetos utilizables", (0, 3.5), [1, 2], [2, 1], ["2", "1"], VERDE, 0.5)

lz = Lienzo("Riesgo de reidentificación según la generalización", "Sin generalizar el 61,5 por ciento es unico; con tramos de 10 y macrozona, 0 por ciento.",
            "Nivel (1 sin generalizar, 2 edad en tramos, 3 tramos + macrozona, 4 tramos de 20 + macrozona)", "%", (0.8, 4.2), (0, 105))
lz.ejes()
lz.linea([1, 2, 3, 4], [61.5, 3.6, 0.0, 0.0], ROJO, "únicos")
lz.linea([1, 2, 3, 4], [99.8, 32.3, 1.4, 0.4], AZUL, "grupos < 5")
guardar(carpeta("078") / "figura-1.svg", lz)

lz = Lienzo("Puntaje de tres personas y margen de revisión", "Puntajes 74,2, 58,5 y 44,0 con corte 60 y margen de revision de mas o menos 6,2; solo B queda dentro del margen.",
            "Persona (1 = A, 2 = B, 3 = C)", "Puntaje", (0.5, 3.5), (30, 90))
lz.ejes()
lz.barras([1, 2, 3], [74.2, 58.5, 44.0], 0.5, AZUL)
lz.linea([0.5, 3.5], [60, 60], VERDE, "corte 60", punteada=True)
lz.linea([0.5, 3.5], [53.8, 53.8], ROJO, "−6,2", punteada=True)
lz.linea([0.5, 3.5], [66.2, 66.2], ROJO, "+6,2", punteada=True)
guardar(carpeta("079") / "figura-1.svg", lz)

barras("080", "Cambio de la proporción de aciertos por ítem", "Los items no filtrados suben 0,007; los 10 filtrados suben 0,069.",
       "1 = no filtrados · 2 = filtrados", "Cambio medio de p", (0, 0.09), [1, 2], [0.007, 0.069], ["0,007", "0,069"], ROJO, 0.5)
print("figuras de la parte 07 generadas")
