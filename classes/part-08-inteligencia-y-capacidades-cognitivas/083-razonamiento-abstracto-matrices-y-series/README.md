# 083 — Razonamiento abstracto: matrices y series

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 5 h · Estado `escrita`
**Prerrequisitos:** clases 010 y 081.

## Objetivos

1. Describir las reglas que hacen difícil un ítem de matrices o series.
2. Generar ítems originales con solución única verificable.
3. Evitar el uso de ítems protegidos: se diseñan los propios.

## Fundamentos

Las tareas de razonamiento abstracto piden inducir una regla y aplicarla. En matrices, la dificultad se explica por el número y tipo de reglas y la carga de memoria de trabajo (Carpenter, Just y Shell, 1990). La **generación automática de ítems** (Embretson, 1998; Gierl y Haladyna, 2013) define la regla, genera instancias y verifica la solución; permite bancos originales y auditables, y calibrar la dificultad con el número de reglas.

Laboratorio: generador propio de series con cuatro reglas (aritmética, geométrica, alternada, de segundo orden) y un resolutor independiente que enumera las reglas candidatas. Resultado: **12 de 12** ítems con solución única. Los distractores se construyen desde errores típicos (continuar la diferencia, duplicar el último término).

| Tipo | Serie visible | Respuesta |
|---|---|---:|
| aritmética | 9, 14, 19, 24, 29, 34 | 39 |
| geométrica | 3, 6, 12, 24, 48 | 96 |
| alternada | 6, 50, 10, 52, 14, 54, 18 | 56 |
| segundo orden | 7, 8, 10, 13, 17, 22 | 28 |

## Ejemplo resuelto

Serie 7, 8, 10, 13, 17, 22: diferencias 1, 2, 3, 4, 5 → la siguiente diferencia es 6 → 28.

## Errores y límites

- Declarar «difícil» un ítem por intuición: la dificultad se estima con datos.
- Ítems con dos explicaciones válidas.
- La serie geométrica puede aparecer duplicada con la semilla; un banco real se deduplica.
- Un banco generado no está validado: necesita piloto y análisis de ítems (clase 010).

## Ejercicios

- **Inicial.** Completa 2, 6, 18, 54, ?  → 162.
- **Intermedio.** Diseña una serie con dos reglas entrelazadas y verifica su unicidad.
- **Avanzado.** Añade una regla (Fibonacci) y actualiza el resolutor.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/083-razonamiento-abstracto-matrices-y-series/lab.py
```

## Autoevaluación y criterios

1. ¿Qué ventaja y qué riesgo tiene la generación automática? 2. ¿Cómo estimarías la dificultad de un ítem generado? 3. ¿Por qué no copiar ítems de pruebas comerciales?
Se logra si el estudiante genera ítems originales y los verifica.

## Bibliografía

- Carpenter, P. A., Just, M. A., & Shell, P. (1990). What one intelligence test measures: A theoretical account of the processing in the Raven Progressive Matrices Test. *Psychological Review*, 97(3), 404-431. ✅ [DOI](https://doi.org/10.1037/0033-295x.97.3.404)
- Embretson, S. E. (1998). A cognitive design system approach to generating valid tests. *Psychological Methods*, 3(3), 380-396. ✅ [DOI](https://doi.org/10.1037/1082-989x.3.3.380)
- Gierl, M. J., & Haladyna, T. M. (Eds.) (2013). *Automatic Item Generation*. Routledge. ✅ [DOI](https://doi.org/10.4324/9780203803912)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
