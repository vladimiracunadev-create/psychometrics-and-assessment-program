"""Figura de la clase 003: los cuatro niveles de medida y lo que permite cada uno."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import cadena  # noqa: E402

(AQUI / "figura-1.svg").write_text(cadena(
    "Los cuatro niveles de medida (Stevens, 1946)",
    "Escalera de cuatro niveles; cada uno hereda lo anterior y suma una operacion: igualdad, orden, distancias iguales y cero absoluto.",
    ["Nominal: nombres", "Ordinal: orden", "Intervalo: distancias iguales", "Razón: cero absoluto"],
    ["= / ≠  (moda)", "< / >  (mediana)", "+ / −  (media)", "× / ÷  (cociente)"]), encoding="utf-8")
print("figuras generadas")
