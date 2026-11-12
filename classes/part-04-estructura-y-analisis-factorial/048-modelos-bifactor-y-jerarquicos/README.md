# 048 — Modelos bifactor y jerárquicos

> [Índice de la parte](../README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 023 y 043.

## Objetivos

1. Distinguir el modelo bifactor del modelo jerárquico de segundo orden.
2. Calcular omega total, omega jerárquico y ECV.
3. Decidir si el puntaje total puede interpretarse como el factor general.

## Fundamentos

El modelo **bifactor** (Holzinger y Swineford, 1937; Reise, 2012) postula un factor general que afecta a todos los ítems y factores de grupo ortogonales. Con las cargas:

```
ω total  = (varianza del general + varianza de grupo) / varianza total
ω jerárquico (ωₕ) = varianza atribuible al general / varianza total
ECV = varianza común del general / varianza común total
```

Laboratorio (9 ítems; 3 grupos de 3; cargas verdaderas conocidas):

| General | Específica | ω total | ωₕ | ECV |
|---:|---:|---:|---:|---:|
| 0,7 | 0,2 | 0,906 | 0,882 | 0,925 |
| 0,5 | 0,5 | 0,857 | 0,643 | 0,500 |
| 0,3 | 0,6 | 0,775 | 0,332 | 0,200 |

Simulación del caso 0,5/0,5: r²(total, factor general) = 0,643, igual a ωₕ. La escala es fiable (ω = 0,86) pero solo ~64 % de la varianza del total es el factor general (ECV 0,50).

## Ejemplo resuelto

Caso 0,5/0,5: var_general = (9·0,5)² = 20,25; var_grupo = 3·(3·0,5)² = 6,75; var_única = 9·(1 − 0,5) = 4,5; total = 31,5. ω = 27/31,5 = 0,857; ωₕ = 20,25/31,5 = 0,643.

## Errores y límites

- Interpretar el total como «el rasgo general» con ωₕ y ECV bajos.
- Aceptar un bifactor solo por su buen ajuste: los bifactor tienden a ajustar mejor por flexibilidad (Rodriguez, Reise y Haviland, 2016).
- Usar cargas estimadas sin revisar su estabilidad (factores de grupo con cargas negativas o casi nulas).
- Las cargas aquí son las verdaderas.

## Ejercicios

- **Inicial.** ¿Qué indica un ω alto con un ωₕ bajo? → la escala es fiable pero no unidimensional.
- **Intermedio.** Calcula ωₕ con cargas 0,6/0,3, 9 ítems en 3 grupos → var_gen = 29,16; grupo = 3·(0,9)² = 2,43; única = 9·(1 − 0,45) = 4,95; total 36,54; ωₕ = 0,798.
- **Avanzado.** Cambia el número de ítems por grupo en `lab.py` y observa ECV.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/048-modelos-bifactor-y-jerarquicos/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo reportarías subpuntajes? 2. ¿Por qué el ajuste del bifactor engaña? 3. ¿Qué es ECV?
Se logra si el estudiante calcula los tres índices y decide cómo reportar el puntaje.

## Bibliografía

- Holzinger, K. J., & Swineford, F. (1937). The bi-factor method. *Psychometrika*, 2(1), 41-54. ✅ [DOI](https://doi.org/10.1007/bf02287965)
- Reise, S. P. (2012). The rediscovery of bifactor measurement models. *Multivariate Behavioral Research*, 47(5), 667-696. ✅ [DOI](https://doi.org/10.1080/00273171.2012.715555)
- Rodriguez, A., Reise, S. P., & Haviland, M. G. (2016). Evaluating bifactor models: Calculating and interpreting statistical indices. *Psychological Methods*, 21(2), 137-150. ✅ [DOI](https://doi.org/10.1037/met0000045)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
