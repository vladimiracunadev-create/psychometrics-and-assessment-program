# 143 — Escritura y producción textual con rúbricas

![Portada de la clase 143](portada.svg)

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 029 y 037.

## Objetivos

1. Diseñar una rúbrica analítica.
2. Planificar cuántas tareas y jueces se necesitan (estudio D).
3. Calcular el coeficiente de generalizabilidad.

## Fundamentos

Las rúbricas aumentan la transparencia y el acuerdo, pero su fiabilidad depende del diseño (Jonsson y Svingby, 2007). Con un diseño personas × tareas × jueces, el coeficiente de generalizabilidad relativo es

```
G = σ²_p / ( σ²_p + σ²_pt/n_t + σ²_pj/n_j + σ²_ptj,e/(n_t·n_j) )
```

(Shavelson y Webb, 1991; Brennan, 2001). Componentes **supuestos** en el laboratorio: persona 1,00; persona × tarea 0,80; persona × juez 0,30; residual 0,50.

| Tareas \ Jueces | 1 | 2 | 3 |
|---:|---:|---:|---:|
| 1 | 0,38 | 0,45 | 0,48 |
| 2 | 0,51 | 0,60 | 0,63 |
| 4 | 0,62 | 0,71 | 0,75 |
| 6 | 0,66 | 0,75 | 0,79 |

Simulación con 2 tareas × 2 jueces: G teórico 0,60; r² simulado 0,59.

## Ejemplo resuelto

2 tareas y 2 jueces: 1/(1 + 0,80/2 + 0,30/2 + 0,50/4) = 1/(1 + 0,4 + 0,15 + 0,125) = 0,60.

## Errores y límites

- Evaluar con una sola tarea.
- Añadir jueces cuando la mayor fuente de error es la tarea.
- Rúbricas con descriptores vagos.
- Los componentes de varianza se estiman con un estudio G real.

## Ejercicios

- **Inicial.** ¿Qué es un estudio D?
- **Intermedio.** Calcula G con 3 tareas y 1 juez → 1/(1 + 0,267 + 0,30 + 0,167) = 0,58.
- **Avanzado.** Reduce σ²_pt a 0,4 en `lab.py` y redibuja la tabla.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/143-escritura-y-produccion-textual-con-rubricas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué criterios incluiría tu rúbrica? 2. ¿Cómo entrenas a los jueces? 3. ¿Cómo das retroalimentación formativa?
Se logra si el estudiante diseña una evaluación de escritura con un G objetivo.

## Bibliografía

- Jonsson, A., & Svingby, G. (2007). The use of scoring rubrics: Reliability, validity and educational consequences. *Educational Research Review*, 2(2), 130-144. ✅ [DOI](https://doi.org/10.1016/j.edurev.2007.05.002)
- Shavelson, R. J., & Webb, N. M. (1991). *Generalizability Theory: A Primer*. Sage. ⚠️ existe, pero Crossref registra 2004 (¿otra edición?; [DOI](https://doi.org/10.1002/0471667196.ess1050))
- Brennan, R. L. (2001). *Generalizability Theory*. Springer. ✅ [DOI](https://doi.org/10.1007/978-1-4757-3456-0)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
