"""Laboratorio 062 - Indices de ajuste: por que el chi-cuadrado depende de N.

Aritmetica exacta sobre las formulas, sin motor de estimacion:
    chi2 = (N - 1) * F_min         RMSEA = sqrt( max(chi2 - gl, 0) / (gl * (N - 1)) )
    CFI  = 1 - max(chi2_m - gl_m, 0) / max(chi2_0 - gl_0, chi2_m - gl_m, 0)
    TLI  = ((chi2_0/gl_0) - (chi2_m/gl_m)) / ((chi2_0/gl_0) - 1)
Se fija un desajuste pequeno del modelo (F_min constante) y se varia el tamano de muestra.
Los valores de F_min y del modelo nulo son ilustrativos, no de un estudio real.
Umbrales usados en la literatura (Hu y Bentler, 1999; RMSEA < .06, CFI > .95) son guias.
"""
from __future__ import annotations

import math

GL_M, GL_0 = 40, 55
F_MIN = 0.06              # desajuste fijo del modelo
F_NULO = 3.00             # el modelo de independencia ajusta muy mal (hay estructura real)


def chi2_p(chi2: float, gl: int) -> float:
    """Cola superior de chi-cuadrado por aproximacion de Wilson-Hilferty (normal)."""
    z = ((chi2 / gl) ** (1 / 3) - (1 - 2 / (9 * gl))) / math.sqrt(2 / (9 * gl))
    return 0.5 * math.erfc(z / math.sqrt(2))


def main() -> None:
    print(f"F_min del modelo = {F_MIN} (constante) | gl = {GL_M}")
    print(f"{'N':>7} {'chi2':>8} {'p':>8} {'RMSEA':>7} {'CFI':>6} {'TLI':>6}")
    print("=" * 48)
    for n in (100, 200, 500, 1000, 5000, 20000):
        chi_m, chi_0 = (n - 1) * F_MIN, (n - 1) * F_NULO
        rmsea = math.sqrt(max(chi_m - GL_M, 0) / (GL_M * (n - 1)))
        d_m, d_0 = max(chi_m - GL_M, 0), max(chi_0 - GL_0, 0)
        cfi = 1 - d_m / max(d_0, d_m, 1e-12)
        tli = ((chi_0 / GL_0) - (chi_m / GL_M)) / ((chi_0 / GL_0) - 1)
        print(f"{n:7d} {chi_m:8.1f} {chi2_p(chi_m, GL_M):8.4f} {rmsea:7.3f} {cfi:6.3f} {tli:6.3f}")
    print()
    print("Lectura: con el MISMO desajuste, el chi-cuadrado rechaza el modelo en cuanto N es")
    print("grande (p -> 0), mientras RMSEA, CFI y TLI se estabilizan. Por eso se reportan")
    print("varios indices y se discute el desajuste concreto (residuos, indices de modificacion)")
    print("en lugar de aplicar un umbral mecanico. Y un buen ajuste no prueba que el modelo")
    print("sea el correcto: modelos distintos pueden ajustar igual de bien.")


if __name__ == "__main__":
    main()
