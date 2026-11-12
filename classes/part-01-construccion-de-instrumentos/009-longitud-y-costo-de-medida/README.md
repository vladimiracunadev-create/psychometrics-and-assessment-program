# 009 — Longitud del test: el intercambio entre precisión y abandono

> [Clase anterior](../008-ipsativo-vs-normativo/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../010-pilotaje-y-analisis-de-items/README.md)

**Parte:** 01 — Construcción de instrumentos
**Nivel:** fundamentos · **Horas estimadas:** 3 · **Estado:** `escrita`
**Prerrequisitos:** clases 004 y 007. Se anticipa la fiabilidad (parte 02).

## Propósito

Responder cuántos ítems hacen falta, con una fórmula y no con una intuición, y
mostrar por qué agregar ítems tiene rendimientos decrecientes.

## Resultados de aprendizaje

1. Aplicar la fórmula de Spearman-Brown directa e inversa.
2. Leer el alfa como función de la longitud y de la correlación entre ítems.
3. Decidir una longitud con criterios técnicos y de carga para el evaluado.

## Fundamentos

Si cada ítem tiene fiabilidad *r₁* (correlación con un ítem paralelo), la
fiabilidad de una escala de *k* ítems paralelos es

```
rₖ = k · r₁ / (1 + (k − 1) · r₁)          (Spearman, 1910; Brown, 1910)
```

y el número de ítems necesarios para alcanzar una fiabilidad objetivo *ρ* es

```
k = ρ · (1 − r₁) / ( r₁ · (1 − ρ) )
```

### Ejemplo con r₁ = 0,25

| Ítems | Predicha | Alfa simulado |
|---:|---:|---:|
| 2 | 0,400 | 0,405 |
| 5 | 0,625 | 0,612 |
| 10 | 0,769 | 0,762 |
| 20 | 0,870 | 0,865 |
| 40 | 0,930 | 0,928 |

Para 0,80 bastan 12 ítems; para 0,90 hacen falta 27. Pasar de 20 a 40 ítems suma
solo 0,06 de fiabilidad y duplica el tiempo de respuesta.

### El otro lado: costo

Cada ítem adicional aumenta cansancio, respuestas apresuradas y abandono. La
fórmula asume ítems **paralelos**; ítems poco relacionados con el constructo no
suben la fiabilidad como predice. Por eso las formas cortas se construyen
eligiendo los ítems más discriminantes (clase 010) y no recortando al azar.

## Ejemplo resuelto

Un cribado de 6 ítems con r₁ = 0,30: r₆ = 6·0,30/(1+5·0,30) = 1,8/2,5 = 0,72. Para llegar a 0,80 harían falta k = 0,80·0,70/(0,30·0,20) = 9,3 → 10 ítems.

## Errores frecuentes

- Afirmar que «más ítems, mejor» sin mirar la ganancia marginal.
- Aplicar Spearman-Brown a ítems heterogéneos.
- Confundir fiabilidad alta con validez alta.

## Limitaciones

Los datos son simulados con errores independientes y normales. En datos reales la
fiabilidad depende de la muestra, y alfa subestima o sobreestima según la
estructura (clase 013).

## Ejercicios

- **Inicial.** Calcula r₄ con r₁ = 0,40. (0,727)
- **Intermedio.** ¿Cuántos ítems para 0,85 con r₁ = 0,30? (≈ 14; la fórmula da 13,2)
- **Avanzado.** Cambia `VARIANZA_ERROR` en `lab.py` y encuentra cuándo 40 ítems no alcanzan 0,90.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/009-longitud-y-costo-de-medida/lab.py
```

## Autoevaluación

1. ¿Por qué la ganancia de fiabilidad decrece con *k*?
2. ¿Qué supuesto falla cuando los ítems no son paralelos?
3. ¿Cuándo preferirías una forma corta a una larga aunque pierdas fiabilidad?

## Criterios de evaluación

El estudiante calcula longitudes objetivo y justifica el equilibrio fiabilidad-carga.

## Bibliografía

- Spearman, C. (1910). Correlation calculated from faulty data. *British Journal of Psychology*, 3, 271-295. ✅ [DOI](https://doi.org/10.1111/j.2044-8295.1910.tb00206.x)
- Brown, W. (1910). Some experimental results in the correlation of mental abilities. *British Journal of Psychology*, 3, 296-322. ✅ [DOI](https://doi.org/10.1111/j.2044-8295.1910.tb00207.x)
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16, 297-334. ✅ [DOI](https://doi.org/10.1007/bf02310555)
- Rammstedt, B., & John, O. P. (2007). Measuring personality in one minute or less. *Journal of Research in Personality*, 41(1), 203-212. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
