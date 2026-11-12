# 195 — Proyecto: informe para una organización

> [Índice de la parte](../README.md)

**Parte 19 — Aplicaciones avanzadas y proyectos integradores** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 112.

## Objetivos

1. Resumir una encuesta por equipo con intervalos de Wilson.
2. Aplicar supresión por n mínimo.
3. Evitar afirmar diferencias que los intervalos no sostienen.

## Fundamentos

El porcentaje favorable de un equipo pequeño es una estimación muy imprecisa; el intervalo de Wilson al 95 % es una opción mejor que el de Wald con pocos casos (Brown et al., 2001). Para proteger la identidad se suprime todo grupo con menos de cinco respuestas. Solo se mencionan diferencias entre equipos cuando sus intervalos no se solapan, y aun así son descriptivas.

Laboratorio (encuesta sintética): Operaciones 65 % [50 %, 77 %], Comercial 81 % [64 %, 91 %], Finanzas 64 % [39 %, 84 %], TI 11 % [2 %, 44 %] (n = 9), Legal suprimido (n = 3); dos diferencias con intervalos separados.

## Ejemplo resuelto

El equipo de 3 personas no se informa ni se calcula por resta: un informe agregado no debe permitir deducir lo que respondió una persona.

## Errores y límites

- Publicar equipos de 2 o 3 personas.
- Interpretar el clima como evaluación de quien lidera.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Por qué Wilson y no Wald con n pequeño?
- **Intermedio.** Cambia el n mínimo a 8 y observa qué se suprime.
- **Avanzado.** Diseña una regla de supresión complementaria.

## Laboratorio

```bash
python classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/195-proyecto-informe-para-una-organizacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué decisión de este proyecto es la más discutible? 2. ¿Qué evidencia falta? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante ejecuta el proyecto, interpreta sus cifras con cautela y declara sus límites.

## Bibliografía

- Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval estimation for a binomial proportion. *Statistical Science*, 16(2), 101-133. ✅ [DOI](https://doi.org/10.1214/ss/1009213286)
- Ley 19.628 y Ley 21.719 (Chile): verificar el texto vigente en bcn.cl. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
