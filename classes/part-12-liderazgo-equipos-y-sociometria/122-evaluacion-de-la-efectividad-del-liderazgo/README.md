# 122 — Evaluación de la efectividad del liderazgo

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 054, 109 y 121.

## Objetivos

1. Calcular acuerdo dentro del equipo (rwg) y CCI.
2. Decidir si se justifica agregar valoraciones al nivel del equipo.
3. Interpretar un promedio de equipo como atributo del líder o del evaluador.

## Fundamentos

Para valorar a un líder con las opiniones de su equipo, el promedio solo es interpretable si (a) los integrantes **coinciden** (acuerdo: rwg = 1 − s²/σ²_nula; James, Demaree y Wolf, 1984) y (b) los equipos **difieren** entre sí (CCI(1)) con un promedio fiable (CCI(2)) (Bliese, 2000; LeBreton y Senter, 2008). Con escala de 5 puntos y distribución nula uniforme, σ²_nula = 2,0.

Laboratorio (60 líderes, equipos de 6):

| Condición | rwg medio | CCI(1) | CCI(2) |
|---|---:|---:|---:|
| Líderes distintos, integrantes coinciden | 0,86 | 0,72 | 0,94 |
| Líderes iguales, cada uno valora distinto | 0,42 | −0,00 | −0,01 |

En la segunda condición el promedio del equipo no tiene fiabilidad: describe al evaluador, no al líder.

## Ejemplo resuelto

Varianza observada del equipo 0,60: rwg = 1 − 0,60/2,0 = 0,70.

## Errores y límites

- Agregar con acuerdo bajo.
- Elegir una distribución nula sin justificarla.
- Interpretar los CCI negativos como problema técnico: indican varianza entre grupos ≈ 0.
- Las convenciones (0,70) son guías.

## Ejercicios

- **Inicial.** ¿Qué mide rwg?
- **Intermedio.** s² = 1,0 y σ²_nula = 2,0 → rwg = 0,50.
- **Avanzado.** Aumenta el tamaño del equipo a 12 en `lab.py` y observa el CCI(2).

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/122-evaluacion-de-la-efectividad-del-liderazgo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué haces si el acuerdo es bajo? 2. ¿Qué otros criterios de efectividad (resultados, rotación) complementan? 3. ¿Cómo informarías a un líder?
Se logra si el estudiante decide agregar o no con los indicadores adecuados.

## Bibliografía

- James, L. R., Demaree, R. G., & Wolf, G. (1984). Estimating within-group interrater reliability with and without response bias. *Journal of Applied Psychology*, 69(1), 85-98. ✅ [DOI](https://doi.org/10.1037/0021-9010.69.1.85)
- Bliese, P. D. (2000). Within-group agreement, non-independence, and reliability. En K. J. Klein & S. W. J. Kozlowski (Eds.), *Multilevel Theory, Research, and Methods in Organizations*. Jossey-Bass. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- LeBreton, J. M., & Senter, J. L. (2008). Answers to 20 questions about interrater reliability and interrater agreement. *Organizational Research Methods*, 11(4), 815-852. ✅ [DOI](https://doi.org/10.1177/1094428106296642)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
