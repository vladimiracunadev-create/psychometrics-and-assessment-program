# 103 — Tipologías frente a rasgos: crítica a MBTI

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 024 y 101.

## Objetivos

1. Distinguir tipos (categorías) de rasgos (dimensiones).
2. Cuantificar la inestabilidad de dicotomizar un continuo.
3. Evaluar con criterios psicométricos un modelo de tipos.

## Fundamentos

Un modelo de **tipos** (como el MBTI, instrumento propietario que aquí solo se analiza conceptualmente) clasifica personas en categorías a partir de puntos de corte sobre dimensiones que, empíricamente, se distribuyen de forma continua y unimodal (McCrae y Costa, 1989). Dicotomizar una variable continua reduce información y potencia (MacCallum et al., 2002) y vuelve inestable la clasificación cerca del corte. La evidencia sobre la utilidad del MBTI para predecir desempeño laboral es limitada (Pittenger, 1993; Gardner y Martinko, 1996).

Laboratorio (fiabilidad test-retest del continuo = 0,85; N = 20 000):

| Medida | Valor |
|---|---:|
| Test-retest del puntaje continuo | 0,850 |
| Cambian de tipo entre dos aplicaciones | 17,2 % |
| ... entre quienes están cerca del corte (±0,3 DE, 23 % de la muestra) | 38,9 % |
| Conservan los 4 rasgos dicotomizados | 45,9 % |

La distribución del puntaje es unimodal (campana), no bimodal.

## Ejemplo resuelto

Con 4 dimensiones independientes y 83 % de consistencia de cada una, la probabilidad de conservar el tipo completo es 0,83⁴ ≈ 0,47: menos de la mitad.

## Errores y límites

- Usar tipos para seleccionar, ubicar o excluir personas.
- Considerar que «tipo» explica conducta específica.
- Tratar un modelo propietario como evidencia por ser popular.
- Los tipos pueden servir como lenguaje de conversación, con esa advertencia.

## Ejercicios

- **Inicial.** ¿Qué pierde la dicotomización?
- **Intermedio.** ¿Qué esperas si la fiabilidad baja a 0,70? Más cambios de tipo.
- **Avanzado.** Cambia RHO a 0,95 en `lab.py` y reporta el cambio de tipo.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/103-tipologias-frente-a-rasgos-critica-a-mbti/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia respaldaría una tipología real? (bimodalidad, taxometría) 2. ¿Qué alternativa propones? 3. ¿Cómo comunicarías un resultado de tipo con cautela?
Se logra si el estudiante evalúa un modelo de tipos con evidencia.

## Bibliografía

- McCrae, R. R., & Costa, P. T. (1989). Reinterpreting the Myers-Briggs Type Indicator from the perspective of the five-factor model of personality. *Journal of Personality*, 57(1), 17-40. ✅ [DOI](https://doi.org/10.1111/j.1467-6494.1989.tb00759.x)
- MacCallum, R. C., Zhang, S., Preacher, K. J., & Rucker, D. D. (2002). On the practice of dichotomization of quantitative variables. *Psychological Methods*, 7(1), 19-40. ✅ [DOI](https://doi.org/10.1037/1082-989x.7.1.19)
- Pittenger, D. J. (1993). Measuring the MBTI... and coming up short. *Journal of Career Planning and Employment*, 54(1), 48-52. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Gardner, W. L., & Martinko, M. J. (1996). Using the Myers-Briggs Type Indicator to study managers. *Journal of Management*, 22(1), 45-83. ✅ [DOI](https://doi.org/10.1177/014920639602200103)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
