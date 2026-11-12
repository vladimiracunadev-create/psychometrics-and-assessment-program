"""Genera las figuras SVG de la clase 011 (datos simulados, semilla fija)."""
from __future__ import annotations

import pathlib
import random
import statistics
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import AZUL, ROJO, Lienzo, guardar  # noqa: E402

rng = random.Random(20260819)
N = 3000
T = [rng.gauss(0, 1) for _ in range(N)]

# Figura 1: observado frente a verdadero para tres tamanos de error
for nombre, sd in (("a", 0.5), ("b", 2.0)):
    X = [t + rng.gauss(0, sd) for t in T]
    fiab = statistics.variance(T) / statistics.variance(X)
    lz = Lienzo(f"Puntaje observado vs verdadero (error DE = {sd})",
                f"Dispersion de {N} personas simuladas: con error de desviacion {sd} la fiabilidad es {fiab:.2f}.",
                "Puntaje verdadero T", "Puntaje observado X", (-4, 4), (-8 if sd > 1 else -5, 8 if sd > 1 else 5))
    lz.ejes()
    lz.puntos(T[:600], X[:600])
    lz.linea([-4, 4], [-4, 4], ROJO, "X = T", punteada=True)
    lz.texto(-3.8, (7 if sd > 1 else 4.2), f"fiabilidad = {fiab:.2f}")
    guardar(AQUI / f"figura-1{nombre}.svg", lz)

# Figura 2: fiabilidad segun el tamano del error
sds = [0.1 * k for k in range(1, 31)]
fi = [1 / (1 + s * s) for s in sds]
lz = Lienzo("La fiabilidad cae al crecer el error", "Con varianza verdadera 1, fiabilidad = 1 / (1 + DE del error al cuadrado).",
            "Desviacion tipica del error", "Fiabilidad", (0, 3), (0, 1))
lz.ejes()
lz.linea(sds, fi, AZUL)
lz.vertical(1.0, ROJO, "error = variacion real: 0,50")
guardar(AQUI / "figura-2.svg", lz)
print("figuras generadas")
