# 172 — Tamaño muestral y potencia

![Portada de la clase 172](portada.svg)

<!-- NAV -->
[← 171 — Diseño de un estudio de validación](../171-diseno-de-un-estudio-de-validacion/README.md) · [📚 Parte 17](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [173 — Simulación de datos psicométricos →](../173-simulacion-de-datos-psicometricos/README.md)
<!-- /NAV -->

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 042 y 171.

## Objetivos

1. Estimar cómo cambia la precisión de las cargas factoriales con N.
2. Entender por qué las reglas fijas de N son heurísticas.
3. Calcular el error de estimación de una matriz de correlaciones.

## Fundamentos

El tamaño muestral necesario para el análisis factorial depende de la fuerza de las cargas, el número de ítems por factor y la comunalidad, más que de una regla fija (MacCallum et al., 1999). Para el alfa existe fórmula de precisión (van Zyl, Neudecker y Nel, 2000; Bonett, 2002). Lo más fiable es **simular**.

Laboratorio (un factor, 10 ítems con cargas de 0,4 a 0,8; 40 réplicas por N):

| N | RMSE de las cargas | Alguna carga subestimada > 0,15 | SRMR muestral |
|---:|---:|---:|---:|
| 50 | 0,094 | 40 % | 0,119 |
| 100 | 0,071 | 28 % | 0,087 |
| 200 | 0,047 | 2 % | 0,058 |
| 500 | 0,032 | 0 % | 0,039 |
| 1 000 | 0,022 | 0 % | 0,027 |

El error decrece aproximadamente con 1/√N.

## Ejemplo resuelto

De N = 200 a N = 800 (× 4) el RMSE debería caer a la mitad: 0,047 → ≈ 0,024.

## Errores y límites

- Aplicar «10 casos por ítem» sin mirar las cargas.
- Confundir ajuste de la matriz (SRMR muestral) con ajuste del modelo.
- Extrapolar a modelos con varios factores o datos ordinales.
- Cargas y ruido del laboratorio supuestos.

## Ejercicios

- **Inicial.** ¿Qué es el RMSE?
- **Intermedio.** Si el RMSE con N = 100 es 0,07, ¿con N = 400? ≈ 0,035.
- **Avanzado.** Reduce las cargas a 0,3–0,5 en `lab.py` y observa el N necesario.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/172-tamano-muestral-y-potencia/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo justificarías el N de tu estudio? 2. ¿Qué pasa con cargas bajas? 3. ¿Qué dirías si te piden «una regla»?
Se logra si el estudiante justifica el N por simulación y no por una regla fija.

## Bibliografía

- MacCallum, R. C., Widaman, K. F., Zhang, S., & Hong, S. (1999). Sample size in factor analysis. *Psychological Methods*, 4(1), 84-99. ✅ [DOI](https://doi.org/10.1037/1082-989x.4.1.84)
- Bonett, D. G. (2002). Sample size requirements for testing and estimating coefficient alpha. *Journal of Educational and Behavioral Statistics*, 27(4), 335-340. ✅ [DOI](https://doi.org/10.3102/10769986027004335)
- van Zyl, J. M., Neudecker, H., & Nel, D. G. (2000). On the distribution of the maximum likelihood estimator of Cronbach's alpha. *Psychometrika*, 65(3), 271-280. ✅ [DOI](https://doi.org/10.1007/bf02296146)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 171 — Diseño de un estudio de validación](../171-diseno-de-un-estudio-de-validacion/README.md)  
[📚 Parte 17](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[173 — Simulación de datos psicométricos →](../173-simulacion-de-datos-psicometricos/README.md)
<!-- /NAV -->
