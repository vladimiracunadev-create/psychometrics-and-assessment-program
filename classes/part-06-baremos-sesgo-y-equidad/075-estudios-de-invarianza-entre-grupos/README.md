# 075 — Estudios de invarianza entre grupos

> [Índice de la parte](../README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 025 y 062.

## Objetivos

1. Planificar una secuencia de modelos configural, métrico y escalar.
2. Aplicar criterios de decisión basados en el cambio del CFI.
3. Cuantificar el efecto de la no invarianza sobre la comparación de medias.

## Fundamentos

Secuencia habitual (Byrne, Shavelson y Muthén, 1989): se ajusta el modelo configural y luego se agregan restricciones de igualdad de cargas (métrico) e interceptos (escalar). Cheung y Rensvold (2002) sugieren aceptar la restricción si ΔCFI ≤ 0,01 (una guía, no una ley; Putnick y Bornstein, 2016). Si falla la invarianza escalar, la **invarianza parcial** libera los parámetros no invariantes y compara medias con los ítems invariantes restantes, siempre que sean suficientes y haya razón sustantiva.

Laboratorio (10 ítems, mismo rasgo medio en ambos grupos; interceptos desplazados en el grupo B):

| Ítems con desplazamiento | Desplazamiento | d (todos los ítems) | d (solo invariantes) |
|---:|---:|---:|---:|
| 0 | 0,0 | −0,02 | −0,01 |
| 1 | 0,6 | 0,05 | −0,03 |
| 3 | 0,6 | 0,22 | −0,02 |
| 5 | 0,6 | 0,38 | −0,03 |
| 3 | 1,2 | 0,48 | −0,01 |

Con cinco ítems desplazados aparece una «diferencia de grupos» de 0,38 DE que es puro artefacto del instrumento.

## Ejemplo resuelto

ΔCFI entre configural (0,962) y métrico (0,958) = 0,004 ≤ 0,01: se acepta la invarianza métrica. Entre métrico y escalar (0,940), ΔCFI = 0,018 > 0,01: se examina qué interceptos liberar (valores ilustrativos).

## Errores y límites

- Liberar parámetros hasta que ajuste sin justificación sustantiva.
- Comparar medias con muy pocos ítems invariantes.
- Aplicar el umbral ΔCFI mecánicamente con muestras pequeñas o modelos complejos.
- El laboratorio conoce cuáles ítems están desplazados; en la práctica se descubren con el modelo.

## Ejercicios

- **Inicial.** ¿Qué nivel de invarianza permite comparar medias?
- **Intermedio.** Si 4 de 10 ítems no son invariantes, ¿qué riesgos hay con la invarianza parcial?
- **Avanzado.** En `lab.py` desplaza un ítem a +2,0 y compara d con y sin él.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/075-estudios-de-invarianza-entre-grupos/lab.py
```

## Autoevaluación y criterios

1. ¿Cuántos ítems invariantes se necesitan? 2. ¿Qué reportarías en un artículo? 3. ¿Qué haces si no hay invarianza escalar?
Se logra si el estudiante planifica la secuencia y estima el sesgo de comparación.

## Bibliografía

- Byrne, B. M., Shavelson, R. J., & Muthén, B. (1989). Testing for the equivalence of factor covariance and mean structures. *Psychological Bulletin*, 105(3), 456-466. ✅ [DOI](https://doi.org/10.1037/0033-2909.105.3.456)
- Cheung, G. W., & Rensvold, R. B. (2002). Evaluating goodness-of-fit indexes for testing measurement invariance. *Structural Equation Modeling*, 9(2), 233-255. ✅ [DOI](https://doi.org/10.1207/s15328007sem0902_5)
- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *Developmental Review*, 41, 71-90. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
