# 129 — Evaluación 360 y sesgos de los evaluadores

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 114 y 122.

## Objetivos

1. Descomponer la varianza de una valoración 360.
2. Estimar la fiabilidad del promedio de pares.
3. Interpretar diferencias entre autoevaluación y valoración de otros.

## Fundamentos

En una evaluación 360, una valoración mezcla el desempeño del evaluado, un **sesgo idiosincrático** del evaluador y error. Un análisis de estructura latente de valoraciones de desempeño encontró que una parte considerable de la varianza era propia del evaluador (Scullen, Mount y Goff, 2000), y los metaanálisis muestran acuerdo modesto entre fuentes (Conway y Huffcutt, 1997). Por eso se promedian varios evaluadores del mismo tipo.

Laboratorio (300 evaluados; sesgo idiosincrático DE 0,7; error DE 0,5; desempeño DE 1,0; parámetros supuestos):

| Pares | Fiabilidad del promedio | r (promedio, verdad) |
|---:|---:|---:|
| 1 | 0,57 | 0,74 |
| 3 | 0,80 | 0,88 |
| 6 | 0,89 | 0,93 |
| 10 | 0,93 | 0,96 |

Acuerdo entre dos pares distintos (icc1) = 0,57. Autoevaluación frente al promedio de 6 pares: r = 0,44; diferencia media +0,74 puntos (indulgencia).

## Ejemplo resuelto

icc1 = 0,57 y k = 6: 6·0,57/(1 + 5·0,57) = 3,42/3,85 = 0,89.

## Errores y límites

- Basar una decisión en un solo evaluador.
- Interpretar la diferencia auto–otros como «falta de autoconocimiento» sin considerar información distinta.
- Usar 360 para decisiones de personal sin validar el instrumento.
- Mantener el anonimato de los evaluadores: se reporta solo con un mínimo de respondentes por fuente.

## Ejercicios

- **Inicial.** ¿Por qué se promedian varios pares?
- **Intermedio.** Con icc1 = 0,40 y k = 4: 1,6/(1 + 1,2) = 0,73.
- **Avanzado.** Duplica el sesgo idiosincrático (SD 1,4) en `lab.py` y observa la fiabilidad.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/129-evaluacion-360-y-sesgos-de-los-evaluadores/lab.py
```

## Autoevaluación y criterios

1. ¿Cuántos evaluadores por fuente? 2. ¿Cómo devuelves un 360 de forma útil? 3. ¿Qué haces con comentarios abiertos hirientes?
Se logra si el estudiante estima fiabilidad y propone un uso para el desarrollo, no para sanción.

## Bibliografía

- Scullen, S. E., Mount, M. K., & Goff, M. (2000). Understanding the latent structure of job performance ratings. *Journal of Applied Psychology*, 85(6), 956-970. ✅ [DOI](https://doi.org/10.1037/0021-9010.85.6.956)
- Conway, J. M., & Huffcutt, A. I. (1997). Psychometric properties of multisource performance ratings. *Human Performance*, 10(4), 331-360. ✅ [DOI](https://doi.org/10.1207/s15327043hup1004_2)
- Murphy, K. R., & Cleveland, J. N. (1995). *Understanding Performance Appraisal*. Sage. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
