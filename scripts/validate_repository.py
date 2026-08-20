"""Comprueba que lo que el repositorio AFIRMA coincida con lo que CONTIENE.

Un README con cifras stale es una forma barata de mentir sin querer. Este script
recalcula cada cifra publicada desde su fuente de verdad y falla si no cuadra.
Lo ejecuta el CI en cada push.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import Licencia, catalogo  # noqa: E402


def main() -> int:
    fallos: list[str] = []
    ins = catalogo()
    readme = (RAIZ / "README.md").read_text(encoding="utf-8")

    n_ins = len(ins)
    n_items = sum(len(i.items) for i in ins)
    n_esc = sum(len(i.escalas) for i in ins)
    n_pub = sum(len(i.items) for i in ins
                if i.procedencia.licencia is Licencia.DOMINIO_PUBLICO)

    # 1. La tabla de cifras del encabezado.
    fila = re.search(r"^\| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| "
                     r"\*\*(\d+) / (\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \|",
                     readme, re.M)
    if not fila:
        fallos.append("README: no se encontro la tabla de cifras del encabezado")
    else:
        d_ins, d_items, d_esc, d_escritas, d_clases, d_labs, _ = map(int, fila.groups())
        if d_ins != n_ins:
            fallos.append(f"README declara {d_ins} instrumentos; hay {n_ins}")
        if d_items != n_items:
            fallos.append(f"README declara {d_items} items; hay {n_items}")
        if d_esc != n_esc:
            fallos.append(f"README declara {d_esc} escalas; hay {n_esc}")

    # 2. El curriculo frente al arbol classes/.
    curr = yaml.safe_load((RAIZ / "curriculum.yaml").read_text(encoding="utf-8"))
    declaradas = [c for p in curr["temario"] for c in p["clases"]]
    if len(declaradas) != curr["clases"]:
        fallos.append(f"curriculum: declara {curr['clases']} clases, enumera {len(declaradas)}")

    escritas = 0
    for clase in declaradas:
        carpeta = RAIZ / clase["ruta"]
        if not carpeta.is_dir():
            fallos.append(f"curriculum: la ruta {clase['ruta']} no existe")
            continue
        if clase["estado"] != "escrita":
            continue
        escritas += 1
        for archivo in ("README.md", "lab.py", "lesson.yaml"):
            if not (carpeta / archivo).is_file():
                fallos.append(f"{clase['ruta']}: declarada escrita pero falta {archivo}")

    if fila and escritas != d_escritas:
        fallos.append(f"README declara {d_escritas} clases escritas; el curriculo tiene {escritas}")
    if fila and len(declaradas) != d_clases:
        fallos.append(f"README declara {d_clases} clases; el curriculo tiene {len(declaradas)}")

    # 3. Los items de dominio publico que afirma el badge.
    if f"{n_pub}%20de%20{n_items}%20items" not in readme.replace("í", "i"):
        if not re.search(rf"dominio%20p[^-]*-{n_pub}%20de%20{n_items}", readme):
            fallos.append(f"README: el badge de dominio publico no dice {n_pub} de {n_items}")

    # 4. Todo instrumento sin validar debe declararlo.
    for i in ins:
        if i.procedencia.licencia is Licencia.AUTORIA_PROPIA:
            notas = " ".join(i.procedencia.notas.values()).lower()
            if "sin validar" not in notas and "sin estudio de validaci" not in notas:
                fallos.append(f"{i.codigo}: autoria propia sin declarar falta de validacion")

    # 5. Los laboratorios declarados deben ejecutarse sin error.
    for clase in declaradas:
        if clase["estado"] != "escrita":
            continue
        lab = RAIZ / clase["ruta"] / "lab.py"
        if not lab.is_file():
            continue
        r = subprocess.run([sys.executable, str(lab)], cwd=RAIZ,
                           capture_output=True, text=True)
        if r.returncode != 0:
            fallos.append(f"{clase['ruta']}/lab.py fallo con codigo {r.returncode}")

    print("Validacion estructural del repositorio")
    print("=" * 60)
    print(f"  instrumentos      {n_ins}")
    print(f"  items             {n_items} ({n_pub} de dominio publico)")
    print(f"  escalas           {n_esc}")
    print(f"  clases            {len(declaradas)} ({escritas} escritas)")
    print()
    if fallos:
        print(f"{len(fallos)} INCOHERENCIA(S):")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print("TODO COHERENTE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
