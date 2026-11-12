# 189 — Interoperabilidad y exportación de resultados

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 188.

## Objetivos

1. Exportar en formato largo con metadatos.
2. Verificar la ida y vuelta.
3. Neutralizar la inyección de fórmulas en CSV.

## Fundamentos

El formato largo (una fila por persona y escala) es aceptado por la mayoría de las herramientas de análisis. Incluir versión, licencia y número de ítems respondidos hace reproducible el cálculo. Un campo que empieza con `=`, `+`, `-` o `@` puede interpretarse como fórmula en una planilla (OWASP, *CSV Injection*), por lo que se antepone un apóstrofo.

Laboratorio: 3 personas × 6 escalas = 18 filas, ida y vuelta CSV correcta, 4 casos de neutralización.

## Ejemplo resuelto

Un nombre de participante `=HYPERLINK(...)` se exporta con un apóstrofo delante y se muestra como texto.

## Errores y límites

- Exportar solo puntajes sin versión.
- Confiar en que los datos «internos» no contienen texto malicioso.
- Los datos son sintéticos.

## Ejercicios

- **Inicial.** ¿Qué columnas lleva un formato largo?
- **Intermedio.** Añade la columna de error estándar y valida la ida y vuelta.
- **Avanzado.** Define un diccionario de datos para la exportación.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/189-interoperabilidad-y-exportacion-de-resultados/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- OWASP. *CSV Injection*. owasp.org.
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles. *Scientific Data*, 3, 160018.
