# 109 — Estados frente a rasgos de personalidad

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 054 y 014.

## Objetivos

1. Distinguir estados de rasgos con datos de mediciones repetidas.
2. Calcular el coeficiente de correlación intraclase CCI(1).
3. Elegir el marco temporal de los enunciados.

## Fundamentos

Las personas fluctúan: la personalidad puede verse como una distribución de estados cuyo promedio es el rasgo (Fleeson, 2001). Con mediciones repetidas (muestreo de experiencias) se descompone la varianza en **entre personas** y **dentro de la persona**: CCI(1) = var_entre/(var_entre + var_dentro) (Shrout y Fleiss, 1979; Bolger y Laurenceau, 2013). Una variable tipo rasgo tiene CCI alto; una tipo estado, bajo.

Laboratorio (300 personas × 20 días):

| Variable | Var. entre | Var. dentro | CCI(1) | Fiabilidad de 1 día | Fiabilidad del promedio de 20 días |
|---|---:|---:|---:|---:|---:|
| Extraversión (rasgo) | 1,02 | 0,24 | 0,81 | 0,81 | 0,99 |
| Ánimo (estado) | 0,09 | 1,03 | 0,08 | 0,08 | 0,64 |

## Ejemplo resuelto

CCI = 0,08 y 20 días: fiabilidad del promedio = 20·0,08/(1 + 19·0,08) = 1,6/2,52 = 0,63.

## Errores y límites

- Usar el puntaje de un solo día como «cómo es» una persona cuando el CCI es bajo.
- Confundir «estado» con «patológico».
- Instrucciones temporales ambiguas («en general» frente a «hoy»).
- La carga de responder repetidamente y la privacidad de datos longitudinales (parte 07).

## Ejercicios

- **Inicial.** ¿Qué es un CCI de 0,10?
- **Intermedio.** Calcula la fiabilidad del promedio de 10 días con CCI 0,3 → 3/(1 + 2,7) = 0,81.
- **Avanzado.** Añade en `lab.py` una variable con tendencia semanal y comenta el efecto en el CCI.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/109-estados-frente-a-rasgos-de-personalidad/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo redactarías un ítem de estado y uno de rasgo? 2. ¿Cuántas mediciones necesitas? 3. ¿Qué datos de contexto recogerías?
Se logra si el estudiante calcula CCI y decide el marco temporal.

## Bibliografía

- Fleeson, W. (2001). Toward a structure- and process-integrated view of personality: Traitlike density distributions of states. *Journal of Personality and Social Psychology*, 80(6), 1011-1027. ✅ [DOI](https://doi.org/10.1037/0022-3514.80.6.1011)
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420-428. ✅ [DOI](https://doi.org/10.1037/0033-2909.86.2.420)
- Bolger, N., & Laurenceau, J.-P. (2013). *Intensive Longitudinal Methods*. Guilford. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
