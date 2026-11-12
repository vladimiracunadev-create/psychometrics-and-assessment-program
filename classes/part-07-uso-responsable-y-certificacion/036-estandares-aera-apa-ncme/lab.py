"""Laboratorio 036 - Auditoria de documentacion al estilo de los Standards.

Revisa cada instrumento de instruments/ contra una lista de verificacion de documentacion
inspirada en los Standards (AERA/APA/NCME, 2014): autores, anio, fuente, licencia, cita,
declaracion de estado de validacion, tipo de respuesta, duracion, y existencia de notas de
limitaciones. NO evalua la calidad psicometrica: evalua que el instrumento DECLARE lo que un
usuario necesita saber para no usarlo mal. La lista es una herramienta didactica propia, no una
transcripcion de los Standards.
"""
from __future__ import annotations

import pathlib

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[3]


def revisa(d: dict) -> dict[str, bool]:
    p = d.get("procedencia", {})
    notas = " ".join(str(v) for v in (p.get("notas") or {}).values()).lower()
    texto = yaml.safe_dump(d, allow_unicode=True).lower()
    return {
        "autores": bool(p.get("autores")),
        "anio": bool(p.get("anio")),
        "fuente": bool(p.get("fuente")),
        "licencia": bool(p.get("licencia")),
        "cita": bool(p.get("cita")),
        "tipo de respuesta": bool(d.get("tipo_respuesta")),
        "duracion": bool(d.get("duracion_min")),
        "estado de validacion declarado": ("sin validar" in texto or "validaci" in notas
                                          or "validaci" in texto),
    }


def main() -> None:
    archivos = sorted((RAIZ / "instruments").glob("*.yaml"))
    criterios = list(revisa(yaml.safe_load(archivos[0].read_text(encoding="utf-8"))))
    print(f"{'instrumento':<20}" + "".join(f"{c[:10]:>11}" for c in criterios) + f"{'total':>7}")
    print("=" * (20 + 11 * len(criterios) + 7))
    for a in archivos:
        r = revisa(yaml.safe_load(a.read_text(encoding="utf-8")))
        print(f"{a.stem:<20}" + "".join(f"{'si' if v else 'NO':>11}" for v in r.values())
              + f"{sum(r.values()):>5}/{len(r)}")
    print()
    print("Lectura: una documentacion completa no demuestra calidad, pero una documentacion")
    print("incompleta impide juzgarla. Los Standards piden que el desarrollador entregue la evidencia")
    print("necesaria para interpretar y usar los puntajes; el usuario es responsable de que el uso")
    print("concreto este respaldado (AERA/APA/NCME, 2014).")


if __name__ == "__main__":
    main()
