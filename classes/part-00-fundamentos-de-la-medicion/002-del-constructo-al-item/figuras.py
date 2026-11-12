"""Figuras de la clase 002: del constructo al item y auditoria de redaccion del catalogo."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "src"))

from psychometrics.figuras import AZUL, ROJO, Lienzo, cadena, guardar  # noqa: E402

(AQUI / "figura-1.svg").write_text(cadena(
    "Del constructo al instrumento final",
    "Seis etapas: constructo, definicion operacional, tabla de especificaciones, banco de items, pilotaje e instrumento final.",
    ["Constructo (idea)", "Definición operacional", "Tabla de especificaciones", "Banco (2 a 3 veces más ítems)", "Pilotaje y descarte", "Instrumento final"],
    ["¿qué es?", "¿qué entra y qué no?", "¿cuántos ítems por faceta?", "se escribe de más", "se mide y se descarta", "se documenta"]), encoding="utf-8")

# Resultado de lab.py sobre el catalogo real: items marcados / items totales por instrumento.
inst = ["disc-abierto", "ipip-neo-120", "ipip-via-r", "onet-riasec-sf", "valores-spranger"]
marcados = [0, 0, 2, 0, 0]
lz = Lienzo("Auditoría automática de redacción", "Items marcados por la auditoria automatica en cada instrumento del catalogo: solo 2 de 344.",
            "Instrumento (1 a 5, en el orden de la tabla)", "Ítems marcados", (0.5, 5.5), (0, 3))
lz.ejes(n=3)
lz.barras([1, 2, 3, 4, 5], marcados, 0.6, ROJO)
for i, (nombre, m) in enumerate(zip(inst, marcados, strict=True), 1):
    lz.texto(i - 0.4, 0.25 if m == 0 else m + 0.15, f"{nombre}: {m}", AZUL if m == 0 else ROJO)
guardar(AQUI / "figura-2.svg", lz)
print("figuras generadas")
