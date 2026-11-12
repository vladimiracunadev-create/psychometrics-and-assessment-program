"""Baterias: pausar/reanudar no cambia el resultado, y el estado alterado se rechaza."""
from __future__ import annotations

import json
import random

import pytest

from psychometrics.baterias import Bateria, BateriaInvalida, Sesion
from psychometrics.motor import Respuesta, cargar, puntuar

BAT = Bateria("demo", ("valores-spranger", "disc-abierto"))


def respuestas_fijas(codigo: str, semilla: int) -> dict[str, int]:
    rng = random.Random(semilla)
    return {i.id: rng.randint(1, 5) for i in cargar(codigo).items}


def completa(sesion: Sesion, hasta: int | None = None) -> None:
    datos = {c: respuestas_fijas(c, 7) for c in BAT.instrumentos}
    n = 0
    for c in BAT.instrumentos:
        for item, v in datos[c].items():
            if hasta is not None and n >= hasta:
                return
            sesion.responder(c, item, v)
            n += 1


def test_bateria_rechaza_vacia_y_repetida():
    with pytest.raises(BateriaInvalida):
        Bateria("x", ())
    with pytest.raises(BateriaInvalida):
        Bateria("x", ("disc-abierto", "disc-abierto"))


def test_el_orden_de_la_bateria_define_el_siguiente_item():
    s = Sesion(BAT, "s001")
    assert s.siguiente()[0] == "valores-spranger"
    for item, v in respuestas_fijas("valores-spranger", 7).items():
        s.responder("valores-spranger", item, v)
    assert s.siguiente()[0] == "disc-abierto"


def test_pausar_y_reanudar_da_el_mismo_resultado():
    continuo = Sesion(BAT, "s001")
    completa(continuo)
    pausada = Sesion(BAT, "s001")
    completa(pausada, hasta=50)
    reanudada = Sesion.cargar(json.loads(json.dumps(pausada.guardar())))   # pasa por JSON real
    datos = {c: respuestas_fijas(c, 7) for c in BAT.instrumentos}
    for c in BAT.instrumentos:
        for item in reanudada.pendientes(c):
            reanudada.responder(c, item, datos[c][item])
    for c in BAT.instrumentos:
        a, b = continuo.resultado(c), reanudada.resultado(c)
        assert {k: p.media_item for k, p in a.puntajes.items()} == {k: p.media_item for k, p in b.puntajes.items()}


def test_resultado_coincide_con_puntuar_directo():
    s = Sesion(BAT, "s001")
    completa(s)
    ins = cargar("disc-abierto")
    directo = puntuar(ins, [Respuesta(i, v) for i, v in respuestas_fijas("disc-abierto", 7).items()])
    assert s.resultado("disc-abierto").puntajes.keys() == directo.puntajes.keys()
    assert s.resultado("disc-abierto")["D"].media_item == directo["D"].media_item


def test_estado_alterado_se_rechaza():
    s = Sesion(BAT, "s001")
    completa(s, hasta=10)
    estado = s.guardar()
    estado["respuestas"]["valores-spranger"][next(iter(estado["respuestas"]["valores-spranger"]))] = 5
    with pytest.raises(BateriaInvalida):
        Sesion.cargar(estado)


def test_valor_fuera_de_rango_y_item_inexistente():
    s = Sesion(BAT, "s001")
    item = cargar("disc-abierto").items[0].id
    with pytest.raises(BateriaInvalida):
        s.responder("disc-abierto", item, 9)
    with pytest.raises(BateriaInvalida):
        s.responder("disc-abierto", "no-existe", 3)
    with pytest.raises(BateriaInvalida):
        s.responder("ipip-neo-120", "q001", 3)


def test_resultado_exige_instrumento_completo():
    s = Sesion(BAT, "s001")
    with pytest.raises(BateriaInvalida):
        s.resultado("disc-abierto")


def test_omision_explicita_cuenta_como_respondida_y_no_como_cero():
    s = Sesion(BAT, "s001")
    datos = respuestas_fijas("disc-abierto", 3)
    primero = next(iter(datos))
    for item, v in datos.items():
        s.responder("disc-abierto", item, None if item == primero else v)
    assert s.completo("disc-abierto")
    assert s.resultado("disc-abierto").omitidas == 1
