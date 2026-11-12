# 026 — Estadística descriptiva aplicada a puntajes

![Portada de la clase 026](portada.svg)

> [Índice de la parte](../README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 004 y 021.

## Objetivos

1. Describir un puntaje total con media, DE, asimetría, curtosis y efectos de suelo y techo.
2. Reconocer cuándo la forma de la distribución limita la discriminación y la fiabilidad.
3. Elegir resúmenes adecuados al nivel de medida (clase 003).

## Fundamentos

Antes de calcular fiabilidad o validez se mira la distribución. Un puntaje total de ítems Likert es una suma de variables ordinales: no es exactamente continuo ni normal.

- **Media y DE** resumen posición y dispersión; la DE entra en el ETM (clase 025).
- **Asimetría** (tercer momento estandarizado) y **curtosis exceso** (cuarto momento − 3) describen la forma; la curtosis refleja colas, no «puntiagudez» (DeCarlo, 1997).
- **Suelo y techo**: porcentaje de personas en el puntaje mínimo y máximo. Una referencia citada en la literatura de instrumentos de salud es 15 % (Terwee et al., 2007); es una alerta, no una norma.

Laboratorio (10 ítems Likert 1-5, N = 5 000):

| Escala | media | DE | asimetría | curtosis | techo | techo − 3 |
|---|---:|---:|---:|---:|---:|---:|
| equilibrada | 30,1 | 8,0 | 0,00 | −0,53 | 0,2 % | 1,6 % |
| fácil (+1,2) | 40,4 | 6,7 | −0,70 | 0,07 | 4,5 % | 20,2 % |

En la escala fácil, uno de cada cinco evaluados está a menos de 3 puntos del máximo: no se distingue entre quienes están arriba y la fiabilidad en esa zona cae.

## Ejemplo resuelto

Datos 2, 3, 3, 4, 8: media 4; DE poblacional = √((4+1+1+0+16)/5) = 2,10; el 8 genera asimetría positiva. La mediana (3) describe mejor al caso típico.

## Errores y límites

- Reportar solo la media.
- Suponer normalidad por tratarse de una suma.
- Corregir la asimetría transformando los datos antes de preguntar si el instrumento cubre el rango del rasgo: a veces el problema es de ítems demasiado fáciles.

## Ejercicios

- **Inicial.** ¿Qué indica una asimetría negativa en un puntaje total?
- **Intermedio.** Calcula media y DE de 2, 4, 4, 6 → media 4; DE = √2 = 1,41.
- **Avanzado.** Modifica `sesgo` en `lab.py` a −1,2 y describe el suelo.

## Laboratorio

```bash
python classes/part-02-fiabilidad/026-estadistica-descriptiva-aplicada-a-puntajes/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué el techo reduce la fiabilidad en la zona alta? 2. ¿Cuándo preferirías mediana y rango intercuartil? 3. ¿Qué haces si encuentras 30 % en el techo?
Se logra si el estudiante describe una distribución real y propone una acción sobre los ítems.

## Bibliografía

- DeCarlo, L. T. (1997). On the meaning and use of kurtosis. *Psychological Methods*, 2(3), 292-307. ✅ [DOI](https://doi.org/10.1037/1082-989x.2.3.292)
- Terwee, C. B., et al. (2007). Quality criteria were proposed for measurement properties of health status questionnaires. *Journal of Clinical Epidemiology*, 60(1), 34-42. ✅ [DOI](https://doi.org/10.1016/j.jclinepi.2006.03.012)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
