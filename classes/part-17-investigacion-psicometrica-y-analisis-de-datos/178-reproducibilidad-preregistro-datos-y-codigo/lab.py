"""Laboratorio 178 - Reproducibilidad verificable: semilla, orden y huella de los resultados.

Se ejecuta el MISMO analisis tres veces:
  1. con semilla fija y estructuras ordenadas -> la huella SHA-256 del resultado es identica;
  2. sin semilla -> la huella cambia en cada ejecucion (no reproducible);
  3. con semilla fija pero iterando un conjunto (set) de cadenas -> el orden puede depender de la
     ejecucion de Python (PYTHONHASHSEED), por lo que el resultado puede cambiar entre procesos.
Ademas imprime la "huella del entorno" (version de Python y de plataforma). Un registro
reproducible incluye: plan previo (preregistro), datos (o su generador), codigo, semilla y entorno.
"""
from __future__ import annotations

import hashlib
import json
import platform
import random
import statistics


def analisis(semilla: int | None) -> dict:
    rng = random.Random(semilla)
    datos = [rng.gauss(0, 1) for _ in range(200)]
    return {"n": len(datos), "media": round(statistics.fmean(datos), 6), "de": round(statistics.pstdev(datos), 6)}


def huella(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:16]


def analisis_con_set(semilla: int) -> dict:
    rng = random.Random(semilla)
    nombres = {"alfa", "beta", "gamma", "delta"}                  # orden de iteracion no garantizado
    return {"orden": "".join(n[0] for n in nombres), "valor": round(rng.random(), 6)}


def main() -> None:
    print("1. Semilla fija, estructuras ordenadas")
    h = [huella(analisis(20260819)) for _ in range(3)]
    print("   huellas:", h, "->", "IDENTICAS" if len(set(h)) == 1 else "DISTINTAS")
    print("2. Sin semilla")
    h2 = [huella(analisis(None)) for _ in range(3)]
    print("   huellas:", h2, "->", "IDENTICAS" if len(set(h2)) == 1 else "DISTINTAS (no reproducible)")
    print("3. Semilla fija, pero se itera un set de cadenas")
    print("   resultado de esta ejecucion:", analisis_con_set(20260819), "(el 'orden' puede variar entre procesos)")
    print(f"\nEntorno: Python {platform.python_version()} / {platform.system()}")
    print()
    print("Lectura: la semilla es necesaria pero no suficiente: tambien importan el orden de iteracion, las")
    print("versiones de las librerias y los datos. Comprobar que dos ejecuciones dan la misma huella es una")
    print("prueba barata, y es lo que hace el CI del repositorio con sus generadores de bancos. El")
    print("preregistro (hipotesis y analisis antes de ver los datos) protege contra analisis flexibles.")


if __name__ == "__main__":
    main()
