# 098 — Planificación y control ejecutivo

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 5 h · Estado `escrita`
**Prerrequisitos:** clases 083 y 097.

## Objetivos

1. Calcular la dificultad objetiva de problemas de planificación.
2. Generar y calificar automáticamente un banco original.
3. Interpretar el exceso de movimientos como indicador de plan.

## Fundamentos

Las tareas tipo Torre de Hanoi o Torre de Londres piden planificar una secuencia de movimientos para llegar a una meta. La **dificultad objetiva** es el número mínimo de movimientos, calculable con una búsqueda en anchura (BFS). El **exceso** de movimientos sobre el óptimo es un indicador de la calidad del plan. Es un ejemplo original, no una prueba normada.

Laboratorio:

| Discos | Configuraciones | Óptimo máximo | Exceso medio (horizonte h = 1 / 3 / 6) |
|---:|---:|---:|---|
| 3 | 27 | 7 | 92,9 / 22,5 / 0,5 |
| 4 | 81 | 15 | 238,4 / 203,1 / 115,0 |

El «planificador miope» solo ve la solución si está a h movimientos o menos; si no, se mueve al azar (tope de 400 movimientos). Con horizonte mayor el exceso cae. La distribución de dificultad tiene 16 configuraciones a 15 movimientos con 4 discos.

## Ejemplo resuelto

Con 3 discos hay 3³ = 27 estados; el estado más lejano de la meta está a 7 movimientos (2³ − 1).

## Errores y límites

- Asumir que la dificultad crece linealmente con el número de discos: crece exponencialmente.
- Interpretar el exceso como «déficit ejecutivo» sin descartar impulsividad, motivación o comprensión de reglas.
- El planificador simulado es una caricatura; los humanos usan estrategias distintas.
- La planificación no se mide con una sola tarea (clase 097).

## Ejercicios

- **Inicial.** ¿Cuántos estados tiene el problema de 4 discos? → 81.
- **Intermedio.** ¿Cuántos movimientos óptimos tiene el caso más difícil de 4 discos? → 15.
- **Avanzado.** Agrega la restricción de «no deshacer el último movimiento» y observa el exceso.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/098-planificacion-y-control-ejecutivo/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo calibrarías la dificultad de un banco de problemas? 2. ¿Qué otras explicaciones tiene un mal desempeño? 3. ¿Cómo estandarizar las instrucciones?
Se logra si el estudiante calcula dificultades objetivas y las usa para diseñar un banco.

## Bibliografía

- Shallice, T. (1982). Specific impairments of planning. *Philosophical Transactions of the Royal Society of London B*, 298, 199-209. ✅ [DOI](https://doi.org/10.1098/rstb.1982.0082)
- Miyake, A., et al. (2000). The unity and diversity of executive functions and their contributions to complex "frontal lobe" tasks. *Cognitive Psychology*, 41(1), 49-100. ✅ [DOI](https://doi.org/10.1006/cogp.1999.0734)
- Hinz, A., & Klavžar, S. (2013). *The Tower of Hanoi — Myths and Maths*. Birkhäuser. ✅ [DOI](https://doi.org/10.1007/978-3-0348-0237-6)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
