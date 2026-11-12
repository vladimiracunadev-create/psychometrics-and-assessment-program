"""Laboratorio 006 - Un linter heuristico de items.

Detecta cuatro defectos de redaccion que la clase explica: doble pregunta,
absolutos, doble negacion y exceso de longitud. Es una AYUDA para revisar, no un
sustituto del juicio de expertos ni de la revision cognitiva (clase 049).
"""
from __future__ import annotations

import re

ABSOLUTOS = {"siempre", "nunca", "jamas", "todos", "ninguno", "todo", "nada"}
NEGACIONES = {"no", "ni", "nunca", "jamas", "nadie", "ninguno", "sin"}
MAX_PALABRAS = 20


def normaliza(texto: str) -> list[str]:
    t = texto.lower()
    for a, b in zip("áéíóúüñ", "aeiouun", strict=True):
        t = t.replace(a, b)
    return re.findall(r"[a-z]+", t)


def revisa(item: str) -> list[str]:
    palabras = normaliza(item)
    problemas = []
    # Doble cañon: dos ideas unidas por "y"/"o" -> la respuesta no es interpretable.
    if re.search(r"\b(y|o)\b", item.lower()) and len(palabras) > 8:
        problemas.append("posible doble pregunta (conjuncion y/o en un item largo)")
    if ABSOLUTOS & set(palabras):
        problemas.append("absoluto: casi nadie responde 'de acuerdo' a 'siempre/nunca'")
    if sum(p in NEGACIONES for p in palabras) >= 2:
        problemas.append("doble negacion: el acuerdo se vuelve ambiguo")
    if len(palabras) > MAX_PALABRAS:
        problemas.append(f"largo ({len(palabras)} palabras > {MAX_PALABRAS})")
    return problemas


ITEMS = [
    ("Me cuesta no distraerme cuando no hay nadie que me supervise.", "mala"),
    ("Siempre termino lo que empiezo.", "mala"),
    ("Planifico mi semana y reviso mi avance cada dia con mis companeros de equipo.", "mala"),
    ("Termino las tareas que empiezo.", "buena"),
    ("Organizo mi trabajo antes de comenzar.", "buena"),
    ("Cuando algo sale mal, busco que cambiar.", "buena"),
]


def main() -> None:
    print("Linter de items")
    print("=" * 72)
    aciertos = 0
    for texto, etiqueta in ITEMS:
        problemas = revisa(texto)
        veredicto = "mala" if problemas else "buena"
        aciertos += veredicto == etiqueta
        print(f"[{veredicto:>5} | esperado {etiqueta:>5}] {texto}")
        for p in problemas:
            print(f"        - {p}")
    print("-" * 72)
    print(f"Coincidencia con la etiqueta humana: {aciertos}/{len(ITEMS)}")
    print("Un linter no ve la ambiguedad semantica: revisa la forma, no el sentido.")


if __name__ == "__main__":
    main()
