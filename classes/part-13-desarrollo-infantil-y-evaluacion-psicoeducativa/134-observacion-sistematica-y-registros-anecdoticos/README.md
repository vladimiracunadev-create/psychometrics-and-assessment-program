# 134 — Observación sistemática y registros anecdóticos

![Portada de la clase 134](portada.svg)

> [Índice de la parte](../README.md)

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 029 y 111.

## Objetivos

1. Distinguir registro sistemático (con definiciones operacionales) de registro anecdótico.
2. Estimar cuánto tiempo observar para obtener tasas fiables.
3. Interpretar el acuerdo entre observadores con conductas poco frecuentes.

## Fundamentos

Un registro sistemático define la conducta de forma observable y usa un método de muestreo (eventos, intervalos, tiempo; Altmann, 1974; Bakeman y Gottman, 1997). El registro anecdótico es descriptivo y útil para generar hipótesis, pero no permite comparar ni cuantificar con fiabilidad. La fiabilidad de una tasa depende del tiempo observado; con conductas poco frecuentes, el acuerdo total engaña.

Laboratorio (400 niños, Poisson; dos sesiones independientes):

| Minutos observados | Fiabilidad entre sesiones |
|---:|---:|
| 5 | 0,17 |
| 30 | 0,42 |
| 60 | 0,60 |
| 120 | 0,72 |

Dos observadores, 180 intervalos de 10 s, conducta en 12 % de los intervalos: acuerdo total 0,87; kappa 0,54; acuerdo en la ocurrencia 0,45.

## Ejemplo resuelto

Si ambos observadores registran 150 intervalos sin conducta de 180, el acuerdo ya es 83 % aunque no coincidan en ninguna ocurrencia.

## Errores y límites

- Basar decisiones en 5 minutos de observación.
- Informar acuerdo total con conductas raras.
- Observar solo en un contexto (clase 136).
- Proteger la privacidad: registros con consentimiento y custodia.

## Ejercicios

- **Inicial.** ¿Qué es una definición operacional?
- **Intermedio.** Calcula el acuerdo en la ocurrencia: ambos 8, solo uno 12 → 8/(8 + 12) = 0,40.
- **Avanzado.** Aumenta la prevalencia de la conducta a 40 % y compara acuerdo total y kappa.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/134-observacion-sistematica-y-registros-anecdoticos/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo entrenarías observadores? 2. ¿Cuándo usar eventos y cuándo intervalos? 3. ¿Qué haces con un registro anecdótico preocupante?
Se logra si el estudiante diseña una observación con tiempos y acuerdo justificados.

## Bibliografía

- Altmann, J. (1974). Observational study of behavior: Sampling methods. *Behaviour*, 49(3-4), 227-267. ✅ [DOI](https://doi.org/10.1163/156853974x00534)
- Bakeman, R., & Gottman, J. M. (1997). *Observing Interaction: An Introduction to Sequential Analysis* (2.ª ed.). Cambridge University Press. ⚠️ existe, pero Crossref registra 1999 (¿otra edición?; [DOI](https://doi.org/10.1177/00238309990420010502))
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46. ✅ [DOI](https://doi.org/10.1177/001316446002000104)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
