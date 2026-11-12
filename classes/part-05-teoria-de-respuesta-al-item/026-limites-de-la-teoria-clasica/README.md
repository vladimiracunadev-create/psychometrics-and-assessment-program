# 026 — Los límites que hay que superar: lo que la teoría clásica no resuelve

> [Índice de la parte](../README.md) · [Siguiente](../027-modelo-de-rasch/README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 010, 011 y 015.

## Objetivos

1. Enumerar tres límites de la teoría clásica (dependencia de la muestra, error único, puntaje dependiente del test).
2. Mostrar con datos que p y r ítem-resto cambian con el grupo.
3. Enunciar la propiedad de invarianza de parámetros de la TRI y su condición.

## Fundamentos

En la teoría clásica la dificultad (p) y la discriminación dependen de **quiénes** respondan, y el puntaje de una persona depende de **cuáles** ítems tuvo. La TRI modela la probabilidad de acierto como función de un rasgo latente θ y de parámetros del ítem, de modo que (si el modelo se sostiene) los parámetros no dependen de la muestra y θ no depende del conjunto de ítems (Hambleton y Jones, 1993; Embretson y Reise, 2000).

Laboratorio (10 ítems de dificultad fija; grupos de media θ −1 y +1):

| Ítem | b real | p baja / alta | r baja / alta | b estimado baja / alta |
|---:|---:|---|---|---|
| 1 | −1,8 | 0,67 / 0,93 | 0,28 / 0,21 | −1,85 / −1,91 |
| 5 | 0,0 | 0,30 / 0,70 | 0,32 / 0,29 | 0,01 / 0,02 |
| 10 | 2,4 | 0,05 / 0,24 | 0,17 / 0,26 | 2,42 / 2,36 |

p y r cambian mucho con el grupo; b estimado coincide con el real en ambos. **Aviso:** la habilidad se conoce porque se simula; en datos reales se estima a la vez (clases 027 y 066).

## Ejemplo resuelto

Un ítem con p = 0,93 en el grupo alto y 0,67 en el bajo parece «fácil» o «medio» según el grupo; su b (−1,85 y −1,91) lo ubica en el mismo punto de la escala de habilidad.

## Errores y límites

- Creer que la TRI «resuelve» automáticamente la muestra: exige que el modelo se ajuste y muestras razonables.
- Interpretar la invarianza como si valiera con ítems sesgados (DIF, clase 033).
- Usar TRI con muestras de decenas de personas.

## Ejercicios

- **Inicial.** ¿Qué dos índices clásicos dependen de la muestra?
- **Intermedio.** Si un ítem tiene p = 0,5 en un grupo con media 0 y b = 0, ¿cuál sería p en un grupo con media +1 (a = 1)? ≈ logistica(1) = 0,73.
- **Avanzado.** Añade un tercer grupo con media 0 en `lab.py` y comprueba que el b estimado se mantiene.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/026-limites-de-la-teoria-clasica/lab.py
```

## Autoevaluación y criterios

1. ¿Qué condiciones requiere la invarianza? 2. ¿Qué ventaja práctica trae para bancos de ítems? 3. ¿Qué se pierde frente a la simplicidad clásica?
Se logra si el estudiante contrasta p y b entre grupos y declara la condición de ajuste del modelo.

## Bibliografía

- Hambleton, R. K., & Jones, R. W. (1993). Comparison of classical test theory and item response theory and their applications to test development. *Educational Measurement: Issues and Practice*, 12(3), 38-47. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Lord, F. M. (1980). *Applications of Item Response Theory to Practical Testing Problems*. Lawrence Erlbaum. ⚠️ existe, pero Crossref registra 2012 (¿otra edición?; [DOI](https://doi.org/10.4324/9780203056615))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
