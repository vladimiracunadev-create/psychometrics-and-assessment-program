# 075 — Rutas de certificación profesional

![Portada de la clase 075](portada.svg)

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 5 h · Estado `escrita`
**Prerrequisitos:** clases 025, 061 y 059.

## Objetivos

1. Establecer un punto de corte con un procedimiento Angoff modificado.
2. Estimar el error del corte y la consistencia de clasificación.
3. Describir qué documentación hace defendible una certificación.

## Fundamentos

Una certificación decide si alguien alcanza un estándar mínimo. El punto de corte no es un hecho: se **establece** por un procedimiento (Angoff, 1971; Cizek y Bunch, 2007). En Angoff modificado, cada juez estima para cada ítem la probabilidad de que una persona «mínimamente competente» lo acierte; el corte es la suma de las medias de los jueces. La **consistencia de clasificación** (Livingston y Lewis, 1995) indica cuántas decisiones se repetirían con otra forma del examen.

Laboratorio (12 jueces, 30 ítems, 8 000 candidatos sintéticos):

| Medida | Valor |
|---|---:|
| Corte | 15,9 de 30 |
| DE entre jueces / error típico del corte | 1,57 / 0,45 |
| Tasa de aprobados | 0,650 |
| Consistencia de clasificación entre formas paralelas | 0,867 |
| Candidatos a menos de ~4 puntos del corte | 38 % |

## Ejemplo resuelto

Tres jueces estiman 0,6; 0,7; 0,8 para un ítem: media 0,70; ese ítem aporta 0,70 al corte. Con 30 ítems semejantes, el corte sería 21.

## Errores y límites

- Presentar el corte como «el nivel de competencia».
- Usar un único juez o jueces sin entrenamiento.
- Ignorar la zona de incertidumbre alrededor del corte (revisión, repetición).
- Los datos son sintéticos; una certificación real documenta jueces, procedimiento, normas y vías de apelación.

## Ejercicios

- **Inicial.** ¿Qué es una «persona mínimamente competente»?
- **Intermedio.** Calcula el corte con 4 ítems de medias 0,5; 0,6; 0,7; 0,9 → 2,7.
- **Avanzado.** Reduce el número de jueces a 5 en `lab.py` y observa el error del corte.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/075-certificacion-profesional/lab.py
```

## Autoevaluación y criterios

1. ¿Qué documentarías sobre los jueces? 2. ¿Cómo manejas a quienes quedan cerca del corte? 3. ¿Qué otras rutas (portafolio, práctica supervisada) complementan un examen?
Se logra si el estudiante fija un corte, estima su error y lo documenta.

## Bibliografía

- Angoff, W. H. (1971). Scales, norms, and equivalent scores. En R. L. Thorndike (Ed.), *Educational Measurement* (2.ª ed.). American Council on Education. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Cizek, G. J., & Bunch, M. B. (2007). *Standard Setting: A Guide to Establishing and Evaluating Performance Standards on Tests*. Sage. ⚠️ existe, pero Crossref registra 2010 (¿otra edición?; [DOI](https://doi.org/10.1111/j.1745-3984.2010.00126.x))
- Livingston, S. A., & Lewis, C. (1995). Estimating the consistency and accuracy of classifications based on test scores. *Journal of Educational Measurement*, 32(2), 179-197. ✅ [DOI](https://doi.org/10.1111/j.1745-3984.1995.tb00462.x)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
