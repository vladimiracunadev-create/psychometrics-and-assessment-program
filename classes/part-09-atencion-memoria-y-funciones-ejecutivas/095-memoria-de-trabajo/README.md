# 095 — Memoria de trabajo

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 011 y 094.

## Objetivos

1. Describir la memoria de trabajo y las tareas de amplitud.
2. Comparar reglas de puntuación.
3. Reconocer que la regla de puntuación afecta la fiabilidad.

## Fundamentos

La memoria de trabajo mantiene y manipula información de forma temporal (Baddeley y Hitch, 1974). Las **tareas de amplitud** (complex span) piden recordar elementos mientras se hace otra tarea. Conway et al. (2005) revisan cómo puntuarlas: *todo-o-nada* (solo ensayos perfectos), *crédito parcial* (proporción de elementos correctos) y *amplitud máxima*.

Laboratorio (600 personas, 12 ensayos de tamaño 2 a 7, capacidad verdadera conocida):

| Puntuación | Fiabilidad por mitades (SB) | r con la capacidad verdadera |
|---|---:|---:|
| Todo-o-nada | 0,686 | 0,849 |
| Crédito parcial | 0,787 | 0,816 |
| Amplitud máxima | 0,652 | 0,748 |

El crédito parcial es el más fiable; la amplitud máxima, la menos. En esta simulación el todo-o-nada se acerca algo más a la capacidad verdadera porque el recuerdo de lo sostenido es casi determinístico: el resultado depende del modelo de respuesta y se verifica con datos reales.

## Ejemplo resuelto

Ensayos de tamaño 4, 5 y 6 con 4, 3 y 5 elementos correctos: parcial = (4/4 + 3/5 + 5/6)/3 = 0,81; todo-o-nada = 4 (solo el ensayo perfecto de tamaño 4).

## Errores y límites

- Interpretar la amplitud de dígitos (directa) como memoria de trabajo: la inversa y las tareas complejas involucran más control ejecutivo.
- Ignorar las estrategias (agrupar, repasar).
- Aplicar el mismo criterio en niños y adultos sin evidencia.
- Los parámetros son ilustrativos.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre memoria a corto plazo y de trabajo?
- **Intermedio.** Calcula el crédito parcial de 3/3, 4/5 y 2/6 → (1 + 0,8 + 0,33)/3 = 0,71.
- **Avanzado.** Cambia la probabilidad de recordar lo no sostenido (0,25) a 0,05 y observa el cambio.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/095-memoria-de-trabajo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué regla de puntuación elegirías y por qué? 2. ¿Cómo evitas efectos de fatiga? 3. ¿Qué otras tareas medirían el mismo constructo?
Se logra si el estudiante compara reglas con evidencia de fiabilidad y validez.

## Bibliografía

- Baddeley, A. D., & Hitch, G. (1974). Working memory. En G. H. Bower (Ed.), *The Psychology of Learning and Motivation* (Vol. 8). Academic Press.
- Conway, A. R. A., Kane, M. J., Bunting, M. F., Hambrick, D. Z., Wilhelm, O., & Engle, R. W. (2005). Working memory span tasks: A methodological review and user's guide. *Psychonomic Bulletin & Review*, 12(5), 769-786.
