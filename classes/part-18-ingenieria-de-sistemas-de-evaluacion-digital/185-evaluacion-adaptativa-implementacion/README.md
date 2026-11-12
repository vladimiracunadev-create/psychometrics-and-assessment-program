# 185 — Evaluación adaptativa: implementación

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 184.

## Objetivos

1. Implementar un CAT con restricciones de contenido.
2. Medir el costo de precisión del balance.
3. Justificar el balance como decisión de validez.

## Fundamentos

Un CAT elige el ítem de mayor información en la estimación actual (clase 059). Sin restricciones puede concentrar el test en el área más informativa; las cuotas de contenido resguardan la validez de contenido a costa de algo de precisión (van der Linden & Glas, 2010).

Laboratorio (banco de 240 ítems 2PL, 3 áreas, test de 15 ítems, 150 examinados): CAT puro RMSE 0,309 con ítems [0,0; 0,3; 14,7] por área y 100 % de los tests con un área sobre 8; CAT balanceado RMSE 0,338 con [5; 5; 5].

## Ejemplo resuelto

El CAT puro es más preciso, pero un test con 14,7 de 15 ítems de una sola área no mide el constructo definido. Se prefiere el balanceado aunque pierda 0,03 de RMSE.

## Errores y límites

- Optimizar solo la precisión.
- Olvidar la exposición de ítems (clase 060).
- Banco y examinados sintéticos.

## Ejercicios

- **Inicial.** ¿Por qué se limita cada área a un tercio?
- **Intermedio.** Cambia el largo del test a 21 y observa el RMSE.
- **Avanzado.** Propón una restricción adicional de exposición máxima.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/185-evaluacion-adaptativa-implementacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- van der Linden, W. J., & Glas, C. A. W. (Eds.) (2010). *Elements of Adaptive Testing*. Springer. ✅ [DOI](https://doi.org/10.1007/978-0-387-85461-8)
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
