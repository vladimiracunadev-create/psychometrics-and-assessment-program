"""Integridad del catalogo ampliado de fichas."""
from __future__ import annotations

import pytest

from psychometrics.fichas import cargar_fichas, resumen, validar_fichas
from psychometrics.motor import catalogo


@pytest.fixture(scope="module")
def fichas():
    return cargar_fichas()


@pytest.fixture(scope="module")
def codigos():
    return {i.codigo for i in catalogo()}


def test_al_menos_cien_fichas(fichas):
    assert len(fichas) >= 100


def test_catalogo_coherente(fichas, codigos):
    assert validar_fichas(fichas, codigos) == []


def test_ninguna_ficha_documental_se_cuenta_como_implementada(fichas, codigos):
    impl = [f for f in fichas if f["estado"] == "implementado"]
    assert {f["implementacion"] for f in impl} == codigos


def test_nada_esta_validado_sin_evidencia(fichas):
    assert resumen(fichas)["validado-uso-especifico"] == 0


def test_quince_instrumentos_laborales_documentados(fichas):
    esperados = {"cie", "arp", "amp", "eel", "pdv", "tdl", "pdr", "eep", "prp",
                 "cet", "ect", "dct", "pfp", "pgp", "mci"}
    assert esperados <= {f["id"] for f in fichas}
    for f in fichas:
        if f["id"] in esperados:
            assert f["estado"] == "documentado"
            assert f["verificado"] is False


def test_familias_cubiertas(fichas):
    assert {f["familia"] for f in fichas} == set("ABCDEFGH")


def test_validador_detecta_errores(codigos):
    malas = [{"id": "x", "nombre": "x", "familia": "Z", "uso": ["laboral"],
              "estado": "implementado", "licencia": "propietaria",
              "redistribuible": "si"}]
    assert len(validar_fichas(malas, codigos)) >= 3
