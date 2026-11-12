# 068 — Modelos de respuesta graduada

> [Índice de la parte](../README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 007 y 028.

## Objetivos

1. Entender el modelo de respuesta graduada (Samejima) para ítems Likert.
2. Calcular probabilidades por categoría y la puntuación esperada.
3. Diagnosticar categorías mal diseñadas.

## Fundamentos

Para un ítem con categorías ordenadas 1 a 5, la probabilidad acumulada de responder la categoría k o más es P*(k) = logística(a·(θ − b_k)), con b₁ < b₂ < b₃ < b₄ (umbrales), y P(k) = P*(k) − P*(k + 1) (Samejima, 1969).

Laboratorio (a = 1,5; umbrales −1,5; −0,5; 0,5; 1,5):

| θ | cat 1 | cat 2 | cat 3 | cat 4 | cat 5 | Puntuación esperada |
|---:|---:|---:|---:|---:|---:|---:|
| −2 | 0,68 | 0,23 | 0,07 | 0,02 | 0,01 | 1,44 |
| 0 | 0,10 | 0,23 | 0,36 | 0,23 | 0,10 | 3,00 |
| 2 | 0,01 | 0,02 | 0,07 | 0,23 | 0,68 | 4,56 |

Las frecuencias simuladas coinciden con las del modelo (0,157; 0,207; 0,266; 0,205; 0,165 frente a 0,161; 0,206; 0,260; 0,208; 0,165).

## Ejemplo resuelto

θ = 0: P*(2) = logística(1,5·1,5) = 0,905; P*(3) = logística(0,75) = 0,679; P(cat 2) = 0,905 − 0,679 = 0,226 → 0,23.

## Errores y límites

- Tratar las categorías como equidistantes.
- Ignorar categorías que nunca son las más probables (señal para fusionarlas).
- El modelo es unidimensional: exige estructura simple (parte 04).

## Ejercicios

- **Inicial.** ¿Por qué las probabilidades por categoría suman 1?
- **Intermedio.** ¿Cuál es la categoría más probable en θ = 1? La 4 (0,36).
- **Avanzado.** Desordena dos umbrales en `lab.py` y observa qué categoría desaparece.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/068-modelos-de-respuesta-graduada/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diferencia hay entre el GRM y el crédito parcial? 2. ¿Cuántas categorías te parecen útiles y por qué? 3. ¿Cómo se relaciona con la clase 007?
Se logra si el estudiante calcula probabilidades y diagnostica categorías.

## Bibliografía

- Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement*, 34(4, Pt. 2), No. 17.
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum.
