"""Laboratorio 196 - Proyecto: estudio de validacion simulado de extremo a extremo.

Se simula un estudio completo y se reporta con el revisor de la clase 180:
  1. diseno y tamano (n = 300),
  2. datos: 10 items sobre un factor, 2 aplicaciones (retest) y un criterio externo,
  3. fiabilidad: alfa e IC bootstrap, test-retest,
  4. validez: correlacion con el criterio (convergente) y con un criterio sin relacion (discriminante),
  5. informe redactado con los hallazgos reales de la simulacion y revisado por la lista de la clase 180.
Datos SINTETICOS: la "verdad" se conoce, de modo que se puede ver si el estudio la recupera.
"""
from __future__ import annotations

import importlib.util
import math
import pathlib
import random
import statistics

RAIZ = pathlib.Path(__file__).resolve().parents[3]
SEMILLA = 20260819
N, K = 300, 10


def cargar_revisor():
    ruta = next((RAIZ / "classes" / "part-17-investigacion-psicometrica-y-analisis-de-datos").glob("180-*/lab.py"))
    spec = importlib.util.spec_from_file_location("lab180", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.revisa


def alfa(m: list[list[float]]) -> float:
    k = len(m[0])
    cols = list(zip(*m, strict=True))
    tot = [sum(f) for f in m]
    return k / (k - 1) * (1 - sum(statistics.pvariance(c) for c in cols) / statistics.pvariance(tot))


def main() -> None:
    rng = random.Random(SEMILLA)
    theta = [rng.gauss(0, 1) for _ in range(N)]
    def aplica():
        return [[0.7 * t + rng.gauss(0, 0.8) for _ in range(K)] for t in theta]
    a1, a2 = aplica(), aplica()
    criterio = [0.45 * t + rng.gauss(0, 0.9) for t in theta]
    ajeno = [rng.gauss(0, 1) for _ in range(N)]
    s1 = [sum(f) for f in a1]
    s2 = [sum(f) for f in a2]
    al = alfa(a1)
    bs = []
    for _ in range(300):
        idx = [rng.randrange(N) for _ in range(N)]
        bs.append(alfa([a1[i] for i in idx]))
    bs.sort()
    ic = (bs[7], bs[292])
    rt = statistics.correlation(s1, s2)
    rc = statistics.correlation(s1, criterio)
    rd = statistics.correlation(s1, ajeno)
    print(f"Fiabilidad: alfa = {al:.2f}, IC 95 % bootstrap [{ic[0]:.2f}, {ic[1]:.2f}]; test-retest r = {rt:.2f} (n = {N})")
    print(f"Validez convergente (criterio relacionado): r = {rc:.2f}; discriminante (variable ajena): r = {rd:.2f}")
    informe = (f"Poblacion: {N} personas sinteticas. Procedimiento: dos aplicaciones de {K} items y un criterio externo. "
              f"Fiabilidad: alfa = {al:.2f}, IC 95 % [{ic[0]:.2f}, {ic[1]:.2f}] (n = {N}); test-retest r = {rt:.2f}. "
              f"Validez: la correlacion con el criterio fue r = {rc:.2f} (n = {N}) y con la variable ajena r = {rd:.2f}. "
              f"El instrumento es valido para describir este constructo en datos simulados como estos, no para decisiones "
              f"sobre personas reales. Limitaciones: datos sinteticos, un solo factor, sin invarianza. "
              f"Uso previsto: ensenanza de la metodologia.")
    revisa = cargar_revisor()
    r = revisa(informe)
    print(f"\nRevision automatica (lista de la clase 180): {sum(r.values())}/{len(r)} criterios")
    for k, v in r.items():
        print(f"   [{'ok' if v else 'FALLA'}] {k}")
    omega = 0.49 * K ** 2 / (0.49 * K ** 2 + 0.64 * K)
    print(f"\nFiabilidad verdadera de la suma de {K} items (omega teorico del modelo simulado): {omega:.2f}")
    print()
    print("Lectura: el estudio recupera la fiabilidad que se simulo y distingue validez convergente de discriminante.")
    print("Que el informe pase la lista solo prueba su forma; la validez en personas reales exige muestras reales,")
    print("equidad entre grupos y replicacion. Este proyecto integra las clases 171-180.")


if __name__ == "__main__":
    main()
