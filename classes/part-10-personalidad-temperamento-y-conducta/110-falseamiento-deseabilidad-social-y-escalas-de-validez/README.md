# 110 — Falseamiento, deseabilidad social y escalas de validez

![Portada de la clase 110](portada.svg)

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 040 y 100.

## Objetivos

1. Evaluar una escala de validez con sensibilidad, especificidad, VPP y AUC.
2. Reconocer los falsos positivos y a quiénes afectan.
3. Definir un uso responsable de estas escalas.

## Fundamentos

Las escalas de validez (infrecuencia, virtudes improbables, deseabilidad social) buscan detectar protocolos distorsionados. Pero parte de la «deseabilidad social» es rasgo sustantivo, no sesgo (Ones, Viswesvaran y Reiss, 1996), y corregir por ella puede quitar validez. Con prevalencia baja de falseamiento, muchos marcados son honestos.

Laboratorio (escala de 5 ítems; honestos 1,0 ± 1,0; falseadores 2,5 ± 1,2; prevalencia 20 %):

| Corte (≥) | Sensibilidad | Especificidad | VPP | Honestos de alta responsabilidad marcados |
|---:|---:|---:|---:|---:|
| 1,5 | 0,81 | 0,69 | 0,39 | 0,49 |
| 2,5 | 0,51 | 0,93 | 0,63 | 0,15 |
| 3,5 | 0,21 | 0,99 | 0,85 | 0,02 |

AUC ≈ 0,83. No hay corte que detecte bien y evite falsos positivos.

## Ejemplo resuelto

Corte 2,5 con prevalencia 20 %: marcados verdaderos = 0,51·0,20 = 0,102; falsos = 0,07·0,80 = 0,056; VPP = 0,102/0,158 = 0,65 (≈ 0,63 en la simulación).

## Errores y límites

- Excluir a personas por una escala de validez.
- Corregir puntajes restando deseabilidad sin evidencia de que mejore la predicción.
- Confiar en una sola contramedida (clase 040).
- Los parámetros son supuestos.

## Ejercicios

- **Inicial.** ¿Qué es el VPP?
- **Intermedio.** Con sensibilidad 0,34, especificidad 0,97 y prevalencia 20 %, calcula el VPP → 0,068/(0,068 + 0,024) = 0,74.
- **Avanzado.** Cambia la prevalencia a 5 % y reporta el VPP.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/110-falseamiento-deseabilidad-social-y-escalas-de-validez/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo usar una escala de validez de forma responsable? 2. ¿Qué otras estrategias reducen el falseamiento? 3. ¿Qué evidencia necesitas para corregir por deseabilidad?
Se logra si el estudiante evalúa una escala de validez con sus costos de error.

## Bibliografía

- Ones, D. S., Viswesvaran, C., & Reiss, A. D. (1996). Role of social desirability in personality testing for personnel selection: The red herring. *Journal of Applied Psychology*, 81(6), 660-679. ✅ [DOI](https://doi.org/10.1037/0021-9010.81.6.660)
- Paulhus, D. L. (1991). Measurement and control of response bias. En J. P. Robinson et al. (Eds.), *Measures of Personality and Social Psychological Attitudes*. Academic Press. ✅ [DOI](https://doi.org/10.1016/b978-0-12-590241-0.50006-x)
- Ziegler, M., MacCann, C., & Roberts, R. D. (Eds.) (2012). *New Perspectives on Faking in Personality Assessment*. Oxford University Press. ✅ [DOI](https://doi.org/10.1093/acprof:oso/9780195387476.001.0001)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
