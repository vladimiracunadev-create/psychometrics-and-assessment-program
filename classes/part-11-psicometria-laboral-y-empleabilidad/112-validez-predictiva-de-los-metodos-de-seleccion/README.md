# 112 — Validez predictiva de los métodos de selección

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 019, 059 y 111.

## Objetivos

1. Calcular la validez de un compuesto de dos predictores.
2. Estimar la utilidad (Brogden–Cronbach–Gleser) con supuestos explícitos.
3. Reconocer que los coeficientes de la literatura se revisan y dependen del contexto.

## Fundamentos

Los metaanálisis de validez de métodos de selección (Schmidt y Hunter, 1998) fueron revisados con tratamientos distintos de la restricción de rango (Sackett et al., 2022): las estimaciones **cambian** según las correcciones. Por eso en este laboratorio los coeficientes son **ilustrativos**. La validez de un compuesto depende de la intercorrelación:

```
R = √( (v₁² + v₂² − 2 r₁₂ v₁ v₂) / (1 − r₁₂²) )
```

La utilidad (Brogden, 1949; Cronbach y Gleser, 1965): ΔU = N_sel · T · R · SD_y · λ − costo total, con λ = φ(z)/razón de selección.

Laboratorio (v₁ = v₂ = 0,35):

| r₁₂ | R del compuesto | Ganancia sobre el mejor |
|---:|---:|---:|
| 0,0 | 0,495 | 0,145 |
| 0,2 | 0,452 | 0,102 |
| 0,4 | 0,418 | 0,068 |
| 0,6 | 0,391 | 0,041 |

Utilidad (100 postulantes, selección 20 %, SD_y = 8 000 000 CLP, 2 años, valores en pesos chilenos): solo entrevista = 152 778 675; entrevista + test = 195 400 400.

## Ejemplo resuelto

Con r₁₂ = 0,2: R = √((0,1225 + 0,1225 − 2·0,2·0,1225)/(1 − 0,04)) = √(0,1960/0,96) = 0,452.

## Errores y límites

- Tomar un coeficiente de un metaanálisis como la validez de *tu* proceso.
- Proyectar utilidades con SD_y que nadie estimó localmente.
- Sumar predictores muy correlacionados esperando mucho más validez.
- Los costos y SD_y del laboratorio son supuestos.

## Ejercicios

- **Inicial.** ¿Por qué baja la ganancia cuando sube r₁₂?
- **Intermedio.** Calcula R con v₁ = 0,30, v₂ = 0,20 y r₁₂ = 0 → √(0,09 + 0,04) = 0,36.
- **Avanzado.** Calcula la utilidad con SD_y a la mitad y compara.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/112-validez-predictiva-de-los-metodos-de-seleccion/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se revisaron las estimaciones? 2. ¿Qué evidencia local reunirías? 3. ¿Cómo presentarías un rango de utilidad?
Se logra si el estudiante calcula compuestos y utilidades y declara supuestos.

## Bibliografía

- Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology. *Psychological Bulletin*, 124(2), 262-274. ✅ [DOI](https://doi.org/10.1037/0033-2909.124.2.262)
- Sackett, P. R., Zhang, C., Berry, C. M., & Lievens, F. (2022). Revisiting meta-analytic estimates of validity in personnel selection. *Journal of Applied Psychology*, 107(11), 2040-2068. ✅ [DOI](https://doi.org/10.1037/apl0000994)
- Brogden, H. E. (1949). When testing pays off. *Personnel Psychology*, 2, 171-183. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.1949.tb01397.x)
- Cronbach, L. J., & Gleser, G. C. (1965). *Psychological Tests and Personnel Decisions* (2.ª ed.). University of Illinois Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
