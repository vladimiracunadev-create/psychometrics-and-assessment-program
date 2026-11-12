# 025 — Error típico de medida e intervalos de confianza del puntaje

> [Índice de la parte](../README.md) · [Anterior](../024-test-retest-y-estabilidad/README.md) · [Siguiente](../../part-03-validez/031-validez-como-argumento/README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 024.

## Objetivos

1. Calcular el error típico de medida (ETM) desde DE y fiabilidad.
2. Construir un intervalo para un puntaje individual y para una diferencia.
3. Explicar por qué una diferencia moderada entre dos aplicaciones puede ser solo error.

## Fundamentos

```
ETM = DE · √(1 − ρ)         intervalo 95 %: X ± 1,96 · ETM
ETM de una diferencia = ETM · √2
```

Laboratorio: media 100, DE 15, ρ = 0,90 → ETM = 4,74; el intervalo es ±9,3 puntos. Por simulación (50 000 personas):

- cobertura del intervalo sobre el puntaje verdadero: 0,950;
- umbral de cambio fiable: 13,1 puntos; personas sin cambio real marcadas como cambiadas: 0,050;
- diferencias de más de 10 puntos entre dos medidas **sin cambio real**: 13,5 % (cerca de una de cada siete).

Con fiabilidad 0,90, que es alta, un puntaje se mueve ±9 puntos solo por error. Una diferencia de 10 puntos entre dos aplicaciones no es evidencia de cambio (idea del índice de cambio fiable de Jacobson y Truax, 1991).

Nota: el intervalo centrado en el observado cubre 95 % en promedio, pero pierde cobertura en los extremos por la regresión a la media; la clase 030 desarrolla la alternativa centrada en el verdadero estimado.

## Ejemplo resuelto

DE 10, ρ = 0,84: ETM = 10 · √0,16 = 4. Un puntaje de 60 tiene intervalo 60 ± 7,84. Dos medidas que difieren 9 puntos: umbral 1,96 · 4 · √2 = 11,1, así que 9 no basta.

## Errores y límites

- Reportar un puntaje sin su intervalo.
- Usar un único ETM para todos los niveles (en la práctica varía con el nivel del rasgo; la TRI lo modela).
- Interpretar «no significativo» como «no cambió».

## Ejercicios

- **Inicial.** DE 15, ρ = 0,75: ETM = 7,5.
- **Intermedio.** Con ese ETM, ¿qué diferencia entre dos aplicaciones es fiable al 95 %? → 1,96 · 7,5 · √2 = 20,8.
- **Avanzado.** En `lab.py` baja ρ a 0,70 y observa cómo cambia la proporción de «cambios» espurios mayores de 10 puntos.

## Laboratorio

```bash
python classes/part-02-fiabilidad/025-error-tipico-de-medida/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué el ETM de una diferencia es mayor que el de un puntaje? 2. ¿Qué decisión de aula o de selección sería indefendible con un cambio de 10 puntos? 3. ¿Qué información falta en un informe que solo dice «mejoró 8 puntos»?
Se logra si el estudiante calcula ETM e intervalos y rechaza conclusiones que caben dentro del error.

## Bibliografía

- Harvill, L. M. (1991). Standard error of measurement. *Educational Measurement: Issues and Practice*, 10(2), 33-41. ✅ [DOI](https://doi.org/10.1111/j.1745-3992.1991.tb00195.x)
- Jacobson, N. S., & Truax, P. (1991). Clinical significance: A statistical approach to defining meaningful change in psychotherapy research. *Journal of Consulting and Clinical Psychology*, 59(1), 12-19. ✅ [DOI](https://doi.org/10.1037/0022-006x.59.1.12)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
