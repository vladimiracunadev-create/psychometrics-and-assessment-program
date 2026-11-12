# 031 — La validez no es una propiedad del test, es un argumento

![Portada de la clase 031](portada.svg)

> [Índice de la parte](../README.md) · [Siguiente](../032-validez-de-contenido/README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 025.

## Objetivos

1. Explicar por qué se valida una interpretación y un uso, no un test.
2. Distinguir fiabilidad de validez con un ejemplo cuantificado.
3. Enumerar las fuentes de evidencia de los Standards (2014).
4. Formular el argumento de validez de un uso concreto.

## Fundamentos

Los *Standards* (AERA/APA/NCME, 2014) definen la validez como el grado en que la evidencia y la teoría respaldan las interpretaciones de los puntajes para los usos propuestos. Messick (1995) la presentó como un concepto unitario; Kane (2013) la formula como un **argumento**: cadena de inferencias (puntaje → generalización → extrapolación → decisión) cada una con evidencia que la sostiene o la debilita.

Fuentes de evidencia: contenido, procesos de respuesta, estructura interna, relaciones con otras variables y consecuencias.

Laboratorio: una prueba de vocabulario con fiabilidad 0,95 y una de razonamiento numérico con fiabilidad 0,80, usadas para predecir rendimiento en matemática:

| Prueba | Fiabilidad | r con el criterio | Techo teórico √(ρₓρᵧ) |
|---|---:|---:|---:|
| A. Vocabulario | 0,95 | 0,090 | 0,905 |
| B. Razonamiento numérico | 0,80 | 0,584 | 0,831 |

A es casi perfecta como medida y casi inútil para este propósito. La fiabilidad es **condición necesaria, no suficiente**.

## Ejemplo resuelto

Uso propuesto: «seleccionar estudiantes para un programa de ingeniería con un test de razonamiento». Argumento: (1) el test cubre razonamiento cuantitativo (contenido); (2) el puntaje es estable (fiabilidad); (3) predice notas de primer año (criterio); (4) el uso no excluye de forma injustificada a grupos (consecuencias). Cada paso es una hipótesis con evidencia o sin ella; donde no hay evidencia, el argumento queda abierto.

## Errores y límites

- Decir «el test X está validado» sin decir para qué, en quién y con qué evidencia.
- Reunir evidencia solo de lo que es fácil de medir.
- Tratar la validez como un sello que se otorga una vez.

## Ejercicios

- **Inicial.** Nombra dos usos distintos de un mismo test de lectura que requieran evidencia diferente.
- **Intermedio.** Si ρₓ = 0,64 y ρᵧ = 0,81, ¿cuál es el techo de r? → √0,5184 = 0,72.
- **Avanzado.** Escribe el argumento de validez de uno de los instrumentos del catálogo, marcando las inferencias sin evidencia.

## Laboratorio

```bash
python classes/part-03-validez/031-validez-como-argumento/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué «test válido» es una frase incompleta? 2. ¿Qué evidencia falta típicamente? 3. ¿Cómo se relaciona fiabilidad con el techo de la validez?
Se logra si el estudiante redacta un argumento con inferencias y evidencia faltante.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Messick, S. (1995). Validity of psychological assessment. *American Psychologist*, 50(9), 741-749. ⚠️ existe, pero Crossref registra 1996 (¿otra edición?; [DOI](https://doi.org/10.1037//0003-066x.51.9.980))
- Kane, M. T. (2013). Validating the interpretations and uses of test scores. *Journal of Educational Measurement*, 50(1), 1-73. ✅ [DOI](https://doi.org/10.1111/jedm.12000)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
