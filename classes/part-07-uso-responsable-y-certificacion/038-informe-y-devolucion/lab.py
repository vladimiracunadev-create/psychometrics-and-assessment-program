"""Laboratorio 038 - Redactar un informe de resultados que no sobreafirma.

Genera un texto en lenguaje claro a partir de un puntaje, la media y la DE del baremo y la
fiabilidad. Reglas de redaccion aplicadas (verificables con las comprobaciones del final):
  1. se informa el intervalo (ETM), no solo el punto;
  2. se describe en terminos de rango y no con etiquetas de persona;
  3. se declara el alcance (que mide, que no) y se invita a hablar el resultado;
  4. si el intervalo cruza el corte, no se emite una conclusion categorica.
Los textos son ejemplos didacticos; un informe real depende del instrumento, el proposito y la ley.
"""
from __future__ import annotations

import math


def informe(puntaje: float, media: float, de: float, rho: float, corte: float | None = None) -> str:
    etm = de * math.sqrt(1 - rho)
    lo, hi = puntaje - 1.96 * etm, puntaje + 1.96 * etm
    z = (puntaje - media) / de
    if z < -1:
        rango = "por debajo de lo que muestra la mayoria del grupo de referencia"
    elif z > 1:
        rango = "por encima de lo que muestra la mayoria del grupo de referencia"
    else:
        rango = "dentro del rango que muestra la mayoria del grupo de referencia"
    lineas = [
        f"Resultado: {puntaje:.0f} puntos. Considerando el margen de error de la prueba, el valor",
        f"mas probable esta entre {lo:.0f} y {hi:.0f}. Este resultado se ubica {rango}.",
        "Esta prueba mide solo un aspecto en un momento determinado; no describe a la persona",
        "completa ni predice por si sola lo que hara. Conversemos el resultado antes de decidir.",
    ]
    if corte is not None:
        if lo <= corte <= hi:
            lineas.append(f"Atencion: el margen de error incluye el punto de referencia ({corte:.0f}); "
                          "con este solo resultado no corresponde una conclusion categorica.")
        else:
            lado = "sobre" if puntaje > corte else "bajo"
            lineas.append(f"El resultado esta {lado} el punto de referencia ({corte:.0f}) incluso "
                          "considerando el margen de error.")
    return "\n".join(lineas)


def revisa(texto: str) -> dict[str, bool]:
    t = texto.lower()
    return {"incluye intervalo": "entre" in t and "error" in t,
            "sin etiquetas de persona": not any(p in t for p in ("deficiente", "inteligente", "debil", "incapaz")),
            "declara alcance": "no describe" in t or "solo un aspecto" in t,
            "invita a conversar": "conversemos" in t}


def main() -> None:
    for caso in ((108, 100, 15, 0.90, 105), (85, 100, 15, 0.90, 105), (130, 100, 15, 0.90, 105)):
        t = informe(*caso)
        print(t)
        print("  comprobaciones:", {k: ("ok" if v else "FALLA") for k, v in revisa(t).items()})
        print("-" * 78)
    print("Lectura: el primer caso (108 con corte 105) no permite una conclusion categorica porque")
    print("el intervalo incluye el corte. Un informe responsable comunica incertidumbre, no la oculta.")


if __name__ == "__main__":
    main()
