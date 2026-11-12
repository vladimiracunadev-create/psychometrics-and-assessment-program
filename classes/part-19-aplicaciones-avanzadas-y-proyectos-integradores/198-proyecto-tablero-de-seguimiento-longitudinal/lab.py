"""Laboratorio 198 - Proyecto: tablero de seguimiento longitudinal en texto.

Seis estudiantes sinteticos, cinco mediciones. Para cada uno se muestra una linea de tendencia en
texto, la banda de error de medida y una marca de cambio solo si supera el Indice de Cambio Fiable
(RCI = diferencia / (sqrt(2) * EEM)). Con fiabilidad 0.85 y SD 10, EEM = 3.87 y el cambio minimo
fiable al 95 % es 10.7 puntos. El tablero evita el semaforo: describe, no clasifica.
"""
from __future__ import annotations

import math
import random

SEMILLA = 20260819
SD, REL = 10.0, 0.85
EEM = SD * math.sqrt(1 - REL)
CMF = 1.96 * math.sqrt(2) * EEM


def barra(v: float) -> str:
    return "#" * max(0, int((v - 30) / 2))


def main() -> None:
    rng = random.Random(SEMILLA)
    perfiles = {"Ana": 2.5, "Bruno": 0.0, "Carla": -2.5, "Diego": 6.0, "Elena": 0.5, "Fabian": 3.0}
    print(f"EEM = {EEM:.2f}; cambio minimo fiable (95 %) = {CMF:.1f} puntos entre dos mediciones\n")
    for nombre, pendiente in perfiles.items():
        verdadero = 50.0
        obs = []
        for t in range(5):
            verdadero += pendiente + rng.gauss(0, 1)
            obs.append(verdadero + rng.gauss(0, EEM))
        primero, ultimo = obs[0], obs[-1]
        dif = ultimo - primero
        marca = ("cambio fiable (+)" if dif > CMF else "cambio fiable (-)" if dif < -CMF else "sin cambio fiable")
        print(f"{nombre:<7} " + " ".join(f"{o:5.1f}" for o in obs) + f"   dif = {dif:+5.1f}  RCI = {dif / (math.sqrt(2) * EEM):+.2f}  {marca}")
        print(f"        ultima medicion {barra(ultimo)} (+/- {1.96 * EEM:.1f})")
    print()
    print("Lectura: la diferencia entre dos mediciones tiene un error mayor que cada medicion; por eso hay que")
    print("superar el cambio minimo fiable antes de hablar de cambio. Un tablero con semaforos convertiria el ruido")
    print("en veredictos; este lo evita mostrando valores, banda y el criterio. Regresion a la media y efectos de")
    print("practica (clase 175) tambien explican parte de las variaciones. Datos sinteticos.")


if __name__ == "__main__":
    main()
