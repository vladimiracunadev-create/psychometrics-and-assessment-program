"""Laboratorio 187 - Auditoria de calculo: una segunda implementacion independiente.

Para los cinco instrumentos del catalogo se generan 200 protocolos aleatorios y se puntua con (a)
el motor y (b) una reimplementacion INDEPENDIENTE escrita aqui desde la definicion (reflejar,
promediar por escala, agregar los items de las escalas hijas). Se verifica coincidencia exacta. Ademas
se construye un registro de auditoria por calculo: huella de las respuestas, version del
instrumento y huella del resultado. Es "differential testing": si una de las dos implementaciones
tiene un error, no coinciden.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import random
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import Respuesta, catalogo, puntuar  # noqa: E402

SEMILLA = 20260819
PROTOCOLOS = 200


def independiente(ins, valores: dict[str, int]) -> dict[str, float]:
    lo = min(o.valor for o in ins.opciones)
    hi = max(o.valor for o in ins.opciones)
    efectivo = {i.id: (valores[i.id] if i.clave == 1 else lo + hi - valores[i.id]) for i in ins.items}

    def hojas(cod: str) -> list[str]:
        hijas = [e.codigo for e in ins.escalas if e.padre == cod]
        return [cod] if not hijas else [h for x in hijas for h in hojas(x)]

    out = {}
    for e in ins.escalas:
        ids = [i.id for i in ins.items if i.escala in hojas(e.codigo)]
        out[e.codigo] = round(sum(efectivo[i] for i in ids) / len(ids), 4)
    return out


def huella(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:12]


def main() -> None:
    rng = random.Random(SEMILLA)
    print(f"{'instrumento':<20} {'protocolos':>11} {'coinciden':>10}  ejemplo de registro de auditoria")
    print("=" * 100)
    for ins in catalogo():
        ok = 0
        reg = None
        for _ in range(PROTOCOLOS):
            vals = {i.id: rng.choice([o.valor for o in ins.opciones]) for i in ins.items}
            motor = puntuar(ins, [Respuesta(k, v) for k, v in vals.items()])
            indep = independiente(ins, vals)
            coincide = all(abs(motor[c].media_item - indep[c]) < 1e-9 for c in indep)
            ok += coincide
            if reg is None:
                reg = {"instrumento": ins.codigo, "version": ins.version, "entrada": huella(vals),
                       "salida": huella({k: p.media_item for k, p in motor.puntajes.items()})}
        print(f"{ins.codigo:<20} {PROTOCOLOS:11d} {ok:10d}  {reg}")
    print()
    print("Lectura: cuando dos implementaciones independientes coinciden en miles de casos, es muy poco")
    print("probable que compartan un error. El registro (version, huella de entrada y de salida) permite")
    print("reproducir y auditar cualquier puntaje, sin guardar las respuestas en claro en el registro.")


if __name__ == "__main__":
    main()
