# 027 — El modelo de Rasch

> [Índice de la parte](../README.md) · [Anterior](../026-limites-de-la-teoria-clasica/README.md) · [Siguiente](../028-modelos-de-dos-y-tres-parametros/README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 026.

## Objetivos

1. Enunciar el modelo y su propiedad de suficiencia.
2. Estimar dificultades y habilidades con un algoritmo explícito.
3. Reconocer sus supuestos y su costo.

## Fundamentos

```
P(acierto) = e^(θ − b) / (1 + e^(θ − b))        (Rasch, 1960)
```

Si θ = b la probabilidad es 0,5; cada unidad de diferencia multiplica los *odds* por e. En Rasch el **puntaje total es estadístico suficiente** de θ: dos personas con el mismo puntaje tienen la misma estimación, sin importar cuáles ítems acertaron. A cambio, todos los ítems tienen la misma discriminación.

El laboratorio implementa estimación conjunta (JMLE) con Newton-Raphson alternado, excluye puntajes 0 y perfecto y aplica la corrección (K − 1)/K; es didáctica, no un reemplazo de eRm/TAM/mirt.

Resultados (800 personas, 15 ítems; 794 con estimación finita):

| Medida | Valor |
|---|---:|
| r(b real, b estimado) | 0,997 |
| RMSE de b | 0,095 |
| r(θ real, θ estimado) | 0,830 |

## Ejemplo resuelto

θ = 1, b = 0: P = 1/(1 + e⁻¹) = 0,731. θ = 0, b = 1: P = 0,269.

## Errores y límites

- Interpretar la escala de Rasch como de intervalo sin comprobar el ajuste.
- Descartar ítems que no ajustan sin mirar su contenido.
- JMLE sesga los parámetros con pocos ítems; hay alternativas (CML, MML).
- Muestras pequeñas dan parámetros inestables.

## Ejercicios

- **Inicial.** ¿Cuál es P si θ = b? → 0,5.
- **Intermedio.** Si b₁ = −1 y b₂ = 1, ¿en cuánto difieren los logits de acierto para la misma persona? → 2.
- **Avanzado.** Aumenta K a 30 en `lab.py` y observa el RMSE.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/027-modelo-de-rasch/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué el puntaje total es suficiente? 2. ¿Qué supuesto es más fuerte que en 2PL? 3. ¿Qué se pierde al excluir puntajes extremos?
Se logra si el estudiante estima parámetros y discute los supuestos.

## Bibliografía

- Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests*. Danish Institute for Educational Research.
- Wright, B. D., & Stone, M. H. (1979). *Best Test Design*. MESA Press.
- Andrich, D. (1988). *Rasch Models for Measurement*. Sage.
