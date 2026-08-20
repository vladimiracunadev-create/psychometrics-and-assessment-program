"""Parsea el IPIP-VIA-R (96 items, 24 fortalezas del caracter) a JSON.

Fuente: https://ipip.ori.org/IPIP-VIA-R_Key.html
Bluemke, M., Partsch, M. V., Saucier, G., & Lechner, C. M. (2021).
Marco VIA: Peterson, C., & Seligman, M. E. P. (2004).

Dominio público (International Personality Item Pool).

El HTML está exportado desde Word, así que un mismo item puede venir partido en
varias líneas dentro de un <p>. Por eso se segmenta por párrafo y no por salto
de linea: partir por \n rompe items como "Experience deep\nemotions when...".
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys

ESPERADAS = 24
ITEMS_POR_ESCALA = 4

# Cabecera de escala: nombre seguido del código entre corchetes. Seis escalas
# arrastran además el código nuevo propuesto por los autores, con la forma
# "[IND (new: PEV)]"; se conserva el histórico y se anota el nuevo aparte.
CABECERA = re.compile(
    r"^(?P<nombre>[A-Za-z][A-Za-z\s\-,'/]*?)\s*"
    r"\[(?P<codigo>[A-Z]{2,4})(?:\s*\(new:\s*(?P<nuevo>[A-Z]{2,4})\)\s*)?\]"
)
KEYED = re.compile(r"^[–—+-]\s*keyed\b", re.I)


def parrafos(ruta: pathlib.Path) -> list[str]:
    """Devuelve el texto plano de cada <p> del cuerpo, ya normalizado."""
    raw = ruta.read_text(encoding="utf-8", errors="replace")
    cuerpo = raw.split("<body", 1)[-1]
    cuerpo = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", cuerpo, flags=re.S | re.I)
    salida = []
    for bruto in re.split(r"<p[\s>]", cuerpo, flags=re.I):
        # El split consume "<p" pero deja los atributos ("class=... style=...>")
        # pegados al contenido. Todo lo anterior al primer ">" es la etiqueta.
        bruto = bruto.split(">", 1)[-1] if ">" in bruto.split("\n", 1)[0] else bruto
        texto = html.unescape(re.sub(r"<[^>]+>", " ", bruto))
        texto = texto.replace("\xa0", " ").replace("’", "'")
        texto = re.sub(r"[\s­]+", " ", texto)
        # Word deja rellenos de Wingdings/privados al final de línea.
        texto = re.sub(r"[�-■-◿]+", " ", texto).strip()
        if texto:
            salida.append(texto)
    return salida


def main() -> int:
    origen = pathlib.Path(sys.argv[1])
    destino = pathlib.Path(sys.argv[2])

    escalas: list[dict] = []
    actual: dict | None = None
    signo: int | None = None
    en_bloque = 0

    for p in parrafos(origen):
        if KEYED.match(p):
            signo = 1 if p.lstrip()[0] == "+" else -1
            en_bloque = 0
            continue
        if (m := CABECERA.match(p)) and "keyed" not in p.lower():
            actual = {
                "codigo": m.group("codigo"),
                "codigo_nuevo": m.group("nuevo"),
                "fortaleza_en": m.group("nombre").strip().lower(),
                "items": [],
            }
            escalas.append(actual)
            signo = None
            en_bloque = 0
            continue
        # Un item es cualquier párrafo de contenido dentro de un bloque keyed.
        # No se exige punto final: el original trae "Believe it is always better
        # to be safe than sorry" sin punto, y varios items arrastran una marca
        # de nota al pie ("Hold grudges. a") que hay que limpiar.
        # Cada bloque keyed aporta exactamente 2 items. El tope por bloque, y no
        # por escala, evita que el pie de pagina posterior al último bloque se
        # cuele como items de la última escala.
        if actual is not None and signo is not None and len(p) > 10 and en_bloque < 2:
            texto = re.sub(r"\s+[a-z]$", "", p).strip()
            if not texto.endswith("."):
                texto += "."
            actual["items"].append({"texto_en": texto, "clave": signo})
            en_bloque += 1

    errores: list[str] = []
    if len(escalas) != ESPERADAS:
        errores.append(f"se esperaban {ESPERADAS} escalas, se parsearon {len(escalas)}")
    for e in escalas:
        if len(e["items"]) != ITEMS_POR_ESCALA:
            errores.append(f"{e['codigo']} {e['fortaleza_en']}: {len(e['items'])} items")
        directos = sum(1 for i in e["items"] if i["clave"] == 1)
        if directos != ITEMS_POR_ESCALA // 2:
            errores.append(
                f"{e['codigo']}: {directos} items directos; el IPIP-VIA-R es de clave "
                "equilibrada y debe tener 2 directos y 2 invertidos"
            )
    total = sum(len(e["items"]) for e in escalas)

    print(json.dumps(
        {"escalas": len(escalas), "items": total, "errores": errores},
        ensure_ascii=False, indent=2,
    ))
    if errores:
        return 1
    destino.write_text(json.dumps(escalas, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
