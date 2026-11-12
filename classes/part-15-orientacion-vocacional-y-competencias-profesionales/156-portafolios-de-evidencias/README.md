# 156 — Portafolios de evidencias

![Portada de la clase 156](portada.svg)

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 143 y 155.

## Objetivos

1. Calcular las características de operación de una regla «al menos k de n».
2. Elegir el número de evidencias según el costo de los errores.
3. Reconocer los problemas de fiabilidad y autoría del portafolio.

## Fundamentos

Los portafolios aportan validez de contenido y ecológica, pero la fiabilidad de su puntuación es un reto histórico (Gipps, 1994; Koretz, 1998). Una regla de decisión «al menos k de n evidencias cumplen el estándar» tiene sensibilidad P(Bin(n, p_competente) ≥ k) y especificidad P(Bin(n, p_no competente) < k), calculables exactamente.

Laboratorio (p = 0,80 competente; p = 0,40 no competente; prevalencia de competencia 70 %; supuestos):

| Regla | Sensibilidad | Especificidad | VPP | VPN |
|---|---:|---:|---:|---:|
| 2 de 3 | 0,90 | 0,65 | 0,86 | 0,73 |
| 3 de 5 | 0,94 | 0,68 | 0,87 | 0,83 |
| 4 de 5 | 0,74 | 0,91 | 0,95 | 0,60 |
| 6 de 8 | 0,80 | 0,95 | 0,97 | 0,67 |
| 8 de 12 | 0,93 | 0,94 | 0,97 | 0,85 |

## Ejemplo resuelto

«2 de 3» con p = 0,40: P(≥ 2) = 3·0,16·0,6 + 0,064 = 0,352 → especificidad = 0,648.

## Errores y límites

- Reglas con pocas evidencias.
- No verificar autoría ni contexto de producción de las evidencias.
- Evaluadores sin calibración (clase 143).
- Probabilidades supuestas, no estimadas.

## Ejercicios

- **Inicial.** ¿Qué es una regla «k de n»?
- **Intermedio.** Calcula la sensibilidad de «2 de 3» con p = 0,8 → 3·0,64·0,2 + 0,512 = 0,896.
- **Avanzado.** Agrega la regla «5 de 8» con otro p y compara.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/156-portafolios-de-evidencias/lab.py
```

## Autoevaluación y criterios

1. ¿Qué rúbrica usarías para cada evidencia? 2. ¿Cómo aseguras la autoría? 3. ¿Qué proceso de apelación defines?
Se logra si el estudiante calcula las características de una regla y justifica n y k.

## Bibliografía

- Gipps, C. V. (1994). *Beyond Testing: Towards a Theory of Educational Assessment*. Falmer Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Koretz, D. (1998). Large-scale portfolio assessments in the US: Evidence pertaining to the quality of measurement. *Assessment in Education*, 5(3), 309-334. ✅ [DOI](https://doi.org/10.1080/0969595980050302)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
