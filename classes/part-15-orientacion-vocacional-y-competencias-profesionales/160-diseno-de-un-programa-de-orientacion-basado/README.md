# 160 — Diseño de un programa de orientación basado en evidencia

![Portada de la clase 160](portada.svg)

<!-- NAV -->
[← 159 — Formación continua y reconversión laboral](../159-formacion-continua-y-reconversion-laboral/README.md) · [📚 Parte 15](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [161 — Bienestar subjetivo y calidad de vida →](../../part-16-evaluacion-socioemocional-y-bienestar/161-bienestar-subjetivo-y-calidad-de-vida/README.md)
<!-- /NAV -->

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 5 h · Estado `escrita`
**Prerrequisitos:** clases 172 y 155.

## Objetivos

1. Calcular el tamaño de muestra para detectar un efecto con un diseño pre-post.
2. Incorporar el ajuste por pretest y el agrupamiento por cursos.
3. Declarar la lógica y la medida del programa antes de empezar.

## Fundamentos

Para comparar dos grupos con potencia 1 − β y nivel α, el tamaño por grupo es n = 2·((z₁₋α/₂ + z₁₋β)/d)². Medir el pretest y ajustar por él reduce la varianza residual en (1 − r²) (Cohen, 1988). Si se asigna por cursos, el **efecto de diseño** es DEFF = 1 + (m − 1)·ICC (Donner y Klar, 2000). La literatura de intervenciones de orientación muestra efectos de magnitud variable (Whiston, Brecheisen y Stephens, 2003).

Laboratorio (potencia 80 %, α = 0,05):

| Efecto d | Sin ajustar | Ajuste (r = 0,6) | Por cursos (m = 30, ICC = 0,05) |
|---:|---:|---:|---:|
| 0,2 | 393 | 252 | 616 |
| 0,3 | 175 | 112 | 274 |
| 0,5 | 63 | 41 | 99 |

Verificación: d = 0,5, r = 0,6, n = 41 por grupo → potencia simulada 0,81.

## Ejemplo resuelto

d = 0,5: n = 2·(2,80/0,5)² = 62,7 → 63 sin ajustar; con r = 0,6: 62,7·0,64 = 40,1 → 41.

## Errores y límites

- Fijar el tamaño muestral después de ver los datos.
- Ignorar el agrupamiento por curso: infla falsamente la significación.
- Medir el resultado con un instrumento no validado para la población.
- Efectos y correlaciones supuestos.

## Ejercicios

- **Inicial.** ¿Qué es el efecto de diseño?
- **Intermedio.** DEFF con m = 20 e ICC = 0,10 → 2,9.
- **Avanzado.** Calcula n para d = 0,4 y r = 0,5 con potencia 90 %.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/160-diseno-de-un-programa-de-orientacion-basado/lab.py
```

## Autoevaluación y criterios

1. ¿Cuál es la lógica de tu programa? 2. ¿Qué resultado medirás y con qué instrumento? 3. ¿Qué harás si no hay efecto?
Se logra si el estudiante diseña una evaluación del programa con tamaño muestral justificado.

## Bibliografía

- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2.ª ed.). Lawrence Erlbaum. ✅ [DOI](https://doi.org/10.2307/2290095)
- Donner, A., & Klar, N. (2000). *Design and Analysis of Cluster Randomization Trials in Health Research*. Arnold. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Whiston, S. C., Brecheisen, B. K., & Stephens, J. (2003). Does treatment modality affect career counseling effectiveness? *Journal of Vocational Behavior*, 62(3), 390-410. ✅ [DOI](https://doi.org/10.1016/s0001-8791(02)00050-7)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 159 — Formación continua y reconversión laboral](../159-formacion-continua-y-reconversion-laboral/README.md)  
[📚 Parte 15](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[161 — Bienestar subjetivo y calidad de vida →](../../part-16-evaluacion-socioemocional-y-bienestar/161-bienestar-subjetivo-y-calidad-de-vida/README.md)
<!-- /NAV -->
