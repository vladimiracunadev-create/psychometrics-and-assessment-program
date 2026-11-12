"""Laboratorio 180 - Revisor automatico de un informe de validacion (lista de control).

Analiza el texto de un informe y comprueba, con reglas simples y transparentes:
  1. secciones minimas presentes (poblacion, procedimiento, fiabilidad, validez, limitaciones, uso);
  2. toda afirmacion de "valido/validado" viene acompanada de poblacion y proposito;
  3. cada coeficiente informado (alfa, r, omega) tiene tamano de muestra o intervalo;
  4. no hay lenguaje absoluto ("demuestra", "garantiza", "probado") sin cualificar.
Aplica la lista a dos informes de ejemplo. Es una ayuda para revisar, no un juicio de calidad: no
evalua si los analisis son correctos.
"""
from __future__ import annotations

import re

SECCIONES = ["poblacion", "procedimiento", "fiabilidad", "validez", "limitaciones", "uso previsto"]
ABSOLUTOS = ["demuestra", "garantiza", "esta probado", "100 %", "siempre", "sin duda"]

BUENO = """
Poblacion: 312 estudiantes de 8.o basico de dos colegios urbanos. Procedimiento: aplicacion
colectiva de 25 minutos. Fiabilidad: alfa = 0.82, IC 95 % [0.79, 0.85] (n = 312). Validez:
la correlacion con la nota de lenguaje fue r = 0.41, IC 95 % [0.31, 0.50]. El instrumento es
valido para describir comprension lectora en estudiantes como estos, no para decisiones de
admision. Limitaciones: muestra no probabilistica, un solo curso. Uso previsto: apoyo docente.
"""

MALO = """
El test fue validado y demuestra que mide inteligencia. Su alfa es 0.91 y la correlacion con
rendimiento es r = 0.55, lo que garantiza su uso en seleccion. Es un instrumento probado.
"""


def revisa(texto: str) -> dict[str, bool]:
    t = texto.lower()
    t_sin = t.replace("poblacion:", "poblacion ")
    secciones_ok = all(s in t_sin for s in SECCIONES)
    afirma_valido = bool(re.search(r"\bvalid[oa]\b|validad[oa]", t))
    valido_cualificado = (not afirma_valido) or ("poblacion" in t and ("para " in t or "proposito" in t) and "no para" in t)
    coefs = re.findall(r"(alfa|omega|\br\b)\s*=\s*[0-9.]+", t)
    con_respaldo = bool(re.search(r"ic 95|n = \d+", t)) or not coefs
    sin_absolutos = not any(a in t for a in ABSOLUTOS)
    return {"secciones minimas": secciones_ok, "'valido' cualificado (poblacion, uso)": valido_cualificado,
            "coeficientes con n o intervalo": con_respaldo, "sin lenguaje absoluto": sin_absolutos}


def main() -> None:
    for nombre, texto in (("Informe A", BUENO), ("Informe B", MALO)):
        r = revisa(texto)
        print(f"{nombre}: {sum(r.values())}/{len(r)} criterios")
        for k, v in r.items():
            print(f"   [{'ok' if v else 'FALLA'}] {k}")
    print()
    print("Lectura: el informe B afirma validez sin poblacion ni proposito, da coeficientes sin n ni intervalo y")
    print("usa lenguaje absoluto. Un informe de validacion cualifica cada afirmacion (para quien, para que)")
    print("y declara limitaciones. La revision automatica detecta la forma; la revision por pares evalua el fondo.")


if __name__ == "__main__":
    main()
