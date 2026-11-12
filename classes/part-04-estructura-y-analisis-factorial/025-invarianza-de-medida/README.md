# 025 — Invarianza de medida entre grupos

> [Índice de la parte](../README.md) · [Anterior](../024-modelos-circumplejos/README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 022 y 023.

## Objetivos

1. Distinguir invarianza configural, métrica, escalar y estricta.
2. Explicar qué comparaciones habilita cada nivel.
3. Reconocer que un problema de invarianza puede pasar inadvertido.

## Fundamentos

Comparar grupos supone que el instrumento mide lo mismo en todos (Meredith, 1993; Vandenberg y Lance, 2000):

| Nivel | Qué se iguala | Habilita |
|---|---|---|
| Configural | mismo patrón de ítems en factores | comparar la estructura |
| Métrica | cargas | comparar correlaciones y varianzas |
| Escalar | cargas + interceptos | comparar **medias** |
| Estricta | + varianzas únicas | comparar puntajes observados |

Laboratorio: ambos grupos tienen el mismo rasgo medio; en un ítem de seis la carga es 0,8 (grupo A) y 0,3 (grupo B):

| Grupo | Carga ítem 6 | Alfa | r(escala, criterio) |
|---|---:|---:|---:|
| A | 0,81 | 0,858 | 0,459 |
| B | 0,31 | 0,808 | 0,462 |

La fiabilidad baja en B, pero la correlación con el criterio apenas cambia: **mirar solo la validez de criterio no delata el problema**.

## Ejemplo resuelto

Un ítem con carga 0,8 aporta 64 % de su varianza al factor; con carga 0,3, solo 9 %. En B el mismo ítem es casi ruido para el rasgo.

## Errores y límites

- Comparar medias de grupos sin probar invarianza escalar.
- Descartar invarianza porque «el ajuste es bueno» en cada grupo por separado.
- Eliminar ítems sin justificación sustantiva (clase 075 trata la invarianza parcial).
- El laboratorio conoce el rasgo; en datos reales se usan modelos multigrupo.

## Ejercicios

- **Inicial.** ¿Qué nivel de invarianza se necesita para comparar medias? → escalar.
- **Intermedio.** ¿Qué diferencias de carga te preocuparían: 0,70 vs 0,65 o 0,70 vs 0,30? La segunda.
- **Avanzado.** Cambia en `lab.py` la carga de dos ítems y observa el alfa de B.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/025-invarianza-de-medida/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué la invarianza es previa a comparar grupos? 2. ¿Qué evidencia delata una carga distinta? 3. ¿Qué haces si falla la escalar?
Se logra si el estudiante ordena los niveles y relaciona cada uno con una comparación legítima.

## Bibliografía

- Meredith, W. (1993). Measurement invariance, factor analysis and factorial invariance. *Psychometrika*, 58(4), 525-543. ✅ [DOI](https://doi.org/10.1007/bf02294825)
- Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature. *Organizational Research Methods*, 3(1), 4-70. ✅ [DOI](https://doi.org/10.1177/109442810031002)
- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *Developmental Review*, 41, 71-90. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
