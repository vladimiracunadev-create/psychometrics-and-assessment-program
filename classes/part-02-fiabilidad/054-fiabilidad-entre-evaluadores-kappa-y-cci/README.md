# 054 — Fiabilidad entre evaluadores: kappa y CCI

> [Índice de la parte](../README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 011, 014 y 052.

## Objetivos

1. Calcular el kappa de Cohen y explicar por qué descuenta el azar.
2. Distinguir acuerdo de consistencia con el coeficiente de correlación intraclase (CCI).
3. Declarar qué tipo de acuerdo importa para la decisión.

## Fundamentos

**Kappa** (Cohen, 1960) para categorías: κ = (pₒ − pₑ) / (1 − pₑ), donde pₑ es el acuerdo esperado por azar según las frecuencias marginales. Con una categoría muy prevalente, el acuerdo crudo es alto y κ baja (Feinstein y Cicchetti, 1990).

**CCI** para puntajes: cociente de varianzas por ANOVA de dos factores (Shrout y Fleiss, 1979). Hay variantes: *consistencia* (ignora diferencias de nivel entre jueces) y *acuerdo absoluto* (las penaliza). La elección se justifica por la decisión.

Laboratorio:

- Hallazgo raro (prevalencia 8 %), cada evaluador con 93 % de aciertos: acuerdo crudo 0,865, **κ = 0,413**.
- Dos jueces, el segundo 1,5 puntos más severo: Pearson 0,850; CCI consistencia 0,850; **CCI acuerdo absoluto 0,580**.

La correlación y el CCI de consistencia no ven la severidad diferencial; el de acuerdo absoluto sí. Para fijar «aprobado/reprobado» con un corte, esa diferencia importa.

## Ejemplo resuelto

Dos jueces clasifican 100 casos: ambos «sí» 20, ambos «no» 70, discrepan 10. pₒ = 0,90. Si cada uno dice «sí» en 25 %, pₑ = 0,25² + 0,75² = 0,625; κ = (0,90 − 0,625)/0,375 = 0,733.

## Errores y límites

- Reportar solo el porcentaje de acuerdo.
- Interpretar κ con tablas universales: las etiquetas (p. ej. Landis y Koch, 1977) son convenciones arbitrarias.
- Usar un CCI sin declarar su tipo y modelo.
- Entrenar a los jueces con los casos de evaluación inflará el acuerdo.

## Ejercicios

- **Inicial.** ¿Por qué κ puede ser bajo con 95 % de acuerdo?
- **Intermedio.** Recalcula el ejemplo con pₑ = 0,5 → κ = 0,80.
- **Avanzado.** En `lab.py` haz que el juez 2 sea 3 puntos más severo y reporta ambos CCI.

## Laboratorio

```bash
python classes/part-02-fiabilidad/054-fiabilidad-entre-evaluadores-kappa-y-cci/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo importa el acuerdo absoluto? 2. ¿Qué evalúas antes de usar rúbricas con varios jueces? 3. ¿Por qué entrenar jueces y reportar el kappa?
Se logra si el estudiante elige y reporta el índice según la decisión.

## Bibliografía

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46. ✅ [DOI](https://doi.org/10.1177/001316446002000104)
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420-428. ✅ [DOI](https://doi.org/10.1037/0033-2909.86.2.420)
- Feinstein, A. R., & Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543-549. ✅ [DOI](https://doi.org/10.1016/0895-4356(90)90159-m)
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159-174. ✅ [DOI](https://doi.org/10.2307/2529310)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
