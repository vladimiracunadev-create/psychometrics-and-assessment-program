.PHONY: ayuda instalar test lint validar catalogo construir limpiar

PY ?= python
export PYTHONPATH := src
export PYTHONIOENCODING := utf-8

ayuda:
	@echo "instalar   dependencias de desarrollo"
	@echo "test       ejecuta la bateria de pruebas"
	@echo "lint       ruff sobre src, tests y scripts"
	@echo "validar    valida todos los instrumentos del catalogo"
	@echo "catalogo   lista los instrumentos disponibles"
	@echo "construir  regenera los instrumentos derivados de bancos publicos"
	@echo "limpiar    borra artefactos de build y caches"

instalar:
	$(PY) -m pip install -e ".[dev]"

test:
	$(PY) -m pytest

lint:
	$(PY) -m ruff check src tests scripts

validar:
	$(PY) -m psychometrics.cli validar

catalogo:
	$(PY) -m psychometrics.cli catalogo

construir:
	$(PY) scripts/build_ipip_neo_120.py
	$(PY) scripts/build_ipip_via_r.py

limpiar:
	rm -rf build dist .pytest_cache .ruff_cache *.egg-info
