"""Figuras de la clase 001 (cadena de inferencia y precision frente al numero de items)."""
from __future__ import annotations

import math
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import AZUL, ROJO, Lienzo, cadena, guardar  # noqa: E402

(AQUI / "figura-1.svg").write_text(cadena(
    "De lo que no se ve a un puntaje",
    "Cadena de seis pasos: rasgo, conducta, item, respuesta, puntaje e interpretacion. Cada paso es un supuesto.",
    ["Rasgo (no observable)", "Conducta que lo manifiesta", "Item que la pregunta", "Respuesta marcada", "Puntaje total", "Interpretacion"],
    ["se postula", "se supone", "se redacta", "se observa", "se calcula", "se infiere"]), encoding="utf-8")

# Valores medidos por lab.py (semilla 20260819, 500 personas) y curva teorica sqrt(k / (k + sd^2)).
ks = [1, 2, 4, 8, 16, 32, 64, 120]
r_lab = [0.677, 0.795, 0.881, 0.940, 0.967, 0.982, 0.992, 0.995]
lz = Lienzo("Más ítems, menos ruido", "Correlacion entre el puntaje y el rasgo verdadero segun el numero de items (laboratorio y curva teorica).",
            "Número de ítems (escala log2)", "Correlación con el rasgo verdadero", (0, 7), (0.6, 1.0))
lz.ejes()
xs = [math.log2(k) for k in ks]
teor = [math.sqrt(k / (k + 1)) for k in ks]
lz.linea(xs, teor, ROJO, "teoría", punteada=True)
lz.linea(xs, r_lab, AZUL)
lz.puntos(xs, r_lab, AZUL, r=4, opacidad=1)
for k, x, r in zip(ks, xs, r_lab, strict=True):
    if k in (1, 8, 120):
        lz.texto(x + 0.1, r - 0.025, f"{k} ítems: {r:.2f}")
guardar(AQUI / "figura-2.svg", lz)
print("figuras generadas")
