# 011 — La teoría clásica: puntaje verdadero y error

> [Índice de la parte](../README.md) · [Siguiente](../012-consistencia-interna-alfa/README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 004, 009 y 010.

## Objetivos

1. Enunciar X = T + E y sus supuestos.
2. Derivar var(X) = var(T) + var(E) y definir fiabilidad como var(T)/var(X).
3. Explicar por qué la fiabilidad es propiedad de los puntajes en una población, no del test.
4. Reconocer que T nunca se observa: la fiabilidad se estima.

## Contexto y fundamentos

Spearman (1904) mostró que correlacionar medidas con error subestima la relación entre los atributos; Novick (1966) y Lord y Novick (1968) formalizaron el modelo.

```
X = T + E      E(E) = 0      cov(T, E) = 0      cov(E₁, E₂) = 0
var(X) = var(T) + var(E)
ρ = var(T) / var(X) = 1 − var(E) / var(X)
```

**T** es el promedio que obtendría la persona en infinitas aplicaciones equivalentes. No es «la verdad» sobre el constructo: un test sesgado tiene un T sesgado y perfectamente fiable. Dos formas **paralelas** correlacionan ρ; por eso fiabilidad = correlación entre formas.

Laboratorio (semilla fija, N = 20 000):

| sd(E) | var(T) | var(E) | var(X) | var(T)/var(X) | r(X, X′) |
|---:|---:|---:|---:|---:|---:|
| 0,5 | 1,003 | 0,254 | 1,246 | 0,805 | 0,799 |
| 1,0 | 1,004 | 1,006 | 2,015 | 0,498 | 0,499 |
| 2,0 | 1,003 | 3,989 | 5,017 | 0,200 | 0,198 |

## Ejemplo resuelto

Test con DE observada 10 y fiabilidad 0,84: var(X) = 100, var(T) = 84, var(E) = 16, DE del error = 4 (error típico de medida, clase 015).

## Errores frecuentes y límites

- Decir «este test tiene fiabilidad 0,90» como constante: en un grupo homogéneo var(T) baja y la fiabilidad también.
- Confundir fiabilidad con validez (parte 03).
- Suponer que E siempre es aleatorio: el sesgo constante de un evaluador entra en T.
- El modelo asume un error homogéneo para todos; la teoría de la generalizabilidad separa fuentes de error y la TRI (parte 05) deja que la precisión varíe con el nivel del rasgo.

## Ejercicios

- **Inicial.** var(T) = 6, var(E) = 2: ¿fiabilidad? → 0,75.
- **Intermedio.** Fiabilidad 0,60: ¿qué porcentaje de la varianza es error? → 40 %.
- **Avanzado.** En `lab.py` correlaciona E con T y explica por qué var(T)/var(X) deja de coincidir con r(X, X′).

## Laboratorio

```bash
python classes/part-02-fiabilidad/011-teoria-clasica-del-error/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué T no equivale al nivel «real» en el constructo? 2. ¿Qué pasa con la fiabilidad en un grupo muy homogéneo? 3. Da un error sistemático que el modelo confunde con T.
Se logra la clase si el estudiante deriva la descomposición, calcula fiabilidad desde varianzas y distingue fiabilidad de validez.

## Bibliografía

- Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72-101.
- Novick, M. R. (1966). The axioms and principal results of classical test theory. *Journal of Mathematical Psychology*, 3(1), 1-18.
- Lord, F. M., & Novick, M. R. (1968). *Statistical Theories of Mental Test Scores*. Addison-Wesley.
