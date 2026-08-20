"""Laboratorio 004 - Promedio de promedios frente a media por item.

Compara los dos metodos de agregacion jerarquica sobre el catalogo real y
sobre un instrumento sintetico con facetas de distinto tamano.

El resultado sobre el catalogo es que COINCIDEN, y el laboratorio explica por
que: todas las escalas hoja tienen 4 items, asi que el promedio de promedios ya
esta ponderado por igual. La divergencia solo aparece cuando los tamanos
difieren, y para eso hace falta el caso sintetico.

Nota metodologica: los calculos se hacen desde `bruto` e `items_respondidos`,
no desde `media_item`, porque esta ultima viene redondeada a 4 decimales y ese
redondeo se confundiria con una divergencia real del metodo. La primera version
de este laboratorio tenia justamente ese fallo y marcaba como divergentes
escalas que coincidian.
"""
from __future__ import annotations

import random
import statistics
import sys

sys.path.insert(0, "src")

from psychometrics.motor import (  # noqa: E402
    Respuesta,
    cargar_desde_texto,
    catalogo,
    puntuar,
)

SEMILLA = 20260819
TOLERANCIA = 1e-9

# Instrumento sintetico: la faceta CORTA tiene 2 items y la LARGA tiene 6.
# Es la unica forma de ver la divergencia, porque el catalogo real no la tiene.
DESIGUAL = """
codigo: sintetico-desigual
version: "1.0.0"
nombre: {es: Instrumento con facetas de distinto tamano}
tipo_respuesta: likert
procedencia:
  autores: laboratorio 004
  anio: 2026
  fuente: classes/part-00-fundamentos-de-la-medicion/004-puntaje-bruto-y-media-por-item/lab.py
  licencia: autoria-propia
  notas: {sin_validar: "sin estudio de validacion; es un caso de demostracion"}
opciones:
  - {valor: 1, etiqueta: {es: uno}}
  - {valor: 2, etiqueta: {es: dos}}
  - {valor: 3, etiqueta: {es: tres}}
  - {valor: 4, etiqueta: {es: cuatro}}
  - {valor: 5, etiqueta: {es: cinco}}
escalas:
  - {codigo: TOT, nombre: {es: Total}}
  - {codigo: CORTA, padre: TOT, nombre: {es: Faceta corta}}
  - {codigo: LARGA, padre: TOT, nombre: {es: Faceta larga}}
items:
  - {id: k1, escala: CORTA, texto: {es: corta 1}}
  - {id: k2, escala: CORTA, texto: {es: corta 2}}
  - {id: l1, escala: LARGA, texto: {es: larga 1}}
  - {id: l2, escala: LARGA, texto: {es: larga 2}}
  - {id: l3, escala: LARGA, texto: {es: larga 3}}
  - {id: l4, escala: LARGA, texto: {es: larga 4}}
  - {id: l5, escala: LARGA, texto: {es: larga 5}}
  - {id: l6, escala: LARGA, texto: {es: larga 6}}
"""


def media_exacta(puntaje) -> float:
    """Media por item sin el redondeo de presentacion."""
    return puntaje.bruto / puntaje.items_respondidos if puntaje.items_respondidos else 0.0


def compara(ins, respuestas):
    res = puntuar(ins, respuestas)
    filas = []
    for raiz in ins.raices:
        hijas = ins.hijas_de(raiz.codigo)
        if not hijas:
            continue
        tamanos = sorted({len(ins.items_de(h.codigo)) for h in hijas})
        a = statistics.fmean(media_exacta(res[h.codigo]) for h in hijas)
        b = media_exacta(res[raiz.codigo])
        filas.append((raiz.codigo, len(hijas), tamanos, a, b))
    return filas


def imprime(titulo, filas) -> bool:
    print(f"\n{titulo}")
    print(f"  {'escala':8} {'hijas':>5} {'tam.hijas':>12} {'A prom.prom':>12} "
          f"{'B media item':>13} {'A - B':>10}")
    hubo = False
    for codigo, n_hijas, tamanos, a, b in filas:
        diverge = abs(a - b) > TOLERANCIA
        hubo |= diverge
        marca = "  <-- DIVERGEN" if diverge else ""
        print(f"  {codigo:8} {n_hijas:5} {str(tamanos):>12} {a:12.6f} {b:13.6f} "
              f"{a - b:10.6f}{marca}")
    return hubo


def main() -> None:
    rng = random.Random(SEMILLA)
    print("Agregacion jerarquica: promedio de promedios (A) frente a media por item (B)")
    print("=" * 78)

    alguna = False
    for ins in catalogo():
        respuestas = [Respuesta(i.id, rng.randint(1, 5)) for i in ins.items]
        filas = compara(ins, respuestas)
        if filas:
            alguna |= imprime(f"{ins.codigo}  (catalogo real)", filas)

    sintetico = cargar_desde_texto(DESIGUAL, origen="sintetico-desigual")
    # Valores elegidos a mano para que la divergencia sea grande y visible:
    # la faceta corta puntua 5 y la larga 1.
    respuestas = [Respuesta(i.id, 5 if i.escala == "CORTA" else 1) for i in sintetico.items]
    diverge_sintetico = imprime("sintetico-desigual  (2 items frente a 6)",
                                compara(sintetico, respuestas))

    print()
    print("=" * 78)
    print("Lectura del resultado")
    print()
    if alguna:
        print("  Hay divergencia en el catalogo real; revisa los tamanos de hija.")
    else:
        print("  En TODO el catalogo real los dos metodos coinciden, porque cada")
        print("  escala hoja tiene exactamente 4 items. Cuando los pesos ya son")
        print("  iguales, ponderar o no ponderar da lo mismo.")
    print()
    if diverge_sintetico:
        print("  En el sintetico si divergen: A = 3.0 porque le da a la faceta de 2")
        print("  items el mismo peso que a la de 6. B = 2.0 porque pondera por")
        print("  item, que es lo que dice la definicion de media por item.")
    print()
    print("  Conclusion: no es que un metodo este mal siempre. Es que A decide en")
    print("  silencio que todas las facetas pesan igual. Si esa es la intencion,")
    print("  hay que declararla; si no lo es, hay que usar B. El motor usa B.")
    print("  Ver src/psychometrics/motor/puntuacion.py, paso 3.")


if __name__ == "__main__":
    main()
