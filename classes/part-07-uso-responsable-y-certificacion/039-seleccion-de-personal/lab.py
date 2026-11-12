"""Laboratorio 039 - Un verificador de procesos de seleccion defendibles.

Cada proceso se describe como un diccionario de decisiones de diseno. El verificador aplica
reglas basadas en las clases 016-020, 059 y 073 y senala los incumplimientos. No es asesoria
juridica ni una auditoria: es una lista de control para pensar el proceso.
"""
from __future__ import annotations

REGLAS = [
    ("hay analisis del puesto", lambda p: p["analisis_de_puesto"]),
    ("cada predictor tiene evidencia de validez para este uso", lambda p: all(p["evidencia_de_validez"].values())),
    ("ninguna prueba sin validar decide por si sola", lambda p: not p["decision_automatica_sin_revision"]),
    ("hay revision humana de los casos cercanos al corte", lambda p: p["revision_humana_cerca_del_corte"]),
    ("se monitorea el impacto adverso", lambda p: p["monitoreo_impacto_adverso"]),
    ("se informo y se pidio consentimiento", lambda p: p["consentimiento"]),
    ("hay vias de acomodacion para quien lo necesite", lambda p: p["acomodaciones"]),
    ("se declara cuanto pesa cada prueba en la decision", lambda p: p["pesos_declarados"]),
]

PROCESOS = {
    "A. Entrevista estructurada + muestra de trabajo": {
        "analisis_de_puesto": True,
        "evidencia_de_validez": {"entrevista estructurada": True, "muestra de trabajo": True},
        "decision_automatica_sin_revision": False, "revision_humana_cerca_del_corte": True,
        "monitoreo_impacto_adverso": True, "consentimiento": True, "acomodaciones": True,
        "pesos_declarados": True},
    "B. Cuestionario propio sin validar como filtro unico": {
        "analisis_de_puesto": False,
        "evidencia_de_validez": {"cuestionario propio": False},
        "decision_automatica_sin_revision": True, "revision_humana_cerca_del_corte": False,
        "monitoreo_impacto_adverso": False, "consentimiento": True, "acomodaciones": False,
        "pesos_declarados": False},
}


def main() -> None:
    for nombre, proceso in PROCESOS.items():
        fallas = [r for r, f in REGLAS if not f(proceso)]
        print(f"{nombre}\n  cumple {len(REGLAS) - len(fallas)} de {len(REGLAS)} reglas")
        for r in fallas:
            print(f"   - FALTA: {r}")
        print()
    print("Lectura: un proceso es defendible por su diseno, no por la sofisticacion de una prueba.")
    print("Un instrumento sin validar para el uso concreto no se usa para seleccionar, ni como")
    print("filtro unico ni como 'apoyo' con peso oculto.")


if __name__ == "__main__":
    main()
