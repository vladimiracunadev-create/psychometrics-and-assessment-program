# 082 — Inteligencia fluida y cristalizada

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 081.

## Objetivos

1. Distinguir Gf (razonar con material nuevo) de Gc (conocimiento acumulado).
2. Diferenciar estudios transversales y longitudinales.
3. Reconocer los efectos de edad, cohorte y periodo.

## Fundamentos

Cattell y Horn distinguieron la inteligencia **fluida** (resolver problemas nuevos) y la **cristalizada** (conocimiento y destrezas aprendidos) (Horn y Cattell, 1967). Las tareas de Gf suelen mostrar menores puntajes con la edad, las de Gc se mantienen o suben. Pero comparar edades en un solo momento mezcla **edad, cohorte y periodo** (Schaie, 1965) y los puntajes cognitivos han subido entre cohortes durante buena parte del siglo XX (efecto Flynn; Flynn, 1987).

Laboratorio (parámetros **supuestos**, no empíricos; efecto de cohorte +0,3 DE por década):

| Edad | Gf transversal | Gc transversal | Gf longitudinal (cohorte 1966) |
|---:|---:|---:|---:|
| 20 | 1,41 | 1,36 | 0,21 |
| 40 | 0,52 | 1,18 | −0,12 |
| 60 | −0,54 | 0,96 | −0,51 |
| 70 | −1,01 | 0,88 | — |

El transversal sugiere ~2 DE de diferencia entre 20 y 60 años; la misma cohorte seguida en el tiempo cae ~0,7 DE.

## Ejemplo resuelto

Un estudio transversal compara personas de 20 y 60 años: diferencia = 1,41 − (−0,54) = 1,95 DE. Si 1,2 DE se debe a la cohorte (0,3 por década, cuatro décadas), el cambio asociado a la edad es 0,75 DE.

## Errores y límites

- Interpretar diferencias transversales como declive individual.
- Atribuir a la edad lo que es cambio en acceso a educación.
- Generalizar parámetros del laboratorio a la población real.

## Ejercicios

- **Inicial.** ¿Qué tipo de tarea medirías para Gf y para Gc?
- **Intermedio.** Si el efecto de cohorte fuera 0,2 por década, ¿cuánto del contraste transversal 20–60 sería cohorte? 0,8 DE.
- **Avanzado.** Introduce un efecto de periodo (mejora para todos) en `lab.py` y describe qué diseño lo separa.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/082-inteligencia-fluida-y-cristalizada/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diseño separa edad, cohorte y periodo? 2. ¿Por qué se debe cuidar el baremo por edad? 3. ¿Qué evidencia sobre cambio cognitivo no es de laboratorio?
Se logra si el estudiante interpreta comparaciones de edad con las amenazas explícitas.

## Bibliografía

- Horn, J. L., & Cattell, R. B. (1967). Age differences in fluid and crystallized intelligence. *Acta Psychologica*, 26, 107-129.
- Schaie, K. W. (1965). A general model for the study of developmental problems. *Psychological Bulletin*, 64(2), 92-107.
- Flynn, J. R. (1987). Massive IQ gains in 14 nations. *Psychological Bulletin*, 101(2), 171-191.
