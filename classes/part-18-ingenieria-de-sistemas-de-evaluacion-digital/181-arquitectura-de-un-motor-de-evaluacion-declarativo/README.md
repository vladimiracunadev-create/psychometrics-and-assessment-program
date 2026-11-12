# 181 — Arquitectura de un motor de evaluación declarativo

![Portada de la clase 181](portada.svg)

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 180.

## Objetivos

1. Separar catálogo, administración, puntuación y datos normativos.
2. Declarar un instrumento nuevo solo como datos.
3. Explicar por qué el esquema validado reduce errores.

## Fundamentos

Un motor declarativo trata el instrumento como dato y el cálculo como código genérico. Eso permite que un especialista aporte contenido sin programar y que el código se pruebe una sola vez (Fowler, 2010, sobre lenguajes específicos de dominio). La puntuación de la TCC (clase 004) es la misma para cualquier escala sumativa.

Laboratorio: el catálogo real tiene 5 instrumentos; un instrumento de 3 ítems definido como texto YAML se carga con `cargar_desde_texto` y se puntúa sin modificar Python (respuestas 3, 1 invertido, 3 → media 3,0).

## Ejemplo resuelto

Para un instrumento nuevo de 10 ítems: se escribe el YAML (escalas, opciones, claves), se ejecuta `cargar` y el motor lo rechaza si una clave es inválida. Nunca se escribe una función de puntuación a medida.

## Errores y límites

- Meter reglas de puntuación en el código de cada instrumento.
- Creer que «declarativo» garantiza validez: solo garantiza consistencia técnica.
- El instrumento de demostración no mide nada real.

## Ejercicios

- **Inicial.** ¿Qué capas separa el motor?
- **Intermedio.** Añade al YAML de ejemplo una segunda escala con dos ítems.
- **Avanzado.** Propón cómo declararías una puntuación con ponderaciones sin tocar el motor.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/181-arquitectura-de-un-motor-de-evaluacion-declarativo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- Fowler, M. (2010). *Domain-Specific Languages*. Addison-Wesley. ✅ [DOI](https://doi.org/10.1109/ms.2009.85)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
