# 081 — Modelos de la inteligencia: Spearman, Thurstone, CHC

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 022 y 063.

## Objetivos

1. Contrastar los modelos de un factor general, de capacidades primarias y jerárquicos (CHC).
2. Calcular las diferencias tetrada de Spearman.
3. Entender por qué el «manifold positivo» no zanja el debate.

## Fundamentos

Spearman (1904) propuso un factor general **g** que explica las correlaciones positivas entre pruebas; Thurstone (1938) planteó varias capacidades primarias; los modelos jerárquicos (Carroll, 1993) y la teoría CHC (McGrew, 2009) organizan capacidades amplias bajo un factor general. Si un solo factor explica todo, las **tetradas** r₁₃r₂₄ − r₁₄r₂₃ son ≈ 0.

Laboratorio (6 pruebas, N = 6 000):

| Modelo | \|tetrada\| media | % varianza 1.er componente | Correlación mínima |
|---|---:|---:|---:|
| A. un factor general | 0,0047 | 50,7 % | 0,26 |
| B. dos factores de grupo (r = 0,4) | 0,0790 | 43,3 % | 0,20 |

En ambos casos todas las correlaciones son positivas y el primer componente es grande: el «manifold positivo» **no distingue** entre un g causal y varias capacidades correlacionadas.

## Ejemplo resuelto

r₁₃ = 0,4; r₂₄ = 0,4; r₁₄ = 0,3; r₂₃ = 0,3: tetrada = 0,16 − 0,09 = 0,07 → se aleja de 0; un solo factor no es suficiente para esas cuatro pruebas.

## Errores y límites

- Usar g como si fuera una «cosa» en el cerebro: es una regularidad estadística cuya interpretación es debatida.
- Elegir el modelo por conveniencia de interpretación.
- Aplicar un modelo de población general a un subgrupo sin comprobarlo.

## Ejercicios

- **Inicial.** ¿Qué predice la teoría de Spearman sobre las tetradas?
- **Intermedio.** Calcula la tetrada con r₁₃ = 0,35; r₂₄ = 0,35; r₁₄ = 0,30; r₂₃ = 0,30 → 0,1225 − 0,09 = 0,0325.
- **Avanzado.** Aumenta a 0,8 la correlación entre los factores de grupo del modelo B y observa las tetradas.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/081-modelos-de-la-inteligencia-spearman-thurstone-chc/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia favorecería un modelo jerárquico? 2. ¿Qué implica para la interpretación de un puntaje total? 3. ¿Qué rol juega la muestra?
Se logra si el estudiante calcula tetradas y discute el alcance de cada modelo.

## Bibliografía

- Spearman, C. (1904). "General intelligence," objectively determined and measured. *American Journal of Psychology*, 15(2), 201-292. ✅ [DOI](https://doi.org/10.2307/1412107)
- Thurstone, L. L. (1938). *Primary Mental Abilities*. University of Chicago Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Carroll, J. B. (1993). *Human Cognitive Abilities*. Cambridge University Press. ✅ [DOI](https://doi.org/10.1017/cbo9780511571312)
- McGrew, K. S. (2009). CHC theory and the human cognitive abilities project. *Intelligence*, 37(1), 1-10. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
