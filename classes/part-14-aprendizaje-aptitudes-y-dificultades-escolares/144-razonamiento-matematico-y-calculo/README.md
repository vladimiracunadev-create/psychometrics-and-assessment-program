# 144 — Razonamiento matemático y cálculo

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 083 y 085.

## Objetivos

1. Controlar la dificultad de un ítem de cálculo por sus características.
2. Verificar claves con dos implementaciones.
3. Usar errores sistemáticos con fin diagnóstico.

## Fundamentos

La dificultad de un ítem de cálculo se explica en parte por propiedades observables, como el número de **reagrupaciones** (préstamos) en una resta. Los errores sistemáticos («bugs»; Brown y Burton, 1978; VanLehn, 1990) producen respuestas características que orientan la enseñanza. Distinguir cálculo, razonamiento y comprensión del enunciado es esencial en la evaluación de dificultades en matemática (Geary, 2004).

Laboratorio (600 ítems originales; algoritmo escrito verificado contra la resta de Python; probabilidades de error **supuestas**):

| Reagrupaciones | Ítems | P(error) supuesta | % error simulado |
|---:|---:|---:|---:|
| 0 | 206 | 0,05 | 6,8 % |
| 1 | 260 | 0,23 | 22,9 % |
| 2 | 134 | 0,41 | 40,2 % |

Ejemplo: 534 − 278 = 256 (2 reagrupaciones); un error típico (restar la cifra menor de la mayor) da 344.

## Ejemplo resuelto

534 − 278: unidades 4 < 8 → préstamo (14 − 8 = 6); decenas 2 < 7 → préstamo (12 − 7 = 5); centenas 4 − 2 = 2 → 256.

## Errores y límites

- Declarar la relación dificultad–reagrupaciones sin datos.
- Interpretar un solo error como «dificultad de aprendizaje».
- Mezclar fluidez de cálculo con razonamiento en un mismo puntaje.
- La enseñanza informada por errores requiere entrevistar al estudiante.

## Ejercicios

- **Inicial.** ¿Cuántas reagrupaciones tiene 305 − 168? → 2.
- **Intermedio.** Calcula la respuesta con el error típico para 83 − 47 → |8−4|·10 + |3−7| = 44.
- **Avanzado.** Agrega restas de 4 cifras al generador y verifica la clave.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/144-razonamiento-matematico-y-calculo/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo estimarías la dificultad con datos? 2. ¿Qué haces ante un error sistemático? 3. ¿Cuándo derivas a evaluación especializada?
Se logra si el estudiante genera ítems con dificultad explicada y usa errores con fin formativo.

## Bibliografía

- Brown, J. S., & Burton, R. R. (1978). Diagnostic models for procedural bugs in basic mathematical skills. *Cognitive Science*, 2(2), 155-192. ✅ [DOI](https://doi.org/10.1016/s0364-0213(78)80004-4)
- VanLehn, K. (1990). *Mind Bugs: The Origins of Procedural Misconceptions*. MIT Press. ⚠️ existe, pero Crossref registra 1991 (¿otra edición?; [DOI](https://doi.org/10.1016/0004-3702(91)90072-r))
- Geary, D. C. (2004). Mathematics and learning disabilities. *Journal of Learning Disabilities*, 37(1), 4-15. ✅ [DOI](https://doi.org/10.1177/00222194040370010201)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
