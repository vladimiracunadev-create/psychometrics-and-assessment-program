"""Regenera los indices de clases a partir de curriculum.yaml.

Fuente unica de verdad: curriculum.yaml. De ahi salen
  - la tabla "El programa" del README principal (entre marcadores),
  - el README.md de cada parte.
Con --check no escribe: falla si algo esta desincronizado (lo usa el CI).
"""
from __future__ import annotations

import pathlib
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
INICIO, FIN = "<!-- PROGRAMA:INICIO -->", "<!-- PROGRAMA:FIN -->"


def cargar() -> list[dict]:
    return yaml.safe_load((RAIZ / "curriculum.yaml").read_text(encoding="utf-8"))["temario"]


def dir_parte(p: dict) -> str:
    return f"part-{p['id']}-{p['slug']}"


def tabla_programa(partes: list[dict]) -> str:
    filas = ["| Parte | Título | Nivel | Clases escritas |", "|---|---|---|---|"]
    for p in partes:
        n = len(p["clases"])
        e = sum(c["estado"] == "escrita" for c in p["clases"])
        marca = "✅" if e == n else ("🟡" if e else "⬜")
        filas.append(f"| {p['id']} | [{p['titulo']}](classes/{dir_parte(p)}/) | "
                     f"{p['nivel']} | {e} / {n} {marca} |")
    tot = sum(len(p["clases"]) for p in partes)
    esc = sum(c["estado"] == "escrita" for p in partes for c in p["clases"])
    filas.append(f"| | **Total** | | **{esc} / {tot}** |")
    return "\n".join(filas)


def readme_parte(p: dict) -> str:
    sal = [f"# Parte {p['id']} — {p['titulo']}", "",
           f"**Nivel:** {p['nivel']} · **Duración estimada:** {p['semanas']} semanas", "",
           p["descripcion"].strip(), "", "## Clases", "",
           "| # | Clase | Horas | Estado |", "|---|---|---|---|"]
    for c in p["clases"]:
        carpeta = pathlib.PurePosixPath(c["ruta"]).name
        if c["estado"] == "escrita":
            titulo, estado = f"[{c['titulo']}]({carpeta}/README.md)", "✅ escrita"
        else:
            titulo, estado = c["titulo"], "⬜ planificada"
        sal.append(f"| {c['id']} | {titulo} | {c['horas_estimadas']} | {estado} |")
    sal += ["", "[← Volver al índice del programa](../../README.md)", ""]
    return "\n".join(sal)


def main() -> int:
    check = "--check" in sys.argv
    partes = cargar()
    desfasados: list[str] = []

    def aplica(ruta: pathlib.Path, nuevo: str) -> None:
        actual = ruta.read_text(encoding="utf-8").replace("\r\n", "\n") if ruta.exists() else None
        if actual != nuevo:
            desfasados.append(str(ruta.relative_to(RAIZ)))
            if not check:
                ruta.write_text(nuevo, encoding="utf-8", newline="\n")

    readme = (RAIZ / "README.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    if INICIO not in readme or FIN not in readme:
        print(f"README.md: faltan los marcadores {INICIO} / {FIN}")
        return 1
    antes, resto = readme.split(INICIO, 1)
    _, despues = resto.split(FIN, 1)
    aplica(RAIZ / "README.md", f"{antes}{INICIO}\n{tabla_programa(partes)}\n{FIN}{despues}")
    for p in partes:
        aplica(RAIZ / "classes" / dir_parte(p) / "README.md", readme_parte(p))

    if desfasados:
        print(("DESFASADOS" if check else "ACTUALIZADOS") + ": " + ", ".join(desfasados))
        return 1 if check else 0
    print("indices sincronizados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
