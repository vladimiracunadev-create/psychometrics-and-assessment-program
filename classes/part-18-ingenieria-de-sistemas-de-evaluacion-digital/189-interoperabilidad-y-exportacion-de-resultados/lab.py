"""Laboratorio 189 - Exportar resultados: formato largo, metadatos y proteccion contra inyeccion en CSV.

Se puntua a 3 personas sinteticas con `valores-spranger` y se exporta en FORMATO LARGO (una fila
por persona-escala) con los metadatos necesarios para reproducir el calculo: instrumento, version,
licencia y numero de items respondidos. Se comprueba la ida y vuelta (CSV -> lectura) y se
protege la exportacion contra la inyeccion de formulas: un campo que empieza con = + - o @ se
interpreta como formula en una planilla, por lo que se neutraliza con un apostrofo.
"""
from __future__ import annotations

import csv
import io
import json
import pathlib
import random
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import Respuesta, cargar, puntuar  # noqa: E402

SEMILLA = 20260819
PELIGROSOS = ("=", "+", "-", "@", "\t", "\r")


def neutraliza(valor: str) -> str:
    return "'" + valor if valor and valor[0] in PELIGROSOS else valor


def main() -> None:
    ins = cargar("valores-spranger")
    rng = random.Random(SEMILLA)
    filas = []
    for k in range(3):
        res = puntuar(ins, [Respuesta(i.id, rng.randint(1, 5)) for i in ins.items])
        for cod, p in res.puntajes.items():
            filas.append({"sujeto": neutraliza(f"s{k + 1:03d}"), "instrumento": ins.codigo,
                          "version": ins.version, "licencia": ins.procedencia.licencia.value,
                          "escala": cod, "media_item": p.media_item,
                          "items_respondidos": p.items_respondidos, "items_totales": p.items_totales})
    salida = io.StringIO()
    w = csv.DictWriter(salida, fieldnames=list(filas[0]))
    w.writeheader()
    w.writerows(filas)
    texto = salida.getvalue()
    leidas = list(csv.DictReader(io.StringIO(texto)))
    print(f"Filas exportadas: {len(filas)}; ida y vuelta CSV: {len(leidas) == len(filas)}")
    print("Primeras filas:")
    for linea in texto.splitlines()[:4]:
        print("  " + linea)
    print("\nProteccion contra inyeccion de formulas:")
    for v in ("s001", "=HYPERLINK(\"http://x\")", "-2+3", "@SUM(A1)"):
        print(f"  {v!r:<30} -> {neutraliza(v)!r}")
    meta = {"formato": "largo", "columnas": list(filas[0]), "instrumento": ins.codigo, "version": ins.version}
    print(f"\nMetadatos (JSON): {json.dumps(meta)[:110]}...")
    print()
    print("Lectura: el formato largo (una fila por persona-escala) es el que aceptan casi todas las herramientas")
    print("de analisis. Incluir version y licencia hace reproducible el calculo y respeta las condiciones del")
    print("banco. Un CSV es codigo potencial para una planilla: se neutralizan los campos de texto libre.")


if __name__ == "__main__":
    main()
