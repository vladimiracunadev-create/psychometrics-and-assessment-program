# 060 — Diseño de bancos para pruebas adaptativas

![Portada de la clase 060](portada.svg)

> [Índice de la parte](../README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 055 y 057.

## Objetivos

1. Relacionar la cobertura del banco con la precisión en las colas.
2. Medir la exposición de ítems.
3. Comparar reglas de selección con control de exposición.

## Fundamentos

La calidad de un CAT depende del banco. Un banco concentrado en un rango no informa en las colas. Con selección por máxima información, unos pocos ítems se usan con muchas personas (**exposición alta**, riesgo de filtración) y otros nunca (**ítems sin uso**, costo de calibración perdido). Reglas como la «randomesque» (elegir al azar entre los *k* más informativos) o Sympson-Hetter equilibran exposición y precisión (Way, 1998; van der Linden y Glas, 2010).

Laboratorio (bancos de 150 ítems; CAT de 15; 400 examinados, θ ~ N(0; 1,3)):

| Banco / regla | RMSE | RMSE colas | Exposición máx. | Ítems sin uso |
|---|---:|---:|---:|---:|
| Amplio / máx. información | 0,333 | 0,420 | 1,00 | 82 |
| Amplio / randomesque (5) | 0,350 | 0,436 | 0,75 | 69 |
| Estrecho / máx. información | 0,372 | 0,530 | 1,00 | 96 |
| Estrecho / randomesque (5) | 0,375 | 0,531 | 0,59 | 82 |

Con máxima información hay ítems vistos por el 100 % de los examinados. El banco estrecho rinde peor en las colas (0,53 frente a 0,42).

## Ejemplo resuelto

Exposición ideal con 150 ítems y 15 por persona = 15/150 = 10 %. Una exposición máxima de 100 % indica un ítem que todos ven: si se filtra, deja de ser informativo.

## Errores y límites

- Diseñar el banco sin plan de contenido (cobertura temática).
- Medir la exposición solo en promedio.
- Ignorar la reposición periódica de ítems (rotación del banco).
- Lo simulado usa parámetros conocidos; el banco real se calibra con error.

## Ejercicios

- **Inicial.** ¿Qué ocurre con un banco concentrado cuando llega un examinado extremo?
- **Intermedio.** Si 40 de 150 ítems nunca se usan, ¿qué fracción del banco es «inútil»? 26,7 %.
- **Avanzado.** Cambia `k_top` a 10 en `lab.py` y reporta precisión y exposición.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/060-diseno-de-bancos-para-pruebas-adaptativas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué compromisos existen entre precisión y seguridad? 2. ¿Cómo se repone un banco? 3. ¿Qué datos auditarías en producción?
Se logra si el estudiante diseña un banco y justifica la regla de exposición.

## Bibliografía

- Way, W. D. (1998). Protecting the integrity of computerized testing item pools. *Educational Measurement: Issues and Practice*, 17(4), 17-27. ✅ [DOI](https://doi.org/10.1111/j.1745-3992.1998.tb00632.x)
- van der Linden, W. J., & Glas, C. A. W. (2010). *Elements of Adaptive Testing*. Springer. ✅ [DOI](https://doi.org/10.1007/978-0-387-85461-8)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
