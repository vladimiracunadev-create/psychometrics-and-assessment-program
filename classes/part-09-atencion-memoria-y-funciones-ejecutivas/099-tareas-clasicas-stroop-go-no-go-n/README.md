# 099 — Tareas clásicas: Stroop, Go/No-Go, n-back

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 091, 095 y 097.

## Objetivos

1. Generar secuencias con restricciones de diseño verificables.
2. Puntuar con d′ y errores de comisión.
3. Entender por qué el diseño es parte de la medición.

## Fundamentos

Los paradigmas clásicos son *procedimientos*, no instrumentos con ítems fijos: su calidad depende de la **secuencia** (proporciones, rachas, repeticiones). En n-back se controla la proporción de objetivos (aquí ≈ 25 %) y que no haya objetivos accidentales; en Go/No-Go, la proporción de No-Go (≈ 25 %) y su dispersión; en Stroop, la proporción de ensayos congruentes y la ausencia de repeticiones inmediatas que provocan priming. El d′ separa sensibilidad de sesgo (clase 091).

Laboratorio (semilla fija):

| Paradigma | Resultado de la verificación |
|---|---|
| 1-back | 35/119 objetivos (29 %); secuencia coherente; d′ simulado 1,99 |
| 2-back | 27/118 (23 %); coherente; d′ 1,82 |
| 3-back | 30/117 (26 %); coherente; d′ 1,49 |
| Go/No-Go | 18/100 No-Go; sin rachas de 4; primeros dos ensayos Go |
| Stroop | 50 % congruentes; 0 repeticiones inmediatas de palabra |

## Ejemplo resuelto

Secuencia B C B: en 2-back, el tercer ítem es objetivo (igual al de 2 atrás). La verificación recorre toda la secuencia y comprueba que la etiqueta de objetivo coincide con esa regla.

## Errores y límites

- Usar secuencias aleatorias sin verificar restricciones.
- Comparar puntajes de versiones con proporciones distintas.
- Dar por norma lo que es un procedimiento: no hay baremo por existir la tarea.
- Los d′ simulados dependen de supuestos; en datos reales se estiman.

## Ejercicios

- **Inicial.** ¿Qué es un objetivo accidental en n-back?
- **Intermedio.** Si aciertos = 0,85 y falsas alarmas = 0,10, ¿d′? ≈ 1,04 + 1,28 = 2,32.
- **Avanzado.** Añade al generador de Stroop una restricción de no más de 3 congruentes seguidos.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/099-tareas-clasicas-stroop-go-no-go-n/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué evitar repeticiones inmediatas? 2. ¿Qué mide cada tarea y qué no? 3. ¿Qué librerías abiertas (jsPsych, PsychoPy, PEBL) implementan estos paradigmas y bajo qué licencia?
Se logra si el estudiante genera y verifica secuencias y puntúa con d′.

## Bibliografía

- MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. *Psychological Bulletin*, 109(2), 163-203. ✅ [DOI](https://doi.org/10.1037/0033-2909.109.2.163)
- Kane, M. J., Conway, A. R. A., Miura, T. K., & Colflesh, G. J. H. (2007). Working memory, attention control, and the n-back task. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 33(3), 615-622. ✅ [DOI](https://doi.org/10.1037/0278-7393.33.3.615)
- Macmillan, N. A., & Creelman, C. D. (2005). *Detection Theory: A User's Guide* (2.ª ed.). Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
