# 074 — Acomodaciones y diseño universal de la evaluación

> [Índice de la parte](../README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 044 y 073.

## Objetivos

1. Distinguir acomodación, modificación y diseño universal.
2. Analizar el efecto del tiempo extendido según el tipo de prueba.
3. Decidir si una acomodación preserva el constructo.

## Fundamentos

Una **acomodación** cambia las condiciones (tiempo, formato, apoyos) sin cambiar el constructo; una **modificación** cambia lo que se mide. El **diseño universal** (Thompson, Johnstone y Thurlow, 2002) incorpora la accesibilidad desde el origen. La hipótesis de interacción (Sireci, Scarpati y Li, 2005) predice que una buena acomodación beneficia al estudiante con necesidad y no altera el puntaje de quien no la necesita.

Modelo de juguete (40 ítems, p de acierto 0,80; velocidades 1,2 y 0,6 ítems/min; tiempo ×1,5):

| Prueba | Grupo | Normal | Extendido | Ganancia |
|---|---|---:|---:|---:|
| Velocidad (30 min) | sin necesidad | 28,8 | 32,0 | 3,2 |
| Velocidad (30 min) | con necesidad | 14,4 | 21,6 | 7,2 |
| Poder (90 min) | ambos | 32,0 | 32,0 | 0,0 |

En la prueba de velocidad el tiempo extendido ayuda más al grupo con necesidad y también al otro: la velocidad es parte de lo que se mide. En la de poder, no cambia nada.

## Ejemplo resuelto

Ganancia = 0,8·(min(40, v·1,5T) − min(40, v·T)). Con v = 0,6, T = 30: 0,8·(27 − 18) = 7,2.

## Errores y límites

- Decidir acomodaciones por etiqueta diagnóstica sin evaluar la necesidad funcional.
- Asumir que cualquier extra de tiempo es neutral: depende de la velocidad como constructo.
- Informar puntajes acomodados sin declarar la acomodación cuando sea relevante para la interpretación.
- El modelo separa velocidad y habilidad por construcción: es una hipótesis.

## Ejercicios

- **Inicial.** ¿Cuándo el tiempo extendido cambia el constructo?
- **Intermedio.** v = 1,2, T = 20 min; ¿cuántos ítems intenta? 24; puntaje esperado 19,2.
- **Avanzado.** Añade una prueba intermedia (45 min) y describe la ganancia de cada grupo.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/074-acomodaciones-y-diseno-universal-de-la-evaluacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia necesitarías para sostener una acomodación? 2. ¿Qué principios de diseño universal aplicarías? 3. ¿Qué dice la normativa educativa chilena sobre apoyos? (consultar la fuente vigente).
Se logra si el estudiante evalúa una acomodación frente al constructo.

## Bibliografía

- Sireci, S. G., Scarpati, S. E., & Li, S. (2005). Test accommodations for students with disabilities: An analysis of the interaction hypothesis. *Review of Educational Research*, 75(4), 457-490. ✅ [DOI](https://doi.org/10.3102/00346543075004457)
- Thompson, S. J., Johnstone, C. J., & Thurlow, M. L. (2002). *Universal Design Applied to Large Scale Assessments* (NCEO Synthesis Report 44). University of Minnesota. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
