# 137 — Atención temprana y apoyos

> [Índice de la parte](../README.md)

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 087 y 134.

## Objetivos

1. Monitorear el progreso de un niño con un diseño de caso único.
2. Calcular el NAP (no superposición de todos los pares).
3. Reconocer cuándo una tendencia previa invalida la conclusión.

## Fundamentos

El monitoreo repetido de una conducta objetivo permite decidir si un apoyo funciona. En un diseño AB se compara la línea base (A) con la fase de apoyo (B). El **NAP** (Parker y Vannest, 2009) es la proporción de pares (a, b) con b > a (empates cuentan 0,5). Los diseños de caso único se fortalecen con replicación y línea base estable (Kratochwill et al., 2010).

Laboratorio (8 + 8 mediciones; 2 000 casos simulados por escenario):

| Escenario | NAP medio | % con NAP ≥ 0,90 |
|---|---:|---:|
| Efecto real (+3), sin tendencia | 0,92 | 67,2 % |
| Sin efecto, sin tendencia | 0,50 | 0,4 % |
| Sin efecto, con tendencia previa | 0,93 | 75,0 % |

Una tendencia de mejora previa produce «efectos grandes» sin efecto del apoyo.

## Ejemplo resuelto

Base 2, 3, 3; apoyo 4, 5, 3: con a = 2 las tres comparaciones favorecen a B (3); cada 3 gana 2 veces y empata 1 (2,5): (3 + 2,5 + 2,5)/9 = 0,89.

## Errores y límites

- Concluir eficacia de un diseño AB con línea base inestable.
- Ignorar otros cambios simultáneos (nuevo docente, medicación, maduración).
- Usar un umbral de NAP como regla mecánica.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué es la línea base?
- **Intermedio.** Calcula el NAP de A = 2, 4 y B = 5, 3 → pares: (2,5)(2,3)(4,5) ganan, (4,3) pierde → 3/4 = 0,75.
- **Avanzado.** Agrega una fase de retirada (ABAB) en `lab.py` y comenta la inferencia.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/137-atencion-temprana-y-apoyos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué conducta objetivo elegirías y cómo la medirías? 2. ¿Cómo involucras a la familia en el registro? 3. ¿Cuándo cambias el apoyo?
Se logra si el estudiante analiza un caso único y declara la debilidad del diseño.

## Bibliografía

- Parker, R. I., & Vannest, K. J. (2009). An improved effect size for single-case research: Nonoverlap of all pairs. *Behavior Therapy*, 40(4), 357-367. ✅ [DOI](https://doi.org/10.1016/j.beth.2008.10.006)
- Kratochwill, T. R., et al. (2010). *Single-Case Designs Technical Documentation*. What Works Clearinghouse. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
