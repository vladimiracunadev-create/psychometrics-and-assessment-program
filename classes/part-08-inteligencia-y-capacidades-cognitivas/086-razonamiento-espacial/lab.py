"""Laboratorio 086 - Rotacion mental: el tiempo de respuesta crece con el angulo.

Paradigma clasico (Shepard y Metzler, 1971): el tiempo de respuesta aumenta ~linealmente con el
angulo de rotacion. Se simulan 200 personas con intercepto (tiempo base) y pendiente (costo por
grado) propios, 8 angulos x 10 ensayos. Se ajusta una recta por persona y se calculan:
  - la pendiente media (ms por grado), el intercepto medio;
  - la fiabilidad (mitades pares/impares) de la PENDIENTE individual;
  - la tasa de error por angulo.
La pendiente es el indicador de "velocidad de rotacion", pero es una medida diferencial, de baja
fiabilidad.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, ANGULOS, ENSAYOS = 200, (0, 45, 90, 135, 180, 225, 270, 315), 10


def pendiente(xs: list[float], ys: list[float]) -> float:
    return statistics.covariance(xs, ys) / statistics.variance(xs)


def main() -> None:
    rng = random.Random(SEMILLA)
    personas = []
    for _ in range(N):
        inter = rng.gauss(900, 150)
        pend = max(1.0, rng.gauss(6.0, 1.5))          # ms por grado
        ensayos = []
        for a in ANGULOS:
            for _ in range(ENSAYOS):
                ang = min(a, 360 - a)                  # rotacion efectiva (camino mas corto)
                rt = inter + pend * ang + rng.gauss(0, 250)
                error = rng.random() < 0.05 + 0.0006 * ang
                ensayos.append((a, ang, rt, error))
        personas.append((inter, pend, ensayos))

    sl_par, sl_imp = [], []
    for _, _, ens in personas:
        pares = [e for i, e in enumerate(ens) if i % 2 == 0 and not e[3]]
        impares = [e for i, e in enumerate(ens) if i % 2 == 1 and not e[3]]
        sl_par.append(pendiente([e[1] for e in pares], [e[2] for e in pares]))
        sl_imp.append(pendiente([e[1] for e in impares], [e[2] for e in impares]))
    r = statistics.correlation(sl_par, sl_imp)
    sb = 2 * r / (1 + r)
    print(f"Pendiente verdadera media = {statistics.fmean(p for _, p, _ in personas):.2f} ms/grado")
    print(f"Pendiente estimada media (mitad pares) = {statistics.fmean(sl_par):.2f} ms/grado")
    print(f"Fiabilidad de la pendiente individual: r mitades = {r:.2f}; Spearman-Brown = {sb:.2f}")
    print("\nTasa de error por angulo efectivo:")
    for ang in (0, 45, 90, 135, 180):
        es = [e[3] for _, _, ens in personas for e in ens if e[1] == ang]
        print(f"  {ang:3d} grados: {statistics.fmean(es):.3f}")
    print()
    print("Lectura: el efecto del angulo es nitido y, con 80 ensayos por mitad, la pendiente individual")
    print("es razonablemente fiable. Es una medida diferencial: con pocos ensayos su fiabilidad cae")
    print("mucho (clase 097), y conviene sumar la precision (aciertos) a la velocidad (clase 089).")


if __name__ == "__main__":
    main()
