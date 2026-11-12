# 187 — Auditoría de cálculo y trazabilidad

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 186.

## Objetivos

1. Verificar el motor con una segunda implementación.
2. Generar un registro de auditoría reproducible.
3. Entender los límites del differential testing.

## Fundamentos

Si dos implementaciones independientes coinciden en muchos casos, es improbable que compartan el mismo error (McKeeman, 1998). Un registro con versión del instrumento y huellas de entrada y salida permite reproducir un puntaje sin exponer las respuestas.

Laboratorio: 5 instrumentos × 200 protocolos aleatorios, 200 de 200 coincidencias en cada uno; ejemplo de registro con versión y huellas.

## Ejemplo resuelto

Un puntaje cuestionado se audita recalculando con la versión registrada y comparando la huella de salida.

## Errores y límites

- Probar solo casos típicos.
- Que ambas implementaciones compartan una mala interpretación del manual.
- La coincidencia prueba consistencia, no validez.

## Ejercicios

- **Inicial.** ¿Qué es una segunda implementación independiente?
- **Intermedio.** Introduce un error deliberado y comprueba que se detecta.
- **Avanzado.** Diseña un registro de auditoría para una batería.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/187-auditoria-de-calculo-y-trazabilidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- McKeeman, W. M. (1998). Differential testing for software. *Digital Technical Journal*, 10(1), 100-107. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
