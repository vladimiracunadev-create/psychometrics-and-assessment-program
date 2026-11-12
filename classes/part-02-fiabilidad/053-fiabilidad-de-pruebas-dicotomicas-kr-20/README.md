# 053 — Fiabilidad de pruebas dicotómicas: KR-20

> [Índice de la parte](../README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 3 h · Estado `escrita`
**Prerrequisitos:** clases 010 y 012.

## Objetivos

1. Calcular KR-20 desde las proporciones de acierto.
2. Demostrar que equivale a alfa en ítems 0/1.
3. Explicar el efecto de la dificultad sobre la fiabilidad.

## Fundamentos

Kuder y Richardson (1937) derivaron, para ítems acierto/error, lo que Cronbach (1951) generalizó:

```
KR-20 = k/(k−1) · ( 1 − Σ pᵢqᵢ / var(total) )          qᵢ = 1 − pᵢ
```

La varianza de un ítem 0/1 es pq, así que KR-20 es alfa con varianza poblacional. **KR-21** supone igual dificultad en todos los ítems y subestima si no es así.

Laboratorio (20 ítems, N = 4 000):

| Prueba | p media | KR-20 | Alfa |
|---|---:|---:|---:|
| Dificultad media (b = 0) | 0,50 | 0,846 | 0,846 |
| Dispersa (b de −2 a 2) | 0,50 | 0,811 | 0,811 |
| Toda fácil (b = −2,5) | 0,92 | 0,712 | 0,712 |

La prueba fácil rinde menos con el mismo número de ítems: con p cerca de 1 casi no hay varianza que covariar.

## Ejemplo resuelto

3 ítems con p = 0,5; 0,6; 0,7. Σpq = 0,25 + 0,24 + 0,21 = 0,70. Con var(total) = 1,5: KR-20 = 3/2 · (1 − 0,70/1,5) = 0,80.

## Errores y límites

- Aplicar KR-20 a ítems politómicos (usar alfa).
- Interpretar un KR-20 alto como prueba de unidimensionalidad (igual que alfa).
- Ignorar que la adivinación (opción múltiple) agrega varianza de error.

## Ejercicios

- **Inicial.** ¿Por qué un ítem con p = 1 no aporta a KR-20?
- **Intermedio.** Calcula KR-20 con k = 4, Σpq = 0,8, var = 2 → 4/3 · (1 − 0,4) = 0,80.
- **Avanzado.** Aumenta a 40 ítems fáciles en `lab.py`: ¿cuánto sube KR-20?

## Laboratorio

```bash
python classes/part-02-fiabilidad/053-fiabilidad-de-pruebas-dicotomicas-kr-20/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo difieren KR-20 y KR-21? 2. ¿Qué prefieres, ítems fáciles o de dificultad media, para fiabilidad? 3. ¿Qué cambia en una prueba de selección múltiple?
Se logra si el estudiante calcula KR-20 y relaciona la dificultad con la precisión.

## Bibliografía

- Kuder, G. F., & Richardson, M. W. (1937). The theory of the estimation of test reliability. *Psychometrika*, 2(3), 151-160.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16, 297-334.
