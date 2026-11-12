"""Laboratorio 077 - Registro de consentimiento con retiro efectivo.

Modelo minimo: cada consentimiento tiene version del texto, finalidades autorizadas, fecha y
posible retiro. Un analisis solo puede usar los registros cuyo consentimiento este vigente y
cubra la finalidad. Se demuestra que (1) retirar el consentimiento excluye los datos de
los analisis posteriores, (2) una finalidad no autorizada bloquea el uso y (3) cada decision
queda en un registro de auditoria con huella (SHA-256) para detectar alteraciones.
Datos 100 % sinteticos.
"""
from __future__ import annotations

import dataclasses
import hashlib
import json


@dataclasses.dataclass
class Consentimiento:
    sujeto: str
    version_texto: str
    finalidades: frozenset[str]
    retirado: bool = False


def puede_usar(c: Consentimiento, finalidad: str) -> bool:
    return (not c.retirado) and finalidad in c.finalidades


def huella(registro: list[dict]) -> str:
    return hashlib.sha256(json.dumps(registro, sort_keys=True).encode()).hexdigest()[:16]


def main() -> None:
    cons = {
        "s001": Consentimiento("s001", "v2", frozenset({"evaluacion", "investigacion"})),
        "s002": Consentimiento("s002", "v2", frozenset({"evaluacion"})),
        "s003": Consentimiento("s003", "v1", frozenset({"evaluacion", "investigacion"})),
    }
    cons["s003"].retirado = True
    auditoria: list[dict] = []
    for finalidad in ("evaluacion", "investigacion"):
        usables = []
        for s, c in cons.items():
            ok = puede_usar(c, finalidad)
            auditoria.append({"sujeto": s, "finalidad": finalidad, "autorizado": ok})
            if ok:
                usables.append(s)
        print(f"Analisis con finalidad '{finalidad}': se usan {usables}")
    print(f"\nHuella del registro de auditoria: {huella(auditoria)}")
    auditoria[0]["autorizado"] = False
    print(f"Huella tras alterar un registro:     {huella(auditoria)}  (distinta => se detecta la alteracion)")
    print()
    print("Lectura: el consentimiento es especifico (finalidad) y revocable; la confidencialidad exige")
    print("que el sistema lo haga cumplir, no solo que exista un formulario. La huella permite")
    print("detectar cambios, no impide que ocurran: el control de acceso es otra capa (clase 080).")


if __name__ == "__main__":
    main()
