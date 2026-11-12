# 039 — Metaanálisis de validez y corrección por atenuación

![Portada de la clase 039](portada.svg)

> [Índice de la parte](../README.md)

**Parte 03 — Validez** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021, 034 y 027.

## Objetivos

1. Calcular la correlación media ponderada y separar varianza de muestreo de varianza real.
2. Aplicar la corrección por atenuación.
3. Reconocer qué asume y qué no controla un metaanálisis.

## Fundamentos

Los estudios individuales difieren por azar de muestreo, por la fiabilidad de sus medidas y por restricción de rango. El metaanálisis «bare-bones» (Hunter y Schmidt, 2004) promedia las correlaciones ponderando por n y compara la varianza observada con la esperada solo por muestreo:

```
r̄ = Σ nᵢ·rᵢ / Σ nᵢ         var_muestreo ≈ (1 − r̄²)² / (n̄ − 1)
corrección por atenuación:   ρ̂ = r̄ / √(r_xx · r_yy)        (Spearman, 1904)
```

Laboratorio (40 estudios, n total 5 250; relación verdadera ρ = 0,50; fiabilidades 0,80 y 0,60):

| Cantidad | Valor |
|---|---:|
| r observada media ponderada | 0,358 (esperada 0,346) |
| Varianza observada de r | 0,0070 |
| Varianza esperada por muestreo | 0,0058 |
| Varianza atribuible a otra cosa | 0,0011 |
| r corregida por atenuación | 0,516 (verdadera 0,50) |

Casi toda la dispersión entre estudios es error de muestreo; la atenuación explica por qué las validezes observadas parecen bajas.

## Ejemplo resuelto

r̄ = 0,30, fiabilidades 0,70 y 0,50: ρ̂ = 0,30/√0,35 = 0,507. Esto es la relación entre **constructos**, no la validez operativa del test real con sus errores.

## Errores y límites

- Presentar ρ̂ como la validez que obtendrá un empleador con el test (que tiene error).
- Ignorar el sesgo de publicación: solo se meta-analiza lo publicado.
- Corregir con fiabilidades mal estimadas.
- La simulación no incluye heterogeneidad real ni sesgo de publicación.

## Ejercicios

- **Inicial.** ¿Por qué se pondera por n?
- **Intermedio.** r̄ = 0,25, r_xx = 0,81, r_yy = 0,64: ρ̂ = 0,25/0,72 = 0,347.
- **Avanzado.** Añade en `lab.py` un efecto heterogéneo (ρ distinto por estudio) y observa la varianza residual.

## Laboratorio

```bash
python classes/part-03-validez/039-metaanalisis-de-validez-y-correccion-por-atenuacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte de la dispersión es solo azar? 2. ¿Qué corrección haría un empleador real? 3. ¿Qué sesgos no corrige el metaanálisis?
Se logra si el estudiante calcula r̄, descompone varianza y comunica las limitaciones.

## Bibliografía

- Hunter, J. E., & Schmidt, F. L. (2004). *Methods of Meta-Analysis* (2.ª ed.). Sage. ✅ [DOI](https://doi.org/10.4135/9781412985031)
- Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology. *Psychological Bulletin*, 124(2), 262-274. ✅ [DOI](https://doi.org/10.1037/0033-2909.124.2.262)
- Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72-101. ✅ [DOI](https://doi.org/10.2307/1412159)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
