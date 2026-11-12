"""Vuelca el contenido compacto de una clase y la salida de su laboratorio (uso interno de trabajo)."""
import pathlib
import re
import subprocess
import sys

R = pathlib.Path(".")
for n in sys.argv[1:]:
    d = next(R.glob(f"classes/*/{n}-*"))
    t = (d / "README.md").read_text(encoding="utf-8")
    t = re.sub(r"<!-- NAV -->.*?<!-- /NAV -->", "", t, flags=re.S)
    lineas = [x for x in t.split("\n") if x.strip() and not x.startswith(("![", "> ", "Leyenda", "---", "```"))]
    print(f"=========== {n} {d.name}")
    print("\n".join(x[:300] for x in lineas[:52]))
    print("--- LAB")
    out = subprocess.run([sys.executable, str(d / "lab.py")], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    print("\n".join(x[:180] for x in out.split("\n")[:24]))
