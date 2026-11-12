"""Regenera los indices de clases a partir de curriculum.yaml.

Fuente unica de verdad: curriculum.yaml. De ahi salen
  - la tabla "El programa" del README principal (entre marcadores),
  - el README.md de cada parte.
Con --check no escribe: falla si algo esta desincronizado (lo usa el CI).
"""
from __future__ import annotations

import pathlib
import re
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


def guias() -> dict:
    return yaml.safe_load((RAIZ / "catalogo" / "guias_partes.yaml").read_text(encoding="utf-8"))


def formato(c: dict) -> str:
    """Pedagogico = tiene el formato completo (con 'Para que te sirve esto'); compacto = formato inicial."""
    ruta = RAIZ / c["ruta"] / "README.md"
    if ruta.is_file() and "## ¿Para qué te sirve esto?" in ruta.read_text(encoding="utf-8"):
        return "✅ pedagógico"
    return "🟡 compacto"


def primer_objetivo(c: dict) -> str:
    """Primer resultado de aprendizaje de la clase (lo que se aprendera), tomado de su README."""
    ruta = RAIZ / c["ruta"] / "README.md"
    if not ruta.is_file():
        return ""
    m = re.search(r"## (?:Objetivos|Resultados de aprendizaje|Al terminar esta clase podrás)\s+(?:1\.\s+|- )(.+)", ruta.read_text(encoding="utf-8"))
    return m.group(1).strip() if m else ""


def readme_parte(p: dict) -> str:
    g = guias().get(p["id"], {})
    sal = [f"# Parte {p['id']} — {p['titulo']}", "",
           f"**Nivel:** {p['nivel']} · **Duración estimada:** {p['semanas']} semanas · **Clases:** {len(p['clases'])}", ""]
    if g:
        sal += ["## De qué trata", "", g["de_que_trata"], "", "## Por qué importa", "", g["por_que_importa"], "",
                "## Según tu papel", "",
                f"- **Si construyes o aplicas instrumentos:** {g['si_construyes']}",
                f"- **Si eres evaluado o recibes resultados:** {g['si_eres_evaluado']}", "",
                "## Al terminar esta parte podrás", ""] + [f"- {x}" for x in g["al_terminar"]]
        sal += ["", "## Cómo estudiarla", "", g["como_estudiarla"], ""]
    else:
        sal += [p["descripcion"].strip(), ""]
    sal += ["## Clases en orden de estudio", "",
            "El número de clase (ID) es permanente y no se reutiliza; por eso en algunas partes no es correlativo. "
            "Sigue la columna **Orden**.", "",
            "| Orden | ID | Clase | Qué aprenderás | Formato | Horas |", "|---:|---|---|---|---|---:|"]
    for i, c in enumerate(p["clases"], 1):
        carpeta = pathlib.PurePosixPath(c["ruta"]).name
        titulo = f"[{c['titulo']}]({carpeta}/README.md)" if c["estado"] == "escrita" else f"{c['titulo']} (planificada)"
        sal.append(f"| {i} | {c['id']} | {titulo} | {primer_objetivo(c)} | {formato(c)} | {c['horas_estimadas']} |")
    sal += ["", "[← Volver al índice del programa](../../README.md) · [Índice numérico de las 200 clases](../../PROGRAMA.md)", ""]
    return "\n".join(sal)


def indice_numerico(partes: list[dict]) -> str:
    sal = ["# Índice numérico de las clases", "",
           "Todas las clases ordenadas por número (001 a 200). Para estudiar usa el **orden de estudio** de cada parte; "
           "el número es un identificador permanente.", "",
           "| ID | Clase | Parte | Orden en la parte |", "|---|---|---|---:|"]
    filas = []
    for p in partes:
        for i, c in enumerate(p["clases"], 1):
            carpeta = pathlib.PurePosixPath(c["ruta"]).name
            filas.append((int(c["id"]), f"| {c['id']} | [{c['titulo']}](classes/{dir_parte(p)}/{carpeta}/README.md) | "
                                         f"[{p['id']} — {p['titulo']}](classes/{dir_parte(p)}/README.md) | {i} |"))
    sal += [f for _, f in sorted(filas)]
    return "\n".join(sal) + "\n"


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
    nuevo = f"{antes}{INICIO}\n{tabla_programa(partes)}\n{FIN}{despues}"
    clases = [c for p in partes for c in p["clases"]]
    esc = sum(c["estado"] == "escrita" for c in clases)
    labs = sum(1 for c in clases
               if c["estado"] == "escrita" and (RAIZ / c["ruta"] / "lab.py").is_file())
    n = len(clases)
    nuevo = re.sub(r"clases-\d+%20de%20\d+%20escritas", f"clases-{esc}%20de%20{n}%20escritas", nuevo)
    nuevo = re.sub(r"(\| \*\*\d+\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \| )\*\*\d+ / \d+\*\* \| \*\*\d+\*\*",
                   rf"\g<1>**{esc} / {n}** | **{labs}**", nuevo)
    nuevo = re.sub(r"🟡 \d+ de \d+ escritas; las \d+ restantes",
                   f"🟡 {esc} de {n} escritas; las {n - esc} restantes", nuevo)
    aplica(RAIZ / "README.md", nuevo)
    for p in partes:
        aplica(RAIZ / "classes" / dir_parte(p) / "README.md", readme_parte(p))
    aplica(RAIZ / "PROGRAMA.md", indice_numerico(partes))

    if desfasados:
        print(("DESFASADOS" if check else "ACTUALIZADOS") + ": " + ", ".join(desfasados))
        return 1 if check else 0
    print("indices sincronizados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
