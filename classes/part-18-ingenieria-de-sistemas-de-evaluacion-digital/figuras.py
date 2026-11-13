"""Figuras de las clases 181 a 190 (parte 18). Valores tomados de la ejecucion de cada lab.py."""
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


barras("181", "Ítems de cada instrumento del catálogo", "disc-abierto 32 ítems, ipip-neo-120 120, ipip-via-r 96, onet-riasec-sf 60 y valores-spranger 36.",
       "1 disc-abierto · 2 ipip-neo-120 · 3 ipip-via-r · 4 onet-riasec-sf · 5 valores-spranger", "Ítems", (0, 150), [1, 2, 3, 4, 5],
       [32, 120, 96, 60, 36], ["32", "120", "96", "60", "36"], AZUL)

barras("182", "Definiciones defectuosas rechazadas", "Las cinco definiciones defectuosas fueron rechazadas con mensaje claro.",
       "1 = defectuosas probadas · 2 = rechazadas", "Definiciones", (0, 7), [1, 2], [5, 5], ["5", "5"], VERDE, 0.5)

barras("183", "Avance de cada instrumento al pausar", "Valores-spranger 36 de 36 ítems respondidos y disc-abierto 24 de 32.",
       "1 = valores-spranger (36) · 2 = disc-abierto (32)", "Ítems respondidos", (0, 45), [1, 2], [36, 24], ["36 de 36", "24 de 32"], AZUL, 0.5)

grupos("184", "Sensibilidad, especificidad y VPP de dos reglas de marcado", "Mediana menor a 2 s: 0,46, 0,93 y 0,46. Más de 50 por ciento de respuestas rápidas: 0,23, 1,00 y 0,92.",
       "1 = mediana < 2 s · 2 = más de 50 % de respuestas rápidas", "Valor", (0, 1.2), ["a", "b"],
       [[0.46, 0.23], [0.93, 1.00], [0.46, 0.92]], [AZUL, ROJO, VERDE], "azul: sensibilidad · rojo: especificidad · verde: VPP")

barras("185", "RMSE del CAT puro y del CAT balanceado", "El CAT puro tiene RMSE 0,309 y el CAT con balance 5/5/5, 0,338.",
       "1 = CAT puro · 2 = CAT con balance 5/5/5", "RMSE de θ", (0, 0.45), [1, 2], [0.309, 0.338], ["0,309", "0,338"], AZUL, 0.5)

barras("186", "Contraste de cada elemento de la interfaz", "Contraste: texto principal 17,40; gris 4,54; gris claro 2,32; botón primario 4,63; botón deshabilitado 2,19; error en rojo 4,77; opción seleccionada 6,40. Mínimo AA: 4,5.",
       "1 principal · 2 gris · 3 gris claro · 4 botón · 5 deshabilitado · 6 error · 7 seleccionada", "Contraste (:1)", (0, 20), [1, 2, 3, 4, 5, 6, 7],
       [17.40, 4.54, 2.32, 4.63, 2.19, 4.77, 6.40], ["17,4", "4,54", "2,32", "4,63", "2,19", "4,77", "6,40"], AZUL, ref=4.5)

barras("187", "Protocolos que coinciden entre las dos implementaciones", "En cada uno de los cinco instrumentos coinciden 200 de 200 protocolos.",
       "1 disc · 2 neo · 3 via · 4 riasec · 5 spranger", "Protocolos que coinciden (de 200)", (0, 250), [1, 2, 3, 4, 5],
       [200, 200, 200, 200, 200], ["200", "200", "200", "200", "200"], VERDE)

barras("188", "Plazos de retención por categoría", "Respuestas 365 días, telemetría agregada 180 días y consentimientos 1 825 días.",
       "1 = respuestas · 2 = telemetría agregada · 3 = consentimientos", "Días", (0, 2200), [1, 2, 3], [365, 180, 1825], ["365", "180", "1 825"], AZUL)

barras("189", "Casos de prueba de neutralización de fórmulas", "De cuatro campos de prueba, uno no cambió y tres fueron neutralizados con un apóstrofo.",
       "1 = sin cambio · 2 = neutralizados", "Campos de prueba", (0, 5), [1, 2], [1, 3], ["1", "3"], ROJO, 0.5)

barras("190", "Casos de prueba del detector de licencias", "Los cinco casos de prueba (MIT, GPL, Apache-2.0, CC BY-NC-SA y texto vacío) se resolvieron correctamente.",
       "1 = casos probados · 2 = resueltos correctamente", "Casos", (0, 7), [1, 2], [5, 5], ["5", "5"], VERDE, 0.5)
print("figuras de la parte 18 generadas")
