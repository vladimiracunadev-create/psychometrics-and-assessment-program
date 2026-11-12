# 046 — Rotaciones y criterios de retención de factores

![Portada de la clase 046](portada.svg)

> [Índice de la parte](../README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clase 042.

## Objetivos

1. Explicar por qué la solución factorial inicial no es única.
2. Rotar con varimax y comprobar que no cambia la varianza explicada.
3. Elegir entre rotación ortogonal y oblicua.

## Fundamentos

Las cargas sin rotar no son interpretables porque cualquier rotación del espacio de factores explica lo mismo (Browne, 2001). La rotación busca la **estructura simple** (Thurstone): cada ítem carga alto en un factor y casi cero en los demás. **Varimax** (Kaiser, 1958) es ortogonal y maximiza la varianza de las cargas al cuadrado por factor. Las rotaciones **oblicuas** (oblimin, promax) permiten factores correlacionados, lo que suele ser más realista en psicología.

Laboratorio (8 ítems; estructura simple verdadera 1–4 / 5–8; N = 1 500):

| Ítem | Sin rotar | Varimax |
|---:|---|---|
| 1 | 0,23 / 0,75 | 0,01 / 0,78 |
| 5 | 0,76 / −0,23 | 0,79 / 0,00 |

Ángulo de rotación −16,7°; varianza explicada total 4,962 antes y después.

## Ejemplo resuelto

Cargas (0,8; 0,2), rotación de 30°: a′ = 0,8·cos30 + 0,2·sen30 = 0,793; b′ = −0,8·sen30 + 0,2·cos30 = −0,227. Comunalidad: 0,68 antes; 0,793² + 0,227² = 0,68 después.

## Errores y límites

- Forzar ortogonalidad cuando los constructos se correlacionan.
- Elegir la rotación que «se ve mejor».
- Interpretar cargas bajas (< 0,3) como evidencia sin considerar el tamaño muestral.
- Costello y Osborne (2005): las decisiones de AFE se reportan con transparencia.

## Ejercicios

- **Inicial.** ¿Cambia la comunalidad de un ítem al rotar? → no.
- **Intermedio.** Rota (0,6; 0,6) en 45° → a′ = 0,6·0,707 + 0,6·0,707 = 0,849; b′ = 0.
- **Avanzado.** Introduce correlación 0,4 entre factores en `lab.py` y compara varimax con la estructura real.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/046-rotaciones-y-criterios-de-retencion-de-factores/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué la rotación no «crea» estructura? 2. ¿Cuándo preferir oblicua? 3. ¿Qué es estructura simple?
Se logra si el estudiante rota, verifica la invarianza de la comunalidad y justifica su elección.

## Bibliografía

- Kaiser, H. F. (1958). The varimax criterion for analytic rotation in factor analysis. *Psychometrika*, 23(3), 187-200. ✅ [DOI](https://doi.org/10.1007/bf02289233)
- Browne, M. W. (2001). An overview of analytic rotation in exploratory factor analysis. *Multivariate Behavioral Research*, 36(1), 111-150. ✅ [DOI](https://doi.org/10.1207/s15327906mbr3601_05)
- Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis. *Practical Assessment, Research & Evaluation*, 10(7). ⚠️ existe, pero Crossref registra 2008 (¿otra edición?; [DOI](https://doi.org/10.4135/9781412995627.d8))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
