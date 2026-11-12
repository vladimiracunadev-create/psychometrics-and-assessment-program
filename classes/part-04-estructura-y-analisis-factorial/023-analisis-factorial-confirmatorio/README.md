# 023 — Análisis factorial confirmatorio y ajuste

> [Índice de la parte](../README.md) · [Anterior](../022-analisis-factorial-exploratorio/README.md) · [Siguiente](../024-modelos-circumplejos/README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 022 y 013.

## Objetivos

1. Distinguir AFC de AFE: el modelo se fija antes de ver los datos.
2. Explicar el ajuste como comparación entre la matriz observada y la implicada por el modelo.
3. Reconocer el riesgo de reajustar el modelo hasta que ajuste.

## Fundamentos

En el AFC se declara qué ítems cargan en qué factor (el resto de cargas se fija en 0) y se evalúa cuánto se parece la matriz que implica el modelo a la observada. Los **residuos** (observada − implicada) son la información más concreta sobre dónde falla. El **SRMR** resume la raíz del promedio de residuos cuadrados; una guía citada es < 0,08 (Hu y Bentler, 1999), que no es un veredicto.

**Aclaración honesta:** el laboratorio NO es un AFC por máxima verosimilitud; ajusta un factor por ejes principales y mide el desajuste con SRMR, para mostrar la lógica del residuo (el AFC real se hace con lavaan, semopy, Mplus, etc.).

| Datos generados por | SRMR del modelo de 1 factor |
|---|---:|
| 1 factor (modelo correcto) | 0,016 |
| 2 factores (mal especificado) | 0,198 |

## Ejemplo resuelto

Residuos 0,10; −0,10; 0,05: SRMR = √((0,01 + 0,01 + 0,0025)/3) = 0,087 → por encima de 0,08, miramos qué residuo domina.

## Errores y límites

- Modificar el modelo con índices de modificación hasta que ajuste: el AFC pasa a ser exploratorio y capitaliza el azar (MacCallum et al., 1992).
- Presentar un buen ajuste como prueba de que el modelo es verdadero: modelos distintos pueden ajustar igual.
- Usar umbrales fijos de ajuste para todo modelo y muestra.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre AFE y AFC en la especificación?
- **Intermedio.** Calcula el SRMR con residuos 0,04; −0,04; 0,02; −0,02 → √((0,0016 + 0,0016 + 0,0004 + 0,0004)/4) = 0,032.
- **Avanzado.** En `lab.py` genera datos con cargas cruzadas pequeñas y observa el SRMR.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/023-analisis-factorial-confirmatorio/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué los residuos informan más que un índice resumen? 2. ¿Qué es capitalizar el azar? 3. ¿Cuándo es legítimo modificar un modelo?
Se logra si el estudiante fija un modelo de antemano y evalúa su ajuste con residuos.

## Bibliografía

- Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis. *Structural Equation Modeling*, 6(1), 1-55.
- MacCallum, R. C., Roznowski, M., & Necowitz, L. B. (1992). Model modifications in covariance structure analysis: The problem of capitalization on chance. *Psychological Bulletin*, 111(3), 490-504.
- Brown, T. A. (2015). *Confirmatory Factor Analysis for Applied Research* (2.ª ed.). Guilford.
