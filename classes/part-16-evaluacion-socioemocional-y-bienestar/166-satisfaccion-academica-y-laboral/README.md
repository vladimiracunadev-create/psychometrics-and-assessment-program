# 166 — Satisfacción académica y laboral

> [Índice de la parte](../README.md)

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 128 y 051.

## Objetivos

1. Informar porcentaje favorable con intervalo de Wilson.
2. Reconocer los extremos espurios en rankings de unidades pequeñas.
3. Evitar comparar unidades como si las diferencias fueran reales.

## Fundamentos

Una forma frecuente de informar satisfacción es el porcentaje «favorable» (respuestas 4–5). Con pocos respondentes es muy variable; el **intervalo de Wilson** (Wilson, 1927; Brown, Cai y DasGupta, 2001) tiene mejor cobertura que el normal. La relación entre satisfacción laboral y desempeño es modesta (Judge et al., 2001): la satisfacción no es desempeño.

Laboratorio (30 unidades con la **misma** satisfacción real de 62 %; n de 8 a 100):

| Puesto | n | % favorable | IC 95 % de Wilson |
|---:|---:|---:|---|
| 1 | 8 | 88 % | [53 %; 98 %] |
| 2 | 20 | 80 % | [58 %; 92 %] |
| 28 | 8 | 50 % | [22 %; 78 %] |
| 30 | 12 | 33 % | [14 %; 61 %] |

De las 6 unidades de arriba, 4 tienen n ≤ 15; de las 6 de abajo, 3. Solo 1 de 30 intervalos excluye el 62 % real.

## Ejemplo resuelto

k = 7 de n = 8: p = 0,875; Wilson ≈ [0,53; 0,98]: la «mejor» unidad es compatible con el promedio.

## Errores y límites

- Publicar rankings sin intervalos.
- Comparar unidades de tamaños muy distintos.
- Reportar unidades con muy pocos respondentes (privacidad, clase 128).
- Datos simulados con satisfacción idéntica.

## Ejercicios

- **Inicial.** ¿Qué es un porcentaje favorable?
- **Intermedio.** p = 0,5 y n = 10: Wilson ≈ [0,26; 0,74].
- **Avanzado.** Aumenta el n mínimo a 30 en `lab.py` y observa los extremos.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/166-satisfaccion-academica-y-laboral/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo informarías unidades pequeñas? 2. ¿Qué acción derivas de una encuesta? 3. ¿Cómo evitas que se use para sancionar?
Se logra si el estudiante informa con intervalos y evita rankings espurios.

## Bibliografía

- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209-212.
- Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval estimation for a binomial proportion. *Statistical Science*, 16(2), 101-133.
- Judge, T. A., Thoresen, C. J., Bono, J. E., & Patton, G. K. (2001). The job satisfaction–job performance relationship. *Psychological Bulletin*, 127(3), 376-407.
