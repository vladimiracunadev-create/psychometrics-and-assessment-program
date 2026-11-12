# 038 — Evidencia basada en procesos de respuesta

![Portada de la clase 038](portada.svg)

<!-- NAV -->
[← 037 — Validez ecológica y generalización](../037-validez-ecologica-y-generalizacion/README.md) · [📚 Parte 03](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [039 — Metaanálisis de validez y corrección por aten… →](../039-metaanalisis-de-validez-y-correccion-por-atenuacion/README.md)
<!-- /NAV -->

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 031 y 012.

## Objetivos

1. Explicar qué aportan los procesos de respuesta al argumento de validez.
2. Usar tiempos de respuesta para detectar adivinación rápida.
3. Reconocer los riesgos de interpretar mecánicamente un tiempo corto.

## Fundamentos

Los *Standards* (2014) incluyen entre las fuentes de evidencia los **procesos de respuesta**: ¿hacen las personas lo que el constructo supone? Se estudian con protocolos de pensamiento en voz alta, entrevistas cognitivas, seguimiento ocular y tiempos de respuesta. En pruebas digitales, los tiempos permiten identificar respuestas dadas sin esfuerzo (Wise y Kong, 2005).

Laboratorio (30 ítems; ~30 % de las personas se apura en la mitad de sus ítems; umbral de 3 s):

- respuestas rápidas: 14,4 % del total, con 0,257 de aciertos (azar con 4 opciones: 0,25);
- respuestas normales: 0,508 de aciertos;
- r(habilidad, puntaje bruto) = 0,882; r(habilidad, puntaje sin respuestas rápidas) = **0,930**.

El puntaje mezcla habilidad con **motivación de esfuerzo**; filtrar las respuestas sin esfuerzo acerca el puntaje a la habilidad.

## Ejemplo resuelto

Un ítem se responde en 1,2 s con acierto. Si la mediana del ítem es 14 s y el 90 % de las respuestas correctas toma más de 5 s, 1,2 s sugiere adivinación (quizá correcta por azar). Si el ítem es una recuperación inmediata de un dato muy practicado, un tiempo corto puede ser pericia.

## Errores y límites

- Fijar el umbral sin mirar la distribución de cada ítem; aquí 3 s es una decisión del laboratorio.
- Penalizar a quienes responden rápido por pericia o por un ritmo lector distinto.
- Descartar datos sin informar qué proporción se descartó.
- Los tiempos son datos de conducta digital: requieren consentimiento y minimización (parte 07).

## Ejercicios

- **Inicial.** ¿Qué dos explicaciones tiene un tiempo muy corto?
- **Intermedio.** Si 14,4 % de las respuestas son rápidas con 25 % de aciertos, ¿cuántos aciertos «regala» el azar en 30 ítems? ≈ 30·0,144·0,25 ≈ 1,1.
- **Avanzado.** Cambia el umbral a 6 s en `lab.py` y describe qué respuestas razonadas se pierden.

## Laboratorio

```bash
python classes/part-03-validez/038-evidencia-basada-en-procesos-de-respuesta/lab.py
```

## Autoevaluación y criterios

1. ¿Qué dice un proceso de respuesta que una correlación no dice? 2. ¿Cómo justificarías un umbral? 3. ¿Qué riesgos éticos tiene registrar tiempos?
Se logra si el estudiante usa tiempos como evidencia sin sobreinterpretarlos.

## Bibliografía

- Wise, S. L., & Kong, X. (2005). Response time effort: A new measure of examinee motivation in computer-based tests. *Applied Measurement in Education*, 18(2), 163-183. ✅ [DOI](https://doi.org/10.1207/s15324818ame1802_2)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 037 — Validez ecológica y generalización](../037-validez-ecologica-y-generalizacion/README.md)  
[📚 Parte 03](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[039 — Metaanálisis de validez y corrección por aten… →](../039-metaanalisis-de-validez-y-correccion-por-atenuacion/README.md)
<!-- /NAV -->
