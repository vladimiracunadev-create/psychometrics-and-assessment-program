"""Aplica el resultado de la verificacion bibliografica a los README de las clases.

Uso: python scripts/aplicar_bibliografia.py <resultados.json>
- Escribe `catalogo/bibliografia.yaml` (una entrada por referencia, con estado y DOI).
- Reescribe cada seccion `## Bibliografia` anotando el estado de cada referencia.
- Genera `docs/VERIFICACION_BIBLIOGRAFIA.md` con las cifras.
Estados (honestos):
  verificada      existe en Crossref con titulo parecido y anio coincidente (+-1); se enlaza el DOI.
  edicion-difiere el titulo existe en Crossref pero el anio es otro (reedicion): revisar la edicion citada.
  sin-verificar   no se encontro en Crossref (libros, normas, sitios web, leyes): verificacion manual pendiente.
Crossref verifica la EXISTENCIA y los metadatos, no que la fuente respalde lo afirmado en la clase.
"""
from __future__ import annotations

import collections
import json
import pathlib
import re
import sys

import yaml

R = pathlib.Path(__file__).resolve().parents[1]
ENC = "## Bibliografía"


def estado(v: dict) -> str:
    if v["estado"] in ("verificado", "revisar") and v.get("doi"):
        mismo_anio = v.get("anio_ref") and v.get("anio_cr") and abs(v["anio_ref"] - v["anio_cr"]) <= 1
        if v["sim"] >= 0.6 and mismo_anio and v.get("autor_ok") is not False:
            return "verificada"
        if v["sim"] >= 0.8:
            return "edicion-difiere"
    return "sin-verificar"


def etiqueta(ref: str, v: dict) -> str:
    e = estado(v)
    if e == "verificada":
        return f"{ref} ✅ [DOI](https://doi.org/{v['doi']})"
    if e == "edicion-difiere":
        return f"{ref} ⚠️ existe, pero Crossref registra {v['anio_cr']} (¿otra edición?; [DOI](https://doi.org/{v['doi']}))"
    return f"{ref} 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)"


def main(ruta: str) -> None:
    res = json.loads(pathlib.Path(ruta).read_text(encoding="utf-8"))
    for p in R.glob("classes/*/*/README.md"):
        s = p.read_text(encoding="utf-8")
        if ENC not in s:
            continue
        cab, cola = s.split(ENC, 1)
        lineas = []
        for ln in cola.splitlines():
            if ln.startswith("- "):
                ref = re.split(r" (?:✅|⚠️|🔎) ", ln[2:].strip())[0]
                v = res.get(ref)
                ln = "- " + (etiqueta(ref, v) if v else ref)
            lineas.append(ln)
        nota = ("\n\nLeyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe "
                "pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la "
                "fuente, no que respalde cada afirmación de la clase.")
        cola2 = "\n".join(lineas).rstrip() + "\n"
        if "Leyenda: ✅" not in cola2:
            cola2 = cola2.rstrip() + nota + "\n"
        p.write_text(cab + ENC + cola2, encoding="utf-8")
    c = collections.Counter(estado(v) for v in res.values())
    reg = {k: {"estado": estado(v), "doi": v.get("doi"), "anio_crossref": v.get("anio_cr"), "clases": v["clases"]} for k, v in res.items()}
    (R / "catalogo" / "bibliografia.yaml").write_text(
        "# Registro de verificacion bibliografica (Crossref). Ver scripts/aplicar_bibliografia.py\n"
        + yaml.safe_dump(reg, allow_unicode=True, sort_keys=True), encoding="utf-8")
    sin = sorted(k for k, v in res.items() if estado(v) == "sin-verificar")
    md = (f"# Verificación bibliográfica\n\nReferencias únicas: **{len(res)}**. Consultadas contra la API pública de Crossref.\n\n"
          f"| Estado | Referencias |\n|---|---:|\n| verificada (DOI) | {c['verificada']} |\n| existe con otro año/edición | {c['edicion-difiere']} |\n"
          f"| sin verificar automáticamente | {c['sin-verificar']} |\n\n"
          "Crossref cubre sobre todo artículos y algunos libros. Los libros sin DOI, las normas (AERA/APA/NCME, ITC, WCAG), las leyes y los "
          "sitios web quedan como *sin verificar* y requieren comprobación manual en la fuente primaria. Una referencia verificada confirma que "
          "el trabajo existe, no que respalde lo que dice la clase.\n\n## Pendientes de comprobación manual\n\n"
          + "\n".join(f"- {k}" for k in sin) + "\n")
    (R / "docs" / "VERIFICACION_BIBLIOGRAFIA.md").write_text(md, encoding="utf-8")
    print(dict(c))


if __name__ == "__main__":
    main(sys.argv[1])
