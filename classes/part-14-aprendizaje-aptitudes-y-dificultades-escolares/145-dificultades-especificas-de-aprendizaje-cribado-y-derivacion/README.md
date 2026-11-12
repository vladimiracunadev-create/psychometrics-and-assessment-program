# 145 — Dificultades específicas de aprendizaje: cribado y derivación

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 135, 142 y 175.

> El diagnóstico de dificultades específicas del aprendizaje corresponde a profesionales habilitados. Esta clase trata del cribado y de la decisión de derivar.

## Objetivos

1. Estimar la pendiente de progreso con monitoreo semanal.
2. Cuantificar los errores de clasificación según la duración del monitoreo.
3. Diseñar un cribado escalonado antes de derivar.

## Fundamentos

La **respuesta a la intervención** usa el progreso del estudiante bajo apoyo como información para decidir (Fuchs y Fuchs, 2006). Pero la pendiente estimada con pocas mediciones es muy imprecisa (Christ, 2006): su error típico decrece fuertemente con las semanas de monitoreo.

Laboratorio (400 estudiantes; ruido 8 PCM; umbral de respuesta 1,5 PCM/semana; supuestos):

| Semanas | Error típico de la pendiente | Clasificación errada | Falsos «no responde» |
|---:|---:|---:|---:|
| 4 | 3,46 | 44,5 % | 45,3 % |
| 8 | 1,20 | 33,8 % | 32,8 % |
| 12 | 0,68 | 23,5 % | 25,5 % |
| 16 | 0,45 | 18,2 % | 15,6 % |

Con 4 semanas el error de la pendiente es mayor que la pendiente a juzgar.

## Ejemplo resuelto

Con ruido σ = 8 y *n* = 8 semanales, EE(pendiente) = σ/√Σ(t − t̄)² = 8/√42 = 1,23 (≈ 1,20 simulado).

## Errores y límites

- Derivar por un monitoreo corto.
- Usar el progreso como único criterio.
- Ignorar la calidad de la intervención y la asistencia.
- Datos sintéticos; criterios reales de decisión se definen con evidencia local.

## Ejercicios

- **Inicial.** ¿Qué es monitoreo del progreso?
- **Intermedio.** EE de la pendiente con σ = 6 y 10 semanas: Σ(t − t̄)² = 82,5 → 0,66.
- **Avanzado.** Reduce el ruido a 4 PCM en `lab.py` y observa cuántas semanas bastan.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/145-dificultades-especificas-de-aprendizaje-cribado-y-derivacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué otra información reúnes antes de derivar? 2. ¿Cómo involucras a la familia? 3. ¿Qué apoyos das mientras esperan?
Se logra si el estudiante diseña un cribado escalonado y justifica la duración del monitoreo.

## Bibliografía

- Fuchs, D., & Fuchs, L. S. (2006). Introduction to response to intervention: What, why, and how valid is it? *Reading Research Quarterly*, 41(1), 93-99.
- Christ, T. J. (2006). Short-term estimates of growth using curriculum-based measurement of oral reading fluency. *School Psychology Review*, 35(1), 128-133.
