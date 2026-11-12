# 101 — Modelo de los cinco factores y sus facetas

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 022 y 063.

## Objetivos

1. Describir los cinco dominios y sus facetas.
2. Plantear el dilema amplitud–fidelidad al predecir un criterio.
3. Elegir el nivel de medida que corresponde a la pregunta.

## Fundamentos

El modelo de cinco factores (neuroticismo, extraversión, apertura, amabilidad y responsabilidad) organiza la variación de rasgos en dominios amplios, cada uno con facetas más específicas (Costa y McCrae, 1992; John y Srivastava, 1999). Un criterio amplio suele predecirse bien con dominios; uno específico, con la faceta pertinente (Paunonen y Ashton, 2001).

Laboratorio (un dominio con 6 facetas; el criterio depende del dominio y de una faceta; N = 3 000, validación en la segunda mitad; pesos supuestos):

| Predictor | r con el criterio |
|---|---:|
| Puntaje de dominio (promedio de 6 facetas) | 0,295 |
| Faceta 1 sola (la relevante) | 0,392 |
| 6 facetas (regresión múltiple) | 0,380 |

Los pesos estimados identifican la faceta relevante (0,43) frente a las demás (≈ 0).

## Ejemplo resuelto

Para predecir «orden en el trabajo» sirve la faceta de orden; para predecir «desempeño global», el dominio completo.

## Errores y límites

- Reportar 30 facetas con muestras pequeñas: sobreajuste y baja fiabilidad por faceta (clase 108).
- Interpretar las facetas como entidades separadas cuando están muy correlacionadas.
- Aplicar el modelo en culturas distintas sin evidencia de invarianza (clase 035).
- Las ganancias del laboratorio dependen de los pesos supuestos.

## Ejercicios

- **Inicial.** Nombra los cinco dominios.
- **Intermedio.** ¿Qué nivel usarías para predecir «ausentismo»? Justifica.
- **Avanzado.** Reduce N a 300 en `lab.py` y compara dominio y facetas.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/101-modelo-de-los-cinco-factores-y-sus/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo preferir dominios? 2. ¿Qué riesgo tiene un perfil de 30 facetas? 3. ¿Cómo informas una faceta con 4 ítems?
Se logra si el estudiante elige el nivel de medida según el criterio.

## Bibliografía

- Costa, P. T., & McCrae, R. R. (1992). *Professional Manual: Revised NEO Personality Inventory (NEO PI-R)*. Psychological Assessment Resources.
- John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy. En L. A. Pervin & O. P. John (Eds.), *Handbook of Personality* (2.ª ed.). Guilford.
- Paunonen, S. V., & Ashton, M. C. (2001). Big Five factors and facets and the prediction of behavior. *Journal of Personality and Social Psychology*, 81(3), 524-539.
