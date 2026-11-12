# 171 — Diseño de un estudio de validación

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 016 a 020 y 059.

## Objetivos

1. Traducir cada afirmación de validez en una hipótesis, un análisis y un tamaño de muestra.
2. Calcular tamaños de muestra mínimos con supuestos explícitos.
3. Preparar un plan previo que se pueda preinscribir.

## Fundamentos

Un estudio de validación reúne evidencia de varias fuentes (contenido, procesos, estructura interna, relaciones con otras variables, consecuencias; AERA/APA/NCME, 2014). Guías prácticas ordenan las fases de desarrollo y validación de escalas (DeVellis, 2017; Boateng et al., 2018). Cada componente tiene su costo muestral.

Laboratorio (aproximaciones estándar, supuestos en el código):

| Componente | N mínimo |
|---|---:|
| Fiabilidad (alfa = 0,80; 12 ítems; ±0,05) | 137 |
| Fiabilidad (alfa = 0,90; 12 ítems; ±0,05) | 36 |
| Correlación con un criterio (r = 0,30) | 85 |
| Convergente 0,50 > discriminante 0,30 | 280 |
| Diferencia entre grupos conocidos (d = 0,30) | 350 |
| AFC (10 casos × 25 parámetros) | 250 |

El componente más exigente fija el N: 350 personas.

## Ejemplo resuelto

Correlación r = 0,30 con 80 % de potencia: n = ((1,96 + 0,84)/atanh 0,30)² + 3 = (2,80/0,3095)² + 3 = 85.

## Errores y límites

- Calcular el N solo para el análisis más fácil.
- No declarar el efecto esperado ni la fiabilidad supuesta.
- Muestra de conveniencia sin discusión de representatividad.
- Fórmulas aproximadas: el plan se afina por simulación (clase 173).

## Ejercicios

- **Inicial.** Nombra las cinco fuentes de evidencia de los Standards.
- **Intermedio.** Calcula n para r = 0,20 y 80 % de potencia → ((2,80)/0,2027)² + 3 = 194.
- **Avanzado.** Completa el plan con un componente de invarianza entre sexos.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/171-diseno-de-un-estudio-de-validacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia es imprescindible para tu uso? 2. ¿Qué harías con N menor al requerido? 3. ¿Qué parte registrarías antes de recolectar?
Se logra si el estudiante produce un plan con hipótesis, análisis y N justificado.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- DeVellis, R. F. (2017). *Scale Development: Theory and Applications* (4.ª ed.). Sage. ⚠️ existe, pero Crossref registra 1992 (¿otra edición?; [DOI](https://doi.org/10.2307/2075704))
- Boateng, G. O., et al. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health*, 6, 149. ✅ [DOI](https://doi.org/10.3389/fpubh.2018.00149)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
