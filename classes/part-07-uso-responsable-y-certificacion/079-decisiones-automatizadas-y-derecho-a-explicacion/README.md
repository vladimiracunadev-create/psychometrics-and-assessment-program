# 079 — Decisiones automatizadas y derecho a explicación

![Portada de la clase 079](portada.svg)

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clases 064, 074 y 076.

> Material educativo, no asesoría jurídica. Verifique el alcance de los derechos en el texto vigente de la Ley 21.719 (clase 076).

## Objetivos

1. Distinguir un modelo transparente de uno opaco para decisiones sobre personas.
2. Emitir motivos y marcar casos de revisión humana.
3. Relacionar el margen de error con una regla de intervención humana.

## Fundamentos

Cuando una decisión que afecta a una persona (seleccionar, admitir, excluir) se apoya en un sistema automático, importan: **explicabilidad** (poder decir qué pesó y cuánto), **contestabilidad** (poder rebatirla) y **intervención humana**. La literatura discute el alcance jurídico del «derecho a explicación» (Wachter, Mittelstadt y Floridi, 2017) y recomienda modelos interpretables para decisiones de alto impacto (Rudin, 2019).

Laboratorio: puntaje lineal con pesos declarados (prueba de razonamiento 0,50; muestra de trabajo 0,35; entrevista estructurada 0,15), corte 60 y margen de revisión ±6,2:

| Persona | Puntaje | Decisión | Revisión |
|---|---:|---|---|
| A | 74,2 | avanza | no |
| B | 58,5 | no avanza | **obligatoria** (dentro del margen) |
| C | 44,0 | no avanza | no |

Cada decisión lista los motivos ordenados por contribución.

## Ejemplo resuelto

Persona B: 0,50·50 + 0,35·70 + 0,15·60 = 25 + 24,5 + 9 = 58,5. Está a 1,5 puntos del corte, dentro del margen: un humano revisa.

## Errores y límites

- Los pesos del laboratorio son un ejemplo sin validez demostrada.
- Una «explicación» puede ser engañosa si no refleja el cálculo real.
- Automatizar sin posibilidad de apelación.
- Un modelo transparente puede igualmente discriminar: la transparencia no reemplaza el análisis de equidad (clase 064).

## Ejercicios

- **Inicial.** ¿Por qué se marcan los casos cercanos al corte?
- **Intermedio.** Cambia el peso de la entrevista a 0,30 y reescala los demás; recalcula B.
- **Avanzado.** Añade un registro de apelaciones y su resultado.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/079-decisiones-automatizadas-y-derecho-a-explicacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué información debe recibir la persona afectada? 2. ¿Quién revisa y con qué criterio? 3. ¿Qué evidencia de equidad exiges?
Se logra si el estudiante diseña una decisión explicable con intervención humana.

## Bibliografía

- Wachter, S., Mittelstadt, B., & Floridi, L. (2017). Why a right to explanation of automated decision-making does not exist in the General Data Protection Regulation. *International Data Privacy Law*, 7(2), 76-99. ✅ [DOI](https://doi.org/10.1093/idpl/ipx005)
- Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1, 206-215. ✅ [DOI](https://doi.org/10.1038/s42256-019-0048-x)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
