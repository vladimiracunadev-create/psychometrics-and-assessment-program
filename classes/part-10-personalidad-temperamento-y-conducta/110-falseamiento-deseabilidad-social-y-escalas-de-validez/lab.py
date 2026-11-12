"""Laboratorio 110 - Escala de validez: deteccion de falseamiento y sus falsos positivos.

Una escala de 5 items de "virtudes improbables" ("nunca he dicho una mentira") se usa para
detectar falseamiento. Honestos: puntaje bajo (p. ej. 1.0 +/- 1.0 de 5), pero los muy
responsables/integros pueden puntuar algo mas alto. Falseadores: 2.5 +/- 1.2. Se calcula, para
distintos puntos de corte:
  - sensibilidad (falseadores marcados), especificidad (honestos no marcados),
  - valor predictivo positivo con prevalencia de falseamiento 20 %,
  - AUC (probabilidad de que un falseador puntue mas que un honesto).
Y cuantos HONESTOS de alta responsabilidad serian marcados injustamente.
"""
from __future__ import annotations

import random

SEMILLA = 20260819
N = 20000
PREV = 0.20


def main() -> None:
    rng = random.Random(SEMILLA)
    honestos, falseadores, hon_altos = [], [], []
    for _ in range(N):
        if rng.random() < PREV:
            falseadores.append(max(0.0, min(5.0, rng.gauss(2.5, 1.2))))
        else:
            resp = rng.gauss(0, 1)
            honestos.append(max(0.0, min(5.0, rng.gauss(1.0 + 0.3 * resp, 1.0))))
            if resp > 1.0:
                hon_altos.append(honestos[-1])
    print(f"{'corte (>=)':>10} {'sensibilidad':>13} {'especificidad':>14} {'VPP (prev. 20%)':>16} "
          f"{'honestos de alta resp. marcados':>33}")
    print("=" * 92)
    for corte in (1.5, 2.0, 2.5, 3.0, 3.5):
        sens = sum(x >= corte for x in falseadores) / len(falseadores)
        esp = sum(x < corte for x in honestos) / len(honestos)
        vpp = sens * PREV / (sens * PREV + (1 - esp) * (1 - PREV))
        marc = sum(x >= corte for x in hon_altos) / len(hon_altos)
        print(f"{corte:10.1f} {sens:13.2f} {esp:14.2f} {vpp:16.2f} {marc:33.2f}")
    muestra = 3000
    auc = sum(f > h for f, h in zip(rng.choices(falseadores, k=muestra), rng.choices(honestos, k=muestra), strict=True)) / muestra
    print(f"\nAUC aproximado = {auc:.2f}")
    print()
    print("Lectura: ningun corte detecta bien y a la vez evita falsos positivos; con prevalencia de 20 %")
    print("muchos 'marcados' son honestos, entre ellos personas de alta responsabilidad. Una escala de")
    print("validez es una ALERTA para examinar el protocolo, no una sentencia: por si sola no se")
    print("descarta ni se juzga a una persona (clases 040 y 100).")


if __name__ == "__main__":
    main()
