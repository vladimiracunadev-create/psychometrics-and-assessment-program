# 124 — Comportamiento en equipos de trabajo

![Portada de la clase 124](portada.svg)

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 122 y 123.

## Objetivos

1. Describir el modelo insumo–proceso–resultado de equipos.
2. Estimar un efecto indirecto con bootstrap.
3. Distinguir efecto estadístico de efecto causal.

## Fundamentos

Los modelos de equipos organizan los factores en **insumos** (composición, tarea), **procesos** (coordinación, comunicación) y **resultados** (desempeño, satisfacción), y evolucionaron a modelos más dinámicos (Ilgen et al., 2005; Mathieu et al., 2008). Un **efecto indirecto** (a·b) mide cuánto del efecto de X sobre Y pasa por M; su inferencia se hace con remuestreo (Preacher y Hayes, 2008).

Laboratorio (80 equipos; X → M con a = 0,6; M → Y con b = 0,5; sin efecto directo):

| Medida | Valor |
|---|---:|
| Efecto indirecto verdadero | 0,300 |
| Estimado | 0,288 |
| Intervalo bootstrap 95 % | [0,122; 0,491] (excluye el 0) |
| Efecto total de X sobre Y | 0,202 |

El intervalo es amplio con 80 equipos.

## Ejemplo resuelto

a = 0,6 y b = 0,5: a·b = 0,30. Con mediación total el efecto total teórico es a·b = 0,30; el estimado (0,20) difiere por error muestral con solo 80 equipos. Con datos reales, total = directo + indirecto.

## Errores y límites

- Analizar individuos como si fueran equipos: la muestra efectiva es el número de equipos.
- Interpretar una mediación transversal como causal.
- Omitir la dependencia dentro de equipos (modelos multinivel).
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué es un proceso de equipo?
- **Intermedio.** Si a = 0,4 y b = 0,3, el indirecto es 0,12.
- **Avanzado.** Añade un efecto directo de 0,2 en `lab.py` y compara el indirecto y el total.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/124-comportamiento-en-equipos-de-trabajo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diseño sustenta la causalidad? 2. ¿Qué tamaño de muestra de equipos necesitas? 3. ¿Cómo medirías los procesos?
Se logra si el estudiante estima e interpreta un efecto indirecto con cautela.

## Bibliografía

- Ilgen, D. R., Hollenbeck, J. R., Johnson, M., & Jundt, D. (2005). Teams in organizations: From input-process-output models to IMOI models. *Annual Review of Psychology*, 56, 517-543. ✅ [DOI](https://doi.org/10.1146/annurev.psych.56.091103.070250)
- Preacher, K. J., & Hayes, A. F. (2008). Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models. *Behavior Research Methods*, 40(3), 879-891. ✅ [DOI](https://doi.org/10.3758/brm.40.3.879)
- Mathieu, J., Maynard, M. T., Rapp, T., & Gilson, L. (2008). Team effectiveness 1997–2007. *Journal of Management*, 34(3), 410-476. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
