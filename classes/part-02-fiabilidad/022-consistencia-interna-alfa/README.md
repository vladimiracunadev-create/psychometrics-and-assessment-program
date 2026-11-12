# 022 — Consistencia interna: alfa de Cronbach y sus abusos

> [Índice de la parte](../README.md) · [Anterior](../021-teoria-clasica-del-error/README.md) · [Siguiente](../023-omega-y-alternativas-a-alfa/README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 5 h · Estado `escrita`
**Prerrequisitos:** clases 014 y 021.

## Objetivos

1. Calcular alfa desde varianzas de ítems y del total.
2. Explicar qué supone alfa y qué no demuestra.
3. Usar «alfa si se elimina el ítem» sin mecanizar la decisión.
4. Reportar alfa con su contexto (muestra, número de ítems, intervalo).

## Fundamentos

```
α = k/(k−1) · ( 1 − Σ var(ítemᵢ) / var(total) )
```

Cronbach (1951) lo presentó como el promedio de todas las particiones por mitades. Es un **límite inferior** de la fiabilidad bajo supuestos (tau-equivalencia, errores no correlacionados) y sube con la correlación entre ítems **y con su número** (clase 014).

### Lo que alfa no demuestra

Doce ítems en tres escenarios (laboratorio):

| Escenario | α |
|---|---:|
| A. Unidimensional | 0,868 |
| B. Dos dimensiones independientes (6 + 6) | 0,779 |
| C. Unidimensional con un ítem de ruido | 0,836 |

**B mezcla dos constructos sin relación y aun así da un alfa que muchos manuales llaman «aceptable».** Alfa mide covarianza media, no estructura (Sijtsma, 2009); la estructura la examina el análisis factorial (parte 04). En C, quitar el ítem 12 sube alfa de 0,836 a 0,861 y señala al ítem de ruido; es una alerta, no una orden: un ítem que baja alfa puede ser necesario para cubrir el contenido (clase 032).

El umbral «0,70» es una convención, no una ley. Alfa > 0,95 puede indicar ítems redundantes.

## Ejemplo resuelto

Cuatro ítems de varianza 1 y varianza total 7: α = 4/3 · (1 − 4/7) = 0,571.

## Errores y límites

- Calcular alfa sobre una escala multidimensional y reportarlo como «fiabilidad del test».
- Olvidar reflejar los ítems invertidos antes de calcular (clase 005): da alfas bajos o negativos.
- Eliminar ítems hasta «maximizar» alfa.
- Alfa subestima si las cargas difieren (clase 023) y sobreestima si hay errores correlacionados; no cubre estabilidad temporal (clase 024).

## Ejercicios

- **Inicial.** ¿Qué pasa con α si se duplican ítems paralelos? → sube (Spearman-Brown, clase 014).
- **Intermedio.** k = 5, Σvar = 5, var(total) = 15: α = 5/4 · (1 − 5/15) = 0,833.
- **Avanzado.** Agrega a `lab.py` un escenario de tres dimensiones y compáralo con B.

## Laboratorio

```bash
python classes/part-02-fiabilidad/022-consistencia-interna-alfa/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un alfa alto no prueba unidimensionalidad? 2. ¿Qué dos factores, además de la calidad, hacen subir alfa? 3. ¿Cuándo conservarías un ítem que baja alfa?
Se logra si el estudiante calcula e interpreta alfa y redacta un reporte con sus límites.

## Bibliografía

- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16, 297-334. ✅ [DOI](https://doi.org/10.1007/bf02310555)
- Sijtsma, K. (2009). On the use, the misuse, and the very limited usefulness of Cronbach's alpha. *Psychometrika*, 74(1), 107-120. ✅ [DOI](https://doi.org/10.1007/s11336-008-9101-0)
- Tavakol, M., & Dennick, R. (2011). Making sense of Cronbach's alpha. *International Journal of Medical Education*, 2, 53-55. ✅ [DOI](https://doi.org/10.5116/ijme.4dfb.8dfd)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
