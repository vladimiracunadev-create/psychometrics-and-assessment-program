# 094 — Memoria visual y auditiva

![Portada de la clase 094](portada.svg)

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 026 y 091.

## Objetivos

1. Interpretar la curva de posición serial (primacía y recencia).
2. Entender el efecto de modalidad.
3. Separar recuerdo inmediato y diferido.

## Fundamentos

En el recuerdo libre de una lista, las primeras palabras se recuerdan mejor (**primacía**, asociada a repaso y almacenamiento a largo plazo) y las últimas también (**recencia**, asociada a memoria a corto plazo) (Glanzer y Cunitz, 1966). Con presentación auditiva la recencia suele ser mayor que con presentación visual (efecto de modalidad). El recuerdo diferido, tras tarea de interferencia, elimina la recencia.

Laboratorio (modelo simple de dos componentes; parámetros ilustrativos):

| Posición | 1 | 5 | 10 | 12 | 15 |
|---|---:|---:|---:|---:|---:|
| Visual | 0,62 | 0,45 | 0,31 | 0,54 | 0,56 |
| Auditiva | 0,60 | 0,43 | 0,35 | 0,65 | 0,75 |

Palabras recordadas (de 15): visual 7,20; auditiva 7,72.

## Ejemplo resuelto

Sumando las probabilidades de las 15 posiciones se obtiene la media esperada de palabras recordadas; la diferencia entre modalidades (0,5 palabras) proviene casi toda de las últimas cuatro posiciones.

## Errores y límites

- Atribuir diferencias de modalidad al «estilo de aprendizaje» de la persona: la evidencia de estilos como guía de enseñanza es débil (Pashler et al., 2008).
- Comparar puntajes totales sin distinguir inmediato y diferido.
- Pruebas que mezclan material verbal y visual sin separar los procesos.

## Ejercicios

- **Inicial.** ¿Qué proceso explica la recencia?
- **Intermedio.** Si la recencia desaparece tras 30 s de interferencia, ¿qué posiciones se afectan más? Las últimas.
- **Avanzado.** Cambia el parámetro de repaso (0,93) en `lab.py` y describe la primacía.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/094-memoria-visual-y-auditiva/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué separar inmediato y diferido? 2. ¿Qué material usarías en niños pequeños? 3. ¿Qué indica una curva plana?
Se logra si el estudiante interpreta la curva y distingue procesos.

## Bibliografía

- Glanzer, M., & Cunitz, A. R. (1966). Two storage mechanisms in free recall. *Journal of Verbal Learning and Verbal Behavior*, 5(4), 351-360. ✅ [DOI](https://doi.org/10.1016/s0022-5371(66)80044-0)
- Baddeley, A. D., & Hitch, G. (1974). Working memory. En G. H. Bower (Ed.), *The Psychology of Learning and Motivation* (Vol. 8). Academic Press. ✅ [DOI](https://doi.org/10.1016/s0079-7421(08)60452-1)
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3), 105-119. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
