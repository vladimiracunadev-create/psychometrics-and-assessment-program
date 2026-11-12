# 034 — Validez de criterio y validez predictiva

> [Índice de la parte](../README.md) · [Anterior](../033-validez-de-constructo/README.md) · [Siguiente](../035-consecuencias-del-uso/README.md)

**Parte 03 — Validez** · Nivel intermedio · 5 h · Estado `escrita`
**Prerrequisitos:** clases 031 y 027.

## Objetivos

1. Distinguir validez concurrente de predictiva.
2. Explicar la restricción de rango y aplicar la corrección de Thorndike (Caso II).
3. Traducir un coeficiente de validez a una tasa de acierto de selección.

## Fundamentos

La validez de criterio es la relación entre el puntaje y una variable externa (desempeño, notas). **Concurrente:** ambas se miden al mismo tiempo. **Predictiva:** el criterio se mide después.

Problema típico: el desempeño solo se observa en quienes fueron seleccionados. La correlación en esa muestra restringida subestima la de la población de postulantes. Para restricción directa en el predictor (Caso II de Thorndike; Sackett y Yang, 2000):

```
r_corr = r·u / √(1 + r²(u² − 1))        u = DE sin restringir / DE restringida
```

Laboratorio (validez verdadera 0,40; se contrata al 30 % superior):

- correlación observada solo en contratados: **0,216**;
- corregida (u = 1,94): **0,395**.

Tasa de buen desempeño entre los contratados según la validez del test:

| Validez | Tasa |
|---:|---:|
| 0,0 | 0,498 |
| 0,2 | 0,592 |
| 0,4 | 0,685 |
| 0,6 | 0,793 |

Sin validez, la selección rinde azar (0,50). Con 0,40, la mejora es real pero acotada.

## Ejemplo resuelto

r observada 0,25 y u = 1,5: r_corr = 0,25·1,5 / √(1 + 0,0625·1,25) = 0,375/1,0384 = 0,361.

## Errores y límites

- Usar la validez observada en contratados como si fuera la de los postulantes.
- Aplicar la corrección cuando la selección no fue por el predictor (otro caso, otra fórmula).
- Ignorar la fiabilidad del criterio: un criterio ruidoso reduce la validez observada.
- Los valores de validez de la literatura de selección (p. ej. Schmidt y Hunter, 1998) son promedios metaanalíticos; no se transfieren automáticamente a un puesto específico.

## Ejercicios

- **Inicial.** ¿Qué tipo de validez de criterio es un estudio donde se aplica el test y 6 meses después se obtienen notas?
- **Intermedio.** r = 0,20, u = 2: r_corr = 0,4/√(1+0,04·3) = 0,378.
- **Avanzado.** En `lab.py` contrata solo al 10 % superior y compara la r observada con la corregida.

## Laboratorio

```bash
python classes/part-03-validez/034-validez-de-criterio/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué la validez observada subestima? 2. ¿Qué supuesto exige la corrección? 3. ¿Qué cambia si el criterio es poco fiable?
Se logra si el estudiante aplica la corrección y traduce la validez a decisiones.

## Bibliografía

- Sackett, P. R., & Yang, H. (2000). Correction for range restriction: An expanded typology. *Journal of Applied Psychology*, 85(1), 112-118. ✅ [DOI](https://doi.org/10.1037/0021-9010.85.1.112)
- Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology. *Psychological Bulletin*, 124(2), 262-274. ✅ [DOI](https://doi.org/10.1037/0033-2909.124.2.262)
- Thorndike, R. L. (1949). *Personnel Selection*. Wiley. ⚠️ existe, pero Crossref registra 2015 (¿otra edición?; [DOI](https://doi.org/10.1002/9781118785317.weom050103))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
