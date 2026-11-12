# 052 — Correlación de Pearson, Spearman y sus supuestos

> [Índice de la parte](../README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 003, 011 y 051.

## Objetivos

1. Calcular e interpretar Pearson y Spearman.
2. Reconocer el efecto de valores extremos, no linealidad y restricción de rango.
3. Elegir el coeficiente según el nivel de medida y la forma de la relación.

## Fundamentos

**Pearson** mide asociación **lineal**; **Spearman** es Pearson sobre rangos (con rangos promedio en los empates) y mide asociación **monótona**. Ambos resumen en un número lo que un diagrama de dispersión muestra completo (Anscombe, 1973): se grafica siempre antes de reportar.

Laboratorio (n = 200):

| Situación | Pearson | Spearman |
|---|---:|---:|
| 1. Lineal con ruido | 0,648 | 0,629 |
| 2. Monótona no lineal (exp) | 0,678 | 0,992 |
| 3a. Sin relación | 0,086 | 0,111 |
| 3b. Igual + un valor extremo (8, 8) | 0,332 | 0,124 |
| 4a. Rango completo | 0,667 | 0,643 |
| 4b. Rango restringido (x > 0,5, n = 57) | 0,464 | 0,410 |

- **2:** Pearson subestima una relación perfectamente monótona.
- **3b:** un solo punto fabrica una correlación apreciable en Pearson.
- **4b:** seleccionar por X reduce r observada; es la restricción de rango (clase 019).

## Ejemplo resuelto

Datos x = (1,2,3,4,100), y = (2,4,5,8,10). Spearman: rangos idénticos → ρ = 1. Pearson es menor (0,75) y está dominado por el 100.

## Errores y límites

- Interpretar r como causalidad o como «porcentaje de acuerdo».
- Correlacionar variables ordinales de pocas categorías con Pearson sin considerar la discretización (clase 065).
- No mirar el gráfico.

## Ejercicios

- **Inicial.** ¿Qué coeficiente usarías para dos rankings?
- **Intermedio.** Si r = 0,5, ¿qué proporción de varianza comparten? → 25 %.
- **Avanzado.** Añade a `lab.py` dos valores extremos opuestos que anulen la correlación y explica el resultado.

## Laboratorio

```bash
python classes/part-02-fiabilidad/052-correlacion-de-pearson-spearman-y-sus-supuestos/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un punto puede cambiar r? 2. ¿Qué es la restricción de rango y a quién afecta? 3. ¿Cuándo Spearman no ayuda?
Se logra si el estudiante elige coeficiente con razones y justifica pedir el gráfico.

## Bibliografía

- Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72-101.
- Anscombe, F. J. (1973). Graphs in statistical analysis. *The American Statistician*, 27(1), 17-21.
- Bishara, A. J., & Hittner, J. B. (2012). Testing the significance of a correlation with nonnormal data. *Psychological Methods*, 17(3), 399-417.
