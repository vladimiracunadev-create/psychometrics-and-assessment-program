# 116 — Personalidad de vendedores y evaluación comercial

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 019, 101 y 114.

## Objetivos

1. Reconocer relaciones no lineales entre rasgos y desempeño.
2. Evaluar la calidad del criterio «ventas».
3. Evitar perfiles genéricos de «vendedor ideal».

## Fundamentos

Los metaanálisis encuentran relaciones modestas entre rasgos como extraversión y responsabilidad y el desempeño de vendedores (Barrick y Mount, 1991; Vinchur et al., 1998). Hay evidencia de que algunas relaciones son **curvilíneas** (Le et al., 2011). El criterio «ventas» está contaminado por factores ajenos al vendedor (territorio, cartera, ciclo del producto).

Laboratorio (el efecto del rasgo se aplana sobre 0,5 DE; el criterio suma un componente de territorio):

| Peso del territorio | R² lineal | R² cuadrático |
|---:|---:|---:|
| 0,0 | 0,255 | 0,285 |
| 0,5 | 0,237 | 0,269 |
| 1,0 | 0,187 | 0,215 |
| 2,0 | 0,094 | 0,106 |

El modelo cuadrático explica más cuando hay curvatura; ambos pierden poder a medida que el criterio incluye más territorio.

## Ejemplo resuelto

Con peso del territorio 2,0, solo ~9 % de la varianza se explica aun con el modelo correcto: la validez observada refleja la calidad del criterio tanto como la del predictor.

## Errores y límites

- Perfil de «vendedor ideal» basado en un solo estudio o en los vendedores actuales (circularidad).
- Ventas brutas como criterio sin ajustar por territorio.
- Asumir linealidad sin examinarla.
- Los parámetros son supuestos del laboratorio.

## Ejercicios

- **Inicial.** ¿Qué es una relación curvilínea?
- **Intermedio.** Propón un criterio alternativo a «ventas totales».
- **Avanzado.** Ajusta un modelo con tope (min) en `lab.py` y compáralo con el cuadrático.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/116-personalidad-de-vendedores-y-evaluacion-comercial/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo depurarías el criterio? 2. ¿Qué dice la literatura sobre validez de personalidad y ventas (a verificar en las fuentes)? 3. ¿Qué alternativas a un test de personalidad existen?
Se logra si el estudiante examina linealidad y calidad del criterio.

## Bibliografía

- Barrick, M. R., & Mount, M. K. (1991). The Big Five personality dimensions and job performance: A meta-analysis. *Personnel Psychology*, 44(1), 1-26. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.1991.tb00688.x)
- Vinchur, A. J., Schippmann, J. S., Switzer, F. S., & Roth, P. L. (1998). A meta-analytic review of predictors of job performance for salespeople. *Journal of Applied Psychology*, 83(4), 586-597. ✅ [DOI](https://doi.org/10.1037/0021-9010.83.4.586)
- Le, H., Oh, I.-S., Robbins, S. B., Ilies, R., Holland, E., & Westrick, P. (2011). Too much of a good thing: Curvilinear relationships between personality traits and job performance. *Journal of Applied Psychology*, 96(1), 113-133. ✅ [DOI](https://doi.org/10.1037/a0021016)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
