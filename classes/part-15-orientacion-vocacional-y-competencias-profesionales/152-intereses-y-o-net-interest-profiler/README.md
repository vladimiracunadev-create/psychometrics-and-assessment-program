# 152 — Intereses y O*NET Interest Profiler

![Portada de la clase 152](portada.svg)

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 151.

## Objetivos

1. Leer la ficha de procedencia y licencia de un instrumento adaptado.
2. Relacionar un perfil de intereses con ocupaciones.
3. Medir la estabilidad del ranking de ocupaciones.

## Fundamentos

El *O\*NET Interest Profiler* es una herramienta del Departamento del Trabajo de EE. UU. (fuente primaria: onetcenter.org). `onet-riasec-sf` es una **adaptación** propia al español con licencia *O\*NET Tools Developer* y una **obligación de validación pendiente** (sección 3(b) para contenido modificado) declarada en su ficha; por eso no se usa para decidir sobre personas. La relación entre perfiles y ocupaciones se hace comparando el perfil de la persona con el de cada ocupación (Armstrong et al., 2008).

Laboratorio (12 ocupaciones **ficticias**; error de medida de una escala de 10 ítems, DE 0,20 en escala 0–1; 800 repeticiones):

| Estabilidad entre dos aplicaciones | Valor |
|---|---:|
| Misma ocupación en el 1.er lugar | 33,9 % |
| Al menos 2 de 3 ocupaciones en común | 60,6 % |

## Ejemplo resuelto

Correlación entre el perfil de una persona (S alto, I medio) y el de «docente» = 0,92; con «contador» = 0,15. El orden de las dos ocupaciones cercanas se invierte con poco error.

## Errores y límites

- Presentar una ocupación como «la ideal».
- Citar datos de ocupaciones sin su fuente y fecha.
- Usar un instrumento con validación pendiente para decisiones.
- Las ocupaciones y sus perfiles del laboratorio son inventados.

## Ejercicios

- **Inicial.** ¿Qué dice la sección de validación pendiente de la ficha?
- **Intermedio.** ¿Por qué un «top 3» es más estable que un «top 1»? Tolera cambios de orden.
- **Avanzado.** Agrega tres ocupaciones ficticias y observa la estabilidad.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/152-intereses-y-o-net-interest-profiler/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo presentarías un listado de opciones a explorar? 2. ¿Qué datos locales del mercado laboral usarías? 3. ¿Cuándo se puede retirar la advertencia de validación?
Se logra si el estudiante audita la licencia y presenta resultados como opciones a explorar.

## Bibliografía y fuentes

- O*NET Resource Center. *O\*NET Interest Profiler* (onetcenter.org). U.S. Department of Labor/ETA. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Armstrong, P. I., Day, S. X., McVay, J. P., & Rounds, J. (2008). Holland's RIASEC model as an integrative framework for individual differences. *Journal of Counseling Psychology*, 55(1), 1-18. ✅ [DOI](https://doi.org/10.1037/0022-0167.55.1.1)
- `instruments/onet-riasec-sf.yaml` y `DISCLAIMER.md` del repositorio. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
