# 184 — Telemetría de interacción y tiempos de respuesta

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 183.

## Objetivos

1. Calcular indicadores simples de respuesta descuidada.
2. Evaluar sensibilidad, especificidad y valor predictivo.
3. Aplicar minimización de datos a la telemetría.

## Fundamentos

Los tiempos de respuesta pueden señalar respuestas sin lectura (Wise & Kong, 2005). Una regla de marcado se evalúa como cualquier prueba de cribado, con sensibilidad, especificidad y VPP; el VPP depende de la prevalencia.

Laboratorio (2.000 personas, 10 % descuidadas, con lectores rápidos legítimos): «mediana < 2 s» da sensibilidad 0,46, especificidad 0,93 y VPP 0,46; «más de 50 % de respuestas rápidas» da sensibilidad 0,23, especificidad 1,00 y VPP 0,92; AUC de la mediana 0,90.

## Ejemplo resuelto

La regla estricta casi no marca a personas honestas, pero deja pasar a tres de cada cuatro descuidadas: el umbral cambia errores de un tipo por otros.

## Errores y límites

- Marcar y descartar sin revisión humana.
- Guardar tiempos por ítem sin necesidad.
- Datos sintéticos: no hay umbrales universales.

## Ejercicios

- **Inicial.** ¿Por qué el VPP cambia con la prevalencia?
- **Intermedio.** Cambia la prevalencia al 2 % y recalcula el VPP.
- **Avanzado.** Redacta el texto de consentimiento que informa el uso de tiempos.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/184-telemetria-de-interaccion-y-tiempos-de-respuesta/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- Wise, S. L., & Kong, X. (2005). Response time effort. *Applied Measurement in Education*, 18(2), 163-183.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
