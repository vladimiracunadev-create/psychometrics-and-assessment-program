"""Laboratorio 168 - Un protocolo de derivacion como maquina de estados verificable.

Entradas: nivel de alerta del cribado (0 ninguna, 1 moderada, 2 alta), presencia de un indicador
de riesgo inmediato (bool) y si hay un profesional disponible (bool). Salida: accion obligatoria,
plazo y registro. Se verifica EXHAUSTIVAMENTE (todas las combinaciones) que se cumplen las
invariantes de seguridad del protocolo:
  I1. riesgo inmediato => contacto humano inmediato (no se espera un informe);
  I2. alerta alta o riesgo => nunca se cierra el caso sin revision humana;
  I3. nunca se responde "no hay accion" cuando hay alerta;
  I4. si no hay profesional disponible, se escala (no se descarta).
Es un modelo didactico; el protocolo real lo definen el establecimiento o la organizacion con
profesionales de salud mental y normativa vigente.
"""
from __future__ import annotations

import itertools


def protocolo(alerta: int, riesgo: bool, profesional: bool) -> dict[str, str]:
    if riesgo:
        accion = "contacto humano inmediato y acompanamiento" if profesional else "escalar de inmediato a la jefatura de turno"
        return {"accion": accion, "plazo": "inmediato", "registro": "obligatorio", "cierre": "no"}
    if alerta == 2:
        accion = "derivar a profesional y contactar a la familia" if profesional else "escalar y agendar derivacion"
        return {"accion": accion, "plazo": "24 h", "registro": "obligatorio", "cierre": "no"}
    if alerta == 1:
        return {"accion": "entrevista de seguimiento y reevaluacion", "plazo": "7 dias", "registro": "obligatorio", "cierre": "con revision"}
    return {"accion": "sin accion especifica; mantener monitoreo universal", "plazo": "-", "registro": "agregado", "cierre": "si"}


def main() -> None:
    violaciones = []
    casos = 0
    for alerta, riesgo, prof in itertools.product((0, 1, 2), (False, True), (False, True)):
        casos += 1
        r = protocolo(alerta, riesgo, prof)
        if riesgo and r["plazo"] != "inmediato":
            violaciones.append(("I1", alerta, riesgo, prof))
        if (alerta == 2 or riesgo) and r["cierre"] != "no":
            violaciones.append(("I2", alerta, riesgo, prof))
        if (alerta > 0 or riesgo) and r["accion"].startswith("sin accion"):
            violaciones.append(("I3", alerta, riesgo, prof))
        if (riesgo or alerta == 2) and not prof and "escal" not in r["accion"]:
            violaciones.append(("I4", alerta, riesgo, prof))
    print(f"Combinaciones verificadas: {casos}; violaciones de invariantes: {len(violaciones)} (debe ser 0)")
    print(f"\n{'alerta':>6} {'riesgo':>7} {'prof.':>6}  accion | plazo")
    for alerta, riesgo, prof in itertools.product((2, 0), (True, False), (True, False)):
        r = protocolo(alerta, riesgo, prof)
        print(f"{alerta:6d} {str(riesgo):>7} {str(prof):>6}  {r['accion']} | {r['plazo']}")
    print()
    print("Lectura: las reglas de seguridad se prueban de forma exhaustiva, no se confia en revisarlas a ojo.")
    print("Un protocolo define quien actua, en que plazo y que queda registrado; la tecnologia no reemplaza al")
    print("equipo humano. Los canales de ayuda y los plazos reales se verifican en la fuente oficial vigente.")


if __name__ == "__main__":
    main()
