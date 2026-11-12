# 068 — Equidad en evaluaciones de alto impacto

> [Índice de la parte](../README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 034, 035 y 064.

## Objetivos

1. Calcular validez y diferencia de grupos de un compuesto de predictores.
2. Cuantificar el compromiso entre validez e impacto adverso.
3. Declarar los supuestos de un análisis de ponderación.

## Fundamentos

Las evaluaciones de alto impacto (selección, admisión) enfrentan el **dilema diversidad-validez** (Pyburn, Ployhart y Kravitz, 2008; Ployhart y Holtz, 2008): los predictores más válidos a veces muestran mayores diferencias entre grupos. Para un compuesto estandarizado de dos predictores con pesos w₁, w₂ e intercorrelación r:

```
sd = √(w₁² + w₂² + 2 w₁ w₂ r)      validez = (w₁ v₁ + w₂ v₂) / sd      d = (w₁ d₁ + w₂ d₂) / sd
```

(Sackett y Ellingson, 1997). Supuestos del laboratorio, **ilustrativos**: P1 validez 0,50, d = 1,0; P2 validez 0,30, d = 0,2; r = 0,20; selección del 20 % superior del grupo mayoritario.

| Peso P1 | Validez | d compuesto | Tasa minoría | Razón |
|---:|---:|---:|---:|---:|
| 1,0 | 0,500 | 1,000 | 0,033 | 0,16 |
| 0,6 | 0,535 | 0,866 | 0,044 | 0,22 |
| 0,4 | 0,484 | 0,663 | 0,066 | 0,33 |
| 0,0 | 0,300 | 0,200 | 0,149 | 0,74 |

Bajar el peso del predictor con mayor d reduce el impacto adverso, y tras cierto punto reduce la validez.

## Ejemplo resuelto

w₁ = w₂ = 0,5: sd = √(0,25 + 0,25 + 0,1) = 0,775; validez = (0,25 + 0,15)/0,775 = 0,516; d = (0,5 + 0,1)/0,775 = 0,775.

## Errores y límites

- Tratar los números del laboratorio como valores del mundo real: dependen de la población y del puesto.
- Optimizar solo validez o solo diversidad sin explicitar el valor de cada una.
- Omitir alternativas: cambiar el método (p. ej. entrevista estructurada, muestras de trabajo), ampliar el reclutamiento o revisar el criterio.
- Una estrategia de ponderación debe ser justificable y auditable.

## Ejercicios

- **Inicial.** ¿Qué es el dilema diversidad-validez?
- **Intermedio.** Calcula la validez para w₁ = 0,2, w₂ = 0,8 → sd = √(0,04 + 0,64 + 0,064) = 0,863; (0,10 + 0,24)/0,863 = 0,394.
- **Avanzado.** Cambia r a 0,5 y describe qué ocurre con la validez del compuesto.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/068-equidad-en-evaluaciones-de-alto-impacto/lab.py
```

## Autoevaluación y criterios

1. ¿Quién decide cuánta validez se sacrifica? 2. ¿Qué alternativas al re-ponderar existen? 3. ¿Qué evidencia local necesitas?
Se logra si el estudiante calcula el compromiso y declara los supuestos y valores involucrados.

## Bibliografía

- Sackett, P. R., & Ellingson, J. E. (1997). The effects of forming multi-predictor composites on group differences and adverse impact. *Personnel Psychology*, 50(3), 707-721. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.1997.tb00711.x)
- Pyburn, K. M., Ployhart, R. E., & Kravitz, D. A. (2008). The diversity-validity dilemma: Overview and legal context. *Personnel Psychology*, 61(1), 143-151. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.2008.00108.x)
- Ployhart, R. E., & Holtz, B. C. (2008). The diversity-validity dilemma: Strategies for reducing racioethnic and sex subgroup differences and adverse impact in selection. *Personnel Psychology*, 61(1), 153-172. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.2008.00109.x)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
