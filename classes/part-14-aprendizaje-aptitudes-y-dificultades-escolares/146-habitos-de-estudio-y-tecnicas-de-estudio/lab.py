"""Laboratorio 146 - Practica distribuida frente a masiva: un modelo de olvido.

Modelo exponencial del olvido (Ebbinghaus): el recuerdo R = exp(-t / S), donde la "fuerza" S
crece con cada sesion de estudio, pero MAS si el estudio ocurre despues de haber olvidado algo
(esfuerzo de recuperacion). Se compara, para 4 sesiones de 30 minutos y una prueba a los 14 dias:
  - MASIVO: las 4 sesiones el dia anterior a la prueba... y el mismo dia,
  - DISTRIBUIDO: una sesion cada 3 dias.
El modelo es una ilustracion cualitativa de un efecto bien documentado (Cepeda et al., 2006;
Dunlosky et al., 2013); los numeros dependen de los parametros supuestos.
"""
from __future__ import annotations

import math


def recuerdo_final(dias_estudio: list[float], dia_prueba: float) -> float:
    s = 1.5                                         # fuerza inicial (dias)
    ultimo = dias_estudio[0]
    for d in dias_estudio[1:]:
        r = math.exp(-(d - ultimo) / s)             # recuerdo justo antes de repasar
        s += 1.5 + 4.0 * (1 - r)                    # mas ganancia si habia olvidado algo
        ultimo = d
    return math.exp(-(dia_prueba - ultimo) / s)


def main() -> None:
    prueba = 14.0
    planes = {
        "masivo (4 sesiones el dia 13)": [13.0, 13.1, 13.2, 13.3],
        "masivo (4 sesiones el dia 0)": [0.0, 0.1, 0.2, 0.3],
        "distribuido (dias 0, 3, 6, 9)": [0.0, 3.0, 6.0, 9.0],
        "distribuido tardio (dias 4, 7, 10, 13)": [4.0, 7.0, 10.0, 13.0],
    }
    print(f"{'plan (4 sesiones)':<44} {'prueba dia 14':>14} {'retencion dia 28':>17}")
    print("=" * 77)
    for nombre, dias in planes.items():
        print(f"{nombre:<44} {recuerdo_final(dias, prueba):14.2f} {recuerdo_final(dias, prueba + 14):17.2f}")
    print()
    print("Lectura: para una prueba inmediata, estudiar pegado a la prueba rinde bien; la ventaja del")
    print("espaciado aparece en la RETENCION duradera (dia 28), donde el estudio masivo se pierde. El")
    print("efecto de espaciado esta bien respaldado en la literatura; las cifras de este modelo son")
    print("ilustrativas y no se interpretan como predicciones.")
    print("Un inventario de 'habitos de estudio' autoinformado no mide cuanto ni como se estudia: se")
    print("complementa con registros de conducta y con orientacion basada en evidencia.")


if __name__ == "__main__":
    main()
