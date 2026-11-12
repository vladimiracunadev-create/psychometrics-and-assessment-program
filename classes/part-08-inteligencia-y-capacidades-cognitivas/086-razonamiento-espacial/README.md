# 086 — Razonamiento espacial

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 052 y 081.

## Objetivos

1. Describir la rotación mental y su medición.
2. Estimar la pendiente individual tiempo-ángulo y su fiabilidad.
3. Combinar velocidad y precisión.

## Fundamentos

Shepard y Metzler (1971) mostraron que el tiempo para decidir si dos figuras tridimensionales son iguales aumenta casi linealmente con el ángulo de rotación. La **pendiente** (ms por grado) se interpreta como velocidad de rotación mental; el **intercepto**, como procesos no espaciales. Las capacidades espaciales son un grupo de habilidades (visualización, rotación, orientación; Linn y Petersen, 1985).

Laboratorio (200 personas, 8 ángulos × 10 ensayos):

| Medida | Valor |
|---|---:|
| Pendiente verdadera media | 5,81 ms/grado |
| Pendiente estimada (mitad pares) | 5,82 ms/grado |
| Fiabilidad de la pendiente individual | r mitades 0,81; Spearman-Brown 0,90 |
| Error a 0° / 90° / 180° | 0,045 / 0,117 / 0,169 |

El efecto del ángulo es nítido y, con 80 ensayos por mitad, la pendiente es razonablemente fiable.

## Ejemplo resuelto

Con intercepto 900 ms y pendiente 6 ms/grado, el tiempo esperado a 135° es 900 + 810 = 1 710 ms.

## Errores y límites

- La pendiente es una medida **diferencial**: con pocos ensayos es poco fiable (clase 097).
- Ignorar errores: quien responde rápido y mal parece veloz.
- Comparar entre dispositivos sin calibrar la medición del tiempo (clase 093).
- Las diferencias de grupo en tareas espaciales dependen de entrenamiento y contexto.

## Ejercicios

- **Inicial.** ¿Qué indica la pendiente?
- **Intermedio.** Calcula el tiempo esperado a 90° con intercepto 800 y pendiente 5 → 1 250 ms.
- **Avanzado.** Reduce a 3 ensayos por ángulo y reporta la fiabilidad de la pendiente.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/086-razonamiento-espacial/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se usa el ángulo efectivo mínimo (≤ 180°)? 2. ¿Cómo combinas velocidad y precisión? 3. ¿Qué entrenamiento mejora la rotación?
Se logra si el estudiante estima pendiente e intercepto y reporta su fiabilidad.

## Bibliografía

- Shepard, R. N., & Metzler, J. (1971). Mental rotation of three-dimensional objects. *Science*, 171(3972), 701-703.
- Linn, M. C., & Petersen, A. C. (1985). Emergence and characterization of sex differences in spatial ability: A meta-analysis. *Child Development*, 56(6), 1479-1498.
