# 007 — Formatos de respuesta: Likert, dicotómico, continuo

> [Clase anterior](../006-redaccion-de-items/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../008-ipsativo-vs-normativo/README.md)

**Parte:** 01 — Construcción de instrumentos
**Nivel:** fundamentos · **Horas estimadas:** 3 · **Estado:** `escrita`
**Prerrequisitos:** clases 003 (escalas de medida) y 006.

## Propósito

Elegir cuántas categorías ofrecer y con qué etiquetas no es estética: fija cuánta
información del rasgo sobrevive al registro y qué errores se facilitan.

## Resultados de aprendizaje

1. Comparar formatos dicotómico, politómico (Likert) y continuo.
2. Cuantificar la información que pierde un formato con pocas categorías.
3. Justificar un número de categorías según población y propósito.
4. Reconocer los efectos de la etiqueta del punto medio y de las anclas.

## Conceptos centrales

`dicotómico` · `Likert` · `escala visual analógica` · `punto medio` · `anclaje` · `discretización`

## Fundamentos

| Formato | Ejemplo | Ventaja | Costo |
|---|---|---|---|
| Dicotómico | Sí / No | Rápido, claro | Mucha información perdida |
| Politómico | 1–5 de acuerdo | Equilibrio habitual | Estilos de respuesta (aquiescencia, extremos) |
| Continuo (EVA) | Marca en una línea | Granularidad aparente | Más lento; la precisión real suele ser menor que la aparente |

### Discretizar es perder información

Si el rasgo es continuo y se registra en *k* categorías, la correlación entre la
categoría y el rasgo es un **techo** para cualquier fiabilidad posterior. Con
umbrales equiespaciados y rasgo normal, el laboratorio obtiene:

| Categorías | r con el rasgo |
|---:|---:|
| 2 | 0,797 (teórico √(2/π) = 0,798) |
| 3 | 0,887 |
| 5 | 0,955 |
| 7 | 0,976 |
| 11 | 0,989 |

De 2 a 5 categorías se gana 0,16; de 7 a 11, 0,013. Los rendimientos decrecen y
además las personas no discriminan tantas categorías: más no es mejor.

### Decisiones prácticas

- **Punto medio sí/no.** Con número impar existe «ni de acuerdo ni en desacuerdo»; sirve de refugio para quien no entiende el ítem. Con número par se fuerza una inclinación. No hay una regla universal: depende del constructo.
- **Etiquetas.** Etiquetar todas las categorías ayuda a que signifiquen lo mismo para todos; etiquetar solo los extremos las deja abiertas a interpretación.
- **Población.** Con niños pequeños o segunda lengua, menos categorías y pictogramas.

## Ejemplo resuelto

Se quiere medir perseverancia en estudiantes de 8.º básico. Una escala de 7
categorías añade 0,02 de fidelidad sobre una de 5, pero eleva la carga cognitiva.
Decisión: 4 categorías etiquetadas con caritas y palabras, sin punto medio,
porque se busca evitar la respuesta neutra por falta de comprensión.

## Errores frecuentes

- Tratar una escala de 5 puntos como si fuera de razón (clase 003).
- Cambiar el número de categorías entre ítems de una misma escala.
- Creer que la EVA «es más precisa» por ser continua.

## Limitaciones

El laboratorio usa un rasgo normal y umbrales equiespaciados; con rasgos
asimétricos o umbrales óptimos las cifras cambian. Es una ilustración, no una norma.

## Ejercicios

- **Inicial.** ¿Qué formato elegirías para un cribado de 3 minutos en una sala de espera? Justifica.
- **Intermedio.** Calcula cuánto mejora la fidelidad de 3 a 5 categorías según la tabla.
- **Avanzado.** Modifica `lab.py` para usar un rasgo asimétrico (p. ej. exponencial) y reporta qué pasa con las 2 categorías.

*Soluciones razonadas:* intermedio: 0,955 − 0,887 = 0,068.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/007-formatos-de-respuesta/lab.py
```

## Autoevaluación

1. ¿Por qué la fidelidad de la discretización limita la fiabilidad?
2. ¿Cuándo preferirías un número par de categorías?
3. ¿Qué evidencia necesitarías para preferir EVA sobre Likert de 5?

## Criterios de evaluación

El estudiante elige y defiende un formato citando fidelidad, carga de respuesta y población.

## Bibliografía

- Likert, R. (1932). A technique for the measurement of attitudes. *Archives of Psychology*, 140, 1-55.
- Preston, C. C., & Colman, A. M. (2000). Optimal number of response categories in rating scales. *Acta Psychologica*, 104(1), 1-15.
- Lozano, L. M., García-Cueto, E., & Muñiz, J. (2008). Effect of the number of response categories on the reliability and validity of rating scales. *Methodology*, 4(2), 73-79.
