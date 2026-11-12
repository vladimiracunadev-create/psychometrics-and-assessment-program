# 067 — Curvas características e información del test

> [Índice de la parte](../README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clase 029.

## Objetivos

1. Construir la curva de información de un test.
2. Calcular la fiabilidad condicional aproximada ρ(θ) = I / (I + 1).
3. Diseñar la distribución de dificultades según el propósito.

## Fundamentos

La información del test es la suma de las de sus ítems. Con θ de varianza 1, una aproximación de la fiabilidad condicional es ρ(θ) ≈ I(θ)/(I(θ) + 1). Una prueba puede tener excelente precisión en el centro y mala en las colas aunque su alfa global sea alto.

Laboratorio (20 ítems 2PL, a = 1,2):

| Test | θ | −3 | −2 | 0 | 2 | 3 |
|---|---|---:|---:|---:|---:|---:|
| Amplia (b de −2,5 a 2,5) | I | 1,78 | 3,09 | 4,19 | 3,09 | 1,78 |
| | ρ(θ) | 0,64 | 0,76 | 0,81 | 0,76 | 0,64 |
| Concentrada (b de −0,5 a 0,5) | I | 0,79 | 2,27 | 6,97 | 2,27 | 0,79 |
| | ρ(θ) | 0,44 | 0,69 | 0,87 | 0,69 | 0,44 |

La concentrada es la más precisa en el centro (0,87) y cae a 0,44 en |θ| = 3, donde la amplia conserva 0,64.

## Ejemplo resuelto

I = 4 → ρ = 4/5 = 0,80, EE = 1/√4 = 0,5.

## Errores y límites

- Reportar solo una fiabilidad global de un test pensado para decidir en una zona.
- Usar ρ = I/(I+1) cuando la distribución de θ no tiene varianza 1.
- Desatender la cobertura de contenido al elegir ítems por información.

## Ejercicios

- **Inicial.** ¿Dónde pondrías las dificultades de un test de selección con corte en θ = 1?
- **Intermedio.** I = 9 → ρ = 0,90; EE = 0,33.
- **Avanzado.** Diseña en `lab.py` un test de 20 ítems con ρ ≥ 0,80 en [−2, 2].

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/067-curvas-caracteristicas-e-informacion-del-test/lab.py
```

## Autoevaluación y criterios

1. ¿Qué ventaja tiene una curva frente a una cifra? 2. ¿Cuándo concentrar y cuándo repartir? 3. ¿Cómo comunicarías esta precisión a una familia?
Se logra si el estudiante diseña un test para un propósito y lo justifica con la curva.

## Bibliografía

- Samejima, F. (1977). A use of the information function in tailored testing. *Applied Psychological Measurement*, 1(3), 233-247. ✅ [DOI](https://doi.org/10.1177/014662167700100209)
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
