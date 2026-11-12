# 047 — Ajuste en modelos de ecuaciones estructurales

> [Índice de la parte](../README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clase 043.

## Objetivos

1. Calcular RMSEA, CFI y TLI a partir de chi-cuadrado y grados de libertad.
2. Explicar por qué el chi-cuadrado depende del tamaño muestral.
3. Evitar la aplicación mecánica de umbrales.

## Fundamentos

```
χ² = (N − 1)·F_min        RMSEA = √( max(χ² − gl, 0) / (gl·(N − 1)) )
CFI = 1 − max(χ²ₘ − glₘ, 0) / max(χ²₀ − gl₀, χ²ₘ − glₘ, 0)
TLI = ( χ²₀/gl₀ − χ²ₘ/glₘ ) / ( χ²₀/gl₀ − 1 )
```

Hu y Bentler (1999) sugirieron combinaciones (RMSEA ≲ 0,06; CFI ≳ 0,95; SRMR ≲ 0,08), pero Marsh, Hau y Wen (2004) advirtieron contra tratarlas como reglas de oro.

Laboratorio: aritmética exacta con F_min fijo en 0,06, gl = 40 (valores ilustrativos, no de un estudio):

| N | χ² | p | RMSEA | CFI |
|---:|---:|---:|---:|---:|
| 200 | 11,9 | 1,000 | 0,000 | 1,000 |
| 1 000 | 59,9 | 0,022 | 0,022 | 0,993 |
| 5 000 | 299,9 | 0,000 | 0,036 | 0,983 |
| 20 000 | 1 199,9 | 0,000 | 0,038 | 0,981 |

Con el mismo desajuste, el chi-cuadrado rechaza el modelo en cuanto N es grande; RMSEA y CFI se estabilizan. (TLI puede superar 1.)

## Ejemplo resuelto

χ² = 100, gl = 40, N = 500: RMSEA = √(60 / (40·499)) = √0,003 = 0,055.

## Errores y límites

- Rechazar un modelo solo por χ² significativo con N grande.
- Aceptar un modelo solo por índices «buenos» sin revisar residuos.
- Comparar índices entre modelos no anidados sin criterios adecuados.
- Ajustar bien no implica que el modelo sea el correcto.

## Ejercicios

- **Inicial.** ¿Qué pasa con χ² si se duplica N con el mismo F_min? → se duplica aproximadamente.
- **Intermedio.** χ² = 50, gl = 50 → RMSEA = 0.
- **Avanzado.** Cambia F_MIN a 0,15 en `lab.py` y describe cuándo RMSEA supera 0,06.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/047-ajuste-en-modelos-de-ecuaciones-estructurales/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se reportan varios índices? 2. ¿Qué indica χ² < gl? 3. ¿Qué miras antes de aceptar un modelo?
Se logra si el estudiante calcula los índices y discute el desajuste concreto.

## Bibliografía

- Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis. *Structural Equation Modeling*, 6(1), 1-55. ✅ [DOI](https://doi.org/10.1080/10705519909540118)
- Marsh, H. W., Hau, K.-T., & Wen, Z. (2004). In search of golden rules. *Structural Equation Modeling*, 11(3), 320-341. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Kline, R. B. (2016). *Principles and Practice of Structural Equation Modeling* (4.ª ed.). Guilford. ⚠️ existe, pero Crossref registra 2012 (¿otra edición?; [DOI](https://doi.org/10.1080/10705511.2012.687667))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
