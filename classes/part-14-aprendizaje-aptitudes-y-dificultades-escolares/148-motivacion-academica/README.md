# 148 — Motivación académica

![Portada de la clase 148](portada.svg)

<!-- NAV -->
[← 147 — Estrategias metacognitivas y autorregulación…](../147-estrategias-metacognitivas-y-autorregulacion-del-aprendizaje/README.md) · [📚 Parte 14](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [149 — Habilidades digitales del estudiantado →](../149-habilidades-digitales-del-estudiantado/README.md)
<!-- /NAV -->

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 175.

## Objetivos

1. Distinguir modelos de motivación (expectativa–valor, autodeterminación).
2. Estimar efectos cruzados entre motivación y rendimiento.
3. Reconocer el sesgo por error de medida.

## Fundamentos

Las teorías de expectativa–valor (Eccles y Wigfield, 2002) y de autodeterminación (Ryan y Deci, 2000) describen cómo creencias y razones se relacionan con el rendimiento. Motivación y rendimiento probablemente se influyen mutuamente, y los modelos de efectos cruzados con dos ondas son sensibles al error de medida y a supuestos (Hamaker, Kuiper y Grasman, 2015).

Laboratorio (50 000 casos; efecto verdadero exitoso → motivación 0,25; motivación → rendimiento 0,00 por construcción):

| Condición de medida | M₁→R₂ (verdad 0,00) | R₁→M₂ (verdad 0,25) |
|---|---:|---:|
| Sin error de medida | −0,001 | 0,256 |
| Fiabilidad M = 0,7 y R = 0,9 | 0,027 | 0,318 |

Con medidas ruidosas aparece un efecto espurio pequeño de la motivación y el efecto del éxito sobre la motivación se **sobreestima**.

## Ejemplo resuelto

El control de M₁ medida con fiabilidad 0,7 es incompleto: parte de la varianza de la motivación verdadera queda «sin controlar» y se atribuye a R₁, que está correlacionada con ella.

## Errores y límites

- Concluir que «motivar mejora las notas» desde un estudio de dos ondas.
- Usar un solo autoinforme de motivación.
- Ignorar efectos entre y dentro de personas (modelos RI-CLPM).
- Simulación con un mecanismo simple.

## Ejercicios

- **Inicial.** ¿Qué es un efecto cruzado?
- **Intermedio.** ¿Qué pasa si M tiene fiabilidad 0,5? Mayor sesgo.
- **Avanzado.** Cambia el efecto verdadero M → R a 0,15 y observa la estimación.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/148-motivacion-academica/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diseño sostiene mejor una conclusión causal? 2. ¿Cómo medirías motivación con más de un método? 3. ¿Qué intervención sustentada en evidencia conoces?
Se logra si el estudiante identifica el sesgo por error de medida en un modelo cruzado.

## Bibliografía

- Eccles, J. S., & Wigfield, A. (2002). Motivational beliefs, values, and goals. *Annual Review of Psychology*, 53, 109-132. ✅ [DOI](https://doi.org/10.1146/annurev.psych.53.100901.135153)
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*, 55(1), 68-78. ✅ [DOI](https://doi.org/10.1037/0003-066x.55.1.68)
- Hamaker, E. L., Kuiper, R. M., & Grasman, R. P. P. P. (2015). A critique of the cross-lagged panel model. *Psychological Methods*, 20(1), 102-116. ✅ [DOI](https://doi.org/10.1037/a0038889)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 147 — Estrategias metacognitivas y autorregulación…](../147-estrategias-metacognitivas-y-autorregulacion-del-aprendizaje/README.md)  
[📚 Parte 14](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[149 — Habilidades digitales del estudiantado →](../149-habilidades-digitales-del-estudiantado/README.md)
<!-- /NAV -->
