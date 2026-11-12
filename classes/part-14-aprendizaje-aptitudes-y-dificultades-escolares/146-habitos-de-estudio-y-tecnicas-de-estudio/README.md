# 146 — Hábitos de estudio y técnicas de estudio

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 094 y 096.

## Objetivos

1. Distinguir técnicas de estudio con respaldo de las populares sin él.
2. Ilustrar el efecto de espaciado con un modelo de olvido.
3. Reconocer los límites de los inventarios de hábitos autoinformados.

## Fundamentos

Una revisión amplia concluyó que la **práctica distribuida** y la **práctica de recuperación** (autoevaluación) tienen alta utilidad, mientras que subrayar y releer tienen utilidad baja (Dunlosky et al., 2013). El efecto de espaciado depende del intervalo de retención (Cepeda et al., 2006). El laboratorio usa un modelo exponencial de olvido (Ebbinghaus, 1885) en que la ganancia de cada repaso es mayor si hubo algo de olvido (esfuerzo de recuperación). **Es una ilustración cualitativa**, no una predicción.

Laboratorio (4 sesiones de estudio; prueba el día 14 y retención el día 28):

| Plan | Prueba día 14 | Retención día 28 |
|---|---:|---:|
| Masivo (4 sesiones el día 13) | 0,90 | 0,10 |
| Masivo (4 sesiones el día 0) | 0,12 | 0,01 |
| Distribuido (días 0, 3, 6, 9) | 0,66 | 0,21 |
| Distribuido tardío (días 4, 7, 10, 13) | 0,92 | 0,29 |

Para una prueba inmediata, estudiar pegado a la prueba rinde bien; el espaciado destaca en la retención duradera.

## Ejemplo resuelto

Recuerdo = exp(−t/S): con S = 6 y t = 15 días, exp(−2,5) = 0,08; con S = 12, exp(−1,25) = 0,29.

## Errores y límites

- Recomendar técnicas por popularidad o por «estilo de aprendizaje».
- Interpretar un inventario de hábitos como medida de conducta real.
- Prometer notas por una técnica: los efectos dependen del material y del estudiante.
- Modelo con parámetros supuestos.

## Ejercicios

- **Inicial.** ¿Qué es la práctica de recuperación?
- **Intermedio.** Calcula exp(−10/5) = 0,135.
- **Avanzado.** Cambia la ganancia por esfuerzo (4,0) a 0 en `lab.py` y describe qué pierde el espaciado.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/146-habitos-de-estudio-y-tecnicas-de-estudio/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo enseñarías a planificar el estudio? 2. ¿Cómo medirías el efecto en tu curso? 3. ¿Qué rol tiene la motivación?
Se logra si el estudiante recomienda técnicas con respaldo y declara los límites.

## Bibliografía

- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354-380.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4-58.
- Ebbinghaus, H. (1885). *Über das Gedächtnis*. Duncker & Humblot.
