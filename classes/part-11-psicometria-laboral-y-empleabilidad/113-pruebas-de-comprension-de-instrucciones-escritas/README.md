# 113 — Pruebas de comprensión de instrucciones escritas

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 084 y 095.

## Objetivos

1. Diseñar ítems originales de seguimiento de instrucciones con clave calculada.
2. Controlar la dificultad por número de pasos y condicionales.
3. Delimitar qué mide (y qué no) una prueba de este tipo.

## Fundamentos

Comprender y ejecutar instrucciones escritas es una demanda frecuente en el trabajo. Una prueba puede mezclar varios constructos: lectura, memoria de trabajo y razonamiento condicional. Para separar la dificultad **de diseño** (pasos, condicionales) de la dificultad de lectura se controlan ambas (clase 084). Aquí los ítems son originales (no replican ninguna prueba comercial) y su respuesta se obtiene ejecutando las instrucciones con un intérprete, **verificado por una segunda implementación independiente**.

Laboratorio (semilla fija; 8 ítems con 2 a 5 pasos y 0 a 3 condicionales):

| Pasos | Condicionales | Ejemplo (resumido) | Respuesta |
|---:|---:|---|---:|
| 2 | 0 | Parta con 7. Multiplíquelo por 3. Multiplíquelo por 2. | 42 |
| 3 | 1 | Parta con 6. Si es impar, sume 2; si es par, reste 6. Sume 5. Sume 7. | 12 |

Concordancia entre intérprete y verificador: **8 / 8**.

## Ejemplo resuelto

«Parta con 6. Si el número es impar, súmele 2; si es par, réstele 6. Súmele 5. Súmele 7.»: 6 es par → 0; 0 + 5 = 5; 5 + 7 = 12.

## Errores y límites

- Declarar «difícil» un ítem por su número de pasos sin datos (clase 010).
- Contaminar el constructo con memoria de trabajo: más pasos exigen retener más (clase 095).
- Usar una prueba de instrucciones numéricas para un puesto sin relación con ese tipo de tarea.
- Evidencia de validez para el puesto: análisis de puestos (clase 111).

## Ejercicios

- **Inicial.** Calcula: «Parta con 4. Sume 3. Multiplique por 2.» → 14.
- **Intermedio.** Agrega una instrucción condicional y recalcula.
- **Avanzado.** Implementa un modo «con distractores textuales» y verifica que la respuesta no cambia.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/113-pruebas-de-comprension-de-instrucciones-escritas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué varianza irrelevante agrega la redacción? 2. ¿Cómo calibrarías la dificultad con datos? 3. ¿Qué evidencia para el puesto necesitas?
Se logra si el estudiante genera y verifica ítems y limita lo que la prueba permite concluir.

## Bibliografía

- Embretson, S. E. (1998). A cognitive design system approach to generating valid tests. *Psychological Methods*, 3(3), 380-396. ✅ [DOI](https://doi.org/10.1037/1082-989x.3.3.380)
- Haladyna, T. M., & Rodriguez, M. C. (2013). *Developing and Validating Test Items*. Routledge. ✅ [DOI](https://doi.org/10.4324/9780203850381)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
