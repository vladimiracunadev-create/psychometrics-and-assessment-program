# 055 — Intervalos de confianza para puntajes individuales

> [Índice de la parte](../README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 011 y 015.

## Objetivos

1. Construir los dos intervalos habituales para un puntaje individual.
2. Explicar por qué el centrado en el observado pierde cobertura en los extremos.
3. Redactar una frase de informe que comunique la incertidumbre.

## Fundamentos

Con puntaje observado X, media M, DE s y fiabilidad ρ:

```
(a) X ± 1,96·ETM                          ETM = s·√(1−ρ)
(b) T̂ ± 1,96·s·√(ρ(1−ρ))                  T̂ = M + ρ(X − M)
```

(a) cubre ~95 % **en el conjunto**, porque X − T = E es independiente de T. Pero dada una persona con X extremo, T tiende a estar más cerca de la media (regresión). (b) incorpora esa regresión (Charter y Feldt, 2001).

Laboratorio (M = 100, DE = 15, ρ = 0,80, N = 200 000):

| Puntaje observado | n | Cobertura (a) | Cobertura (b) |
|---|---:|---:|---:|
| todos | 200 000 | 0,949 | 0,950 |
| 120 o más | 18 338 | 0,894 | 0,949 |
| 130 o más | 4 549 | 0,834 | 0,950 |
| 85 a 115 | 136 517 | 0,965 | 0,950 |
| 70 o menos | 4 539 | 0,831 | 0,949 |

Justo donde las decisiones pesan (extremos), el intervalo (a) cubre bastante menos de lo declarado.

## Ejemplo resuelto

X = 130, M = 100, s = 15, ρ = 0,80: T̂ = 124; error = 15·√0,16 = 6; intervalo (b) = 124 ± 11,8 → [112,2; 135,8]. El intervalo (a) sería 130 ± 13,2.

## Errores y límites

- Informar «tu puntaje verdadero es X».
- Usar (a) para decisiones de cola sin advertirlo.
- Con ρ alta la diferencia entre (a) y (b) es pequeña; con ρ baja es grande.
- Supone normalidad y homocedasticidad del error.

## Ejercicios

- **Inicial.** Con ρ = 1, ¿cuánto vale el ETM? → 0.
- **Intermedio.** Calcula (b) para X = 70 con los mismos parámetros → T̂ = 76; 76 ± 11,8.
- **Avanzado.** Cambia ρ a 0,95 en `lab.py` y compara las coberturas.

## Laboratorio

```bash
python classes/part-02-fiabilidad/055-intervalos-de-confianza-para-puntajes-individuales/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué T̂ está más cerca de la media que X? 2. ¿Cuándo el intervalo (a) basta? 3. Redacta una frase de informe para X = 130 sin sobreafirmar.
Se logra si el estudiante construye ambos intervalos y comunica la incertidumbre.

## Bibliografía

- Charter, R. A., & Feldt, L. S. (2001). Confidence intervals for true scores: Is there a correct approach? *Journal of Psychoeducational Assessment*, 19(4), 350-364.
- Harvill, L. M. (1991). Standard error of measurement. *Educational Measurement: Issues and Practice*, 10(2), 33-41.
