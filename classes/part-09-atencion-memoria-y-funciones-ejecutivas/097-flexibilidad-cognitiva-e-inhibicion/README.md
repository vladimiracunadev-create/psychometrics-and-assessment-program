# 097 — Flexibilidad cognitiva e inhibición

![Portada de la clase 097](portada.svg)

<!-- NAV -->
[← 096 — Memoria verbal y aprendizaje de listas](../096-memoria-verbal-y-aprendizaje-de-listas/README.md) · [📚 Parte 09](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [098 — Planificación y control ejecutivo →](../098-planificacion-y-control-ejecutivo/README.md)
<!-- /NAV -->

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 087 y 093.

## Objetivos

1. Describir la paradoja de la fiabilidad.
2. Estimar la fiabilidad de un efecto de diferencia.
3. Determinar el número de ensayos necesario.

## Fundamentos

Las tareas de inhibición (Stroop, flancos) y flexibilidad (cambio de tarea) producen efectos muy robustos en el promedio del grupo, pero su fiabilidad como **diferencias individuales** suele ser baja: la varianza entre personas del efecto es pequeña frente al ruido ensayo a ensayo (Hedge, Powell y Sumner, 2018). Sin fiabilidad no hay correlaciones útiles con otras variables.

Laboratorio (1 000 personas; efecto Stroop individual M = 60, DE = 15 ms; ruido de ensayo DE = 120 ms):

| Ensayos por condición | Efecto medio (ms) | Fiabilidad del RT medio | Fiabilidad del **efecto** |
|---:|---:|---:|---:|
| 20 | 59,2 | 0,938 | 0,109 |
| 60 | 60,2 | 0,975 | 0,324 |
| 200 | 59,8 | 0,986 | 0,620 |

El RT medio es fiable con pocos ensayos; el efecto necesita cientos.

## Ejemplo resuelto

Con DE entre personas del efecto = 15 ms (varianza 225) y ruido del efecto por mitad = 2·120²/n: con n = 30 por condición y mitad, ruido = 960; fiabilidad de la mitad = 225/(225 + 960) = 0,19; Spearman-Brown ≈ 0,32.

## Errores y límites

- Correlacionar efectos de varias tareas ejecutivas y concluir que «no hay un factor ejecutivo» cuando las medidas no son fiables (atenuación).
- Usar un efecto como rasgo sin fiabilidad.
- Alternativas: modelos de difusión o jerárquicos que estiman el efecto con pooling.
- Los parámetros son supuestos del laboratorio.

## Ejercicios

- **Inicial.** ¿Por qué un efecto robusto puede ser una mala medida individual?
- **Intermedio.** ¿Cuántos ensayos por condición para una fiabilidad ~0,60? Del orden de 200 en este diseño.
- **Avanzado.** Aumenta la DE del efecto individual a 30 ms en `lab.py` y observa.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/097-flexibilidad-cognitiva-e-inhibicion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es la atenuación por baja fiabilidad? 2. ¿Cómo diseñarías una tarea más fiable? 3. ¿Qué informarías sobre la fiabilidad?
Se logra si el estudiante estima la fiabilidad de un efecto y decide el número de ensayos.

## Bibliografía

- Hedge, C., Powell, G., & Sumner, P. (2018). The reliability paradox: Why robust cognitive tasks do not produce reliable individual differences. *Behavior Research Methods*, 50(3), 1166-1186. ✅ [DOI](https://doi.org/10.3758/s13428-017-0935-1)
- Miyake, A., et al. (2000). The unity and diversity of executive functions and their contributions to complex "frontal lobe" tasks. *Cognitive Psychology*, 41(1), 49-100. ✅ [DOI](https://doi.org/10.1006/cogp.1999.0734)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 096 — Memoria verbal y aprendizaje de listas](../096-memoria-verbal-y-aprendizaje-de-listas/README.md)  
[📚 Parte 09](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[098 — Planificación y control ejecutivo →](../098-planificacion-y-control-ejecutivo/README.md)
<!-- /NAV -->
