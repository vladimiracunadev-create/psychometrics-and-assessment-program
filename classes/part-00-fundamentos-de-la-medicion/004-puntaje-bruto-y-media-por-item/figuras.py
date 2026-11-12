"""Figuras de la clase 004: puntaje bruto frente a media por item, y promedio de promedios."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, guardar  # noqa: E402

# Figura 1: mismas respuestas (todas 3) en una escala de 24 items y otra de 4 items.
lz = Lienzo("Mismo nivel de respuesta, brutos distintos", "Con todas las respuestas en 3, el bruto es 72 en Responsabilidad (24 items) y 12 en Orden (4 items); la media por item es 3,0 en ambas.",
            "Escala (1 = Responsabilidad, 24 ítems; 2 = Orden, 4 ítems)", "Puntaje", (0.4, 2.6), (0, 80))
lz.ejes()
lz.barras([0.8, 1.8], [72, 12], 0.35, ROJO)
lz.barras([1.2, 2.2], [3, 3], 0.35, VERDE)
lz.texto(0.62, 76, "bruto 72", ROJO)
lz.texto(1.62, 16, "bruto 12", ROJO)
lz.texto(1.05, 8, "media 3,0", VERDE)
lz.texto(2.05, 8, "media 3,0", VERDE)
guardar(AQUI / "figura-1.svg", lz)

# Figura 2: instrumento sintetico con facetas de 2 y 6 items (resultado de lab.py): A = 3,0; B = 2,0.
lz = Lienzo("Promedio de promedios (A) frente a media por ítem (B)", "En un dominio con una faceta de 2 items (media 4) y otra de 6 items (media 1,67), A da 3,0 y B da 2,0.",
            "Método (1 = A: promedio de promedios; 2 = B: media por ítem)", "Media del dominio", (0.4, 2.6), (0, 4))
lz.ejes(n=4)
lz.barras([1, 2], [3.0, 2.0], 0.5, AZUL)
lz.texto(0.75, 3.15, "A = 3,0", AZUL)
lz.texto(1.75, 2.15, "B = 2,0", AZUL)
guardar(AQUI / "figura-2.svg", lz)
print("figuras generadas")
