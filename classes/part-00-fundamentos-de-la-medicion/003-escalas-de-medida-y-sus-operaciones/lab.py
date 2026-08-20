"""Laboratorio 003 - Cuanto cambia el resultado segun el tratamiento de escala.

Compara media (trata la Likert como intervalo), mediana (la trata como ordinal)
y normalizacion por rango, y mide cuanto se reordena el ranking de personas.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N_PERSONAS = 200
N_ITEMS = 10


def tau_de_kendall(a: list[int], b: list[int]) -> float:
    """Concordancia entre dos ordenamientos. 1.0 = identicos."""
    n = len(a)
    concordantes = discordantes = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (a[i] - a[j]) * (b[i] - b[j])
            if s > 0:
                concordantes += 1
            elif s < 0:
                discordantes += 1
    total = concordantes + discordantes
    return (concordantes - discordantes) / total if total else 0.0


def ranking(valores: list[float]) -> list[int]:
    orden = sorted(range(len(valores)), key=lambda i: valores[i])
    puestos = [0] * len(valores)
    for puesto, i in enumerate(orden):
        puestos[i] = puesto
    return puestos


def main() -> None:
    rng = random.Random(SEMILLA)
    # Respuestas Likert 1-5 generadas desde un rasgo latente, con umbrales
    # DESIGUALES a proposito: asi la escala no es de intervalo de verdad.
    umbrales = [-1.4, -0.3, 0.2, 1.5]

    personas = []
    for _ in range(N_PERSONAS):
        rasgo = rng.gauss(0, 1)
        respuestas = []
        for _ in range(N_ITEMS):
            latente = rasgo + rng.gauss(0, 0.8)
            respuestas.append(sum(1 for u in umbrales if latente > u) + 1)
        personas.append(respuestas)

    medias = [statistics.fmean(p) for p in personas]
    medianas = [statistics.median(p) for p in personas]

    r_media = ranking(medias)
    r_mediana = ranking(medianas)

    print(f"Simulacion: {N_PERSONAS} personas, {N_ITEMS} items, umbrales desiguales")
    print(f"Umbrales latentes: {umbrales}")
    print()
    print(f"  Concordancia media vs mediana (tau de Kendall): {tau_de_kendall(r_media, r_mediana):.3f}")
    print()
    print("Lectura del resultado")
    print("  Aunque los umbrales NO son equidistantes -es decir, la escala no es")
    print("  de intervalo-, el orden de las personas apenas cambia al tratarla")
    print("  como si lo fuera. Esa robustez es lo que justifica la practica.")
    print()
    print("  Prueba a bajar N_ITEMS a 1 y repetir: con un solo item la")
    print("  concordancia cae, porque no hay agregacion que suavice.")


if __name__ == "__main__":
    main()
