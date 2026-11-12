# 128 — Clima organizacional y escolar

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 122 y 078.

## Objetivos

1. Tratar el clima como constructo de grupo (ICC).
2. Aplicar una regla de supresión de grupos pequeños.
3. Equilibrar utilidad estadística y protección del anonimato.

## Fundamentos

El clima organizacional o escolar describe percepciones compartidas del ambiente (Schneider, Ehrhart y Macey, 2013; Thapa et al., 2013). Es un constructo de grupo: se justifica agregar si hay variación entre grupos (ICC(1)) y el promedio es fiable (ICC(2)). Con grupos pequeños, reportar resultados expone a quienes respondieron; se aplica una **regla de supresión** (aquí, menos de 5 respuestas no se reportan; umbral que se decide con criterios de privacidad, parte 07).

Laboratorio (40 grupos de 3 a 40 personas; 504 respuestas):

| Medida | Valor |
|---|---:|
| Tamaño medio armónico | 6,9 |
| ICC(1) / ICC(2) | 0,084 / 0,530 |
| Grupos con < 5 respuestas (suprimidos) | 9 de 40 |
| Personas en grupos suprimidos | 32 (6,3 % de las respuestas) |

La fiabilidad del promedio por grupo es modesta (0,53), lo que sugiere cautela al comparar grupos.

## Ejemplo resuelto

Un equipo de 3 personas en que 2 declaran sentirse maltratadas: reportarlo identifica a casi todos. Se agrega a un nivel superior.

## Errores y límites

- Reportar a un nivel con pocos respondentes.
- Usar el clima para evaluar o sancionar a jefaturas sin evidencia de validez.
- Triangulación: complementar con otros datos (rotación, ausentismo).
- Datos sintéticos; los umbrales de supresión varían según la política y la ley.

## Ejercicios

- **Inicial.** ¿Por qué el clima es de grupo?
- **Intermedio.** Con ICC(1) = 0,1 y tamaño 10: ICC(2) = 10·0,1/(1 + 9·0,1) = 0,53 (Spearman-Brown).
- **Avanzado.** Cambia el umbral a 8 y reporta cuántos grupos se suprimen.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/128-clima-organizacional-y-escolar/lab.py
```

## Autoevaluación y criterios

1. ¿Quién ve los resultados y a qué nivel? 2. ¿Cómo comunicar un resultado suprimido? 3. ¿Qué acción derivas de una encuesta de clima?
Se logra si el estudiante calcula ICC y aplica una regla de supresión justificada.

## Bibliografía

- Schneider, B., Ehrhart, M. G., & Macey, W. H. (2013). Organizational climate and culture. *Annual Review of Psychology*, 64, 361-388. ✅ [DOI](https://doi.org/10.1146/annurev-psych-113011-143809)
- Thapa, A., Cohen, J., Guffey, S., & Higgins-D'Alessandro, A. (2013). A review of school climate research. *Review of Educational Research*, 83(3), 357-385. ✅ [DOI](https://doi.org/10.3102/0034654313483907)
- Bliese, P. D. (2000). Within-group agreement, non-independence, and reliability. En K. J. Klein & S. W. J. Kozlowski (Eds.), *Multilevel Theory, Research, and Methods in Organizations*. Jossey-Bass. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
