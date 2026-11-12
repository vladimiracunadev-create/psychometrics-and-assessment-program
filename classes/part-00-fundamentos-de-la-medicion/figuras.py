"""Figuras de las clases 006 a 010 (parte 00). Datos simulados con semilla fija o valores de cada lab.py."""
from __future__ import annotations

import math
import pathlib
import random
import statistics
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


# 006 Galton: regresion a la media
rng = random.Random(20260819)
padres = [rng.gauss(0, 1) for _ in range(5000)]
hijos = [0.5 * p + math.sqrt(0.75) * rng.gauss(0, 1) for p in padres]
lz = Lienzo("Hijos de padres altos: altos, pero menos extremos", "Dispersion de alturas estandarizadas de padres e hijos con correlacion 0,5; la recta de regresion tiene pendiente 0,5, no 1.",
            "Altura del padre (desviaciones típicas)", "Altura del hijo (desviaciones típicas)", (-4, 4), (-4, 4))
lz.ejes()
lz.puntos(padres[:700], hijos[:700])
lz.linea([-4, 4], [-4, 4], ROJO, "si fuera 1 a 1", punteada=True)
lz.linea([-4, 4], [-2, 2], VERDE, "pendiente real 0,5")
guardar(carpeta("006") / "figura-1.svg", lz)

# 007 constructo y tres operacionalizaciones
lz = Lienzo("Qué tanto se parece cada medida al constructo", "Correlacion con el constructo latente: autoinforme 0,81, tercero 0,59, conductual 0,41 y compuesto sin ponderar 0,80.",
            "Medida (1 autoinforme, 2 tercero, 3 conductual, 4 compuesto)", "Correlación con el constructo", (0.4, 4.6), (0, 1))
lz.ejes()
lz.barras([1, 2, 3, 4], [0.81, 0.59, 0.41, 0.80], 0.6, AZUL)
for x, v in zip([1, 2, 3, 4], [0.81, 0.59, 0.41, 0.80], strict=True):
    lz.texto(x - 0.2, v + 0.03, f"{v:.2f}")
guardar(carpeta("007") / "figura-1.svg", lz)

# 008 maximo frente a tipico
lz = Lienzo("Efecto de «querer verse bien»", "Tamano del cambio (d de Cohen) al pedir causar buena impresion: casi nulo en rendimiento maximo, 0,78 en desempeno tipico.",
            "Tipo de prueba (1 rendimiento máximo, 2 desempeño típico)", "d de Cohen", (0.4, 2.6), (-0.2, 1))
lz.ejes()
lz.barras([1, 2], [-0.01, 0.78], 0.5, ROJO)
lz.texto(0.8, 0.05, "d = −0,01")
lz.texto(1.8, 0.83, "d = 0,78")
guardar(carpeta("008") / "figura-1.svg", lz)

# 009 velocidad: items no alcanzados por posicion
pos = [1, 20, 30, 35, 40]
no_alc = [0, 11, 60, 81, 92]
lz = Lienzo("Ítems no alcanzados por posición", "Con tiempo limitado, el porcentaje de personas que no llega a responder crece al final: 0 % en el item 1 y 92 % en el 40.",
            "Posición del ítem", "% de personas que no lo alcanzan", (0, 40), (0, 100))
lz.ejes()
lz.linea(pos, no_alc, ROJO)
lz.puntos(pos, no_alc, ROJO, r=4, opacidad=1)
guardar(carpeta("009") / "figura-1.svg", lz)

# 010 descriptiva: tiempos con cola larga
rng = random.Random(20260819)
t = [math.exp(rng.gauss(1.4, 0.7)) for _ in range(1000)]
bins = [0] * 12
for v in t:
    bins[min(11, int(v / 2.5))] += 1
lz = Lienzo("Tiempos de respuesta: cola larga", "Histograma de 1000 tiempos simulados con cola larga; la media (5,3 s) queda por encima de la mediana (4,1 s).",
            "Segundos", "Personas", (0, 30), (0, max(bins) * 1.1))
lz.ejes()
lz.barras([2.5 * i + 1.25 for i in range(12)], bins, 2.5, AZUL)
lz.vertical(statistics.median(t), VERDE, "mediana")
lz.vertical(statistics.fmean(t), ROJO, "media")
guardar(carpeta("010") / "figura-1.svg", lz)
print("figuras de la parte 00 generadas")
