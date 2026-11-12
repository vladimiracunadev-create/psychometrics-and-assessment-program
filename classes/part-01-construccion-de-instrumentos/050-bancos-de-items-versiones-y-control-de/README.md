# 050 — Bancos de ítems, versiones y control de cambios

> [Índice de la parte](../README.md)

**Parte 01 — Construcción de instrumentos** · Nivel introductorio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 049.

## Objetivos

1. Calcular una huella por ítem.
2. Comparar dos versiones de un banco.
3. Aplicar una regla de comparabilidad por ítems ancla.

## Fundamentos

Un banco necesita identificadores estables y control de cambios: la huella SHA-256 del texto y de la clave detecta cualquier modificación. Reescribir un ítem cambia el estímulo y, si la proporción de ítems ancla es baja, los puntajes de las versiones no se comparan sin equiparación.

Laboratorio (ítems reales de valores-spranger y una versión 2 simulada): 31 intactos, 4 modificados, 1 retirado y 2 nuevos; 86 % de ancla frente a un umbral de ejemplo de 80 %; versión sugerida: menor (1.1.0).

## Ejemplo resuelto

El umbral del 80 % es una regla de ejemplo, no una norma: lo que importa es documentar el criterio y la evidencia de equiparación.

## Errores y límites

- Cambiar ítems sin registro.
- Comparar versiones sin ítems ancla.
- La versión 2 es una simulación; el instrumento real no se modificó.

## Ejercicios

- **Inicial.** ¿Para qué sirve una huella por ítem?
- **Intermedio.** Cambia el umbral al 90 % y revisa la decisión.
- **Avanzado.** Diseña el formato de un registro de cambios de banco.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/050-bancos-de-items-versiones-y-control-de/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del resultado depende de que los datos sean sintéticos? 2. ¿Qué cambiaría con personas reales? 3. ¿Qué límite declararías?
Se logra si el estudiante ejecuta el laboratorio, interpreta las cifras con cautela y declara sus límites.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Kolen, M. J., & Brennan, R. L. (2014). *Test Equating, Scaling, and Linking* (3.ª ed.). Springer. ✅ [DOI](https://doi.org/10.1007/978-1-4939-0317-7)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
