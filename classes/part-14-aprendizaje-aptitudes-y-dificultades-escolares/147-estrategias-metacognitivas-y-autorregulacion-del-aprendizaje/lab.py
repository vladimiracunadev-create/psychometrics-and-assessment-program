"""Laboratorio 147 - Calibracion de la confianza: sobreconfianza real frente a artefacto estadistico.

Cada estudiante estima su puntaje (0-100) tras una prueba. Su autoestimacion es INSESGADA
respecto de su habilidad real pero tiene ruido, y su puntaje real tambien tiene ruido. Al agrupar
por cuartiles de PUNTAJE OBSERVADO, el cuartil inferior parece "sobreestimar" y el superior
"subestimar" aun sin sesgo alguno (regresion a la media), lo que se suele leer como efecto
Dunning-Kruger. Se compara con una condicion con sobreconfianza real y se calculan:
  - media (autoestimacion - puntaje) por cuartil,
  - el patron cuando se agrupa por HABILIDAD verdadera (no por puntaje observado).
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N = 20000


def main() -> None:
    rng = random.Random(SEMILLA)
    for etiqueta, sesgo in (("sin sesgo real (autoestimacion insesgada)", 0.0), ("con sobreconfianza real (+8 puntos)", 8.0)):
        hab = [rng.gauss(60, 12) for _ in range(N)]
        real = [h + rng.gauss(0, 8) for h in hab]                  # puntaje observado
        auto = [h + sesgo + rng.gauss(0, 8) for h in hab]          # autoestimacion
        orden = sorted(range(N), key=lambda i: real[i])
        print(etiqueta)
        print(f"  {'cuartil (por puntaje observado)':<34} {'auto - real':>12}")
        for q in range(4):
            idx = orden[q * N // 4:(q + 1) * N // 4]
            print(f"  {'Q' + str(q + 1):<34} {statistics.fmean(auto[i] - real[i] for i in idx):12.1f}")
        orden_h = sorted(range(N), key=lambda i: hab[i])
        q1h = orden_h[:N // 4]
        q4h = orden_h[-N // 4:]
        print(f"  agrupando por HABILIDAD verdadera: Q1 {statistics.fmean(auto[i] - hab[i] for i in q1h):+.1f}, "
              f"Q4 {statistics.fmean(auto[i] - hab[i] for i in q4h):+.1f}\n")
    print("Lectura: sin ningun sesgo, el cuartil inferior 'sobreestima' unos +6 puntos y el superior")
    print("'subestima' unos 5 por regresion a la media: lo que se llama efecto Dunning-Kruger puede ser en parte un")
    print("artefacto de agrupar por el puntaje ruidoso. Para evaluar metacognicion se usan medidas de")
    print("calibracion por item y se evita agrupar por el mismo puntaje que se compara.")


if __name__ == "__main__":
    main()
