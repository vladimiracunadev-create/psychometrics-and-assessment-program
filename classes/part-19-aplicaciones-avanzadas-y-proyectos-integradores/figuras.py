"""Figuras de las clases 191 a 200 (parte 19). Valores tomados de la ejecucion de cada lab.py."""
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


grupos("191", "Sensibilidad, especificidad y VPP de las dos estrategias", "Etapa 1 sola: 0,96, 0,75 y 0,30. Etapa 1 más etapa 2: 0,79, 0,95 y 0,62.",
       "1 = etapa 1 sola · 2 = etapa 1 + etapa 2", "Valor", (0, 1.2), ["a", "b"],
       [[0.96, 0.79], [0.75, 0.95], [0.30, 0.62]], [AZUL, ROJO, VERDE], "azul: sensibilidad · rojo: especificidad · verde: VPP")

barras("192", "Requisitos del cargo cubiertos y brechas", "De siete requisitos, cuatro están cubiertos de forma descriptiva y tres son brechas.",
       "1 = cubiertos (descriptivo) · 2 = brechas", "Requisitos", (0, 6), [1, 2], [4, 3], ["4", "3"], AZUL, 0.5)

barras("193", "I-CVI de los 12 ítems", "I-CVI: i01 a i03, 1,00; i04, 0,50; i05 a i07, 1,00; i08, 0,83; i09, 0,50; i10, 1,00; i11, 0,83; i12, 1,00. Umbral: 0,78.",
       "ítems i01 a i12", "I-CVI", (0, 1.2), list(range(1, 13)),
       [1.00, 1.00, 1.00, 0.50, 1.00, 1.00, 1.00, 0.83, 0.50, 1.00, 0.83, 1.00],
       ["1", "1", "1", ".50", "1", "1", "1", ".83", ".50", "1", ".83", "1"], AZUL, 0.6, ref=0.78)

barras("194", "Reglas cumplidas por cada informe", "El informe generado cumple 5 de 5 reglas; el contraejemplo, 0 de 5.",
       "1 = informe generado · 2 = contraejemplo", "Reglas cumplidas (de 5)", (0, 6), [1, 2], [5, 0], ["5/5", "0/5"], VERDE, 0.5)

lz = Lienzo("Intervalo de Wilson de cada equipo publicado", "Operaciones 65 por ciento [50, 77]; Comercial 81 [64, 91]; Finanzas 64 [39, 84]; TI 11 [2, 44]; Legal suprimido por n menor a 5.",
            "% favorable", "1 Operaciones · 2 Comercial · 3 Finanzas · 4 TI", (0, 100), (0.5, 4.5))
lz.ejes()
for y, (a, b, p) in enumerate([(50, 77, 65), (64, 91, 81), (39, 84, 64), (2, 44, 11)], start=1):
    lz.linea([a, b], [y, y], AZUL)
    lz.puntos([p], [y], ROJO, r=5, opacidad=1)
guardar(carpeta("195") / "figura-1.svg", lz)

barras("196", "Coeficientes del estudio simulado", "Alfa 0,85; test-retest 0,84; validez convergente 0,36; validez discriminante -0,07.",
       "1 = alfa · 2 = test-retest · 3 = convergente · 4 = discriminante", "Coeficiente", (-0.2, 1.0), [1, 2, 3, 4], [0.85, 0.84, 0.36, -0.07],
       ["0,85", "0,84", "0,36", "-0,07"], AZUL)

barras("197", "Fichas verificadas y sin verificar", "De 140 fichas, 5 están verificadas y 135 sin verificar.",
       "1 = verificadas · 2 = sin verificar", "Fichas", (0, 160), [1, 2], [5, 135], ["5", "135"], ROJO, 0.5)

barras("198", "Índice de cambio fiable de cada estudiante", "RCI: Ana +2,45; Bruno +0,59; Carla -2,22; Diego +2,36; Elena +1,11; Fabián +3,06. El umbral de cambio fiable es 1,96.",
       "1 Ana · 2 Bruno · 3 Carla · 4 Diego · 5 Elena · 6 Fabián", "RCI", (-3, 4), [1, 2, 3, 4, 5, 6], [2.45, 0.59, -2.22, 2.36, 1.11, 3.06],
       ["+2,45", "+0,59", "-2,22", "+2,36", "+1,11", "+3,06"], AZUL, ref=1.96)

barras("199", "Comprobaciones y etapas del instrumento original", "Las siete comprobaciones automáticas de forma pasan y las siete etapas de validación siguen pendientes.",
       "1 = comprobaciones de forma superadas · 2 = etapas de validación por completar", "Cantidad", (0, 9), [1, 2], [7, 7], ["7", "7"], VERDE, 0.5)

grupos("200", "Clases escritas y con laboratorio en las 20 partes", "Cada una de las 20 partes tiene 10 clases escritas, todas con laboratorio, y ninguna planificada.",
       "1 a 20 = partes del programa", "Clases por parte", (0, 13), [str(i) for i in range(20)],
       [[10] * 20, [10] * 20], [AZUL, VERDE], "azul: escritas · verde: con laboratorio")
print("figuras de la parte 19 generadas")
