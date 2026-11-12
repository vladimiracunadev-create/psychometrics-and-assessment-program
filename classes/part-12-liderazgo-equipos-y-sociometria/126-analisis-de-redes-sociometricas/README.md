# 126 — Análisis de redes sociométricas

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 064 y 125.

## Objetivos

1. Calcular densidad, reciprocidad, centralización y componentes.
2. Comparar contra un modelo nulo.
3. Compartir resultados de redes sin vulnerar privacidad.

## Fundamentos

El análisis de redes sociales (Wasserman y Faust, 1994) describe un grupo como un grafo dirigido. Medidas: **densidad** (elecciones realizadas/posibles), **reciprocidad** (elecciones devueltas), **centralización** (cuánto se concentran las elecciones en pocas personas; Freeman, 1978), **componentes** y **homofilia** (elecciones dentro del subgrupo). Para interpretarlas se compara con un modelo nulo.

Laboratorio (dos cursos ficticios de 24; 3 elecciones cada uno):

| Métrica | Aleatorio | Con subgrupos |
|---|---:|---:|
| Densidad | 0,130 | 0,130 |
| Reciprocidad | 0,111 | 0,389 |
| Centralización (grado de entrada) | 0,190 | 0,142 |
| Componentes | 1 | 1 |
| Elecciones dentro del grupo | 0,458 | 0,972 |

En el curso aleatorio ~48 % de las elecciones cae dentro del grupo por azar (11 de 23 posibles).

## Ejemplo resuelto

24 estudiantes con 3 elecciones: 72 elecciones; densidad = 72/(24·23) = 0,130 (igual en ambos cursos por diseño).

## Errores y límites

- Interpretar la reciprocidad sin referencia al azar.
- Publicar gráficos con nombres o con datos que permitan reconocer a los niños.
- Confundir popularidad (grado de entrada) con influencia.
- Las redes sintéticas no tienen la complejidad de las reales.

## Ejercicios

- **Inicial.** ¿Qué es la reciprocidad?
- **Intermedio.** Si hay 10 elecciones devueltas de 72, reciprocidad = 0,139.
- **Avanzado.** Calcula la reciprocidad esperada por azar en `lab.py` mediante simulación.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/126-analisis-de-redes-sociometricas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué te indica la homofilia alta? 2. ¿Cómo anonimizas un gráfico? 3. ¿Qué librerías abiertas usarías (NetworkX u otras) y con qué licencia?
Se logra si el estudiante calcula métricas y las contrasta con un modelo nulo.

## Bibliografía

- Wasserman, S., & Faust, K. (1994). *Social Network Analysis: Methods and Applications*. Cambridge University Press. ✅ [DOI](https://doi.org/10.1017/cbo9780511815478)
- Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. *Social Networks*, 1(3), 215-239. ✅ [DOI](https://doi.org/10.1016/0378-8733(78)90021-7)
- Borgatti, S. P., Mehra, A., Brass, D. J., & Labianca, G. (2009). Network analysis in the social sciences. *Science*, 323, 892-895. ✅ [DOI](https://doi.org/10.1126/science.1165821)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
