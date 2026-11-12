"""Laboratorio 157 - Alineamiento entre lo que se ensena, lo que se evalua y el perfil de egreso.

Matriz de contenidos para una especialidad tecnico-profesional FICTICIA: 6 competencias del perfil
de egreso con su peso en el perfil (importancia definida por el sector productivo), su peso en el
curriculo (horas de formacion) y su peso en la evaluacion (puntos del examen). Se calculan:
  - la distancia de variacion total entre distribuciones (0 = alineadas, 1 = disjuntas),
  - las competencias sub-representadas (peso evaluativo < 70 % del peso en el perfil),
  - el efecto de redisenar la evaluacion para cerrar las brechas.
Es un modelo de analisis de cobertura; los pesos son inventados.
"""
from __future__ import annotations

COMPETENCIAS = ["seguridad y prevencion", "lectura de planos", "operacion de equipos",
                "diagnostico de fallas", "mantenimiento preventivo", "comunicacion tecnica"]
PERFIL = [0.20, 0.15, 0.20, 0.20, 0.15, 0.10]            # importancia segun el perfil de egreso
CURRICULO = [0.10, 0.25, 0.30, 0.10, 0.15, 0.10]         # horas de formacion
EVALUACION = [0.05, 0.30, 0.40, 0.10, 0.10, 0.05]        # puntos del examen
EVALUACION_REDISENADA = [0.18, 0.15, 0.22, 0.20, 0.15, 0.10]


def tv(p: list[float], q: list[float]) -> float:
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q, strict=True))


def main() -> None:
    print(f"{'competencia':<26} {'perfil':>7} {'curriculo':>10} {'evaluacion':>11} {'eval/perfil':>12}")
    for c, p, cu, e in zip(COMPETENCIAS, PERFIL, CURRICULO, EVALUACION, strict=True):
        marca = "  <- sub-representada" if e < 0.7 * p else ""
        print(f"{c:<26} {p:7.0%} {cu:10.0%} {e:11.0%} {e / p:12.2f}{marca}")
    print(f"\nDistancia de variacion total: perfil-curriculo = {tv(PERFIL, CURRICULO):.2f}; "
          f"perfil-evaluacion = {tv(PERFIL, EVALUACION):.2f}")
    print(f"Con la evaluacion redisenada: perfil-evaluacion = {tv(PERFIL, EVALUACION_REDISENADA):.2f}")
    print()
    print("Lectura: el examen premia lo que se ensena mas (operacion de equipos) y casi no evalua lo que el")
    print("sector considera critico (seguridad, diagnostico). La validez de contenido exige que lo")
    print("evaluado represente el perfil, no la comodidad de evaluar. La orientacion en la educacion")
    print("tecnico-profesional se apoya en informacion actualizada del mercado laboral, verificable y local.")


if __name__ == "__main__":
    main()
