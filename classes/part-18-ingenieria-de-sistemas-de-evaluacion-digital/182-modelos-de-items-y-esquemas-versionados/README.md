# 182 — Modelos de ítems y esquemas versionados

![Portada de la clase 182](portada.svg)

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 181.

## Objetivos

1. Validar estrictamente la definición de un instrumento.
2. Aplicar versionado semántico a instrumentos.
3. Justificar por qué un cambio de redacción cambia el instrumento.

## Fundamentos

Un esquema estricto detecta temprano licencias desconocidas, ítems duplicados, escalas vacías y propietarios con ítems. El versionado semántico (mayor.menor.parche) comunica si los puntajes siguen siendo comparables. Cambiar el texto de un ítem altera el estímulo y, por tanto, el instrumento (AERA et al., 2014).

Laboratorio: 5 definiciones defectuosas, 5 rechazadas con mensaje claro; política de versiones: 1.2.0→1.2.3 comparable, →1.3.0 recalcular y documentar, →2.0.0 ruptura.

## Ejemplo resuelto

Si corriges una errata de ortografía: parche. Si cambias el sentido de un ítem o la clave: menor o mayor y se documenta; los puntajes viejos no se mezclan sin análisis.

## Errores y límites

- Aceptar datos «casi bien» y corregirlos en silencio.
- Comparar puntajes de versiones distintas sin evidencia de equivalencia.
- El esquema valida forma, no calidad psicométrica.

## Ejercicios

- **Inicial.** ¿Qué indica el número mayor de una versión?
- **Intermedio.** Escribe una sexta definición defectuosa y comprueba su rechazo.
- **Avanzado.** Diseña un registro de cambios para un instrumento con dos versiones.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/182-modelos-de-items-y-esquemas-versionados/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- Preston-Werner, T. *Semantic Versioning 2.0.0*. semver.org. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
