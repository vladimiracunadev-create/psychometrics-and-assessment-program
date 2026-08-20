"""Invariantes estructurales del catálogo de instrumentos.

Estos tests no comprueban psicometría sino integridad: que los archivos digan
lo que el motor espera. Un instrumento que carga pero está mal declarado
produce un informe plausible y equivocado sobre una persona real.
"""

from __future__ import annotations

import pathlib
import unicodedata

import pytest
import yaml

from psychometrics.motor import Licencia, catalogo

RAIZ = pathlib.Path(__file__).resolve().parents[1]
INSTRUMENTOS = sorted((RAIZ / "instruments").glob("*.yaml"))

# Instrumentos cuyo diseño declara clave equilibrada: mitad de ítems directos
# y mitad invertidos por escala. Es lo que contiene el sesgo de aquiescencia.
CLAVE_EQUILIBRADA = {"ipip-via-r", "disc-abierto"}


def ids(rutas):
    return [r.stem for r in rutas]


@pytest.fixture(scope="module")
def instrumentos():
    return {i.codigo: i for i in catalogo()}


def test_hay_instrumentos():
    assert INSTRUMENTOS, "el catálogo está vacío"


@pytest.mark.parametrize("ruta", INSTRUMENTOS, ids=ids(INSTRUMENTOS))
def test_carga_sin_errores(ruta):
    from psychometrics.motor import cargar

    cargar(ruta.stem)


@pytest.mark.parametrize("ruta", INSTRUMENTOS, ids=ids(INSTRUMENTOS))
def test_claves_yaml_en_ascii(ruta):
    """Las claves estructurales nunca llevan tilde.

    Regresión de un fallo real: una pasada automática de tildes acentuó las
    claves `codigo` y `version`, y el cargador dejó de encontrarlas. La prosa
    lleva tildes; la estructura, no.
    """
    crudo = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    malas: list[str] = []

    def recorre(nodo, camino=""):
        if isinstance(nodo, dict):
            for clave, valor in nodo.items():
                if isinstance(clave, str) and not clave.isascii():
                    malas.append(f"{camino}.{clave}")
                recorre(valor, f"{camino}.{clave}")
        elif isinstance(nodo, list):
            for n, x in enumerate(nodo):
                recorre(x, f"{camino}[{n}]")

    recorre(crudo)
    assert not malas, f"claves con caracteres no ASCII: {malas}"


@pytest.mark.parametrize("ruta", INSTRUMENTOS, ids=ids(INSTRUMENTOS))
def test_licencia_es_valor_conocido(ruta):
    crudo = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    valor = crudo["procedencia"]["licencia"]
    assert valor in {x.value for x in Licencia}, f"licencia desconocida: {valor!r}"


@pytest.mark.parametrize("codigo", [r.stem for r in INSTRUMENTOS])
def test_ids_de_item_unicos(codigo, instrumentos):
    i = instrumentos[codigo]
    vistos = [x.id for x in i.items]
    assert len(vistos) == len(set(vistos))


@pytest.mark.parametrize("codigo", [r.stem for r in INSTRUMENTOS])
def test_toda_escala_hoja_tiene_items(codigo, instrumentos):
    i = instrumentos[codigo]
    for e in i.escalas:
        if i.hijas_de(e.codigo):
            continue
        assert i.items_de(e.codigo), f"{codigo}: la escala hoja {e.codigo} no tiene ítems"


@pytest.mark.parametrize("codigo", [r.stem for r in INSTRUMENTOS])
def test_todo_item_tiene_texto_en_espanol(codigo, instrumentos):
    i = instrumentos[codigo]
    for x in i.items:
        assert x.texto.get("es", "").strip(), f"{codigo}/{x.id}: sin texto en español"


@pytest.mark.parametrize("codigo", [r.stem for r in INSTRUMENTOS])
def test_procedencia_declarada(codigo, instrumentos):
    """Sin fuente verificable no hay instrumento, solo una encuesta de revista."""
    p = instrumentos[codigo].procedencia
    assert p.fuente.strip(), f"{codigo}: procedencia.fuente vacía"
    assert p.autores.strip(), f"{codigo}: procedencia.autores vacía"


@pytest.mark.parametrize("codigo", sorted(CLAVE_EQUILIBRADA))
def test_clave_equilibrada(codigo, instrumentos):
    """En estos instrumentos cada escala debe tener tantos directos como invertidos."""
    i = instrumentos[codigo]
    for e in i.escalas:
        items = i.items_de(e.codigo)
        if not items:
            continue
        directos = sum(1 for x in items if x.clave == 1)
        assert directos * 2 == len(items), (
            f"{codigo}/{e.codigo}: {directos} directos de {len(items)} ítems; "
            "el diseño declara clave equilibrada"
        )


@pytest.mark.parametrize("codigo", [r.stem for r in INSTRUMENTOS])
def test_prosa_en_espanol_lleva_tildes_bien_formadas(codigo, instrumentos):
    """Detecta mojibake: texto UTF-8 leído como latin-1 y vuelto a guardar."""
    i = instrumentos[codigo]
    sospechosos = ("Ã", "Â", "�", "�")
    for x in i.items:
        texto = x.texto.get("es", "")
        assert not any(s in texto for s in sospechosos), (
            f"{codigo}/{x.id}: el texto en español parece mal codificado: {texto!r}"
        )
        assert unicodedata.is_normalized("NFC", texto), (
            f"{codigo}/{x.id}: el texto no está en forma normal NFC"
        )


def test_instrumentos_sin_validar_lo_declaran(instrumentos):
    """Un banco de autoría propia debe advertir que no tiene estudio de validación.

    Publicar ítems propios sin decirlo es lo que convierte un ejercicio
    didáctico en una herramienta que alguien usa para decidir sobre personas.
    """
    for i in instrumentos.values():
        if i.procedencia.licencia is not Licencia.AUTORIA_PROPIA:
            continue
        notas = " ".join(i.procedencia.notas.values()).lower()
        assert "sin estudio de validación" in notas or "sin validar" in notas, (
            f"{i.codigo}: es de autoría propia y no declara su falta de validación"
        )
