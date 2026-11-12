"""Laboratorio 186 - Contraste de color segun WCAG: una verificacion automatica de accesibilidad.

Las pautas WCAG 2.x definen la relacion de contraste entre dos colores:
    L = 0.2126 R + 0.7152 G + 0.0722 B  (con cada canal linealizado desde sRGB)
    contraste = (L_claro + 0.05) / (L_oscuro + 0.05)
Nivel AA: >= 4.5:1 para texto normal, >= 3:1 para texto grande y componentes de interfaz.
Se calcula el contraste de varias combinaciones de una pantalla de evaluacion y se verifican los
casos limite (blanco sobre negro = 21:1). Es UN aspecto de accesibilidad: no sustituye pruebas con
lectores de pantalla, navegacion por teclado, tiempos ajustables ni pruebas con usuarios.
"""
from __future__ import annotations


def canal(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4


def luminancia(hexa: str) -> float:
    h = hexa.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a: str, b: str) -> float:
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


COMBINACIONES = [
    ("texto principal", "#1a1a1a", "#ffffff"),
    ("texto secundario gris", "#767676", "#ffffff"),
    ("texto gris claro", "#aaaaaa", "#ffffff"),
    ("boton primario", "#ffffff", "#1f6feb"),
    ("boton deshabilitado", "#9aa0a6", "#e8eaed"),
    ("error en rojo", "#d93025", "#ffffff"),
    ("opcion seleccionada", "#ffffff", "#5b2eff"),
]


def main() -> None:
    assert abs(contraste("#000000", "#ffffff") - 21.0) < 1e-9
    print("Verificacion: negro sobre blanco = 21.0:1")
    print(f"{'elemento':<24} {'texto':>8} {'fondo':>8} {'contraste':>10}  AA normal  AA grande/UI")
    print("=" * 76)
    for nombre, fg, bg in COMBINACIONES:
        c = contraste(fg, bg)
        print(f"{nombre:<24} {fg:>8} {bg:>8} {c:9.2f}:1  {'si' if c >= 4.5 else 'NO':>9}  {'si' if c >= 3 else 'NO':>11}")
    print()
    print("Lectura: un gris que 'se ve bien' al disenador puede no cumplir el contraste para quien tiene baja")
    print("vision. La verificacion automatica del color es barata y se incluye en el CI de una interfaz; ")
    print("el resto (teclado, lectores de pantalla, tiempos, lenguaje claro, descripcion de imagenes) se")
    print("verifica con pruebas especificas y usuarios. Una evaluacion inaccesible mide la barrera, no el constructo.")


if __name__ == "__main__":
    main()
