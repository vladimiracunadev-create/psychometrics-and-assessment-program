"""Figuras de las clases 151 a 160 (parte 15). Valores tomados de la ejecucion de cada lab.py."""
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


barras("151", "Coincidencia del código entre dos aplicaciones", "Coincide la primera letra en 69,2 por ciento, el conjunto de tres en 75,6 y el código exacto en 39,4.",
       "1 = primera letra · 2 = conjunto de tres · 3 = código exacto", "% de coincidencia", (0, 100), [1, 2, 3], [69.2, 75.6, 39.4],
       ["69,2 %", "75,6 %", "39,4 %"], AZUL)

barras("152", "Estabilidad del ranking de ocupaciones", "La misma ocupación queda primera en 33,9 por ciento y al menos 2 de 3 coinciden en 60,6 por ciento.",
       "1 = misma ocupación en 1.er lugar · 2 = al menos 2 de 3 en común", "% de aplicaciones", (0, 80), [1, 2], [33.9, 60.6], ["33,9 %", "60,6 %"], ROJO, 0.5)

grupos("153", "Peso verdadero y estimado de los valores", "Pesos verdaderos y estimados: autonomía 1,32 y 1,35; equilibrio 1,23 y 1,29; seguridad 1,15 y 1,13; ingreso 0,99 y 0,91; servicio 0,82 y 0,90; prestigio 0,49 y 0,42.",
       "1 autonomía · 2 equilibrio · 3 seguridad · 4 ingreso · 5 servicio · 6 prestigio", "Peso w", (0, 1.7), ["a", "b", "c", "d", "e", "f"],
       [[1.32, 1.23, 1.15, 0.99, 0.82, 0.49], [1.35, 1.29, 1.13, 0.91, 0.90, 0.42]], [AZUL, ROJO], "azul: verdadero · rojo: estimado")

barras("154", "Puntaje de cada opción", "D obtiene 6,95; B, 6,75; A, 6,50; y C, 5,90.",
       "1 = D · 2 = B · 3 = A · 4 = C", "Puntaje (de 10)", (0, 9), [1, 2, 3, 4], [6.95, 6.75, 6.50, 5.90], ["6,95", "6,75", "6,50", "5,90"], VERDE)

lz = Lienzo("Probabilidad posterior de cada nivel tras cada tarea", "Para un estudiante de nivel intermedio, el posterior del nivel intermedio sube y baja entre 0,29 y 0,66 en ocho tareas.",
            "Tareas realizadas", "Probabilidad posterior", (1, 8), (0, 1.0))
lz.ejes()
t = [1, 2, 3, 4, 5, 6, 7, 8]
lz.linea(t, [0.17, 0.07, 0.22, 0.11, 0.05, 0.13, 0.06, 0.03], ROJO, "básico")
lz.linea(t, [0.33, 0.29, 0.50, 0.48, 0.42, 0.66, 0.64, 0.57], VERDE, "intermedio")
lz.linea(t, [0.50, 0.64, 0.28, 0.41, 0.53, 0.21, 0.30, 0.40], AZUL, "avanzado")
guardar(carpeta("155") / "figura-1.svg", lz)

grupos("156", "Sensibilidad y especificidad de cada regla k de n", "2 de 3: 0,90 y 0,65; 3 de 5: 0,94 y 0,68; 4 de 5: 0,74 y 0,91; 5 de 8: 0,94 y 0,83; 6 de 8: 0,80 y 0,95; 8 de 12: 0,93 y 0,94.",
       "1 = 2 de 3 · 2 = 3 de 5 · 3 = 4 de 5 · 4 = 5 de 8 · 5 = 6 de 8 · 6 = 8 de 12", "Valor", (0, 1.15), ["a", "b", "c", "d", "e", "f"],
       [[0.90, 0.94, 0.74, 0.94, 0.80, 0.93], [0.65, 0.68, 0.91, 0.83, 0.95, 0.94]], [AZUL, ROJO], "azul: sensibilidad · rojo: especificidad")

grupos("157", "Pesos de perfil, currículo y evaluación", "Perfil, currículo y evaluación: seguridad 20, 10 y 5; planos 15, 25 y 30; equipos 20, 30 y 40; diagnóstico 20, 10 y 10; mantenimiento 15, 15 y 10; comunicación 10, 10 y 5 por ciento.",
       "1 seguridad · 2 planos · 3 equipos · 4 diagnóstico · 5 mantenimiento · 6 comunicación", "Peso (%)", (0, 50), ["a", "b", "c", "d", "e", "f"],
       [[20, 15, 20, 20, 15, 10], [10, 25, 30, 10, 15, 10], [5, 30, 40, 10, 10, 5]], [AZUL, VERDE, ROJO], "azul: perfil · verde: currículo · rojo: evaluación")

grupos("158", "TPR y FPR por grupo", "G0: TPR 0,37 y FPR 0,15. G1: TPR 0,39 y FPR 0,15.",
       "1 = G0 · 2 = G1", "Tasa", (0, 0.6), ["g0", "g1"],
       [[0.37, 0.39], [0.15, 0.15]], [AZUL, ROJO], "azul: TPR · rojo: FPR")

barras("159", "Brecha ponderada de cada destino", "Soporte técnico: brecha 1,08 (93,6 por ciento de ser el de menor brecha). Coordinación: 1,67 (6,3). Analista de datos: 2,33 (0,1).",
       "1 = soporte técnico · 2 = coordinación de proyectos · 3 = analista de datos junior", "Brecha ponderada", (0, 3), [1, 2, 3], [1.08, 1.67, 2.33],
       ["1,08 (93,6 %)", "1,67 (6,3 %)", "2,33 (0,1 %)"], AZUL)

grupos("160", "Tamaño de muestra por grupo", "Para d = 0,2: 393 sin ajustar, 252 con pretest y 616 por cursos. Para d = 0,3: 175, 112 y 274. Para d = 0,5: 63, 41 y 99.",
       "1 = d 0,2 · 2 = d 0,3 · 3 = d 0,5", "n por grupo", (0, 700), ["a", "b", "c"],
       [[393, 175, 63], [252, 112, 41], [616, 274, 99]], [AZUL, VERDE, ROJO], "azul: sin ajustar · verde: con pretest · rojo: por cursos")
print("figuras de la parte 15 generadas")
