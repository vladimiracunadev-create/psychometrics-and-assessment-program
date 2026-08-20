"""Deriva la lista de dependencias desde pyproject.toml.

Existe para que la auditoría de seguridad no tenga que duplicar a mano lo que ya
declara `pyproject.toml`. Se audita la LISTA de dependencias y no el entorno
instalado, porque el entorno contiene el propio paquete, que no está publicado
en PyPI: `pip-audit --strict` lo trataría como dependencia no auditable y
fallaría, y `--skip-editable` tampoco sirve porque `--strict` considera error
también la omisión.

Uso:
    python scripts/export_requirements.py > requirements-audit.txt
    python -m pip_audit --strict -r requirements-audit.txt
"""
from __future__ import annotations

import pathlib
import sys
import tomllib

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    datos = tomllib.loads((RAIZ / "pyproject.toml").read_text(encoding="utf-8"))
    proyecto = datos["project"]

    dependencias = list(proyecto.get("dependencies", []))
    for extra in proyecto.get("optional-dependencies", {}).values():
        dependencias.extend(extra)

    if not dependencias:
        print("pyproject.toml no declara ninguna dependencia", file=sys.stderr)
        return 1

    for d in sorted(set(dependencias)):
        print(d)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
