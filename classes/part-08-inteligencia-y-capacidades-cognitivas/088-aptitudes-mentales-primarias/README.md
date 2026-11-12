# 088 — Aptitudes mentales primarias

![Portada de la clase 088](portada.svg)

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 025 y 081.

## Objetivos

1. Describir el modelo de aptitudes primarias de Thurstone.
2. Calcular el error típico de la diferencia entre subpruebas.
3. Evitar sobreinterpretar perfiles.

## Fundamentos

Thurstone (1938) propuso capacidades primarias (comprensión verbal, fluidez, razonamiento, espacial, numérica, memoria, velocidad perceptual). Las baterías basadas en este enfoque entregan **perfiles**. Una diferencia entre dos subpruebas es fiable solo si supera su error:

```
EE_dif = DE · √(2 − ρ_a − ρ_b)
```

Laboratorio (5 aptitudes, DE = 15, fiabilidad 0,85 cada una): EE de la diferencia = 8,22 puntos; diferencia mínima fiable al 95 % = **16,1** puntos. Con 20 000 personas de perfil verdaderamente plano:

| Medida | Proporción |
|---|---:|
| Alguna diferencia ≥ 10 puntos entre subpruebas | 74,2 % |
| Alguna diferencia mayor al umbral fiable (16,1) | 28,8 % |

Con cinco subpruebas hay 10 comparaciones por persona: encontrar «fortalezas y debilidades» en perfiles planos es lo esperable.

## Ejemplo resuelto

Dos subpruebas con fiabilidad 0,90 y 0,80, DE 15: EE_dif = 15·√(2 − 1,7) = 8,2; umbral 16,1. Una diferencia de 12 puntos no es fiable.

## Errores y límites

- Interpretar cada fortaleza o debilidad de un perfil como un hallazgo.
- Basar decisiones individuales en análisis de perfil sin evidencia de validez incremental (McDermott et al., 1990).
- Ignorar que el umbral del laboratorio no corrige por comparaciones múltiples (28,8 % de falsos positivos aun con umbral).

## Ejercicios

- **Inicial.** ¿Cuántas comparaciones hay entre 6 subpruebas? → 15.
- **Intermedio.** Calcula EE_dif con ρ = 0,9 y 0,9, DE 10 → 10·√0,2 = 4,47.
- **Avanzado.** Aplica una corrección de Bonferroni al umbral en `lab.py`.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/088-aptitudes-mentales-primarias/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo un perfil agrega información sobre un puntaje global? 2. ¿Cómo redactas un perfil sin sobreafirmar? 3. ¿Qué evidencia necesitarías?
Se logra si el estudiante calcula umbrales de diferencia fiable y limita la interpretación de perfiles.

## Bibliografía

- Thurstone, L. L. (1938). *Primary Mental Abilities*. University of Chicago Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- McDermott, P. A., Fantuzzo, J. W., & Glutting, J. J. (1990). Just say no to subtest analysis: A critique on Wechsler theory and practice. *Journal of Psychoeducational Assessment*, 8(3), 290-302. ✅ [DOI](https://doi.org/10.1177/073428299000800307)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
