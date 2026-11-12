# 056 — Validez convergente y discriminante: la matriz multirrasgo-multimétodo

> [Índice de la parte](../README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 018 y 052.

## Objetivos

1. Leer una matriz multirrasgo-multimétodo (MRMM).
2. Aplicar los criterios de Campbell y Fiske.
3. Diagnosticar dominancia del método.

## Fundamentos

Campbell y Fiske (1959) propusieron medir varios rasgos con varios métodos. En la matriz aparecen tres tipos de correlación:

- **Validez** (mismo rasgo, distinto método): deben ser altas.
- **Heterorrasgo-heterométodo:** deben ser bajas.
- **Heterorrasgo-monométodo:** si superan a las de validez, domina el método.

Laboratorio (3 rasgos × 2 métodos; rasgos correlacionados 0,2 entre sí):

| Condición | Validez | Hetero-mono | Hetero-hetero | Criterio 3 |
|---|---:|---:|---:|---|
| Poco método (0,2) | 0,630 | 0,167 | 0,115 | cumple |
| Mucho método (1,0) | 0,288 | 0,632 | 0,064 | **no cumple** |

Con mucho método común, rasgos **distintos** medidos con el mismo formato correlacionan más que el **mismo** rasgo medido con formatos distintos: se está midiendo el formato.

## Ejemplo resuelto

Autoinforme y juicio de un colega sobre responsabilidad y sociabilidad: r(resp-auto, resp-colega) = 0,40; r(resp-auto, soc-auto) = 0,55. El criterio 3 falla: se sospecha estilo de respuesta o deseabilidad en el autoinforme.

## Errores y límites

- Usar un solo método y llamar al resultado «validez discriminante».
- Interpretar los criterios como pruebas estadísticas formales: son comparaciones descriptivas; hoy se modelan con modelos factoriales de rasgo-método.
- Elegir métodos que comparten sesgo (autoinforme y diario autoinformado).

## Ejercicios

- **Inicial.** ¿Qué tipo de correlación es la de dos cuestionarios distintos sobre ansiedad?
- **Intermedio.** Si validez = 0,45 y hetero-mono = 0,50, ¿qué sospechas? Dominancia del método.
- **Avanzado.** Añade un tercer método a `lab.py` y verifica si el criterio 3 se recupera.

## Laboratorio

```bash
python classes/part-03-validez/056-validez-convergente-y-discriminante-matriz-multirrasgo-multimetodo/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se necesita más de un método? 2. ¿Qué indica el criterio 3? 3. ¿Cómo lo abordarías con modelos factoriales?
Se logra si el estudiante lee una MRMM y diagnostica el método.

## Bibliografía

- Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin*, 56(2), 81-105. ✅ [DOI](https://doi.org/10.1037/h0046016)
- Podsakoff, P. M., et al. (2003). Common method biases in behavioral research. *Journal of Applied Psychology*, 88(5), 879-903. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
