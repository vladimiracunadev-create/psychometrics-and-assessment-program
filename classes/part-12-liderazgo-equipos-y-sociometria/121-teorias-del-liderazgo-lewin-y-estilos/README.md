# 121 — Teorías del liderazgo: Lewin y estilos

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 014 y 103.

## Objetivos

1. Distinguir la tipología de Lewin de los modelos de dos dimensiones.
2. Estimar la estabilidad de una clasificación por cuadrantes.
3. Reconocer la dependencia situacional de la efectividad.

## Fundamentos

Lewin, Lippitt y White (1939) compararon en grupos experimentales de niños los climas *autocrático, democrático y laissez-faire*: es un marco **conceptual** clásico, no un instrumento. Los estudios posteriores (Ohio State; Stogdill, 1948) identificaron dos dimensiones, *consideración* (personas) y *estructura* (tarea); un metaanálisis encontró relaciones de ambas con criterios de liderazgo, de magnitud variable según el criterio (Judge, Piccolo e Ilies, 2004). Clasificar en cuadrantes agrega la inestabilidad de dicotomizar (clase 103).

Laboratorio (cada dimensión con fiabilidad 0,80; N = 20 000; cuadrantes por mediana):

| Medida | Valor |
|---|---:|
| Test-retest observado de cada dimensión | 0,81 |
| Líderes que cambian de cuadrante entre dos mediciones | 36,6 % (con cambio totalmente aleatorio sería 75 %) |
| Mantienen el cuadrante (los cuatro) | 63–64 % |

## Ejemplo resuelto

Con la misma probabilidad de conservar cada dimensión (≈ 0,80 de acuerdo respecto de la mediana), conservar ambas es ≈ 0,64: coincide con lo observado.

## Errores y límites

- Etiquetar a un líder por un cuadrante («autoritario», «democrático»).
- Deducir que un estilo es «el mejor»: la efectividad depende de la situación y del criterio.
- Usar autoevaluaciones del líder como única fuente (clase 129).
- Los parámetros son supuestos.

## Ejercicios

- **Inicial.** ¿Qué dimensiones propone el enfoque de Ohio State?
- **Intermedio.** Si cada dimensión se conserva con prob. 0,90, ¿cuánto se conserva el cuadrante? 0,81.
- **Avanzado.** Cambia RHO a 0,90 en `lab.py` y reporta el cambio.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/121-teorias-del-liderazgo-lewin-y-estilos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué criterio de efectividad usarías? 2. ¿Por qué evitar tipologías cerradas? 3. ¿Qué información adicional pedirías?
Se logra si el estudiante cuantifica la estabilidad de una clasificación y la interpreta con cautela.

## Bibliografía

- Lewin, K., Lippitt, R., & White, R. K. (1939). Patterns of aggressive behavior in experimentally created "social climates". *Journal of Social Psychology*, 10(2), 271-299. ✅ [DOI](https://doi.org/10.1080/00224545.1939.9713366)
- Stogdill, R. M. (1948). Personal factors associated with leadership: A survey of the literature. *Journal of Psychology*, 25, 35-71. ✅ [DOI](https://doi.org/10.1080/00223980.1948.9917362)
- Judge, T. A., Piccolo, R. F., & Ilies, R. (2004). The forgotten ones? The validity of consideration and initiating structure in leadership research. *Journal of Applied Psychology*, 89(1), 36-51. ✅ [DOI](https://doi.org/10.1037/0021-9010.89.1.36)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
