# 020 — La cara olvidada: consecuencias del uso del test

> [Índice de la parte](../README.md) · [Anterior](../019-validez-de-criterio/README.md)

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 016 y 019.

## Objetivos

1. Explicar por qué las consecuencias forman parte del argumento de validez.
2. Calcular tasas de selección y razón de impacto adverso a partir de un punto de corte.
3. Distinguir una alerta estadística de una conclusión sobre discriminación.

## Fundamentos

Messick (1995) incluyó la **validez consecuencial**: el uso de un test tiene efectos sociales que deben evaluarse junto con la evidencia técnica. Una diferencia entre grupos no prueba por sí sola sesgo del test: puede reflejar diferencias reales de oportunidad, sesgo del instrumento o ambos. El laboratorio **no distingue causas**; muestra cómo el diseño del uso amplifica o atenúa la diferencia.

Laboratorio: dos grupos con diferencia media d = 0,5 DE. Razón = tasa del grupo 2 / tasa del grupo 1:

| Corte (percentil global) | Tasa G1 | Tasa G2 | Razón |
|---:|---:|---:|---:|
| 10 | 0,942 | 0,858 | 0,91 |
| 30 | 0,787 | 0,613 | 0,78 |
| 50 | 0,600 | 0,400 | 0,67 |
| 70 | 0,385 | 0,215 | 0,56 |
| 90 | 0,143 | 0,057 | 0,40 |
| 97 | 0,046 | 0,014 | 0,32 |

Cuanto más selectivo el corte, menor la razón: una diferencia modesta se amplifica en la cola. La «regla de los cuatro quintos» (0,80) de las *Uniform Guidelines* de EE. UU. (1978) se usa aquí solo como alerta orientativa; **no es norma chilena** ni prueba de discriminación.

## Ejemplo resuelto

Tasas 0,60 y 0,40: razón 0,67 < 0,80 → alerta. Qué hacer: revisar la validez del criterio, la relevancia del contenido, alternativas con menor impacto adverso y el peso del test dentro de la decisión.

## Errores y límites

- Adoptar un test sin estimar sus consecuencias en los grupos afectados.
- Declarar sesgo, o su ausencia, solo por una razón de tasas.
- Usar el mismo corte para propósitos distintos (cribado frente a selección final).

## Ejercicios

- **Inicial.** ¿Qué información adicional necesitas antes de concluir sesgo a partir de una razón de 0,67?
- **Intermedio.** Tasas 0,30 y 0,27: razón 0,90, ¿alerta? No.
- **Avanzado.** En `lab.py` reduce d a 0,2 y describe el cambio de la razón en el corte 90.

## Laboratorio

```bash
python classes/part-03-validez/020-consecuencias-del-uso/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un corte más estricto aumenta el impacto adverso? 2. ¿Qué alternativas reducen la diferencia sin bajar la validez? 3. ¿Quién debería participar en evaluar las consecuencias?
Se logra si el estudiante calcula tasas y razones y redacta una evaluación de consecuencias sin sobreafirmar causas.

## Bibliografía

- Messick, S. (1995). Validity of psychological assessment. *American Psychologist*, 50(9), 741-749. ⚠️ existe, pero Crossref registra 1996 (¿otra edición?; [DOI](https://doi.org/10.1037//0003-066x.51.9.980))
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Uniform Guidelines on Employee Selection Procedures (1978), 29 CFR Part 1607 (EE. UU.). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
