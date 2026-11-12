# 119 — Dominio del inglés laboral: evaluación de idioma

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 040 y 066.

## Objetivos

1. Entender niveles de idioma como clasificaciones con incertidumbre.
2. Estimar la matriz de clasificación de un test con cortes.
3. Distinguir comprensión de producción.

## Fundamentos

Los marcos de referencia (p. ej. el *Marco Común Europeo de Referencia*, Consejo de Europa, 2001/2020) describen niveles A1–C2. Un test traduce una habilidad estimada en un nivel mediante **cortes** fijados por un panel (clase 040). Cerca de cada corte, el error de medida produce clasificaciones erróneas. Este laboratorio no replica un examen oficial ni se equipara a un marco: usa tres niveles de ejemplo (A2, B1, B2).

Laboratorio (40 ítems 2PL; N = 4 000; cortes de θ en −0,5 y 0,7):

| Verdadero \ asignado | A2 | B1 | B2 | Exactitud |
|---|---:|---:|---:|---:|
| A2 | 1 008 | 189 | 0 | 84,2 % |
| B1 | 141 | 1 543 | 121 | 85,5 % |
| B2 | 0 | 184 | 814 | 81,6 % |

Exactitud global 84,1 %; todos los errores son a un nivel adyacente (15,9 %).

## Ejemplo resuelto

Una persona con θ = 0,65 está 0,05 por debajo del corte B2; con un error típico de ~0,3 su clasificación es casi un sorteo entre B1 y B2.

## Errores y límites

- Tratar «B2» como un hecho cuando es una categoría con error.
- Evaluar solo comprensión (lectura, escucha) y concluir sobre expresión oral o escrita.
- Usar el nivel como filtro sin analizar si el puesto lo requiere (análisis de puestos).
- Un test propio no equivale a una certificación reconocida.

## Ejercicios

- **Inicial.** ¿Dónde se concentran los errores de clasificación?
- **Intermedio.** Si el error típico baja a la mitad, ¿qué esperas de la exactitud? Sube.
- **Avanzado.** Añade un cuarto nivel (C1) y recalcula.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/119-dominio-del-ingles-laboral-evaluacion-de-idioma/lab.py
```

## Autoevaluación y criterios

1. ¿Qué habilidades evaluarías para un puesto de atención telefónica? 2. ¿Cómo informar el nivel? 3. ¿Qué evidencia de equivalencia con un marco necesitas?
Se logra si el estudiante evalúa la clasificación y recomienda cómo informarla.

## Bibliografía

- Council of Europe (2001). *Common European Framework of Reference for Languages*. Cambridge University Press (con el *Companion Volume*, 2020).
- Bachman, L. F., & Palmer, A. S. (2010). *Language Assessment in Practice*. Oxford University Press.
- Cizek, G. J., & Bunch, M. B. (2007). *Standard Setting*. Sage.
