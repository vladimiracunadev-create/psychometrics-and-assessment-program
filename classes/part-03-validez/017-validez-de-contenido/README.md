# 017 — Validez de contenido y el juicio de expertos

> [Índice de la parte](../README.md) · [Anterior](../016-validez-como-argumento/README.md) · [Siguiente](../018-validez-de-constructo/README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 006 y 016.

## Objetivos

1. Explicar la representatividad del contenido frente a la tabla de especificaciones.
2. Calcular el I-CVI, el S-CVI/Ave y la V de Aiken.
3. Reconocer lo que estos índices no miden.

## Fundamentos

La validez de contenido pregunta si los ítems representan el dominio que se quiere cubrir. Se apoya en una **tabla de especificaciones** (clase 046) y en el juicio de expertos.

```
I-CVI = jueces que califican 3 o 4 / total de jueces       (escala 1-4)
V de Aiken = Σ(rᵢ − mínimo) / ( n · (categorías − 1) )     (Aiken, 1985)
S-CVI/Ave = promedio de los I-CVI
```

Un umbral habitual de I-CVI es 0,78 con seis o más jueces (Lynn, 1986; Polit y Beck, 2006): es una convención, no una ley.

Laboratorio (6 jueces, 12 ítems; los ítems 11 y 12 son poco relevantes por diseño):

| Ítems | I-CVI | V de Aiken | Juicio |
|---|---:|---:|---|
| 1–10 | 0,83–1,00 | 0,67–1,00 | ok |
| 11 | 0,17 | 0,33 | revisar |
| 12 | 0,00 | 0,28 | revisar |

S-CVI/Ave = 0,79. Los índices detectan los dos ítems defectuosos.

## Ejemplo resuelto

Cinco jueces califican un ítem con 4, 4, 3, 2, 3. I-CVI = 4/5 = 0,80. V de Aiken = (3+3+2+1+2)/(5·3) = 0,73.

## Errores y límites

- Los índices cuantifican **acuerdo** entre jueces, no **cobertura**: un banco con todos los ítems relevantes puede omitir una faceta completa. Eso se ve contra la tabla de especificaciones.
- Elegir jueces sin experiencia en el dominio o en la población evaluada.
- Aplicar el índice a constructos sin dominio acotado.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre relevancia y claridad como criterios de juicio?
- **Intermedio.** Calcula el I-CVI de un ítem con calificaciones 4, 4, 4, 3, 2, 1 → 4/6 = 0,67.
- **Avanzado.** Añade a `lab.py` un séptimo juez sesgado y observa el efecto sobre el I-CVI.

## Laboratorio

```bash
python classes/part-03-validez/017-validez-de-contenido/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un S-CVI alto no garantiza cobertura? 2. ¿Cómo eliges expertos? 3. ¿Qué haces con un ítem de I-CVI 0,67?
Se logra si el estudiante calcula los índices y propone cómo revisar la cobertura.

## Bibliografía

- Aiken, L. R. (1985). Three coefficients for analyzing the reliability and validity of ratings. *Educational and Psychological Measurement*, 45(1), 131-142.
- Lynn, M. R. (1986). Determination and quantification of content validity. *Nursing Research*, 35(6), 382-385.
- Polit, D. F., & Beck, C. T. (2006). The content validity index: Are you sure you know what's being reported? *Research in Nursing & Health*, 29(5), 489-497.
