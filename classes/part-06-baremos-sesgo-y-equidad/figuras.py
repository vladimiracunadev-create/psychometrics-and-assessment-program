"""Figuras de las clases 061 a 070 (parte 06). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

import math
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


def barras(n, titulo, desc, xl, yl, yr, xs, ys, etiquetas, color=AZUL, ancho=0.6, xr=None):
    lz = Lienzo(titulo, desc, xl, yl, xr or (0.4, len(xs) + 0.6), yr)
    lz.ejes()
    lz.barras(xs, ys, ancho, color)
    for x, y, t in zip(xs, ys, etiquetas, strict=True):
        lz.texto(x - 0.3, y + (yr[1] - yr[0]) * 0.03, t)
    guardar(carpeta(n) / "figura-1.svg", lz)


def fi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


xs = [60 + i for i in range(81)]
lz = Lienzo("Percentil según el puntaje bruto", "Con media 100 y DE 15 el percentil sube rapido en el centro y casi no cambia en las colas.",
            "Puntaje bruto", "Percentil", (60, 140), (0, 100))
lz.ejes()
lz.linea(xs, [100 * fi((x - 100.2) / 14.8) for x in xs], AZUL)
lz.vertical(100, ROJO, "5 puntos = 13,5 de percentil")
guardar(carpeta("061") / "figura-1.svg", lz)

barras("062", "Percentil del puntaje 105 según el baremo", "El percentil es 64,7 con el baremo poblacional, 41,5 con el de conveniencia y 63,0 con el de conveniencia reponderado.",
       "1 poblacional · 2 conveniencia · 3 reponderado", "Percentil", (0, 80), [1, 2, 3], [64.7, 41.5, 63.0], ["64,7", "41,5", "63,0"])

lz = Lienzo("|Δ| de Mantel-Haenszel por ítem", "Los items 1 a 3 tienen |Δ| menor que 0,4; el item 7, con DIF sembrado, 2,03 (clase C).",
            "Ítem (1, 2, 3 y 7)", "|Δ|", (0.4, 4.6), (0, 2.5))
lz.ejes()
lz.barras([1, 2, 3, 4], [0.17, 0.24, 0.35, 2.03], 0.6, AZUL)
lz.linea([0.4, 4.6], [1.0, 1.0], VERDE, "umbral B (1,0)", punteada=True)
lz.linea([0.4, 4.6], [1.5, 1.5], ROJO, "umbral C (1,5)", punteada=True)
guardar(carpeta("063") / "figura-1.svg", lz)

lz = Lienzo("Selección, TPR y VPP por grupo y mundo", "En el mundo 2 el VPP del grupo B cae a 0,595; en ambos mundos la selección de B es 0,160 frente a 0,307 de A.",
            "Métrica (1 selección, 2 TPR, 3 VPP)", "Valor", (0.4, 3.6), (0, 0.9))
lz.ejes()
lz.barras([0.8, 1.8, 2.8], [0.307, 0.453, 0.742], 0.2, AZUL)
lz.barras([1.0, 2.0, 3.0], [0.160, 0.285, 0.715], 0.2, VERDE)
lz.barras([1.2, 2.2, 3.2], [0.160, 0.326, 0.595], 0.2, ROJO)
lz.texto(0.5, 0.85, "azul: A · verde: B (mundo 1) · rojo: B (mundo 2)")
guardar(carpeta("064") / "figura-1.svg", lz)

barras("065", "Congruencia alta, medias distorsionadas", "Congruencia de Tucker 0,986 y diferencia de medias 0,71 aunque el rasgo medio es igual.",
       "1 = φ de Tucker · 2 = dif. de medias (puntos)", "Valor", (0, 1.2), [1, 2], [0.986, 0.71], ["0,986", "0,71"], ROJO, 0.5)

lz = Lienzo("T lineal frente a T normalizado", "En una prueba con techo, la cola larga da T=63 lineal y T=70 normalizado para el maximo.",
            "Puntaje bruto", "Puntaje T", (5, 42), (0, 80))
lz.ejes()
br = [10, 20, 28, 34, 38, 40]
lz.linea(br, [7.4, 26.0, 40.9, 52.0, 59.5, 63.2], AZUL, "T lineal")
lz.linea(br, [19.1, 30.1, 40.7, 50.0, 59.1, 70.1], ROJO, "T normalizado")
guardar(carpeta("066") / "figura-1.svg", lz)

lz = Lienzo("Salto artificial en el borde de banda", "Dos ninos de 6;11 y 7;00 con bruto 30: T = 76,0 y 62,2 con bandas; 70,1 y 69,0 con norma continua.",
            "Edad (6;11 y 7;00)", "Puntaje T", (6.85, 7.05), (55, 80))
lz.ejes(n=5)
lz.linea([6.92, 7.00], [76.0, 62.2], ROJO, "bandas")
lz.puntos([6.92, 7.00], [76.0, 62.2], ROJO, r=5, opacidad=1)
lz.linea([6.92, 7.00], [70.1, 69.0], AZUL, "continua")
lz.puntos([6.92, 7.00], [70.1, 69.0], AZUL, r=5, opacidad=1)
guardar(carpeta("067") / "figura-1.svg", lz)

lz = Lienzo("Validez y razón de tasas según el peso del predictor 1", "Bajar el peso del predictor con mayor d sube la razon de tasas de 0,16 a 0,74 y reduce la validez de 0,50 a 0,30.",
            "Peso del predictor 1", "Valor", (0, 1), (0, 0.8))
lz.ejes()
w = [1.0, 0.8, 0.6, 0.5, 0.4, 0.2, 0.0]
lz.linea(w, [0.500, 0.533, 0.535, 0.516, 0.484, 0.394, 0.300], AZUL, "validez")
lz.linea(w, [0.16, 0.17, 0.22, 0.27, 0.33, 0.52, 0.74], ROJO, "razón de tasas")
guardar(carpeta("068") / "figura-1.svg", lz)

barras("069", "Ganancia por tiempo extendido", "Prueba de velocidad: gana 3,2 el grupo sin necesidad y 7,2 el grupo con necesidad; prueba de poder: 0 en ambos.",
       "1 velocidad sin nec. · 2 velocidad con nec. · 3 poder sin · 4 poder con", "Ganancia (ítems)", (0, 9), [1, 2, 3, 4], [3.2, 7.2, 0.0, 0.0], ["3,2", "7,2", "0,0", "0,0"])

lz = Lienzo("Diferencia de grupos aparente por ítems desplazados", "Con 5 items desplazados aparece d = 0,38 que no existe en el rasgo; con solo items invariantes d vuelve a casi 0.",
            "Escenario (1 sin desplazar; 2 = 1 ítem; 3 = 3; 4 = 5; 5 = 3 con +1,2)", "d de Cohen", (0.5, 5.5), (-0.1, 0.6))
lz.ejes()
lz.linea([1, 2, 3, 4, 5], [-0.02, 0.05, 0.22, 0.38, 0.48], ROJO, "todos los ítems")
lz.puntos([1, 2, 3, 4, 5], [-0.02, 0.05, 0.22, 0.38, 0.48], ROJO, r=4, opacidad=1)
lz.linea([1, 2, 3, 4, 5], [-0.01, -0.03, -0.02, -0.03, -0.01], AZUL, "solo invariantes")
guardar(carpeta("070") / "figura-1.svg", lz)
print("figuras de la parte 06 generadas")
