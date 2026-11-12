# 142 — Fluidez y precisión lectora

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 015 y 133.

## Objetivos

1. Calcular el error de medida de las palabras correctas por minuto (PCM).
2. Comparar una lectura con la mediana de varias.
3. Estimar la zona de incertidumbre alrededor de un criterio de logro.

## Fundamentos

La fluidez lectora (precisión, velocidad y prosodia) se evalúa con lecturas de un minuto (PCM). Las normas de PCM se usan como referencia (Hasbrouck y Tindal, 2006), pero el error de medida de una lectura es grande: depende del texto y del día (Christ y Silberglitt, 2007). Se recomienda usar la mediana de varias lecturas.

Laboratorio (500 estudiantes; habilidad ~ N(80; 25); texto DE 8, día DE 9; criterio 60 PCM; supuestos):

| Procedimiento | Fiabilidad (test-retest) | Cambian de lado del criterio |
|---|---:|---:|
| 1 lectura | 0,80 | 18,6 % |
| Mediana de 3 lecturas | 0,90 | 10,8 % |

Error típico de una lectura = 12,0 PCM; 55 % de los estudiantes está a menos de ±24 PCM del criterio.

## Ejemplo resuelto

ETM = √(8² + 9²) = 12,04. Un estudiante con 54 PCM tiene intervalo 54 ± 23,6: el criterio de 60 cae dentro.

## Errores y límites

- Clasificar con una sola lectura.
- Tomar la velocidad por comprensión: leer rápido no es leer mejor.
- Aplicar criterios de logro de otro país o curso sin verificarlos.
- Valores del laboratorio ilustrativos.

## Ejercicios

- **Inicial.** ¿Qué componentes tiene la fluidez?
- **Intermedio.** Calcula ETM con texto 6 y día 6 → 8,5.
- **Avanzado.** Usa la media de 5 lecturas en `lab.py` y reporta el error de clasificación.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/142-fluidez-y-precision-lectora/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo eliges textos equivalentes? 2. ¿Cómo registras errores de lectura? 3. ¿Qué haces con quienes están cerca del criterio?
Se logra si el estudiante cuantifica el error y propone un procedimiento de decisión.

## Bibliografía

- Hasbrouck, J., & Tindal, G. A. (2006). Oral reading fluency norms: A valuable assessment tool for reading teachers. *The Reading Teacher*, 59(7), 636-644.
- Christ, T. J., & Silberglitt, B. (2007). Estimates of the standard error of measurement for curriculum-based measures of oral reading fluency. *School Psychology Review*, 36(1), 130-146.
