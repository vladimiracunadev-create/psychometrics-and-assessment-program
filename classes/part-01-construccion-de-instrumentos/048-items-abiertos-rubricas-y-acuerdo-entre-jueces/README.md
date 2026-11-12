# 048 — Ítems abiertos, rúbricas y acuerdo entre jueces

> [Índice de la parte](../README.md)

**Parte 01 — Construcción de instrumentos** · Nivel introductorio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 047.

## Objetivos

1. Calcular acuerdo exacto, adyacente y kappa ponderado.
2. Identificar el sesgo de severidad.
3. Evaluar el efecto del entrenamiento de jueces.

## Fundamentos

Las respuestas abiertas se califican con una rúbrica de descriptores observables. El acuerdo exacto, el adyacente y el kappa ponderado cuadrático miden aspectos distintos; la diferencia media entre jueces revela severidad sistemática.

Laboratorio (400 respuestas sintéticas, 4 niveles): sin entrenamiento, exacto 0,35, adyacente 0,86, kappa 0,49, diferencia media +0,69; con entrenamiento, exacto 0,70, adyacente 1,00, kappa 0,81, diferencia +0,11.

## Ejemplo resuelto

Un acuerdo adyacente de 0,86 parece bueno, pero con acuerdo exacto de 0,35 y un juez 0,69 niveles más severo las notas dependen de quién corrige.

## Errores y límites

- Informar un solo indicador de acuerdo.
- Entrenar a los jueces una sola vez.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre acuerdo exacto y adyacente?
- **Intermedio.** Añade un tercer juez y calcula el acuerdo por pares.
- **Avanzado.** Diseña un procedimiento de calibración con respuestas ancla.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/048-items-abiertos-rubricas-y-acuerdo-entre-jueces/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del resultado depende de que los datos sean sintéticos? 2. ¿Qué cambiaría con personas reales? 3. ¿Qué límite declararías?
Se logra si el estudiante ejecuta el laboratorio, interpreta las cifras con cautela y declara sus límites.

## Bibliografía

- Fleiss, J. L., & Cohen, J. (1973). The equivalence of weighted kappa and the intraclass correlation coefficient. *Educational and Psychological Measurement*, 33, 613-619.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
