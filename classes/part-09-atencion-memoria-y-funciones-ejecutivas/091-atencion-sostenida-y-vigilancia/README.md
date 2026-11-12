# 091 — Atención sostenida y vigilancia

![Portada de la clase 091](portada.svg)

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 027 y 089.

## Objetivos

1. Describir una tarea de desempeño continuo y el decremento de vigilancia.
2. Calcular d′ y el criterio c (teoría de detección de señales).
3. Distinguir sensibilidad de cautela.

## Fundamentos

En tareas de vigilancia el rendimiento suele empeorar con el tiempo en la tarea. La teoría de detección de señales separa **sensibilidad** (d′ = z(aciertos) − z(falsas alarmas)) de **criterio** (c = −½[z(aciertos) + z(falsas alarmas)]). Para evitar proporciones 0 o 1 se aplica una corrección log-lineal (Hautus, 1995).

Laboratorio (4 bloques de 200 estímulos, 10 % señales, 40 observadores simulados por bloque):

| Bloque | Aciertos | Falsas alarmas | d′ | c | Verdad (d′, c) |
|---:|---:|---:|---:|---:|---|
| 1 | 0,859 | 0,161 | 2,04 | −0,03 | (2,0; 0,0) |
| 2 | 0,801 | 0,132 | 1,94 | 0,15 | (1,9; 0,15) |
| 3 | 0,724 | 0,112 | 1,79 | 0,32 | (1,8; 0,30) |
| 4 | 0,644 | 0,099 | 1,64 | 0,46 | (1,7; 0,45) |

Los aciertos caen de 0,86 a 0,64, pero d′ cae solo 0,4 y c sube casi 0,5: gran parte del «decremento» es un criterio más conservador.

## Ejemplo resuelto

Aciertos 0,80 y falsas alarmas 0,10: z(0,80) = 0,84; z(0,10) = −1,28; d′ = 2,12; c = −½(0,84 − 1,28) = 0,22.

## Errores y límites

- Informar solo omisiones: confunde atención con cautela.
- Usar d′ por persona con pocas señales (20 por bloque): muy ruidoso.
- Interpretar un decremento como «déficit de atención» (diagnóstico) sin evaluación clínica.

## Ejercicios

- **Inicial.** ¿Qué indica un c positivo?
- **Intermedio.** Aciertos 0,70 y falsas alarmas 0,05 → z = 0,52 y −1,64; d′ = 2,16.
- **Avanzado.** Simula un observador cuyo d′ cae pero c se mantiene y compara los patrones.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/091-atencion-sostenida-y-vigilancia/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué se necesita registrar las falsas alarmas? 2. ¿Cuántas señales necesitas? 3. ¿Qué otra explicación tiene un decremento?
Se logra si el estudiante separa d′ y c al interpretar una tarea.

## Bibliografía

- Hautus, M. J. (1995). Corrections for extreme proportions and their biasing effects on estimated values of d′. *Behavior Research Methods, Instruments, & Computers*, 27(1), 46-51. ✅ [DOI](https://doi.org/10.3758/bf03203619)
- Macmillan, N. A., & Creelman, C. D. (2005). *Detection Theory: A User's Guide* (2.ª ed.). Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Warm, J. S., Parasuraman, R., & Matthews, G. (2008). Vigilance requires hard mental work and is stressful. *Human Factors*, 50(3), 433-441. ✅ [DOI](https://doi.org/10.1518/001872008x312152)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
