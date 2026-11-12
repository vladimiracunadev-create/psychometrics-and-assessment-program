# 040 — Amenazas a la validez: falseamiento y deseabilidad social

![Portada de la clase 040](portada.svg)

> [Índice de la parte](../README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 013, 034 y 035.

## Objetivos

1. Distinguir deseabilidad social, falseamiento intencional y estilos de respuesta.
2. Estimar el efecto del falseamiento sobre una selección.
3. Reconocer las limitaciones de las contramedidas.

## Fundamentos

En contextos de alto riesgo (selección, admisión) las personas pueden presentar una imagen favorable. **Deseabilidad social** es una tendencia general (Paulhus, 1991); **falseamiento** es un intento deliberado. Un metaanálisis de estudios de falseamiento encontró que las personas pueden elevar sus puntajes de forma notable cuando se les instruye hacerlo (Viswesvaran y Ones, 1999); lo que pasa en situaciones reales depende del contexto y se debate (Ziegler et al., 2012).

Laboratorio (escala de responsabilidad; validez verdadera 0,30; 25 % de falseadores que suman un desplazamiento aditivo; se selecciona el 10 % superior):

| Desplazamiento medio | Falseadores en el top 10 % | r con desempeño |
|---:|---:|---:|
| 0,0 | 27,2 % | 0,268 |
| 0,5 | 43,3 % | 0,263 |
| 1,0 | 61,4 % | 0,249 |
| 1,5 | 76,9 % | 0,231 |

Con 25 % de falseadores, un desplazamiento de 1,0 DE hace que ocupen más de seis de cada diez plazas del tramo superior. La validez cae poco, pero el **efecto sobre quién queda seleccionado** es grande.

## Ejemplo resuelto

Si 1 000 personas postulan a 100 cupos y el 25 % falsea con +1 DE, esperaríamos ~61 falseadores entre los 100 elegidos frente a ~25 sin falseamiento. Cambia la composición de la selección aunque r global apenas varíe.

## Errores y límites

- Interpretar un puntaje muy alto de «virtud» como rasgo y no como posible imagen.
- Eliminar a quienes puntúan alto en una escala de deseabilidad sin evidencia de que esa escala mida falseamiento y no rasgo real.
- Confiar en una sola contramedida (escalas de validez, elección forzada, advertencias).
- El modelo es un desplazamiento aditivo: simplifica.

## Ejercicios

- **Inicial.** Diferencia deseabilidad social de falseamiento.
- **Intermedio.** Con 10 % de falseadores y +1 DE, ¿esperas más o menos falseadores en el top 10 % que con 25 %? Menos.
- **Avanzado.** Modifica `PREVALENCIA` en `lab.py` y reporta el falseadores-en-top para 5 %, 10 % y 40 %.

## Laboratorio

```bash
python classes/part-03-validez/040-amenazas-a-la-validez-falseamiento-y-deseabilidad/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un efecto pequeño sobre r puede ser grande para la selección? 2. ¿Qué contramedidas existen y qué costo tiene cada una? 3. ¿Cuándo no usarías un autoinforme para decidir?
Se logra si el estudiante cuantifica el efecto y declara el límite al informar.

## Bibliografía

- Paulhus, D. L. (1991). Measurement and control of response bias. En J. P. Robinson et al. (Eds.), *Measures of Personality and Social Psychological Attitudes*. Academic Press. ✅ [DOI](https://doi.org/10.1016/b978-0-12-590241-0.50006-x)
- Viswesvaran, C., & Ones, D. S. (1999). Meta-analyses of fakability estimates. *Educational and Psychological Measurement*, 59(2), 197-210. ✅ [DOI](https://doi.org/10.1177/00131649921969802)
- Ziegler, M., MacCann, C., & Roberts, R. D. (Eds.) (2012). *New Perspectives on Faking in Personality Assessment*. Oxford University Press. ✅ [DOI](https://doi.org/10.1093/acprof:oso/9780195387476.001.0001)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
