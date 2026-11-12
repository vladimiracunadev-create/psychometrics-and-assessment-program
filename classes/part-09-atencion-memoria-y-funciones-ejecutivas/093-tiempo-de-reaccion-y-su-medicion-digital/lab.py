"""Laboratorio 093 - Medir el tiempo de reaccion en pantalla: ruido de medicion y recortes.

El RT verdadero sigue una ex-Gaussiana (normal + exponencial: cola larga a la derecha). El
dispositivo agrega (1) cuantizacion por tasa de refresco (60 Hz = 16.7 ms) y (2) latencia de
entrada variable. Se compara, en 300 personas con 40 ensayos, la fiabilidad por mitades de
tres resumenes: media, mediana y media recortada (descartar RT < 150 ms y > 1 s), con
dispositivo ideal y con dispositivo ruidoso.
"""
from __future__ import annotations

import random
import statistics

SEMILLA = 20260819
N, ENSAYOS = 300, 40


def ensayo(mu: float, rng: random.Random, ruidoso: bool) -> float:
    rt = rng.gauss(mu, 30) + rng.expovariate(1 / 90)
    if rng.random() < 0.02:
        rt = rng.uniform(40, 120)                     # anticipacion
    if ruidoso:
        rt += rng.uniform(0, 25)                       # latencia de entrada
        rt = round(rt / 16.7) * 16.7                   # cuantizacion por refresco
    return rt


def resumenes(v: list[float]) -> dict[str, float]:
    recort = [x for x in v if 150 <= x <= 1000] or v
    return {"media": statistics.fmean(v), "mediana": statistics.median(v),
            "media recortada": statistics.fmean(recort)}


def main() -> None:
    rng = random.Random(SEMILLA)
    mus = [rng.gauss(300, 40) for _ in range(N)]
    print(f"{'dispositivo':<12} {'resumen':<16} {'fiabilidad (mitades + SB)':>26}")
    print("=" * 58)
    for ruidoso in (False, True):
        mitad = {"media": ([], []), "mediana": ([], []), "media recortada": ([], [])}
        for mu in mus:
            rts = [ensayo(mu, rng, ruidoso) for _ in range(ENSAYOS)]
            a, b = resumenes(rts[0::2]), resumenes(rts[1::2])
            for k in mitad:
                mitad[k][0].append(a[k])
                mitad[k][1].append(b[k])
        for k, (a, b) in mitad.items():
            r = statistics.correlation(a, b)
            print(f"{'ruidoso' if ruidoso else 'ideal':<12} {k:<16} {2 * r / (1 + r):26.3f}")
    print()
    print("Lectura: la cola larga de los RT hace que la media sea inestable; recortar o usar la")
    print("mediana mejora la fiabilidad. El ruido del dispositivo (refresco, latencia) la reduce un")
    print("poco: por eso se calibran los equipos y se registra el dispositivo. Y recortar es una")
    print("decision que se declara de antemano, no despues de ver los datos.")


if __name__ == "__main__":
    main()
