"""Figura de la clase 005: aquiescencia con clave unica y con clave equilibrada (valores de lab.py)."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import AZUL, ROJO, Lienzo, guardar  # noqa: E402

aq = [-1.0, -0.5, 0.0, 0.5, 1.0]
unica = [2.10, 2.50, 3.10, 3.50, 4.10]
equil = [2.90, 3.00, 2.90, 3.00, 2.90]
lz = Lienzo("Misma persona, distinto estilo de respuesta", "Puntaje de personas con el mismo rasgo segun su aquiescencia: con clave unica sube de 2,1 a 4,1; con clave equilibrada se mantiene cerca de 3.",
            "Aquiescencia (tendencia a estar de acuerdo con todo)", "Puntaje medio por ítem", (-1.2, 1.2), (1.5, 4.5))
lz.ejes()
lz.linea(aq, unica, ROJO, "clave única")
lz.puntos(aq, unica, ROJO, r=4, opacidad=1)
lz.linea(aq, equil, AZUL, "clave equilibrada")
lz.puntos(aq, equil, AZUL, r=4, opacidad=1)
lz.texto(-1.1, 4.3, "rango clave única: 2,00", ROJO)
lz.texto(-1.1, 4.05, "rango equilibrada: 0,10", AZUL)
guardar(AQUI / "figura-1.svg", lz)
print("figuras generadas")
