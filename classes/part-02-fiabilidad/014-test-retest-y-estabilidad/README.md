# 014 — Test-retest: estabilidad frente a consistencia

> [Índice de la parte](../README.md) · [Anterior](../013-omega-y-alternativas-a-alfa/README.md) · [Siguiente](../015-error-tipico-de-medida/README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 3 h · Estado `escrita`
**Prerrequisitos:** clases 011 y 012.

## Objetivos

1. Diseñar un estudio test-retest y justificar el intervalo.
2. Interpretar la correlación sin confundirla con acuerdo absoluto.
3. Distinguir ruido transitorio de cambio real.
4. Elegir entre correlación y coeficiente intraclase.

## Fundamentos

Alfa mira el instrumento en una ocasión; el test-retest mira a las personas en el tiempo. El coeficiente de **estabilidad** baja por ruido transitorio (ánimo, sueño), por cambio real del rasgo o por efectos de recuerdo y práctica, y la cifra no separa esas causas.

Laboratorio (N = 10 000):

| Caso | r test-retest | Dif. de medias |
|---|---:|---:|
| Estable, poco ruido transitorio | 0,914 | −0,002 |
| Estable, mucho ruido transitorio | 0,506 | −0,016 |
| El rasgo cambia entre ocasiones | 0,727 | −0,003 |
| Estable, con práctica (+1 DE) | 0,920 | 0,996 |

La última fila es la lección: todo el grupo sube una desviación estándar y la correlación es 0,92. **r mide orden relativo, no acuerdo.** Para acuerdo absoluto se añade la diferencia de medias o un coeficiente intraclase, declarando su tipo (Shrout y Fleiss, 1979; Koo y Li, 2016).

**Intervalo:** muy corto → recuerdo; muy largo → cambio real. No hay valor universal: se justifica por la estabilidad esperada del constructo (un estado de ánimo no es un rasgo) y se declara.

## Ejemplo resuelto

Una escala de ansiedad rasgo da r = 0,55 a 6 meses. No se concluye «mala fiabilidad»: se contrasta con r a 2 semanas y con alfa; si a 2 semanas es alta, la caída es cambio, no ruido.

## Errores y límites

- Reportar r sin diferencia de medias.
- Aplicar test-retest a constructos que cambian por definición (estados).
- Llamar «fiabilidad» a la estabilidad sin precisarlo.
- La simulación usa errores independientes entre ocasiones; el recuerdo real los correlaciona e infla r.

## Ejercicios

- **Inicial.** ¿Por qué r alta no implica puntajes iguales?
- **Intermedio.** Propón y justifica un intervalo para un Big Five y otro para una escala de ánimo.
- **Avanzado.** Agrega correlación entre los errores de ambas ocasiones en `lab.py` y observa r.

## Laboratorio

```bash
python classes/part-02-fiabilidad/014-test-retest-y-estabilidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué tres causas bajan el test-retest y cuál no se separa? 2. ¿Cuándo prefieres un CCI? 3. ¿Qué intervalo evitarías en una prueba de rendimiento?
Se logra si el estudiante reporta correlación, diferencia de medias y su limitación.

## Bibliografía

- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420-428. ✅ [DOI](https://doi.org/10.1037/0033-2909.86.2.420)
- Weir, J. P. (2005). Quantifying test-retest reliability using the intraclass correlation coefficient and the SEM. *Journal of Strength and Conditioning Research*, 19(1), 231-240. ✅ [DOI](https://doi.org/10.1519/00124278-200502000-00038)
- Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine*, 15(2), 155-163. ✅ [DOI](https://doi.org/10.1016/j.jcm.2016.02.012)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
