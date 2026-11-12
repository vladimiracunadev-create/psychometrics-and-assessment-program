"""Laboratorio 102 - Auditar un banco IPIP del repositorio: balance de clave y aquiescencia.

Lee instruments/ipip-neo-120.yaml (items y claves reales) y calcula, por escala:
  - cuantos items directos e invertidos hay,
  - que puntaje obtendria una persona que responde SIEMPRE el mismo valor (todo 5, todo 3 o todo 1)
    con la regla de puntuacion con reflejo de invertidos.
Una escala con clave equilibrada da el punto medio ante la aquiescencia pura; una desequilibrada
se desvia. NO se usan datos de personas: solo la estructura del instrumento.
"""
from __future__ import annotations

import collections
import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]


def main() -> None:
    d = yaml.safe_load((RAIZ / "instruments" / "ipip-neo-120.yaml").read_text(encoding="utf-8"))
    escalas = {e["codigo"]: e["nombre"] for e in d["escalas"]}
    por_escala: dict[str, list[int]] = collections.defaultdict(list)
    for it in d["items"]:
        por_escala[it["escala"]].append(it["clave"])
    print(f"Instrumento: {d['codigo']} | items: {len(d['items'])} | escalas: {len(escalas)}")
    print(f"Licencia declarada: {d['procedencia']['licencia']}\n")
    print(f"{'escala':<8} {'items':>5} {'inv.':>5} {'todo 5':>7} {'todo 3':>7} {'todo 1':>7}")
    print("=" * 46)
    desv = []
    for cod in sorted(por_escala):
        claves = por_escala[cod]
        def puntaje(valor: int) -> float:
            return sum(valor if c == 1 else 6 - valor for c in claves) / len(claves)
        if len(cod) == 2:                              # facetas (p. ej. N1)
            inv = sum(c == -1 for c in claves)
            desv.append(abs(puntaje(5) - 3))
            if cod[1] in "12":
                print(f"{cod:<8} {len(claves):5d} {inv:5d} {puntaje(5):7.2f} {puntaje(3):7.2f} {puntaje(1):7.2f}")
    print("  ...")
    print(f"\nDesvio medio de las facetas respecto del punto medio ante 'todo 5': {sum(desv) / len(desv):.2f} "
          f"(0 = clave perfectamente equilibrada)")
    print()
    print("Lectura: el IPIP-NEO-120 NO tiene clave equilibrada dentro de cada faceta (p. ej. N1 todo")
    print("directo y A2 todo invertido): ante aquiescencia pura, las facetas se desvian de 3 en sentidos")
    print("opuestos. El equilibrio solo se logra, si acaso, a nivel de dominio. El banco es de dominio")
    print("publico y se puede usar y adaptar, pero eso no lo vuelve un test validado para tu poblacion y")
    print("proposito: la evidencia de fiabilidad y validez se reune localmente.")


if __name__ == "__main__":
    main()
