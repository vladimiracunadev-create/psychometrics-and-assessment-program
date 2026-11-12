# 173 — Simulación de datos psicométricos

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 172 y 052.

## Objetivos

1. Diseñar un estudio de Monte Carlo con escenarios justificados.
2. Medir la cobertura real de un intervalo de confianza.
3. Detectar condiciones donde un método no cumple lo que promete.

## Fundamentos

Un estudio de simulación genera datos de un modelo conocido, aplica un método y compara sus resultados con la verdad (Morris, White y Crowther, 2019). Se informan sesgo, error y **cobertura**. El intervalo de Fisher para r (Fisher, 1915) supone aproximadamente normalidad bivariada.

Laboratorio (r verdadera ≈ 0,40; 2 000 réplicas por celda; la correlación poblacional se recalcula en cada distribución):

| Distribución | r poblacional | Cobertura n = 30 | n = 60 | n = 200 |
|---|---:|---:|---:|---:|
| Normal | 0,399 | 95,5 % | 94,5 % | 95,3 % |
| Asimétrica (lognormal) | 0,288 | 86,7 % | 83,9 % | 78,5 % |
| Con extremos (10 %) | 0,403 | 70,7 % | 68,0 % | 67,8 % |

## Ejemplo resuelto

Con 2 000 réplicas, el error de Monte Carlo de una cobertura de 95 % es √(0,95·0,05/2 000) = 0,5 %: diferencias de 1 punto ya son detectables.

## Errores y límites

- Probar un método solo en el escenario favorable.
- Reportar muy pocas réplicas.
- No fijar la semilla (clase 178).
- Una simulación solo prueba lo que se le pregunta.

## Ejercicios

- **Inicial.** ¿Qué es la cobertura?
- **Intermedio.** Error de Monte Carlo para cobertura 90 % con 500 réplicas → √(0,09/500) = 1,3 %.
- **Avanzado.** Agrega un escenario con datos ordinales de 5 categorías.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/173-simulacion-de-datos-psicometricos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué escenarios incluirías? 2. ¿Cómo reportarías los resultados? 3. ¿Qué método alternativo usarías con datos asimétricos? (bootstrap, Spearman)
Se logra si el estudiante mide cobertura bajo varias condiciones y concluye con cautela.

## Bibliografía

- Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine*, 38(11), 2074-2102.
- Fisher, R. A. (1915). Frequency distribution of the values of the correlation coefficient in samples from an indefinitely large population. *Biometrika*, 10(4), 507-521.
