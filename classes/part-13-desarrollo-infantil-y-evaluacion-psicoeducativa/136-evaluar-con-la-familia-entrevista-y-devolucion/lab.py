"""Laboratorio 136 - Informantes: la concordancia padres-docentes y las reglas de combinacion.

Una conducta con prevalencia real de 15 %. Cada informante (madre/padre, docente) la percibe con
sensibilidad y especificidad propias y con sesgo de contexto (la conducta puede manifestarse mas
en casa que en el aula). Se compara:
  - concordancia entre informantes (kappa),
  - regla "cualquiera de los dos": sensibilidad alta, muchos falsos positivos,
  - regla "ambos": especificidad alta, se pierden casos que solo se ven en un contexto.
Parametros supuestos. Sirve para pensar la integracion de fuentes, no para fijar reglas.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N, PREV = 40000, 0.15


def main() -> None:
    rng = random.Random(SEMILLA)
    filas = []
    for _ in range(N):
        caso = rng.random() < PREV
        en_casa = caso and rng.random() < 0.85                        # se manifiesta en casa
        en_aula = caso and rng.random() < 0.70                        # se manifiesta en el aula
        padre = (en_casa and rng.random() < 0.85) or (rng.random() < 0.08)
        docente = (en_aula and rng.random() < 0.80) or (rng.random() < 0.06)
        filas.append((caso, padre, docente))
    po = sum(p == d for _, p, d in filas) / N
    pp, pd = sum(p for _, p, _ in filas) / N, sum(d for _, _, d in filas) / N
    pe = pp * pd + (1 - pp) * (1 - pd)
    print(f"Concordancia entre padre/madre y docente: acuerdo = {po:.2f}; kappa = {(po - pe) / (1 - pe):.2f}")
    print(f"\n{'regla':<22} {'sensibilidad':>13} {'especificidad':>14} {'VPP':>6}")
    reglas = {"solo familia": lambda p, d: p, "solo docente": lambda p, d: d,
              "cualquiera de los dos": lambda p, d: p or d, "ambos": lambda p, d: p and d}
    for nombre, f in reglas.items():
        tp = sum(c and f(p, d) for c, p, d in filas)
        fp = sum((not c) and f(p, d) for c, p, d in filas)
        n_c = sum(c for c, _, _ in filas)
        print(f"{nombre:<22} {tp / n_c:13.2f} {1 - fp / (N - n_c):14.2f} {tp / max(tp + fp, 1):6.2f}")
    print()
    print("Lectura: padres y docentes concuerdan solo moderadamente, y no por ello uno 'miente': ven")
    print("contextos distintos. 'Cualquiera de los dos' detecta mas y deriva a mas ninos sin la condicion;")
    print("'ambos' pierde los casos de un solo contexto. La entrevista a la familia busca entender el")
    print("contexto, y la devolucion es una conversacion que integra fuentes, no un veredicto.")


if __name__ == "__main__":
    main()
