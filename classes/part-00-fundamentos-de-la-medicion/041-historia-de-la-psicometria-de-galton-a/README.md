# 041 — Historia de la psicometría: de Galton a la medición moderna

> [Índice de la parte](../README.md)

**Parte 00 — Fundamentos de la medición psicológica** · Nivel fundamentos · 4 h · Estado `escrita`
**Prerrequisitos:** clase 001.

## Objetivos

1. Explicar la regresión a la media a partir de Galton.
2. Distinguir pendiente y correlación.
3. Ubicar a Spearman y a Binet y Simon en la tradición.

## Fundamentos

Galton (1886) observó que los hijos de padres muy altos eran altos pero menos extremos que sus padres. Pearson formalizó la correlación; Spearman (1904) propuso un factor general y Binet y Simon (1905) construyeron la primera escala práctica de inteligencia. Las fechas provienen de manuales de historia de la psicología y deben contrastarse con las fuentes primarias.

Laboratorio (5.000 pares sintéticos, r = 0,5): pendiente 0,52; el 10 % de padres más altos (1,75 DE) tiene hijos con media de 0,93 DE; la desviación típica se mantiene (0,99 y 1,01).

## Ejemplo resuelto

Un estudiante que puntúa muy alto en una primera medición suele puntuar menos alto en la segunda sin que haya habido «declive»: es el mismo fenómeno.

## Errores y límites

- Interpretar la regresión como una fuerza biológica.
- Creer que la dispersión de la población disminuye.
- Los pares son sintéticos.

## Ejercicios

- **Inicial.** ¿Qué valor tiene la pendiente cuando r = 0,5 y ambas variables tienen igual desviación?
- **Intermedio.** Simula r = 0,8 y compara la media de los hijos.
- **Avanzado.** Explica cómo la regresión a la media puede inflar el efecto de un programa.

## Laboratorio

```bash
python classes/part-00-fundamentos-de-la-medicion/041-historia-de-la-psicometria-de-galton-a/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del resultado depende de que los datos sean sintéticos? 2. ¿Qué cambiaría con personas reales? 3. ¿Qué límite declararías?
Se logra si el estudiante ejecuta el laboratorio, interpreta las cifras con cautela y declara sus límites.

## Bibliografía

- Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute*, 15, 246-263.
- Spearman, C. (1904). «General intelligence» objectively determined and measured. *American Journal of Psychology*, 15(2), 201-292.
