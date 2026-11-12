"""Laboratorio 192 - Proyecto: bateria laboral con ajuste justificado, sin porcentajes inventados.

Dado un perfil de cargo (requisitos) se arma una bateria con los instrumentos y escalas del catalogo
REAL del repositorio. Regla de ajuste: cada instrumento incluido debe justificarse por al menos un
requisito, y cada requisito sin cobertura se declara como BRECHA (no se rellena con otro test). El
informe no calcula "porcentaje de ajuste": un numero asi exigiria normas y evidencia de validez
predictiva que este repositorio no tiene. Ejemplo ficticio: "Coordinador/a de proyectos".
"""
from __future__ import annotations

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "src"))

from psychometrics.motor import catalogo  # noqa: E402

# requisito -> (instrumento, escala) que podria aportar INFORMACION descriptiva sobre el.
# La relacion es un supuesto de diseno que debe respaldar un analisis de puesto, no una prueba.
REQUISITOS = {
    "organizacion y cumplimiento de plazos": ("ipip-neo-120", "C"),
    "orientacion a personas y colaboracion": ("ipip-neo-120", "A"),
    "estabilidad bajo presion": ("ipip-neo-120", "N"),
    "intereses vocacionales hacia la gestion": ("onet-riasec-sf", "E"),
    "comprension de instrucciones escritas": None,
    "razonamiento numerico": None,
    "dominio de herramientas de planificacion": None,
}


def main() -> None:
    cat = {i.codigo: {e.codigo for e in i.escalas} for i in catalogo()}
    print(f"{'requisito del cargo':<46} {'cobertura':<30} estado")
    print("=" * 96)
    usados: dict[str, list[str]] = {}
    brechas = []
    for req, ref in REQUISITOS.items():
        if ref and ref[0] in cat and ref[1] in cat[ref[0]]:
            usados.setdefault(ref[0], []).append(req)
            print(f"{req:<46} {ref[0] + ' / ' + ref[1]:<30} cubierto (descriptivo)")
        else:
            brechas.append(req)
            print(f"{req:<46} {'-':<30} BRECHA")
    print(f"\nInstrumentos justificados: {', '.join(f'{k} ({len(v)} requisitos)' for k, v in usados.items())}")
    print(f"Brechas declaradas ({len(brechas)}): {brechas}")
    print()
    print("Lectura: la bateria no cubre habilidades cognitivas ni conocimientos tecnicos; esos requisitos se")
    print("evaluan con pruebas de aptitud y con muestras de trabajo cuya validez se documente (fichas CIE, AMP, etc.,")
    print("todas 'no verificadas'). Los rasgos de personalidad describen preferencias, no desempeno futuro, y no")
    print("deben ser el unico criterio de decision. El informe entrega evidencia descriptiva y brechas, no un puntaje de ajuste.")


if __name__ == "__main__":
    main()
