# 176 — Estimación de incertidumbre y bootstrap

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 022 y 173.

## Objetivos

1. Construir un intervalo bootstrap percentil para un coeficiente.
2. Compararlo con un intervalo analítico.
3. Informar la incertidumbre junto con la estimación puntual.

## Fundamentos

El **bootstrap** (Efron y Tibshirani, 1993) remuestrea con reemplazo los casos observados, recalcula el estadístico y usa los percentiles 2,5 y 97,5 como intervalo. No exige fórmula y sirve para coeficientes sin distribución sencilla. El alfa tiene intervalos analíticos (Feldt, 1965; van Zyl et al., 2000).

Laboratorio (6 ítems, cargas 0,6; alfa poblacional 0,771; 40 réplicas × 100 remuestreos; cobertura ruidosa):

| n | Cobertura bootstrap | Cobertura analítica | Ancho medio del intervalo |
|---:|---:|---:|---:|
| 40 | 90 % | 98 % | 0,258 |
| 80 | 95 % | 98 % | 0,170 |
| 200 | 90 % | 90 % | 0,100 |

Con 40 réplicas la cobertura tiene un error de ±7 %; para afirmar que cubre 95 % se simulan miles. El ancho informa: con n = 40 el alfa de 0,77 admite valores de ~0,65 a ~0,90.

## Ejemplo resuelto

De 100 remuestreos ordenados, el intervalo 95 % usa los valores en las posiciones 3 y 98.

## Errores y límites

- Usar pocos remuestreos (< 1 000 en análisis reales).
- Aplicar bootstrap con muestras muy pequeñas o muy dependientes (grupos).
- Reportar solo el estimador puntual.
- Los resultados del laboratorio son ruidosos por diseño (ejecución rápida).

## Ejercicios

- **Inicial.** ¿Qué es un remuestreo con reemplazo?
- **Intermedio.** ¿Cuánto se reduce el ancho al cuadruplicar n? A la mitad.
- **Avanzado.** Aumenta REPS y BOOT en `lab.py` y estabiliza la cobertura.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/176-estimacion-de-incertidumbre-y-bootstrap/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo falla el bootstrap? 2. ¿Cómo informarías un alfa con su intervalo? 3. ¿Cómo manejas datos agrupados (por curso)?
Se logra si el estudiante construye e interpreta un intervalo y declara su método.

## Bibliografía

- Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall. ✅ [DOI](https://doi.org/10.1007/978-1-4899-4541-9)
- Feldt, L. S. (1965). The approximate sampling distribution of Kuder-Richardson reliability coefficient twenty. *Psychometrika*, 30(3), 357-370. ✅ [DOI](https://doi.org/10.1007/bf02289499)
- van Zyl, J. M., Neudecker, H., & Nel, D. G. (2000). On the distribution of the maximum likelihood estimator of Cronbach's alpha. *Psychometrika*, 65(3), 271-280. ✅ [DOI](https://doi.org/10.1007/bf02296146)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
