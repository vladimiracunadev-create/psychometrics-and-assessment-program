# 019 — Juicio de expertos y revisión cognitiva de ítems

> [Índice de la parte](../README.md)

**Parte 01 — Construcción de instrumentos** · Nivel introductorio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 018.

## Objetivos

1. Calcular I-CVI y kappa modificado.
2. Combinar el juicio de expertos con entrevistas cognitivas.
3. Decidir conservar, revisar o reescribir.

## Fundamentos

El I-CVI es la proporción de expertos que califican el ítem como relevante; el kappa modificado k* = (I-CVI − Pc) / (1 − Pc), con Pc = C(N, A) × 0,5^N, descuenta el acuerdo esperado por azar (Polit et al., 2007). Las entrevistas cognitivas revelan cómo la población objetivo entiende el ítem.

Laboratorio (8 expertos, 12 entrevistados, 10 ítems sintéticos): los ítems 3, 4 y 6 se marcan por ambigüedad (67 %, 42 % y 58 % lo interpreta distinto) y los ítems 4, 6, 7 y 9 por relevancia (I-CVI < 0,78).

## Ejemplo resuelto

Un ítem puede ser relevante y ambiguo (ítem 3: I-CVI 1,00 y 67 % de interpretaciones distintas): los expertos no habrían detectado el problema.

## Errores y límites

- Usar solo expertos.
- Tratar el umbral 0,78 como regla universal.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué corrige el kappa modificado?
- **Intermedio.** Cambia a 6 expertos y observa los umbrales.
- **Avanzado.** Diseña la guía de una entrevista cognitiva con parafraseo.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/019-juicio-de-expertos-y-revision-cognitiva-de/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del resultado depende de que los datos sean sintéticos? 2. ¿Qué cambiaría con personas reales? 3. ¿Qué límite declararías?
Se logra si el estudiante ejecuta el laboratorio, interpreta las cifras con cautela y declara sus límites.

## Bibliografía

- Polit, D. F., Beck, C. T., & Owen, S. V. (2007). Is the CVI an acceptable indicator of content validity? *Research in Nursing & Health*, 30(4), 459-467. ✅ [DOI](https://doi.org/10.1002/nur.20199)
- Willis, G. B. (2005). *Cognitive Interviewing*. Sage. ✅ [DOI](https://doi.org/10.4135/9781412983655)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
