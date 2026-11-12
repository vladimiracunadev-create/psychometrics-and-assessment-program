# 179 — Metaanálisis psicométrico

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 039 y 176.

## Objetivos

1. Agrupar coeficientes alfa con efectos aleatorios.
2. Interpretar heterogeneidad (τ², I²).
3. Informar un intervalo de predicción.

## Fundamentos

La **generalización de la fiabilidad** (Vacha-Haase, 1998) estudia cómo varía la fiabilidad entre muestras. Se transforma el alfa con ln(1 − α) (Bonett, 2010), se agrupa con el modelo de efectos aleatorios de DerSimonian y Laird (1986) y se informa el intervalo de **predicción** para un estudio nuevo (IntHout et al., 2016), que es más ancho que el intervalo del promedio.

Laboratorio (25 estudios, 10 ítems; alfa verdadero ~ N(0,80; 0,05); sintético):

| Medida | Valor |
|---|---:|
| Alfa observado: media simple (rango) | 0,796 (0,67–0,90) |
| Alfa agrupado (efectos aleatorios), IC 95 % | 0,803 [0,779; 0,824] |
| τ² / I² | 0,0700 / 86 % |
| Intervalo de predicción | [0,665; 0,884] |

## Ejemplo resuelto

Un estudio nuevo puede dar un alfa tan bajo como 0,67 o tan alto como 0,88 aunque el alfa agrupado sea 0,80: el IC del promedio (0,78–0,82) no describe al estudio siguiente.

## Errores y límites

- Informar «el alfa de la escala es 0,80» sin muestra.
- Ignorar el sesgo de publicación.
- Agrupar estudios con escalas o formatos distintos.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué mide I²?
- **Intermedio.** ¿Por qué el intervalo de predicción es más ancho? Incluye la heterogeneidad (τ²).
- **Avanzado.** Reduce la DE entre estudios a 0,02 y observa I².

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/179-metaanalisis-psicometrico/lab.py
```

## Autoevaluación y criterios

1. ¿Qué moderadores explicarían la variación? 2. ¿Cómo buscarías estudios? 3. ¿Cómo registrarías el protocolo?
Se logra si el estudiante agrupa fiabilidades e informa heterogeneidad y predicción.

## Bibliografía

- DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials*, 7(3), 177-188. ✅ [DOI](https://doi.org/10.1016/0197-2456(86)90046-2)
- Bonett, D. G. (2010). Varying coefficient meta-analytic methods for alpha reliability. *Psychological Methods*, 15(4), 368-385. ✅ [DOI](https://doi.org/10.1037/a0020142)
- Vacha-Haase, T. (1998). Reliability generalization. *Educational and Psychological Measurement*, 58(1), 6-20. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open*, 6, e010247. ✅ [DOI](https://doi.org/10.1136/bmjopen-2015-010247)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
