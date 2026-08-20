"""Parsea el listado público del IPIP-NEO-120 (ipip.ori.org) a JSON estructurado.

Fuente: https://ipip.ori.org/30FacetNEO-PI-RItems.htm
Johnson, J. A. (2014). Journal of Research in Personality, 51, 78-89.
Dominio publico: los items del IPIP pueden usarse sin permiso ni pago.
"""
import html
import json
import pathlib
import re
import sys

DOMINIOS = {"N": "neuroticismo", "E": "extraversion", "O": "apertura",
            "A": "amabilidad", "C": "responsabilidad"}

raw = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
# Los tags se eliminan SIN insertar saltos: la estructura de líneas del HTML
# ya separa cabecera de item. Sustituirlos por \n parte "N1: <b>ANXIETY</b>(...)"
# en dos líneas y la cabecera deja de matchear.
texto = html.unescape(re.sub(r"<[^>]*>", "", raw)).replace("–", "-").replace("’", "'")
lineas = [linea.strip() for linea in texto.splitlines() if linea.strip()]

# El listado termina en la cita bibliografica; todo lo posterior es pie de pagina.
for i, linea in enumerate(lineas):
    if linea.startswith("Johnson, J. A."):
        lineas = lineas[:i]
        break

CAB = re.compile(r"^([NEOAC])(\d):\s*([A-Z][A-Z\s\-']*?)\s*\((?:Alpha\s*=\s*)?\.(\d+)\)")
KEY = re.compile(r"^([+-])\s*keyed", re.I)

facetas, actual, signo = [], None, None
for linea in lineas:
    if m := CAB.match(linea):
        dom, num, nombre, alpha = m.groups()
        actual = {"codigo": f"{dom}{num}", "dominio": DOMINIOS[dom],
                  "faceta_en": nombre.strip().lower(), "alpha": float(f"0.{alpha}"),
                  "items": []}
        facetas.append(actual)
        signo = None
    elif k := KEY.match(linea):
        signo = 1 if k.group(1) == "+" else -1
    elif actual is not None and signo is not None and linea.endswith("."):
        actual["items"].append({"texto_en": linea, "clave": signo})

errores = []
if len(facetas) != 30:
    errores.append(f"se esperaban 30 facetas, se parsearon {len(facetas)}")
for f in facetas:
    if len(f["items"]) != 4:
        errores.append(f"{f['codigo']} {f['faceta_en']}: {len(f['items'])} items (esperados 4)")
for d in DOMINIOS.values():
    n = sum(1 for f in facetas if f["dominio"] == d)
    if n != 6:
        errores.append(f"dominio {d}: {n} facetas (esperadas 6)")
total = sum(len(f["items"]) for f in facetas)
if total != 120:
    errores.append(f"se esperaban 120 items, se parsearon {total}")

print(json.dumps({"facetas": len(facetas), "items": total,
                  "invertidos": sum(1 for f in facetas for i in f["items"] if i["clave"] == -1),
                  "errores": errores}, ensure_ascii=False, indent=2))
if errores:
    sys.exit(1)
pathlib.Path(sys.argv[2]).write_text(json.dumps(facetas, ensure_ascii=False, indent=2), encoding="utf-8")
