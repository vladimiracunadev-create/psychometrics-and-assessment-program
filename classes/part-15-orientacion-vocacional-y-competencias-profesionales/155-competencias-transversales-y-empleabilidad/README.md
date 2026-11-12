# 155 — Competencias transversales y empleabilidad

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 111 y 115.

## Objetivos

1. Acumular evidencia sobre una competencia con una actualización bayesiana.
2. Calcular cuántas tareas se necesitan para un criterio de decisión.
3. Declarar el criterio de «insignia» o certificación de competencias.

## Fundamentos

Las competencias transversales (comunicación, trabajo en equipo, resolución de problemas) se evidencian en **tareas** situadas. El enfoque de diseño centrado en la evidencia (Mislevy, Steinberg y Almond, 2003) formaliza cómo cada observación cambia lo que creemos del nivel de competencia (redes bayesianas; Almond et al., 2015). Con tareas poco discriminantes, se necesitan muchas para separar niveles contiguos.

Laboratorio (3 niveles; P(tarea bien) = 0,30; 0,60; 0,90, **supuestos**; criterio: posterior ≥ 90 %):

| Medida | Valor |
|---|---:|
| Tareas necesarias en promedio | 10,6 |
| Clasificados en un nivel equivocado | 8,7 % |
| Sin decisión tras 20 tareas | 13,1 % |

Ejemplo (estudiante de nivel intermedio): tras 8 tareas, posterior intermedio = 0,57; avanzado = 0,40.

## Ejemplo resuelto

Previo uniforme y una tarea bien resuelta: posterior ∝ (0,30; 0,60; 0,90) → (0,17; 0,33; 0,50).

## Errores y límites

- Decidir un nivel con 2 o 3 tareas.
- Tratar el 90 % como acierto garantizado (depende del modelo).
- Evaluar competencias transversales solo con cuestionarios de autopercepción.
- Parámetros supuestos; en la práctica se calibran con datos.

## Ejercicios

- **Inicial.** ¿Qué es una probabilidad posterior?
- **Intermedio.** Con previo uniforme y dos tareas mal resueltas: ∝ (0,49; 0,16; 0,01) → (0,74; 0,24; 0,02).
- **Avanzado.** Cambia P(bien) del nivel intermedio a 0,70 y observa tareas necesarias.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/155-competencias-transversales-y-empleabilidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia mínima exiges para una insignia? 2. ¿Cómo equilibras costo y precisión? 3. ¿Cómo informas la incertidumbre?
Se logra si el estudiante modela evidencia acumulada y define un criterio de decisión.

## Bibliografía

- Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003). On the structure of educational assessments. *Measurement: Interdisciplinary Research and Perspectives*, 1(1), 3-62. ✅ [DOI](https://doi.org/10.1207/s15366359mea0101_02)
- Almond, R. G., Mislevy, R. J., Steinberg, L. S., Yan, D., & Williamson, D. M. (2015). *Bayesian Networks in Educational Assessment*. Springer. ✅ [DOI](https://doi.org/10.1007/978-1-4939-2125-6)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
