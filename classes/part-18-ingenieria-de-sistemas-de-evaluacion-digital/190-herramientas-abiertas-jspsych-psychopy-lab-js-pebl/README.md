# 190 — Herramientas abiertas: jsPsych, PsychoPy, lab.js y PEBL

![Portada de la clase 190](portada.svg)

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 189.

## Objetivos

1. Detectar la familia de una licencia a partir de su texto.
2. Aplicar una tabla de compatibilidad para un proyecto MIT.
3. Registrar la revisión de cada recurso externo.

## Fundamentos

Antes de incorporar un recurso conviene leer su licencia. El laboratorio detecta MIT, Apache-2.0, GPL, LGPL, BSD y variantes Creative Commons por frases características, y aplica una guía de compatibilidad para un proyecto de código MIT. No es asesoría jurídica. Las herramientas del título (jsPsych, PsychoPy, lab.js, PEBL) se evalúan leyendo su LICENSE en la fuente oficial; este repositorio no afirma sus licencias sin verificarlas.

Laboratorio: `LICENSE` detectada como MIT; casos de prueba MIT, GPL, Apache-2.0, CC BY-NC-SA y vacío resueltos correctamente.

## Ejemplo resuelto

Antes de adoptar una librería: URL, versión, licencia leída, fecha de revisión y estado de mantenimiento quedan en su ficha.

## Errores y límites

- Asumir que «abierto» significa compatible.
- Detectar la licencia solo por el nombre del repositorio.
- El detector reconoce familias, no la licencia exacta.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre MIT y GPL para quien redistribuye?
- **Intermedio.** Añade la licencia MPL-2.0 al detector.
- **Avanzado.** Elabora la ficha de revisión de un recurso abierto de tu elección.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/190-herramientas-abiertas-jspsych-psychopy-lab-js-pebl/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- Open Source Initiative. *Open Source Definition*. opensource.org. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Choose a License. choosealicense.com. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
