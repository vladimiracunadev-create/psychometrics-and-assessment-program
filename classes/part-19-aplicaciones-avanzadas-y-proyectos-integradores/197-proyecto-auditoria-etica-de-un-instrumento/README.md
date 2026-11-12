# 197 — Proyecto: auditoría ética de un instrumento

> [Índice de la parte](../README.md)

**Parte 19 — Aplicaciones avanzadas y proyectos integradores** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 078.

## Objetivos

1. Auditar fichas e instrumentos con una lista de control.
2. Distinguir lo que el script verifica de lo que exige un humano.
3. Informar los hallazgos sin ocultarlos.

## Fundamentos

Una auditoría solo sirve si puede fallar y si muestra el hallazgo. El laboratorio revisa el catálogo real: consistencia de fichas, estados sin evidencia, propiedad intelectual y marca de «sin validar» en los instrumentos propios.

Laboratorio: controles A, B, C y E cumplen; hallazgo D: 5 fichas verificadas y 135 sin verificar de 140 (135 documentadas y 5 implementadas).

## Ejemplo resuelto

El hallazgo principal no es un error de código sino un riesgo de lectura: que alguien confunda una ficha documentada con un instrumento validado. La mitigación son los estados separados y el campo `verificado`.

## Errores y límites

- Considerar «cumple» como sinónimo de «validado».
- Esperar que un script contraste la fuente primaria.
- La lista de control es parcial.

## Ejercicios

- **Inicial.** ¿Qué controles automatiza el laboratorio?
- **Intermedio.** Añade un control sobre fichas laborales sin nota de contenido no verificado.
- **Avanzado.** Diseña el procedimiento humano para verificar una familia de fichas.

## Laboratorio

```bash
python classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/197-proyecto-auditoria-etica-de-un-instrumento/lab.py
```

## Autoevaluación y criterios

1. ¿Qué decisión de este proyecto es la más discutible? 2. ¿Qué evidencia falta? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante ejecuta el proyecto, interpreta sus cifras con cautela y declara sus límites.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- American Psychological Association (2017). *Ethical Principles of Psychologists and Code of Conduct*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
