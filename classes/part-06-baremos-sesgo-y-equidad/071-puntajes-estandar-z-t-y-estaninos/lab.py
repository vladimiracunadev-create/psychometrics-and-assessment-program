"""Laboratorio 071 - Puntajes estandar: z, T, estaninos y la normalizacion.

Se transforman puntajes de una distribucion ASIMETRICA (prueba facil con efecto techo):
  - lineal: z = (x - media)/DE; T = 50 + 10 z; estanino = 5 + 2z (acotado a 1-9);
  - normalizada (area): rango percentil -> cuantil normal -> escala deseada.
Las bandas del estanino por percentil acumulado son 4, 11, 23, 40, 60, 77, 89, 96 %.
La transformacion lineal conserva la forma asimetrica; la normalizada fuerza una normal,
lo que solo es defendible si el rasgo es normal y la asimetria es un artefacto del test.
"""
from __future__ import annotations

import bisect
import random
import statistics
from statistics import NormalDist

SEMILLA = 20260819
CORTES = [4, 11, 23, 40, 60, 77, 89, 96]


def estanino_percentil(pct: float) -> int:
    return 1 + bisect.bisect_right(CORTES, pct)


def main() -> None:
    rng = random.Random(SEMILLA)
    crudos = sorted(min(40, max(0, round(40 - abs(rng.gauss(0, 9))))) for _ in range(5000))
    m, s = statistics.fmean(crudos), statistics.pstdev(crudos)
    nd = NormalDist()

    def pct_rango(x: int) -> float:
        return 100 * (bisect.bisect_left(crudos, x) + bisect.bisect_right(crudos, x)) / 2 / len(crudos)

    print(f"Puntajes brutos (0-40): media = {m:.1f}, DE = {s:.1f}; asimetria negativa (techo)")
    print(f"{'bruto':>6} {'pct':>6} | {'T lineal':>9} {'T normaliz.':>12} | {'estanino lineal':>16} {'estanino normaliz.':>19}")
    print("=" * 80)
    for x in (10, 20, 28, 34, 38, 40):
        z = (x - m) / s
        pct = pct_rango(x)
        zn = nd.inv_cdf(min(max(pct / 100, 0.001), 0.999))
        est_lin = max(1, min(9, round(5 + 2 * z)))
        print(f"{x:6d} {pct:6.1f} | {50 + 10 * z:9.1f} {50 + 10 * zn:12.1f} | {est_lin:16d} {estanino_percentil(pct):19d}")
    print()
    print("Lectura: con distribucion asimetrica, T lineal y T normalizado dan lecturas distintas")
    print("(especialmente en la cola larga). La normalizacion es una decision con supuestos, y se")
    print("declara en el manual. Los estaninos agrupan en 9 bandas: ocultan diferencias pequenas,")
    print("que es justo lo que se quiere cuando la medida no es tan precisa (clase 015).")


if __name__ == "__main__":
    main()
