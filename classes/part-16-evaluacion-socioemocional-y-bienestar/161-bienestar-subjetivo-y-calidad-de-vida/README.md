# 161 — Bienestar subjetivo y calidad de vida

> [Índice de la parte](../README.md)

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 014 y 039.

## Objetivos

1. Distinguir bienestar subjetivo, satisfacción con la vida y calidad de vida.
2. Comparar un ítem único con una escala.
3. Calcular el tamaño de muestra según la fiabilidad de la medida.

## Fundamentos

El bienestar subjetivo incluye juicios de satisfacción con la vida y afecto positivo/negativo (Diener et al., 2018). La *Satisfaction With Life Scale* (Diener et al., 1985) tiene 5 ítems; un ítem único de satisfacción tiene validez razonable para estudios poblacionales, pero menor fiabilidad (Cheung y Lucas, 2014).

Laboratorio (relación verdadera con un criterio de 0,40; supuestos):

| Medida | Fiabilidad | r observada | r esperada | n para 80 % de potencia |
|---|---:|---:|---:|---:|
| 1 ítem | 0,60 | 0,303 | 0,310 | 84 |
| Escala de 5 ítems | 0,85 | 0,359 | 0,369 | 59 |

Efecto techo de un ítem 1–7 con media alta: 40,8 % responde 6 o 7.

## Ejemplo resuelto

r_obs = r_verdadera·√(ρ_x) (con criterio perfecto): 0,40·√0,60 = 0,31.

## Errores y límites

- Usar un ítem para decisiones individuales.
- Considerar una escala de satisfacción como medida de salud mental.
- Comparar culturas sin invarianza (clase 070).
- Parámetros supuestos.

## Ejercicios

- **Inicial.** ¿Qué es bienestar subjetivo?
- **Intermedio.** r_obs con ρ = 0,85: 0,40·0,92 = 0,37.
- **Avanzado.** Cambia la relación verdadera a 0,20 y recalcula el tamaño de muestra.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/161-bienestar-subjetivo-y-calidad-de-vida/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo basta un ítem? 2. ¿Cómo comunicas un resultado de bienestar? 3. ¿Qué haces si alguien muestra malestar importante? (clase 168)
Se logra si el estudiante elige una medida según el propósito y calcula su costo en muestra.

## Bibliografía

- Diener, E., Emmons, R. A., Larsen, R. J., & Griffin, S. (1985). The Satisfaction With Life Scale. *Journal of Personality Assessment*, 49(1), 71-75. ✅ [DOI](https://doi.org/10.1207/s15327752jpa4901_13)
- Cheung, F., & Lucas, R. E. (2014). Assessing the validity of single-item life satisfaction measures. *Quality of Life Research*, 23, 2809-2818. ✅ [DOI](https://doi.org/10.1007/s11136-014-0726-4)
- Diener, E., Oishi, S., & Tay, L. (2018). Advances in subjective well-being research. *Nature Human Behaviour*, 2, 253-260. ✅ [DOI](https://doi.org/10.1038/s41562-018-0307-6)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
