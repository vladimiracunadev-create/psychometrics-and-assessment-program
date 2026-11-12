# 045 — Introducción a la estadística descriptiva para evaluación

> [Índice de la parte](../README.md)

**Parte 00 — Fundamentos de la medición psicológica** · Nivel fundamentos · 4 h · Estado `escrita`
**Prerrequisitos:** clase 004.

## Objetivos

1. Elegir el resumen según la forma de la distribución.
2. Leer un histograma de texto.
3. Evaluar la robustez de media y mediana ante un valor erróneo.

## Fundamentos

La media es sensible a valores extremos; la mediana y el rango intercuartil son robustos. Con distribuciones asimétricas (tiempos de respuesta) conviene reportar ambos y graficar antes de resumir.

Laboratorio (1.000 personas sintéticas): puntajes simétricos (media 55,0, mediana 54,5, asimetría 0,03); tiempos de cola larga (media 5,3, mediana 4,1, asimetría 2,18); al añadir un único valor erróneo de 9.999 s, la media pasa a 15,3 y la mediana sigue en 4,1.

## Ejemplo resuelto

Un informe con la media de tiempos de 15,3 s estaría equivocado por un solo error de digitación; la mediana habría delatado que algo no cuadra.

## Errores y límites

- Borrar valores extremos sin registro.
- Resumir sin graficar.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Cuándo difieren la media y la mediana?
- **Intermedio.** Calcula la media recortada al 5 % y compárala.
- **Avanzado.** Escribe una regla de registro para valores extremos.

## Laboratorio

```bash
python classes/part-00-fundamentos-de-la-medicion/045-introduccion-a-la-estadistica-descriptiva-para-evaluacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del resultado depende de que los datos sean sintéticos? 2. ¿Qué cambiaría con personas reales? 3. ¿Qué límite declararías?
Se logra si el estudiante ejecuta el laboratorio, interpreta las cifras con cautela y declara sus límites.

## Bibliografía

- Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
- Wilcox, R. R. (2012). *Introduction to Robust Estimation and Hypothesis Testing* (3.ª ed.). Academic Press.
