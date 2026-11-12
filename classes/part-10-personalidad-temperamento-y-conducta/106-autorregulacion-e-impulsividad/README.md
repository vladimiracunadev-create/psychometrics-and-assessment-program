# 106 — Autorregulación e impulsividad

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 099 y 100.

## Objetivos

1. Estimar un parámetro conductual (descuento temporal).
2. Contrastar tarea conductual y autoinforme.
3. Reconocer que «impulsividad» es un conjunto de constructos.

## Fundamentos

El **descuento temporal hiperbólico** (Mazur, 1987) describe cuánto pierde valor una recompensa con la demora: V = R / (1 + kD). Una *k* mayor indica preferencia por lo inmediato. La **BIS-11** (Patton, Stanford y Barratt, 1995) es un autoinforme de impulsividad. Meta-análisis muestran que autoinformes y tareas conductuales correlacionan poco (Sharma, Markon y Clark, 2014): miden aspectos distintos.

Laboratorio (300 personas; 28 elecciones cada una; *k* verdadera mediana 0,030):

| Medida | Valor |
|---|---:|
| k estimada, mediana | 0,030 |
| r(log k verdadera, log k estimada) | 0,946 |
| r(log k estimada, autoinforme simulado débilmente ligado) | 0,090 |

## Ejemplo resuelto

k = 0,03; D = 90 días: V = 100/(1 + 2,7) = 27. Una persona prefiere $30 ahora a $100 en 90 días.

## Errores y límites

- Etiquetar a una persona como «impulsiva» por una escala.
- Usar la BIS-11 como diagnóstico: es una escala de investigación.
- Asumir que la tarea y el autoinforme miden lo mismo.
- Modelos de elección con ruido: el modelo logístico del laboratorio es una simplificación.

## Ejercicios

- **Inicial.** ¿Qué indica una k alta?
- **Intermedio.** Calcula V con k = 0,05, D = 30, R = 100 → 100/2,5 = 40.
- **Avanzado.** Reduce las elecciones a 8 en `lab.py` y observa la recuperación de k.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/106-autorregulacion-e-impulsividad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué otras tareas medirían control inhibitorio? 2. ¿Qué implica una correlación baja entre tarea y escala? 3. ¿Cuándo derivarías?
Se logra si el estudiante estima k y discute la multidimensionalidad de la impulsividad.

## Bibliografía

- Mazur, J. E. (1987). An adjusting procedure for studying delayed reinforcement. En M. L. Commons et al. (Eds.), *Quantitative Analyses of Behavior* (Vol. 5). Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Patton, J. H., Stanford, M. S., & Barratt, E. S. (1995). Factor structure of the Barratt Impulsiveness Scale. *Journal of Clinical Psychology*, 51(6), 768-774. ✅ [DOI](https://doi.org/10.1002/1097-4679(199511)51:6<768::aid-jclp2270510607>3.0.co;2-1)
- Sharma, L., Markon, K. E., & Clark, L. A. (2014). Toward a theory of distinct types of "impulsive" behaviors. *Psychological Bulletin*, 140(2), 374-408. ✅ [DOI](https://doi.org/10.1037/a0034418)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
