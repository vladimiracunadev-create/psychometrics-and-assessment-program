# 100 — Límites de la evaluación neuropsicológica no clínica

![Portada de la clase 100](portada.svg)

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 035 y 095.

## Objetivos

1. Calcular el valor predictivo de un cribado según la prevalencia.
2. Calcular la probabilidad de un hallazgo bajo por azar en una batería.
3. Delimitar qué puede y qué no puede hacerse fuera del contexto clínico.

## Fundamentos

Un cribado no diagnostica. Con sensibilidad *S*, especificidad *E* y prevalencia *p*, el **valor predictivo positivo** es VPP = S·p / (S·p + (1 − E)(1 − p)). Con prevalencias bajas, la mayoría de los positivos son falsos. Además, en una batería de *k* pruebas independientes, la probabilidad de al menos un puntaje bajo por azar es 1 − (1 − q)ᵏ, con q la probabilidad de un puntaje bajo en una prueba.

Laboratorio (S = 0,85; E = 0,90):

| Prevalencia | VPP | Falsos por cada 100 positivos |
|---:|---:|---:|
| 1 % | 7,9 % | 92 |
| 5 % | 30,9 % | 69 |
| 10 % | 48,6 % | 51 |
| 30 % | 78,5 % | 22 |

Batería de 10 pruebas independientes con q = P(z < −1,5) = 0,067: P(al menos un puntaje bajo) = 0,499 (teórico y simulado).

## Ejemplo resuelto

p = 0,05: 0,85·0,05 = 0,0425; falsos = 0,10·0,95 = 0,095; VPP = 0,0425/0,1375 = 0,309.

## Errores y límites

- Informar un puntaje bajo aislado como hallazgo.
- Cribados escolares masivos sin protocolo de seguimiento y derivación.
- Con pruebas correlacionadas la probabilidad baja, pero sigue siendo alta.
- Fuera del contexto clínico, la evaluación se limita a cribado, investigación y apoyo educativo; el diagnóstico corresponde a profesionales habilitados.

## Ejercicios

- **Inicial.** ¿Qué es el valor predictivo positivo?
- **Intermedio.** Con 6 pruebas y q = 0,067, P(al menos un bajo) → 1 − 0,933⁶ = 0,34.
- **Avanzado.** Introduce correlación 0,5 entre pruebas en `lab.py` y estima la nueva probabilidad.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/100-limites-de-la-evaluacion-neuropsicologica-no-clinica/lab.py
```

## Autoevaluación y criterios

1. ¿Qué haces ante un cribado positivo? 2. ¿Cómo comunicas un resultado de cribado a una familia? 3. ¿Qué evidencia necesitarías para usar una batería como diagnóstico?
Se logra si el estudiante aplica Bayes y rechaza interpretaciones diagnósticas sin respaldo.

## Bibliografía

- Ingraham, L. J., & Aiken, C. B. (1996). An empirical approach to determining criteria for abnormality in test batteries with multiple measures. *Neuropsychology*, 10(1), 120-124. ✅ [DOI](https://doi.org/10.1037/0894-4105.10.1.120)
- Streiner, D. L., & Norman, G. R. (2008). *Health Measurement Scales: A Practical Guide to Their Development and Use* (4.ª ed.). Oxford University Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
