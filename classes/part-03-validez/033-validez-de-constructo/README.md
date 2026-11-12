# 033 — Validez de constructo: convergente y discriminante

![Portada de la clase 033](portada.svg)

> [Índice de la parte](../README.md) · [Anterior](../032-validez-de-contenido/README.md) · [Siguiente](../034-validez-de-criterio/README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 031 y 027.

## Objetivos

1. Formular predicciones teóricas de correlación antes de mirar los datos.
2. Distinguir evidencia convergente y discriminante.
3. Reconocer cómo la varianza de método compartida distorsiona el patrón.

## Fundamentos

Cronbach y Meehl (1955) plantearon que un constructo se apoya en una **red nomológica**: predicciones sobre cómo se relaciona con otras variables. La validez de constructo se acumula contrastando ese patrón. **Convergente:** medidas del mismo constructo correlacionan alto. **Discriminante:** medidas de constructos distintos correlacionan menos (Campbell y Fiske, 1959).

Laboratorio: A y B miden X; C mide otro constructo con r verdadera 0,30 con X.

| Condición | r(A,B) convergente | r(A,C) | r(B,C) |
|---|---:|---:|---:|
| Sin varianza de método compartida | 0,744 | 0,211 | 0,212 |
| A y C comparten formato | 0,637 | 0,421 | 0,181 |

Con método compartido r(A,C) se infla frente a r(B,C): parte de la «relación entre constructos» es relación entre formatos.

## Ejemplo resuelto

Se propone que «perseverancia» correlaciona 0,5 con «responsabilidad» y ~0 con «inteligencia fluida». Se observa 0,48 y 0,05 → el patrón respalda la hipótesis. Si se observara 0,05 y 0,48, el patrón la refuta, aun con buenos coeficientes de fiabilidad.

## Errores y límites

- Reportar una sola correlación como «validez de constructo».
- Formular las predicciones después de ver los datos.
- No distinguir correlaciones por método compartido de relaciones sustantivas.
- Un patrón compatible no demuestra el constructo: lo hace más plausible.

## Ejercicios

- **Inicial.** Da un par de constructos para los cuales esperarías evidencia discriminante.
- **Intermedio.** Si r(A,B) = 0,45 y la fiabilidad de A y B es 0,8, ¿cuál es la r corregida? → 0,45/0,8 = 0,56.
- **Avanzado.** Cambia el peso del método en `lab.py` y grafica r(A,C) en función de él.

## Laboratorio

```bash
python classes/part-03-validez/033-validez-de-constructo/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se escriben las predicciones antes? 2. ¿Qué es varianza de método? 3. ¿Qué evidencia refutaría la hipótesis?
Se logra si el estudiante plantea predicciones y las contrasta con un patrón.

## Bibliografía

- Cronbach, L. J., & Meehl, P. E. (1955). Construct validity in psychological tests. *Psychological Bulletin*, 52(4), 281-302. ✅ [DOI](https://doi.org/10.1037/h0040957)
- Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin*, 56(2), 81-105. ✅ [DOI](https://doi.org/10.1037/h0046016)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
