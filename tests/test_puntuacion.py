"""Comportamiento del motor de puntuación.

Se usa un instrumento sintético mínimo para que cada test aísle una decisión
del algoritmo, y los instrumentos reales solo para las pruebas de integración.
"""

from __future__ import annotations

import pytest

from psychometrics.motor import (
    Respuesta,
    RespuestaFueraDeRango,
    cargar,
    cargar_desde_texto,
    ordenar_por_media,
    puntuar,
)

MINIMO = """
codigo: prueba
version: "1.0.0"
nombre: {es: Instrumento de prueba}
tipo_respuesta: likert
procedencia:
  autores: tests
  anio: 2026
  fuente: tests/test_puntuacion.py
  licencia: autoria-propia
  notas: {sin_validar: "sin estudio de validación"}
opciones:
  - {valor: 1, etiqueta: {es: uno}}
  - {valor: 2, etiqueta: {es: dos}}
  - {valor: 3, etiqueta: {es: tres}}
  - {valor: 4, etiqueta: {es: cuatro}}
  - {valor: 5, etiqueta: {es: cinco}}
escalas:
  - codigo: TOT
    nombre: {es: Total}
  - codigo: A
    padre: TOT
    nombre: {es: Faceta A}
  - codigo: B
    padre: TOT
    nombre: {es: Faceta B}
items:
  - {id: a1, escala: A, clave: 1, texto: {es: directo}}
  - {id: a2, escala: A, clave: -1, texto: {es: invertido}}
  - {id: b1, escala: B, clave: 1, texto: {es: directo}}
  - {id: b2, escala: B, clave: 1, texto: {es: directo}}
  - {id: b3, escala: B, clave: 1, texto: {es: directo}}
"""


@pytest.fixture
def ins():
    return cargar_desde_texto(MINIMO, origen="prueba")


def test_item_invertido_se_refleja_antes_de_sumar(ins):
    """Responder 5 a un ítem invertido debe aportar 1, no 5."""
    r = puntuar(ins, [Respuesta("a1", 5), Respuesta("a2", 5)])
    assert r["A"].bruto == 6  # 5 directo + 1 reflejado
    assert r["A"].media_item == 3.0


def test_reflejo_es_simetrico(ins):
    """El punto medio de la escala no se mueve al reflejar."""
    r = puntuar(ins, [Respuesta("a1", 3), Respuesta("a2", 3)])
    assert r["A"].bruto == 6


def test_omision_no_vale_cero(ins):
    """Omitir no debe arrastrar la media hacia abajo: se excluye del cálculo."""
    r = puntuar(ins, [Respuesta("b1", 4), Respuesta("b2", 4), Respuesta("b3", None)])
    assert r["B"].items_respondidos == 2
    assert r["B"].media_item == 4.0  # no 8/3
    assert r.omitidas == 3  # b3 + los dos de la faceta A, nunca enviados


def test_escala_incompleta_se_marca(ins):
    r = puntuar(ins, [Respuesta("b1", 4)])
    assert not r["B"].completa
    assert any("B" in a for a in r.advertencias)


def test_escala_compuesta_agrega_desde_items_no_desde_medias(ins):
    """TOT tiene 2 ítems en A y 3 en B: el promedio debe pesarlos por ítem.

    Con A=[5,5→1] y B=[1,1,1]: media de medias daría (3.0+1.0)/2 = 2.0, pero la
    media por ítem correcta es (5+1+1+1+1)/5 = 1.8.
    """
    r = puntuar(ins, [
        Respuesta("a1", 5), Respuesta("a2", 5),
        Respuesta("b1", 1), Respuesta("b2", 1), Respuesta("b3", 1),
    ])
    assert r["A"].media_item == 3.0
    assert r["B"].media_item == 1.0
    assert r["TOT"].media_item == 1.8
    assert r["TOT"].items_totales == 5


def test_valor_fuera_de_rango_es_error_en_modo_estricto(ins):
    with pytest.raises(RespuestaFueraDeRango):
        puntuar(ins, [Respuesta("a1", 9)])


def test_valor_fuera_de_rango_es_omision_en_modo_laxo(ins):
    r = puntuar(ins, [Respuesta("a1", 9)], estricto=False)
    assert r["A"].items_respondidos == 0
    assert any("fuera de rango" in a for a in r.advertencias)


def test_respuesta_en_linea_recta_se_detecta(ins):
    """Marcar el mismo valor en todo es un protocolo que no debe interpretarse."""
    r = puntuar(ins, [Respuesta(i.id, 3) for i in ins.items])
    assert any("línea recta" in a for a in r.advertencias)


def test_respuesta_variada_no_dispara_la_alerta(ins):
    r = puntuar(ins, [Respuesta("a1", 1), Respuesta("a2", 5), Respuesta("b1", 2),
                      Respuesta("b2", 4), Respuesta("b3", 3)])
    assert not any("línea recta" in a for a in r.advertencias)


def test_respuestas_de_items_inexistentes_se_ignoran_con_aviso(ins):
    r = puntuar(ins, [Respuesta("a1", 4), Respuesta("no_existe", 5)])
    assert any("no corresponden" in a for a in r.advertencias)
    assert r["A"].items_respondidos == 1


# --- integración con los instrumentos reales ------------------------------


def test_riasec_produce_codigo_holland_de_tres_letras():
    ip = cargar("onet-riasec-sf")
    # Perfil construido a mano: máximo en Investigador, mínimo en Realista.
    preferencias = {"I": 5, "A": 4, "S": 3, "C": 3, "E": 2, "R": 1}
    r = puntuar(ip, [Respuesta(i.id, preferencias[i.escala]) for i in ip.items])
    codigo = "".join(c for c, _ in ordenar_por_media(r, list("RIASEC"))[:3])
    assert codigo == "IAC" or codigo == "IAS", codigo
    assert r["I"].media_item == 5.0
    assert r["R"].media_item == 1.0


def test_big_five_agrega_las_seis_facetas_de_cada_dominio():
    ip = cargar("ipip-neo-120")
    r = puntuar(ip, [Respuesta(i.id, 3) for i in ip.items])
    for dominio in "NEOAC":
        assert r[dominio].items_totales == 24, dominio
        # Con todo en el punto medio, reflejar no cambia nada: media = 3.
        assert r[dominio].media_item == 3.0


def test_via_agrega_virtudes_desde_las_fortalezas():
    ip = cargar("ipip-via-r")
    r = puntuar(ip, [Respuesta(i.id, 4) for i in ip.items])
    # Sabiduría tiene 5 fortalezas de 4 ítems.
    assert r["SAB"].items_totales == 20
    # Clave equilibrada: 2 directos en 4 y 2 invertidos en 2 -> media 3.
    assert r["SAB"].media_item == 3.0
