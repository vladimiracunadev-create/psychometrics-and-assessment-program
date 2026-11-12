"""Laboratorio 151 - Codigo Holland de tres letras con el motor del repositorio.

Usa el instrumento real `onet-riasec-sf` (60 items, escalas R I A S E C) y el motor de
puntuacion. Se simulan 500 personas con intereses de estructura hexagonal y se les aplica el
instrumento DOS veces (respuestas con ruido). Se calcula con `psychometrics.motor`:
  - el codigo de tres letras de cada aplicacion (ordenar_por_media),
  - la coincidencia de la primera letra, del conjunto de tres letras y del codigo exacto.
Los datos son sinteticos; el instrumento tiene licencia especifica con validacion pendiente
(ver DISCLAIMER.md) y NO se usa aqui para decidir sobre personas.
"""
from __future__ import annotations

import math
import pathlib
import random
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import Respuesta, cargar, ordenar_por_media, puntuar  # noqa: E402

SEMILLA = 20260819
N = 500
CODIGOS = "RIASEC"


def responde(inst, afinidad: dict[str, float], ruido: float, rng: random.Random) -> list[Respuesta]:
    out = []
    for it in inst.items:
        base = 3 + 1.3 * afinidad[it.escala]
        v = max(1, min(5, round(base + rng.gauss(0, ruido))))
        out.append(Respuesta(it.id, v if it.clave == 1 else 6 - v))
    return out


def main() -> None:
    inst = cargar("onet-riasec-sf")
    rng = random.Random(SEMILLA)
    primera = conjunto = exacto = 0
    ejemplo = None
    for _ in range(N):
        ang = rng.uniform(0, 2 * math.pi)
        afin = {c: math.cos(ang - k * math.pi / 3) + rng.gauss(0, 0.25) for k, c in enumerate(CODIGOS)}
        cods = []
        for _ in range(2):
            res = puntuar(inst, responde(inst, afin, 1.0, rng))
            cods.append("".join(c for c, _ in ordenar_por_media(res, list(CODIGOS))[:3]))
        primera += cods[0][0] == cods[1][0]
        conjunto += set(cods[0]) == set(cods[1])
        exacto += cods[0] == cods[1]
        ejemplo = ejemplo or cods
    print(f"Instrumento {inst.codigo}: {len(inst.items)} items; licencia: {inst.procedencia.licencia.value}")
    print(f"Personas simuladas: {N}; cada una responde dos veces (ruido de respuesta DE 1.0)")
    print(f"  coincide la PRIMERA letra   : {primera / N:.1%}")
    print(f"  coincide el CONJUNTO de 3   : {conjunto / N:.1%}")
    print(f"  coincide el CODIGO EXACTO   : {exacto / N:.1%}")
    print(f"  ejemplo de dos aplicaciones : {ejemplo}")
    print()
    print("Lectura: el codigo exacto de tres letras es la lectura mas inestable; la primera letra y el")
    print("conjunto de intereses son mas estables. Por eso se presenta el perfil completo y se")
    print("conversa, en lugar de decidir por un codigo. Los intereses orientan la exploracion; no")
    print("determinan capacidades, desempeno ni oportunidades.")


if __name__ == "__main__":
    main()
