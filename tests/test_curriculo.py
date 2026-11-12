"""El curriculo ampliado conserva lo original y no infla lo escrito."""
from __future__ import annotations

import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CURR = yaml.safe_load((RAIZ / "curriculum.yaml").read_text(encoding="utf-8"))
CLASES = [c for p in CURR["temario"] for c in p["clases"]]


def test_veinte_partes_doscientas_clases():
    assert CURR["partes"] == len(CURR["temario"]) == 20
    assert CURR["clases"] == len(CLASES) == 200


def test_identificadores_unicos_y_consecutivos():
    assert [c["numero"] for c in sorted(CLASES, key=lambda c: c["numero"])] == list(range(1, 201))
    assert len({c["ruta"] for c in CLASES}) == 200


def test_las_cuarenta_originales_se_conservan():
    originales = [c for c in CLASES if c["numero"] <= 40]
    assert len(originales) == 40
    assert sum(c["estado"] == "escrita" for c in originales) == 5


def test_las_nuevas_no_se_declaran_escritas():
    assert all(c["estado"] == "planificada" for c in CLASES if c["numero"] > 40)


def test_toda_clase_tiene_carpeta():
    assert all((RAIZ / c["ruta"]).is_dir() for c in CLASES)
