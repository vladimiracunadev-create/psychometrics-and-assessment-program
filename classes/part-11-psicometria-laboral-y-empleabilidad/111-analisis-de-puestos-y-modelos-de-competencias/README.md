# 111 — Análisis de puestos y modelos de competencias

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 017 y 054.

## Objetivos

1. Describir el análisis de puestos como base de cualquier evaluación laboral.
2. Calcular criticidad de tareas y la fiabilidad del acuerdo entre especialistas.
3. Documentar de forma reproducible un modelo de competencias.

## Fundamentos

El análisis de puestos identifica tareas y requisitos (conocimientos, habilidades, otras características) y es la base de la validez de contenido y de la defensa de un proceso (Brannick, Levine y Morgeson, 2007; Sanchez y Levine, 2012). Un procedimiento común: especialistas califican **importancia** y **frecuencia** de cada tarea; la criticidad es su producto. La fiabilidad del promedio de *k* evaluadores se estima con el CCI(3,k).

Laboratorio (8 especialistas, 12 tareas sintéticas):

| Medida | Valor |
|---|---:|
| CCI(3,k): importancia / frecuencia / criticidad | 0,88 / 0,96 / 0,91 |
| Tareas con criticidad ≥ 12 (entran al modelo) | 3 de 12 (tareas 3, 1, 4) |
| Top-4 con 8 evaluadores / con 3 | [3, 1, 4, 10] / [3, 4, 1, 10] |

Con menos evaluadores cambia el orden del ranking.

## Ejemplo resuelto

Una tarea con importancia 5 y frecuencia 3 tiene criticidad 15; otra con 4 y 2, criticidad 8. El umbral (12 en el laboratorio) es una decisión que se declara.

## Errores y límites

- Definir competencias por listas genéricas sin análisis del puesto.
- Usar muy pocos especialistas, o solo supervisores.
- Olvidar que los puestos cambian: el análisis se actualiza.
- Los datos son sintéticos y el puesto es hipotético.

## Ejercicios

- **Inicial.** ¿Qué es la criticidad de una tarea?
- **Intermedio.** Importancia media 3,5 y frecuencia media 4,0 → 14,0 (entra con umbral 12).
- **Avanzado.** Aumenta a 15 evaluadores en `lab.py` y observa la estabilidad del ranking.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/111-analisis-de-puestos-y-modelos-de-competencias/lab.py
```

## Autoevaluación y criterios

1. ¿Qué fuentes usarías además de especialistas? (observación, O*NET como referencia) 2. ¿Cómo documentarías el modelo? 3. ¿Cuándo lo revisarías?
Se logra si el estudiante construye y justifica un modelo desde un análisis documentado.

## Bibliografía

- Brannick, M. T., Levine, E. L., & Morgeson, F. P. (2007). *Job and Work Analysis* (2.ª ed.). Sage. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Sanchez, J. I., & Levine, E. L. (2012). The rise and fall of job analysis and the future of work analysis. *Annual Review of Psychology*, 63, 397-425. ✅ [DOI](https://doi.org/10.1146/annurev-psych-120710-100401)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
