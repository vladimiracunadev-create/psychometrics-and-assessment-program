# 174 — Datos faltantes en instrumentos

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 052 y 172.

## Objetivos

1. Distinguir MCAR, MAR y MNAR.
2. Comparar casos completos, imputación por la media y regresión estocástica.
3. Planificar la prevención de datos faltantes.

## Fundamentos

Rubin (1976) clasificó los mecanismos: **MCAR** (al azar), **MAR** (depende de variables observadas) y **MNAR** (depende del propio valor faltante). Los casos completos son insesgados bajo MCAR; bajo MAR se requiere un método que use las variables observadas (imputación múltiple, máxima verosimilitud; Schafer y Graham, 2002; Enders, 2010); bajo MNAR ningún método simple corrige. El motor del repositorio **no trata las omisiones como cero**: las excluye y las informa (clase 004).

Laboratorio (30 % faltante en Y; r verdadera 0,50; media verdadera 0; 300 réplicas; sesgos):

| Mecanismo | Método | Sesgo de la media | Sesgo de r |
|---|---|---:|---:|
| MCAR | completos | −0,001 | −0,001 |
| MCAR | media | −0,001 | −0,082 |
| MAR | completos | +0,161 | −0,041 |
| MAR | media | +0,161 | −0,161 |
| MAR | regresión estocástica | +0,005 | −0,003 |
| MNAR | completos | +0,314 | −0,038 |
| MNAR | regresión estocástica | +0,249 | −0,030 |

## Ejemplo resuelto

Bajo MAR (los de bajo X responden menos), la media de Y de los completos sobreestima; imputar con Y ~ X recupera la media (sesgo +0,005) porque X explica la ausencia.

## Errores y límites

- Imputar por la media y analizar como si fuera completo.
- Suponer MAR sin argumento: no es verificable con los datos.
- Descartar variables que explican la ausencia.
- Simulación con mecanismos simples; en la práctica, imputación múltiple.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre MAR y MNAR?
- **Intermedio.** ¿Cómo previene un diseño las omisiones? Instrucciones claras, pocas preguntas sensibles, seguimiento.
- **Avanzado.** Reduce el porcentaje faltante a 10 % y observa los sesgos.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/174-datos-faltantes-en-instrumentos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué mecanismo es plausible en tu estudio? 2. ¿Qué análisis de sensibilidad harías? 3. ¿Qué informarías?
Se logra si el estudiante elige un tratamiento según el mecanismo y declara sus supuestos.

## Bibliografía

- Rubin, D. B. (1976). Inference and missing data. *Biometrika*, 63(3), 581-592.
- Schafer, J. L., & Graham, J. W. (2002). Missing data: Our view of the state of the art. *Psychological Methods*, 7(2), 147-177.
- Enders, C. K. (2010). *Applied Missing Data Analysis*. Guilford.
