# 087 — Resolución de problemas y aprendizaje

![Portada de la clase 087](portada.svg)

<!-- NAV -->
[← 086 — Razonamiento espacial](../086-razonamiento-espacial/README.md) · [📚 Parte 08](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [088 — Aptitudes mentales primarias →](../088-aptitudes-mentales-primarias/README.md)
<!-- /NAV -->

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 025.

## Objetivos

1. Describir la evaluación dinámica (pre–instrucción–post).
2. Calcular la fiabilidad de un puntaje de ganancia.
3. Interpretar la «ganancia» individual con cautela.

## Fundamentos

La evaluación dinámica mide el cambio tras una breve ayuda para estimar el potencial de aprendizaje (Grigorenko y Sternberg, 1998). El puntaje de ganancia G = post − pre es problemático: su fiabilidad cae cuando pre y post correlacionan alto (Lord, 1956; Cronbach y Furby, 1970):

```
ρ_G = (ρ_x·σ_x² + ρ_y·σ_y² − 2·r_xy·σ_x·σ_y) / (σ_x² + σ_y² − 2·r_xy·σ_x·σ_y)
```

Laboratorio (fiabilidad de pre y de post = 0,90; N = 20 000):

| r(pre, post) | Fiabilidad de la ganancia (fórmula) | Simulada |
|---:|---:|---:|
| 0,19 | 0,876 | 0,879 |
| 0,50 | 0,801 | 0,804 |
| 0,70 | 0,670 | 0,672 |

La fórmula coincide con la simulación. Con r mayor, la ganancia es menos fiable.

## Ejemplo resuelto

σ_x = σ_y = 1; ρ = 0,9; r_xy = 0,8: ρ_G = (0,9 + 0,9 − 1,6)/(2 − 1,6) = 0,2/0,4 = 0,50.

## Errores y límites

- Etiquetar a alguien como «aprende rápido» o «lento» por un par de puntajes.
- Ignorar el efecto techo y la regresión a la media.
- Los resultados de grupo (efecto de un programa) son más fiables que los individuales.
- Preferir el nivel post controlando por el pre, o el cambio fiable (clase 025).

## Ejercicios

- **Inicial.** ¿Por qué la ganancia suele ser poco fiable?
- **Intermedio.** Calcula ρ_G con ρ = 0,85 y r = 0,6 → (1,7 − 1,2)/(2 − 1,2) = 0,625.
- **Avanzado.** Añade en `lab.py` un efecto techo y observa la ganancia.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/087-resolucion-de-problemas-y-aprendizaje/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo es útil una evaluación dinámica? 2. ¿Qué alternativa a la ganancia usarías? 3. ¿Qué evidencia de validez requiere?
Se logra si el estudiante calcula la fiabilidad de una ganancia y la interpreta con cautela.

## Bibliografía

- Lord, F. M. (1956). The measurement of growth. *Educational and Psychological Measurement*, 16(4), 421-437. ✅ [DOI](https://doi.org/10.1177/001316445601600401)
- Cronbach, L. J., & Furby, L. (1970). How we should measure "change"—or should we? *Psychological Bulletin*, 74(1), 68-80. ✅ [DOI](https://doi.org/10.1037/h0029382)
- Grigorenko, E. L., & Sternberg, R. J. (1998). Dynamic testing. *Psychological Bulletin*, 124(1), 75-111. ✅ [DOI](https://doi.org/10.1037/0033-2909.124.1.75)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 086 — Razonamiento espacial](../086-razonamiento-espacial/README.md)  
[📚 Parte 08](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[088 — Aptitudes mentales primarias →](../088-aptitudes-mentales-primarias/README.md)
<!-- /NAV -->
