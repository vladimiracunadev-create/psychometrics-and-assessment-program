# 162 — Estrés percibido

> [Índice de la parte](../README.md)

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 015 y 055.

## Objetivos

1. Distinguir estrés percibido de estresores y de trastornos.
2. Comparar criterios de diferencia mínima importante.
3. Calcular umbrales de cambio fiable.

## Fundamentos

La *Perceived Stress Scale* (Cohen, Kamarck y Mermelstein, 1983) mide cuán impredecible, incontrolable y sobrecargada se percibe la vida; es una escala de percepción, no de diagnóstico. Para interpretar un cambio existen criterios: **0,5 DE** (Norman, Sloan y Wyrwich, 2003), **1 ETM** y el **cambio fiable** (Jacobson y Truax, 1991) = 1,96·ETM·√2. La importancia clínica o personal requiere un criterio externo (ancla).

Laboratorio (DE = 7; alfa = 0,85; ETM = 2,71; 20 000 personas **sin** cambio real):

| Criterio | Umbral (puntos) | Falsos cambios |
|---|---:|---:|
| 0,5 DE | 3,50 | 35,8 % |
| 1 ETM | 2,71 | 47,6 % |
| Cambio fiable | 7,51 | 5,1 % |

## Ejemplo resuelto

ETM = 7·√0,15 = 2,71; umbral fiable = 1,96·2,71·1,414 = 7,51.

## Errores y límites

- Declarar «mejoró» con un cambio de 3 puntos.
- Confundir estrés percibido con depresión o ansiedad.
- Usar umbrales de otra población sin evidencia local.
- Distribuciones simuladas y alfa supuesto.

## Ejercicios

- **Inicial.** ¿Qué es un ancla?
- **Intermedio.** DE = 6, alfa = 0,90: ETM = 1,90; cambio fiable = 5,26.
- **Avanzado.** Cambia alfa a 0,70 y observa los umbrales.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/162-estres-percibido/lab.py
```

## Autoevaluación y criterios

1. ¿Qué criterio usarías para evaluar un taller de manejo del estrés? 2. ¿Qué más reportarías? 3. ¿Cuándo derivas?
Se logra si el estudiante calcula umbrales y evita sobreinterpretar cambios pequeños.

## Bibliografía

- Cohen, S., Kamarck, T., & Mermelstein, R. (1983). A global measure of perceived stress. *Journal of Health and Social Behavior*, 24(4), 385-396.
- Norman, G. R., Sloan, J. A., & Wyrwich, K. W. (2003). Interpretation of changes in health-related quality of life: The remarkable universality of half a standard deviation. *Medical Care*, 41(5), 582-592.
- Jacobson, N. S., & Truax, P. (1991). Clinical significance: A statistical approach to defining meaningful change in psychotherapy research. *Journal of Consulting and Clinical Psychology*, 59(1), 12-19.
