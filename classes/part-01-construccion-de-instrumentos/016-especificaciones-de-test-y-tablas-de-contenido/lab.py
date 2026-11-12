"""Laboratorio 016 - Tabla de especificaciones: asignar items por peso y verificar las formas.

Una tabla de especificaciones fija cuantos items de cada contenido y nivel cognitivo debe tener la
prueba. Se reparten 40 items segun pesos (contenido x nivel) con el metodo del resto mayor, que
garantiza que la suma sea exactamente 40. Luego se ensamblan DOS formas desde un banco sintetico
y se verifica que ambas cumplan la tabla. Datos sinteticos.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
TOTAL = 40
PESOS = {
    ("Numeros", "Recordar"): 0.08, ("Numeros", "Aplicar"): 0.14, ("Numeros", "Razonar"): 0.08,
    ("Geometria", "Recordar"): 0.06, ("Geometria", "Aplicar"): 0.12, ("Geometria", "Razonar"): 0.07,
    ("Datos", "Recordar"): 0.05, ("Datos", "Aplicar"): 0.15, ("Datos", "Razonar"): 0.10,
    ("Algebra", "Recordar"): 0.03, ("Algebra", "Aplicar"): 0.09, ("Algebra", "Razonar"): 0.03,
}


def resto_mayor(pesos: dict, total: int) -> dict:
    s = sum(pesos.values())
    exactos = {k: v / s * total for k, v in pesos.items()}
    base = {k: math.floor(v) for k, v in exactos.items()}
    faltan = total - sum(base.values())
    for k in sorted(exactos, key=lambda k: exactos[k] - base[k], reverse=True)[:faltan]:
        base[k] += 1
    return base


def main() -> None:
    cuotas = resto_mayor(PESOS, TOTAL)
    redondeo = {k: round(v / sum(PESOS.values()) * TOTAL) for k, v in PESOS.items()}
    print(f"Suma de pesos = {sum(PESOS.values()):.2f}; suma con redondeo simple = {sum(redondeo.values())}; "
          f"suma con resto mayor = {sum(cuotas.values())}")
    niveles = ["Recordar", "Aplicar", "Razonar"]
    print(f"\n{'contenido':<12}" + "".join(f"{n:>10}" for n in niveles) + f"{'total':>8}")
    for c in ("Numeros", "Geometria", "Datos", "Algebra"):
        fila = [cuotas[(c, n)] for n in niveles]
        print(f"{c:<12}" + "".join(f"{v:10d}" for v in fila) + f"{sum(fila):8d}")
    rng = random.Random(SEMILLA)
    banco = {k: [(f"{k[0][:3]}-{k[1][:3]}-{i:02d}", rng.gauss(0, 1)) for i in range(2 * v + 3)] for k, v in cuotas.items()}
    usados: set[str] = set()
    formas = []
    for _ in range(2):
        forma = []
        for k, v in cuotas.items():
            libres = sorted((it for it in banco[k] if it[0] not in usados), key=lambda x: x[1])
            sel = libres[::2][:v] if len(libres) >= 2 * v else libres[:v]
            usados.update(i for i, _ in sel)
            forma += [(k, d) for _, d in sel]
        formas.append(forma)
    for n, f in enumerate(formas, 1):
        cumple = all(sum(1 for k, _ in f if k == kk) == v for kk, v in cuotas.items())
        media_d = sum(d for _, d in f) / len(f)
        print(f"Forma {n}: {len(f)} items; cumple la tabla: {cumple}; dificultad media = {media_d:+.2f}")
    print()
    print("Lectura: el redondeo simple puede no sumar el total (aqui coincidio, pero no esta garantizado); el resto mayor lo asegura. La tabla es el")
    print("puente entre el dominio y los items: sin ella la validez de contenido (clase 032) no se puede auditar.")
    print("Los pesos reflejan decisiones curriculares que deben justificarse con el programa y con expertos.")


if __name__ == "__main__":
    main()
