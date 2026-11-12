# 096 — Memoria verbal y aprendizaje de listas

![Portada de la clase 096](portada.svg)

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 087 y 094.

## Objetivos

1. Calcular los índices de una tarea de aprendizaje de listas.
2. Estimar su fiabilidad con formas paralelas.
3. Distinguir índices básicos de índices derivados.

## Fundamentos

Las tareas de aprendizaje de listas (varios ensayos, interferencia, evocación diferida y reconocimiento) producen índices: **aprendizaje total** (suma de ensayos), **ganancia** (último − primero), **retención** (diferido/último) e **intrusiones**. Los derivados (diferencias y cocientes) heredan el problema de fiabilidad de las puntuaciones de cambio (clase 087).

Laboratorio (800 personas, dos formas paralelas de una lista de 15 palabras en 5 ensayos; sintético):

| Índice | Media | DE | Fiabilidad entre formas |
|---|---:|---:|---:|
| Aprendizaje total | 28,14 | 14,17 | 0,934 |
| Ganancia | 5,75 | 3,23 | 0,543 |
| Retención | 0,76 | 0,37 | 0,077 |
| Intrusiones | 0,21 | 0,44 | −0,056 |

## Ejemplo resuelto

Ensayos 6, 9, 11, 12, 13 y diferido 9: total = 51; ganancia = 7; retención = 9/13 = 0,69.

## Errores y límites

- Interpretar la retención individual como «olvido» sin considerar la fiabilidad.
- Reportar solo un puntaje total cuando el propósito es diagnóstico.
- Usar formas sin evidencia de equivalencia.
- Para fines clínicos hay normas y criterios que corresponden a profesionales habilitados.

## Ejercicios

- **Inicial.** ¿Qué índice es más fiable y por qué?
- **Intermedio.** Calcula el total y la ganancia de 5, 8, 10, 11, 13 → 47 y 8.
- **Avanzado.** Aumenta a 8 ensayos en `lab.py` y observa la fiabilidad de la ganancia.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/096-memoria-verbal-y-aprendizaje-de-listas/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué las intrusiones son poco fiables? 2. ¿Qué evidencia necesitas para usar formas alternativas? 3. ¿Cómo informarías un índice poco fiable?
Se logra si el estudiante reporta cada índice con su fiabilidad.

## Bibliografía

- Lezak, M. D., Howieson, D. B., Bigler, E. D., & Tranel, D. (2012). *Neuropsychological Assessment* (5.ª ed.). Oxford University Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Cronbach, L. J., & Furby, L. (1970). How we should measure "change"—or should we? *Psychological Bulletin*, 74(1), 68-80. ✅ [DOI](https://doi.org/10.1037/h0029382)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
