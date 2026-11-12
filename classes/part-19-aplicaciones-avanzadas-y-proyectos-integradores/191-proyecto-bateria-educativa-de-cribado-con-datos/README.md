# 191 — Proyecto: batería educativa de cribado con datos

![Portada de la clase 191](portada.svg)

<!-- NAV -->
[← 190 — Herramientas abiertas: jsPsych, PsychoPy, lab…](../../part-18-ingenieria-de-sistemas-de-evaluacion-digital/190-herramientas-abiertas-jspsych-psychopy-lab-js-pebl/README.md) · [📚 Parte 19](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [192 — Proyecto: batería laboral con ajuste justific… →](../192-proyecto-bateria-laboral-con-ajuste-justificado/README.md)
<!-- /NAV -->

**Parte 19 — Aplicaciones avanzadas y proyectos integradores** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 145.

## Objetivos

1. Diseñar un cribado en dos etapas.
2. Evaluar sensibilidad, especificidad y VPP con una condición poco frecuente.
3. Redactar los límites de un cribado.

## Fundamentos

Un cribado en dos etapas aplica una prueba breve a todos y una prueba más larga solo a quienes quedan bajo el corte. Como la condición es poco frecuente, el VPP de la etapa 1 sola es bajo aunque su sensibilidad sea alta (clase 061).

Laboratorio (1.200 estudiantes sintéticos, condición = 10 % inferior de la habilidad): etapa 1 sola, 381 derivados, sensibilidad 0,96, especificidad 0,75, VPP 0,30; etapa 1 + etapa 2, 154 derivados, sensibilidad 0,79, especificidad 0,95, VPP 0,62, con 381 pruebas largas aplicadas.

## Ejemplo resuelto

Derivar solo a quien queda bajo corte en ambas etapas reduce los derivados de 381 a 154 y duplica el VPP, a costa de perder 17 puntos de sensibilidad. Esa elección se justifica con el costo de no apoyar a alguien y el costo de derivar de más.

## Errores y límites

- Tratar el resultado del cribado como diagnóstico.
- Fijar el corte sin datos del contexto.
- Datos y condición sintéticos: en la vida real la condición verdadera no se observa.

## Ejercicios

- **Inicial.** ¿Por qué el VPP es bajo con una condición poco frecuente?
- **Intermedio.** Cambia el corte de la etapa 1 y observa el cambio de sensibilidad.
- **Avanzado.** Calcula el costo total de cada estrategia con costos que tú definas y justifiques.

## Laboratorio

```bash
python classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/191-proyecto-bateria-educativa-de-cribado-con-datos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué decisión de este proyecto es la más discutible? 2. ¿Qué evidencia falta? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante ejecuta el proyecto, interpreta sus cifras con cautela y declara sus límites.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Jenkins, J. R., Hudson, R. F., & Johnson, E. S. (2007). Screening for at-risk readers in a response to intervention framework. *School Psychology Review*, 36(4), 582-600. ✅ [DOI](https://doi.org/10.1080/02796015.2007.12087919)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 190 — Herramientas abiertas: jsPsych, PsychoPy, lab…](../../part-18-ingenieria-de-sistemas-de-evaluacion-digital/190-herramientas-abiertas-jspsych-psychopy-lab-js-pebl/README.md)  
[📚 Parte 19](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[192 — Proyecto: batería laboral con ajuste justific… →](../192-proyecto-bateria-laboral-con-ajuste-justificado/README.md)
<!-- /NAV -->
