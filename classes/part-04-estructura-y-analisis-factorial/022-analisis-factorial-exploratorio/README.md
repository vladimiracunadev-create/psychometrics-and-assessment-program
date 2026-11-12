# 022 — Análisis factorial exploratorio

> [Índice de la parte](../README.md) · [Anterior](../021-correlacion-y-matriz/README.md) · [Siguiente](../023-analisis-factorial-confirmatorio/README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 021.

## Objetivos

1. Explicar el modelo factorial común: cargas, comunalidades y unicidades.
2. Decidir cuántos factores retener y por qué la regla de Kaiser es insuficiente.
3. Interpretar cargas sin rotar y entender por qué se rota.

## Fundamentos

Modelo: cada ítem = suma ponderada de factores comunes + factor único. La varianza de un ítem se divide en **comunalidad** (compartida) y **unicidad**. El AFE estima las cargas sin imponer cuáles ítems cargan en qué factor.

**Cuántos factores.** Kaiser retiene autovalores > 1, regla que suele sobreestimar. El **análisis paralelo** (Horn, 1965) retiene los autovalores que superan los de datos aleatorios del mismo tamaño (aquí, percentil 95 de 40 réplicas). Fabrigar et al. (1999) recomiendan combinar criterios.

Laboratorio (12 ítems, dos factores independientes verdaderos, N = 400):

| # | Autovalor | Azar p95 | Kaiser | Paralelo |
|---:|---:|---:|---|---|
| 1 | 2,81 | 1,38 | sí | sí |
| 2 | 2,67 | 1,25 | sí | sí |
| 3 | 0,83 | 1,19 | no | no |

Ambos reconocen 2. Con más ítems o cargas bajas Kaiser tiende a sobrestimar; el paralelo es más conservador. Las cargas sin rotar mezclan ambos factores (cada ítem carga ≈ 0,5 en los dos), lo que obliga a rotar (clase 061).

## Ejemplo resuelto

Un ítem con cargas 0,6 y 0,3: comunalidad = 0,36 + 0,09 = 0,45; unicidad = 0,55.

## Errores y límites

- Usar componentes principales y llamarlo «análisis factorial» sin aclarar (el laboratorio usa componentes como aproximación didáctica).
- Retener factores por la regla de Kaiser sin otro criterio.
- Usar muestras pequeñas: las cargas son inestables.
- Interpretar el nombre que uno le pone al factor como evidencia del constructo.

## Ejercicios

- **Inicial.** Comunalidad de un ítem con cargas 0,5 y 0,5 → 0,50.
- **Intermedio.** Si los autovalores son 3,1; 1,2; 1,05; 0,9 y el azar p95 = 1,3; 1,15; 1,1; 1,0, ¿cuántos retiene el análisis paralelo? → 1.
- **Avanzado.** Cambia las cargas verdaderas a 0,4 en `lab.py` y compara Kaiser con paralelo.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/022-analisis-factorial-exploratorio/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es la comunalidad? 2. ¿Por qué el paralelo es más defendible? 3. ¿Qué criterios no estadísticos usarías?
Se logra si el estudiante decide el número de factores con más de un criterio.

## Bibliografía

- Horn, J. L. (1965). A rationale and test for the number of factors in factor analysis. *Psychometrika*, 30(2), 179-185.
- Fabrigar, L. R., Wegener, D. T., MacCallum, R. C., & Strahan, E. J. (1999). Evaluating the use of exploratory factor analysis in psychological research. *Psychological Methods*, 4(3), 272-299.
