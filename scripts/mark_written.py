"""Marca clases como escritas (curriculum.yaml + lesson.yaml) tras verificar sus archivos.

Uso: python scripts/mark_written.py 11 12 13 ...
Falla si a una clase le falta README.md o lab.py: no se declara escrito lo que no existe.
"""
from __future__ import annotations

import pathlib
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
LESSON = (
    'id: "{id}"\nnumero: {numero}\ntitulo: "{titulo}"\nparte: "{parte}"\n'
    "horas_estimadas: {horas}\nestado: escrita\nlaboratorio: lab.py\n"
)


def main(numeros: list[int]) -> int:
    ruta = RAIZ / "curriculum.yaml"
    texto = ruta.read_text(encoding="utf-8")
    curr = yaml.safe_load(texto)
    cabecera = "".join(x for x in texto.splitlines(True) if x.startswith("#"))
    hechos: set[int] = set()
    for parte in curr["temario"]:
        for c in parte["clases"]:
            if c["numero"] not in numeros:
                continue
            carpeta = RAIZ / c["ruta"]
            faltan = [a for a in ("README.md", "lab.py") if not (carpeta / a).is_file()]
            if faltan:
                print(f"{c['id']}: faltan {faltan}; no se marca")
                return 1
            c["estado"] = "escrita"
            (carpeta / "lesson.yaml").write_text(
                LESSON.format(id=c["id"], numero=c["numero"], titulo=c["titulo"],
                              parte=parte["id"], horas=c["horas_estimadas"]),
                encoding="utf-8")
            hechos.add(c["numero"])
    if hechos != set(numeros):
        print(f"no existen: {sorted(set(numeros) - hechos)}")
        return 1
    ruta.write_text(cabecera + yaml.safe_dump(curr, allow_unicode=True, sort_keys=False, width=100),
                    encoding="utf-8")
    print(f"marcadas {len(hechos)} clases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main([int(x) for x in sys.argv[1:]]))
