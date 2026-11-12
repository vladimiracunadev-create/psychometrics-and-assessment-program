"""Figuras de las clases 011 a 020 (parte 01). Valores tomados de la ejecucion de cada lab.py."""
from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "src"))

from psychometrics.figuras import AZUL, ROJO, VERDE, Lienzo, cadena, guardar  # noqa: E402


def carpeta(n: str) -> pathlib.Path:
    return next(AQUI.glob(f"{n}-*"))


# 011 proceso de respuesta y defectos
(carpeta("011") / "figura-1.svg").write_text(cadena(
    "Cada defecto rompe un paso de la respuesta", "Responder un item tiene cuatro pasos; cada defecto de redaccion rompe uno y produce un dato contaminado.",
    ["1. Comprender el ítem", "2. Recordar o buscar información", "3. Juzgar la respuesta", "4. Elegir una categoría"],
    ["jerga, doble negación", "ambigüedad de frecuencia", "absolutos, deseabilidad", "doble pregunta"]), encoding="utf-8")

# 012 fidelidad del formato
cats = [2, 3, 4, 5, 7, 11]
r = [0.797, 0.887, 0.932, 0.955, 0.976, 0.989]
lz = Lienzo("Más categorías, rendimientos decrecientes", "Correlacion entre la categoria registrada y el rasgo: de 0,80 con 2 categorias a 0,99 con 11.",
            "Número de categorías de respuesta", "Correlación con el rasgo", (0, 12), (0.75, 1.0))
lz.ejes()
lz.linea(cats, r, AZUL)
lz.puntos(cats, r, AZUL, r=4, opacidad=1)
lz.texto(2.2, 0.80, "2 categorías: 0,80")
lz.texto(7.2, 0.965, "7: 0,976")
guardar(carpeta("012") / "figura-1.svg", lz)

# 013 ipsativo: correlacion media inducida
ks = [3, 4, 6, 8]
lz = Lienzo("El formato ipsativo fabrica correlaciones negativas", "Correlacion media entre escalas independientes: cerca de 0 en formato normativo y -1/(k-1) en ipsativo.",
            "Número de escalas (k)", "Correlación media entre escalas", (2, 9), (-0.6, 0.1))
lz.ejes()
lz.linea(ks, [0.004, 0.001, -0.002, -0.001], VERDE, "normativo")
lz.linea(ks, [-0.5, -0.333, -0.2, -0.143], ROJO, "ipsativo = −1/(k−1)")
lz.puntos(ks, [-0.5, -0.333, -0.2, -0.143], ROJO, r=4, opacidad=1)
guardar(carpeta("013") / "figura-1.svg", lz)

# 014 Spearman-Brown
ks = list(range(1, 41))
sb = [k * 0.25 / (1 + (k - 1) * 0.25) for k in ks]
lz = Lienzo("Fiabilidad según el número de ítems (r₁ = 0,25)", "Curva de Spearman-Brown: 0,80 con unos 12 items y 0,90 con unos 27; despues crece poco.",
            "Número de ítems", "Fiabilidad", (0, 40), (0, 1))
lz.ejes()
lz.linea(ks, sb, AZUL)
lz.vertical(12, VERDE, "12 ítems → 0,80")
lz.vertical(27, ROJO, "27 → 0,90")
guardar(carpeta("014") / "figura-1.svg", lz)

# 015 dificultad y discriminacion
p = [0.70, 0.65, 0.55, 0.53, 0.42, 0.39, 0.30, 0.25, 0.69, 0.41, 0.95, 0.50]
d = [0.48, 0.34, 0.39, 0.31, 0.43, 0.38, 0.38, 0.37, 0.39, 0.53, 0.27, 0.06]
lz = Lienzo("Dificultad y discriminación de 12 ítems", "Los items 11 (demasiado facil) y 12 (casi no discrimina) quedan fuera del rango habitual.",
            "Dificultad (proporción que acierta)", "Discriminación (r ítem-resto)", (0, 1), (0, 0.6))
lz.ejes()
lz.puntos(p[:10], d[:10], AZUL, r=5, opacidad=0.9)
lz.puntos(p[10:], d[10:], ROJO, r=6, opacidad=1)
lz.texto(0.78, 0.30, "ítem 11: p = 0,95", ROJO)
lz.texto(0.40, 0.09, "ítem 12: r = 0,06", ROJO)
guardar(carpeta("015") / "figura-1.svg", lz)

# 016 tabla de especificaciones
lz = Lienzo("Reparto de 40 ítems por contenido", "Numeros: 12 de Numeros, 10 de Geometria, 12 de Datos y 6 de Algebra.",
            "Contenido (1 Números, 2 Geometría, 3 Datos, 4 Álgebra)", "Ítems", (0.4, 4.6), (0, 14))
lz.ejes(n=7)
lz.barras([1, 2, 3, 4], [12, 10, 12, 6], 0.6, AZUL)
guardar(carpeta("016") / "figura-1.svg", lz)

# 017 distractores del item q1
g = [1, 2, 3]
lz = Lienzo("Quién elige cada opción (ítem con buenos distractores)", "La clave B la elige mas el grupo alto; los distractores A, C y D, mas el grupo bajo.",
            "Grupo de habilidad (1 bajo, 2 medio, 3 alto)", "Proporción que elige la opción", (0.8, 3.2), (0, 1))
lz.ejes()
lz.linea(g, [0.36, 0.64, 0.87], VERDE, "B (clave)")
lz.linea(g, [0.29, 0.15, 0.04], ROJO, "A")
lz.linea(g, [0.21, 0.10, 0.04], AZUL, "C")
lz.linea(g, [0.14, 0.11, 0.05], "#a4561b", "D")
guardar(carpeta("017") / "figura-1.svg", lz)

# 018 jueces
lz = Lienzo("El entrenamiento mejora el acuerdo entre jueces", "Acuerdo exacto 0,35 a 0,70 y kappa ponderado 0,49 a 0,81 tras entrenar a los jueces.",
            "1–2: acuerdo exacto (sin / con entrenamiento); 3–4: kappa", "Valor", (0.4, 4.6), (0, 1))
lz.ejes()
lz.barras([1, 2], [0.35, 0.70], 0.6, AZUL)
lz.barras([3, 4], [0.49, 0.81], 0.6, VERDE)
guardar(carpeta("018") / "figura-1.svg", lz)

# 019 I-CVI por item
icvi = [1.0, 1.0, 1.0, 0.62, 1.0, 0.75, 0.75, 0.88, 0.25, 1.0]
lz = Lienzo("Relevancia según expertos (I-CVI)", "Items bajo el umbral 0,78: el 4 (0,62), el 6 y el 7 (0,75) y el 9 (0,25).",
            "Ítem", "I-CVI", (0.4, 10.6), (0, 1.1))
lz.ejes(n=5)
lz.barras(list(range(1, 11)), icvi, 0.6, AZUL)
lz.linea([0.4, 10.6], [0.78, 0.78], ROJO, "umbral 0,78", punteada=True)
guardar(carpeta("019") / "figura-1.svg", lz)

# 020 control de cambios
lz = Lienzo("Qué cambió entre la versión 1 y la 2", "De 36 items: 31 intactos, 4 modificados, 1 retirado; ademas 2 nuevos.",
            "1 intactos · 2 modificados · 3 retirados · 4 nuevos", "Ítems", (0.4, 4.6), (0, 36))
lz.ejes(n=6)
lz.barras([1, 2, 3, 4], [31, 4, 1, 2], 0.6, AZUL)
guardar(carpeta("020") / "figura-1.svg", lz)
print("figuras de la parte 01 generadas")
