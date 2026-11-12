# 133 — Desarrollo del lenguaje

![Portada de la clase 133](portada.svg)

> [Índice de la parte](../README.md)

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 061 y 131.

## Objetivos

1. Describir la variabilidad del vocabulario temprano.
2. Calcular qué parte de la recuperación de los «hablantes tardíos» es regresión a la media.
3. Plantear criterios de apoyo más allá de un percentil.

## Fundamentos

El vocabulario expresivo a los 24 meses es muy variable (Fenson et al., 1994). Un «hablante tardío» suele definirse por un percentil bajo (p. ej. < 10) a esa edad; la evidencia sobre qué predice la evolución posterior es limitada (Rescorla, 2011). Con estabilidad moderada entre mediciones, parte de la «recuperación» es estadística.

Laboratorio (correlación 0,5 entre 24 y 36 meses, supuesto; N = 50 000):

| Percentil | 10 | 25 | 50 | 75 | 90 |
|---|---:|---:|---:|---:|---:|
| Palabras a los 24 meses | 36 | 58 | 100 | 172 | 279 |

Hablantes tardíos (< P10): z medio −1,75 a los 24 meses y −0,88 a los 36 (sin intervención); solo 32,9 % sigue bajo el P10.

## Ejemplo resuelto

Con r = 0,5 el z esperado a los 36 meses de quien tuvo z = −1,75 es −0,5·1,75 = −0,88: coincide con el laboratorio.

## Errores y límites

- Predecir la evolución desde un percentil aislado.
- Usar baremos de otra lengua o de niños monolingües para niños bilingües.
- Equiparar «tardío» con trastorno.
- Considerar la comprensión, los gestos y el juego, no solo la producción de palabras.

## Ejercicios

- **Inicial.** ¿Qué es regresión a la media?
- **Intermedio.** Con r = 0,7 y z = −2: z esperado = −1,4.
- **Avanzado.** Cambia RHO a 0,8 en `lab.py` y reporta cuántos siguen bajo el P10.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/133-desarrollo-del-lenguaje/lab.py
```

## Autoevaluación y criterios

1. ¿Qué otra evidencia pedirías? 2. ¿Cómo orientarías a la familia mientras tanto? 3. ¿Cuándo repetirías la evaluación?
Se logra si el estudiante distingue recuperación estadística de recuperación real.

## Bibliografía

- Fenson, L., et al. (1994). Variability in early communicative development. *Monographs of the Society for Research in Child Development*, 59(5). ✅ [DOI](https://doi.org/10.2307/1166093)
- Rescorla, L. (2011). Late talkers: Do good predictors of outcome exist? *Developmental Disabilities Research Reviews*, 17(2), 141-150. ✅ [DOI](https://doi.org/10.1002/ddrr.1108)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
