# 006 — Redacción de ítems: las reglas y por qué existen

> [Clase anterior](../../part-00-fundamentos-de-la-medicion/005-items-invertidos-y-aquiescencia/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../007-formatos-de-respuesta/README.md)

**Parte:** 01 — Construcción de instrumentos
**Nivel:** fundamentos · **Horas estimadas:** 4 · **Estado:** `escrita`
**Prerrequisitos:** clases 001–005 (constructo, ítem, escalas, reflejo).

## Propósito

Un ítem es la unidad mínima de medida: si está mal escrito, ninguna técnica
posterior lo repara. Esta clase enseña las reglas de redacción habituales y,
sobre todo, el mecanismo por el que cada regla protege la interpretación de la
respuesta.

## Resultados de aprendizaje

1. Identificar y corregir doble pregunta, absolutos, doble negación y exceso de longitud.
2. Explicar para cada regla qué error de medida introduce su infracción.
3. Distinguir un defecto de forma (detectable por reglas) de uno de sentido (requiere personas).
4. Revisar un banco de ítems con una lista de verificación reproducible.

## Introducción conceptual

Responder un ítem es un proceso de varios pasos: comprender, recuperar información,
juzgar y elegir una categoría. Cada defecto de redacción rompe un paso concreto.
Cuando el paso se rompe, la persona **responde de todos modos**: el defecto no
produce un dato faltante sino un dato **contaminado**, y por eso es peligroso.

## Las reglas y su mecanismo

| Defecto | Ejemplo | Qué se rompe |
|---|---|---|
| Doble pregunta | «Planifico mi semana y reviso mi avance cada día» | Quien hace lo uno y no lo otro no tiene respuesta válida; la elige al azar. |
| Absoluto | «Siempre termino lo que empiezo» | Casi nadie asiente; el ítem pierde varianza y discrimina poco. |
| Doble negación | «Me cuesta no distraerme cuando no hay nadie…» | El acuerdo significa lo contrario de lo que parece; sube el error de lectura. |
| Exceso de longitud | más de ~20 palabras | Cae la comprensión, sobre todo con lectores menos fluidos o en segunda lengua. |
| Jerga o ambigüedad | «Soy proactivo» | Cada persona le da un significado; se mide vocabulario, no rasgo. |
| Deseabilidad evidente | «Soy una persona honesta» | Todos asienten; el ítem mide imagen, no conducta. |

Las reglas no son leyes: son hipótesis sobre cómo se rompe la respuesta. Un
absoluto es defendible si el constructo es genuinamente extremo (p. ej. un
indicador de riesgo en cribado), y **por eso se documenta la excepción**.

## Ejemplo resuelto

Ítem original: *«Siempre planifico mi trabajo y nunca me distraigo»*.

1. Dos ideas (planificar, distraerse) → separar en dos ítems.
2. «Siempre» y «nunca» → absolutos; suavizar con frecuencia («Planifico mi trabajo antes de comenzar»).
3. «nunca me distraigo» es negación + absoluto; se reformula en positivo: «Mantengo la atención en lo que hago».
4. Longitud final: 6 y 7 palabras.

## Errores frecuentes

- Corregir la forma y olvidar el sentido: un ítem breve y afirmativo puede seguir siendo ambiguo.
- Invertir un ítem añadiendo «no» en lugar de redactar el polo opuesto del rasgo (clase 005).
- Dar por válido un ítem porque «se entiende bien» a quien lo escribió.

## Limitaciones

Las reglas se infieren de la práctica y de estudios sobre procesos de respuesta,
no son un algoritmo. Un ítem que cumple todas puede fallar en otra población o
cultura: la revisión con personas reales (clase 049) es insustituible.

## Ejercicios

- **Inicial.** Marca cuál de estos ítems tiene doble pregunta: a) «Disfruto aprender y enseñar»; b) «Disfruto aprender».
- **Intermedio.** Reescribe «Nunca dejo de ser amable con quien no me cae bien» sin negaciones ni absolutos.
- **Avanzado.** Toma diez ítems del catálogo (`psychometrics ficha ...`), pásalos por el linter y discute dos casos que el linter marque pero que tú aceptes.

*Soluciones razonadas:* a) tiene doble pregunta, aprender y enseñar son conductas distintas.
La reescritura debe medir amabilidad, p. ej. «Trato con amabilidad a personas que me caen mal».

## Laboratorio

`lab.py` es un linter heurístico que detecta cuatro defectos de forma y acierta
6 de 6 ítems etiquetados. Muestra además su límite: revisa la forma, no el sentido.

```bash
python classes/part-01-construccion-de-instrumentos/006-redaccion-de-items/lab.py
```

## Autoevaluación

1. ¿Por qué un absoluto reduce la discriminación y no solo «parece raro»?
2. ¿Qué paso del proceso de respuesta rompe una doble negación?
3. Da un caso en que un absoluto sea legítimo y cómo lo documentarías.

## Criterios de evaluación

Se logra la clase si el estudiante corrige ítems defectuosos justificando cada
cambio con el mecanismo, y distingue defectos detectables por regla de los que
exigen revisión con personas.

## Bibliografía

- Haladyna, T. M., & Rodriguez, M. C. (2013). *Developing and Validating Test Items*. Routledge.
- Krosnick, J. A. (1991). Response strategies for coping with the cognitive demands of attitude measures in surveys. *Applied Cognitive Psychology*, 5(3), 213-236.
- Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research. *Journal of Applied Psychology*, 88(5), 879-903.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
