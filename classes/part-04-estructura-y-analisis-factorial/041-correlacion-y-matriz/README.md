# 041 — Correlación, matriz y lo que se puede leer en ella

![Portada de la clase 041](portada.svg)

<!-- NAV -->
[← 040 — Amenazas a la validez: falseamiento y deseabi…](../../part-03-validez/040-amenazas-a-la-validez-falseamiento-y-deseabilidad/README.md) · [📚 Parte 04](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [042 — Análisis factorial exploratorio →](../042-analisis-factorial-exploratorio/README.md)
<!-- /NAV -->

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 027 y 022.

## Objetivos

1. Leer una matriz de correlaciones: bloques, magnitudes y signos.
2. Calcular autovalores y relacionarlos con la estructura.
3. Aplicar dos comprobaciones previas: determinante y KMO.

## Fundamentos

Todo análisis factorial parte de la matriz de correlaciones R entre ítems. Si no hay correlaciones compartidas, no hay nada que factorizar. Los **autovalores** de R suman el número de ítems; un autovalor grande indica una dirección de covariación común. El **determinante** cercano a 0 señala multicolinealidad (ítems casi duplicados). El **KMO** (Kaiser, 1974) compara correlaciones con correlaciones parciales: valores cercanos a 1 indican que las correlaciones se explican por factores comunes.

Laboratorio (6 ítems: 1–3 miden A, 4–6 miden B; factores correlacionados 0,3; N = 2 000):

| Medida | Valor |
|---|---:|
| Correlación media dentro de bloque | 0,466 |
| Correlación media entre bloques | 0,163 |
| Autovalores | 2,42; 1,44; 0,56; 0,54; 0,53; 0,51 |
| Determinante | 0,282 |
| KMO global | 0,727 |

La estructura en dos bloques se ve a simple vista y en los dos autovalores sobre 1.

## Ejemplo resuelto

Matriz [[1; 0,5]; [0,5; 1]]: autovalores 1 + 0,5 = 1,5 y 1 − 0,5 = 0,5 (suman 2 = número de ítems). El primero explica 75 % de la varianza total.

## Errores y límites

- Factorizar sin mirar la matriz.
- Interpretar el KMO como prueba de unidimensionalidad.
- Ignorar ítems con correlaciones casi nulas con todos (no pertenecen a la escala).
- Con ítems ordinales de pocas categorías, la matriz de Pearson subestima (clase 050).

## Ejercicios

- **Inicial.** ¿Qué suma dan los autovalores de una matriz de correlaciones 10 × 10? → 10.
- **Intermedio.** Autovalores de [[1; 0,3]; [0,3; 1]] → 1,3 y 0,7.
- **Avanzado.** Aumenta a 0,7 la correlación entre factores en `lab.py` y describe los autovalores.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/041-correlacion-y-matriz/lab.py
```

## Autoevaluación y criterios

1. ¿Qué significa un determinante de 0,001? 2. ¿Por qué un KMO bajo desaconseja factorizar? 3. ¿Qué dos bloques ves y qué predice la teoría?
Se logra si el estudiante lee la estructura de una matriz y decide si procede factorizar.

## Bibliografía

- Kaiser, H. F. (1974). An index of factorial simplicity. *Psychometrika*, 39(1), 31-36. ✅ [DOI](https://doi.org/10.1007/bf02291575)
- Fabrigar, L. R., & Wegener, D. T. (2012). *Exploratory Factor Analysis*. Oxford University Press. ✅ [DOI](https://doi.org/10.1093/acprof:osobl/9780199734177.001.0001)
- Brown, T. A. (2015). *Confirmatory Factor Analysis for Applied Research* (2.ª ed.). Guilford. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 040 — Amenazas a la validez: falseamiento y deseabi…](../../part-03-validez/040-amenazas-a-la-validez-falseamiento-y-deseabilidad/README.md)  
[📚 Parte 04](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[042 — Análisis factorial exploratorio →](../042-analisis-factorial-exploratorio/README.md)
<!-- /NAV -->
