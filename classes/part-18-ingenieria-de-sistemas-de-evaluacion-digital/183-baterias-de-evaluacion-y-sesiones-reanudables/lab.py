"""Laboratorio 183 - Baterias y sesiones reanudables con el modulo `psychometrics.baterias`.

Una bateria agrupa dos instrumentos del catalogo. Una persona sintetica responde 60 items, la
sesion se PAUSA (se serializa a JSON), se REANUDA desde el JSON y termina. Se comprueba que:
  - el resultado coincide con el de una sesion continua,
  - alterar el JSON guardado invalida la sesion (huella de integridad),
  - la bitacora registra los eventos con un indice, sin datos personales ni reloj.
"""
from __future__ import annotations

import json
import pathlib
import random
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.baterias import Bateria, BateriaInvalida, Sesion  # noqa: E402
from psychometrics.motor import cargar  # noqa: E402

SEMILLA = 20260819


def main() -> None:
    bat = Bateria("demo-orientacion", ("valores-spranger", "disc-abierto"), "demostracion con datos sinteticos")
    rng = random.Random(SEMILLA)
    datos = {c: {i.id: rng.randint(1, 5) for i in cargar(c).items} for c in bat.instrumentos}

    continua = Sesion(bat, "sujeto-0001")
    for c in bat.instrumentos:
        for item, v in datos[c].items():
            continua.responder(c, item, v)

    pausada = Sesion(bat, "sujeto-0001")
    n = 0
    for c in bat.instrumentos:
        for item, v in datos[c].items():
            if n < 60:
                pausada.responder(c, item, v)
                n += 1
    estado = json.dumps(pausada.guardar())
    print(f"Sesion pausada con avance: {pausada.avance()} | tamano del JSON: {len(estado)} bytes")
    reanudada = Sesion.cargar(json.loads(estado))
    print(f"Tras reanudar, siguiente item: {reanudada.siguiente()}")
    for c in bat.instrumentos:
        for item in reanudada.pendientes(c):
            reanudada.responder(c, item, datos[c][item])

    iguales = all(
        {k: p.media_item for k, p in continua.resultado(c).puntajes.items()}
        == {k: p.media_item for k, p in reanudada.resultado(c).puntajes.items()}
        for c in bat.instrumentos)
    print(f"Resultado de la sesion pausada == sesion continua: {iguales}")
    alterado = json.loads(estado)
    alterado["respuestas"]["valores-spranger"]["t01"] = 5 if alterado["respuestas"]["valores-spranger"]["t01"] != 5 else 4
    try:
        Sesion.cargar(alterado)
        print("Alteracion detectada: NO (error)")
    except BateriaInvalida as e:
        print(f"Alteracion detectada: SI ({e})")
    print(f"Eventos en la bitacora: {len(reanudada.bitacora)}; primer evento: {reanudada.bitacora[0]}")
    print()
    print("Lectura: guardar solo respuestas y recalcular los puntajes al pedirlos evita datos viejos si el")
    print("motor se corrige. La huella detecta cambios accidentales o manipulacion del archivo, pero no")
    print("impide el acceso: el almacenamiento necesita cifrado y control de acceso (clase 188).")


if __name__ == "__main__":
    main()
