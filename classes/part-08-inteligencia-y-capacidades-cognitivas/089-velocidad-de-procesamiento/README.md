# 089 — Velocidad de procesamiento

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 086 y 093.

## Objetivos

1. Explicar el compromiso velocidad–precisión.
2. Interpretar un modelo de difusión mínimo.
3. Evaluar indicadores combinados como el IES.

## Fundamentos

La velocidad de procesamiento se asocia con otras capacidades y con la edad (Salthouse, 1996). Pero el tiempo de respuesta mezcla **capacidad** y **estrategia**: más cautela implica más lentitud y más precisión (Heitz, 2014). El modelo de difusión (Ratcliff, 1978) separa la tasa de acumulación de evidencia (capacidad), la barrera (cautela) y el tiempo no decisional.

Laboratorio (1 500 ensayos por caso; deriva v = capacidad, barrera a = cautela):

| Caso | RT medio (s) | Precisión | IES |
|---|---:|---:|---:|
| capacidad media, cauto | 1,364 | 0,929 | 1,468 |
| capacidad media, apurado | 0,579 | 0,765 | 0,757 |
| capacidad alta, apurado | 0,531 | 0,911 | 0,582 |
| capacidad baja, cauto | 1,680 | 0,776 | 2,165 |

Con la **misma capacidad**, el RT cambia de 1,36 a 0,58 s y la precisión de 0,93 a 0,77 solo por la cautela. El IES (RT/precisión) no elimina ese efecto.

## Ejemplo resuelto

IES = 1,364/0,929 = 1,468; para «media apurado» 0,579/0,765 = 0,757. Aunque hay la misma capacidad, el IES varía casi a la mitad.

## Errores y límites

- Comparar RT entre personas con instrucciones o estilos distintos.
- Usar solo el RT medio (también importa la variabilidad y la cola larga).
- El modelo es mínimo: no incluye variabilidad entre ensayos ni sesgo de inicio.
- No concluir «procesamiento lento» de un tiempo largo en una persona con prudencia o ansiedad.

## Ejercicios

- **Inicial.** ¿Qué parámetro representa la cautela?
- **Intermedio.** Si la precisión sube de 0,77 a 0,93 y el RT de 0,58 a 1,36, ¿qué implica para la comparación? Hay un compromiso.
- **Avanzado.** Añade variabilidad de ensayo a ensayo en la deriva (`v`) y observa los errores lentos.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/089-velocidad-de-procesamiento/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo estandarizar instrucciones? 2. ¿Cuándo es útil un modelo de difusión? 3. ¿Qué informarías además del RT?
Se logra si el estudiante separa estrategia y capacidad al interpretar tiempos.

## Bibliografía

- Ratcliff, R. (1978). A theory of memory retrieval. *Psychological Review*, 85(2), 59-108. ✅ [DOI](https://doi.org/10.1037/0033-295x.85.2.59)
- Heitz, R. P. (2014). The speed-accuracy tradeoff: History, physiology, methodology, and behavior. *Frontiers in Neuroscience*, 8, 150. ✅ [DOI](https://doi.org/10.3389/fnins.2014.00150)
- Salthouse, T. A. (1996). The processing-speed theory of adult age differences in cognition. *Psychological Review*, 103(3), 403-428. ✅ [DOI](https://doi.org/10.1037/0033-295x.103.3.403)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
