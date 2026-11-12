# 198 — Proyecto: tablero de seguimiento longitudinal

> [Índice de la parte](../README.md)

**Parte 19 — Aplicaciones avanzadas y proyectos integradores** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 175.

## Objetivos

1. Mostrar trayectorias con su banda de error.
2. Marcar cambio solo si supera el cambio mínimo fiable.
3. Evitar semáforos que conviertan ruido en veredictos.

## Fundamentos

El índice de cambio fiable divide la diferencia entre dos mediciones por √2 × EEM (Jacobson & Truax, 1991). Con desviación 10 y fiabilidad 0,85, EEM = 3,87 y el cambio mínimo fiable al 95 % es 10,7 puntos.

Laboratorio (6 estudiantes sintéticos, 5 mediciones): tres con cambio fiable positivo (RCI +2,45, +2,36, +3,06), uno con cambio fiable negativo (−2,22) y dos sin cambio fiable.

## Ejemplo resuelto

Una diferencia de +6,1 puntos (RCI +1,11) no se informa como mejora: está dentro del ruido de medida.

## Errores y límites

- Ignorar efectos de práctica y regresión a la media.
- Usar colores de semáforo para clasificar personas.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Por qué la diferencia tiene más error que cada medición?
- **Intermedio.** Cambia la fiabilidad a 0,70 y recalcula el cambio mínimo.
- **Avanzado.** Añade un indicador de variabilidad entre mediciones.

## Laboratorio

```bash
python classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/198-proyecto-tablero-de-seguimiento-longitudinal/lab.py
```

## Autoevaluación y criterios

1. ¿Qué decisión de este proyecto es la más discutible? 2. ¿Qué evidencia falta? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante ejecuta el proyecto, interpreta sus cifras con cautela y declara sus límites.

## Bibliografía

- Jacobson, N. S., & Truax, P. (1991). Clinical significance. *Journal of Consulting and Clinical Psychology*, 59(1), 12-19.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
