"""Figuras de las clases 022 a 030 (parte 02). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

import math
import pathlib
import random
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402

NARANJA = "#a4561b"


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


def barras(n, titulo, desc, xl, yl, yr, xs, ys, etiquetas, color=AZUL, ancho=0.6, xr=None):
    lz = Lienzo(titulo, desc, xl, yl, xr or (0.4, len(xs) + 0.6), yr)
    lz.ejes()
    lz.barras(xs, ys, ancho, color)
    for x, y, t in zip(xs, ys, etiquetas, strict=True):
        lz.texto(x - 0.28, y + (yr[1] - yr[0]) * 0.03, t)
    guardar(carpeta(n) / "figura-1.svg", lz)


barras("022", "Alfa en tres escenarios", "Alfa de 0,868 (unidimensional), 0,779 (dos dimensiones independientes) y 0,836 (con un item de ruido).",
       "Escenario (1 unidimensional, 2 dos dimensiones, 3 con ítem de ruido)", "Alfa de Cronbach", (0, 1), [1, 2, 3], [0.868, 0.779, 0.836], ["0,868", "0,779", "0,836"])

lz = Lienzo("Alfa frente a omega según las cargas", "Con cargas iguales alfa y omega coinciden; con cargas muy desiguales alfa baja a 0,569 y omega a 0,644.",
            "Caso (1 cargas iguales, 2 desiguales, 3 muy desiguales)", "Coeficiente", (0.4, 3.6), (0, 1))
lz.ejes()
lz.barras([0.85, 1.85, 2.85], [0.770, 0.748, 0.569], 0.3, AZUL)
lz.barras([1.15, 2.15, 3.15], [0.771, 0.769, 0.644], 0.3, VERDE)
lz.texto(0.55, 0.88, "azul: alfa · verde: omega")
guardar(carpeta("023") / "figura-1.svg", lz)

barras("024", "Estabilidad en cuatro situaciones", "Correlacion test-retest de 0,914, 0,506, 0,727 y 0,920; el efecto de practica deja r casi intacta aunque todo el grupo suba una desviacion.",
       "1 poco ruido · 2 mucho ruido · 3 rasgo cambia · 4 práctica", "r test-retest", (0, 1), [1, 2, 3, 4], [0.914, 0.506, 0.727, 0.920], ["0,914", "0,506", "0,727", "0,920"])

rhos = [0.5 + 0.005 * i for i in range(100)]
lz = Lienzo("Error típico de medida según la fiabilidad (DE = 15)", "El ETM baja de 10,6 con fiabilidad 0,50 a 1,5 con 0,99; con 0,90 vale 4,74.",
            "Fiabilidad", "ETM (puntos)", (0.5, 1.0), (0, 11))
lz.ejes()
lz.linea(rhos, [15 * math.sqrt(1 - r) for r in rhos], AZUL)
lz.vertical(0.90, ROJO, "ρ = 0,90 → ETM 4,74")
guardar(carpeta("025") / "figura-1.svg", lz)

lz = Lienzo("Techo: escala equilibrada frente a escala fácil", "Porcentaje de personas a menos de 3 puntos del maximo: 1,6 % en la equilibrada y 20,2 % en la facil.",
            "Escala (1 equilibrada, 2 fácil)", "% a menos de 3 puntos del máximo", (0.4, 2.6), (0, 25))
lz.ejes()
lz.barras([1, 2], [1.6, 20.2], 0.5, ROJO)
lz.texto(0.8, 3, "1,6 %")
lz.texto(1.8, 21.3, "20,2 %")
guardar(carpeta("026") / "figura-1.svg", lz)

rng = random.Random(20260819)
xs = [rng.random() for _ in range(199)]
ys = [rng.random() for _ in range(199)]
lz = Lienzo("Un solo punto fabrica una correlación", "Nube sin relacion mas un punto extremo en (8, 8): Pearson sube a 0,33 y Spearman queda en 0,12.",
            "x", "y", (0, 9), (0, 9))
lz.ejes()
lz.puntos(xs, ys)
lz.puntos([8], [8], ROJO, r=7, opacidad=1)
lz.texto(5.2, 8.2, "valor extremo (8, 8)", ROJO)
guardar(carpeta("027") / "figura-1.svg", lz)

barras("028", "KR-20 según la dificultad de la prueba", "KR-20 de 0,846 con dificultad media, 0,811 con dificultad dispersa y 0,712 si toda la prueba es facil.",
       "Prueba (1 dificultad media, 2 dispersa, 3 toda fácil)", "KR-20", (0, 1), [1, 2, 3], [0.846, 0.811, 0.712], ["0,846", "0,811", "0,712"])

barras("029", "Distintas medidas de acuerdo, distintas conclusiones", "Acuerdo crudo 0,865 frente a kappa 0,413; correlacion 0,850 y CCI de consistencia 0,850 frente a CCI de acuerdo absoluto 0,580.",
       "1 acuerdo crudo · 2 kappa · 3 Pearson · 4 CCI consist. · 5 CCI absoluto", "Valor", (0, 1), [1, 2, 3, 4, 5], [0.865, 0.413, 0.850, 0.850, 0.580],
       ["0,865", "0,413", "0,850", "0,850", "0,580"])

lz = Lienzo("Cobertura del intervalo según el puntaje observado", "El intervalo centrado en el observado (a) cubre 0,83 en los extremos; el centrado en el verdadero estimado (b) mantiene 0,95.",
            "Grupo (1 todos, 2 ≥120, 3 ≥130, 4 85–115, 5 ≤70)", "Cobertura", (0.5, 5.5), (0.7, 1.0))
lz.ejes(n=6)
lz.linea([1, 2, 3, 4, 5], [0.949, 0.894, 0.834, 0.965, 0.831], ROJO, "(a) centrado en lo observado")
lz.puntos([1, 2, 3, 4, 5], [0.949, 0.894, 0.834, 0.965, 0.831], ROJO, r=4, opacidad=1)
lz.linea([1, 2, 3, 4, 5], [0.950, 0.949, 0.950, 0.950, 0.949], VERDE, "(b) centrado en el verdadero estimado")
lz.linea([0.5, 5.5], [0.95, 0.95], "#888888", None, punteada=True)
guardar(carpeta("030") / "figura-1.svg", lz)
print("figuras de la parte 02 generadas")
