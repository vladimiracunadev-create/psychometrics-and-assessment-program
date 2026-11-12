# 037 — Validez ecológica y generalización

> [Índice de la parte](../README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 031.

## Objetivos

1. Explicar la generalización de un puntaje a otras tareas, ocasiones y contextos.
2. Estimar componentes de varianza en un diseño personas × tareas.
3. Calcular un coeficiente de generalizabilidad y decidir cuántas tareas se necesitan.

## Fundamentos

Un puntaje obtenido en una tarea de laboratorio sirve si generaliza a las situaciones de interés (validez ecológica). La **teoría de la generalizabilidad** (Cronbach et al., 1972) descompone la varianza en fuentes: personas, tareas, interacción persona × tarea y error. Para n tareas:

```
G(n) = var_persona / ( var_persona + var_(persona×tarea, error) / n )
```

Laboratorio (400 personas × 12 tareas; varianza real de persona 1,00 y persona × tarea + error 1,44):

- estimado: persona 0,92; interacción + error 1,42.

| Tareas | G |
|---:|---:|
| 1 | 0,394 |
| 2 | 0,566 |
| 4 | 0,723 |
| 8 | 0,839 |
| 12 | 0,887 |

Con una sola tarea, menos de la mitad de la varianza es «persona». Generalizar a otras situaciones exige **muestrear situaciones**, no solo ítems.

## Ejemplo resuelto

var_persona = 1, var_resto = 3. Con 1 tarea G = 0,25; con 6 tareas G = 1/(1+0,5) = 0,667; para G = 0,80 se necesitan n = 12 tareas.

## Errores y límites

- Medir en una sola situación y generalizar a «el trabajo» o «el aula».
- Confundir realismo aparente (cara) con validez ecológica demostrada.
- El diseño del laboratorio ignora la varianza de ocasiones y de evaluadores; en la práctica se estudian varias facetas a la vez.

## Ejercicios

- **Inicial.** ¿Qué fuentes de varianza ve la teoría clásica como un único «error»?
- **Intermedio.** var_persona = 2, var_resto = 3: G(3) = 2/(2+1) = 0,667.
- **Avanzado.** Cambia `SD_PXT` a 0,6 en `lab.py` y observa cuántas tareas bastan para G = 0,80.

## Laboratorio

```bash
python classes/part-03-validez/037-validez-ecologica-y-generalizacion/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué más ítems de la misma tarea no resuelven la generalización? 2. ¿Qué facetas muestrear en una evaluación de desempeño laboral? 3. ¿Cómo informarías este límite?
Se logra si el estudiante estima G y decide el número de tareas.

## Bibliografía

- Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). *The Dependability of Behavioral Measurements*. Wiley. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Shavelson, R. J., & Webb, N. M. (1991). *Generalizability Theory: A Primer*. Sage. ⚠️ existe, pero Crossref registra 2004 (¿otra edición?; [DOI](https://doi.org/10.1002/0471667196.ess1050))
- Brennan, R. L. (2001). *Generalizability Theory*. Springer. ✅ [DOI](https://doi.org/10.1007/978-1-4757-3456-0)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
