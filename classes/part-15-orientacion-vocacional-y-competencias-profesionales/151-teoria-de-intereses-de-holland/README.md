# 151 — Teoría de intereses de Holland

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 024 y 107.

## Objetivos

1. Describir los seis tipos RIASEC y el código de tres letras.
2. Puntuar un instrumento real del repositorio con el motor.
3. Cuantificar la estabilidad del código ante el error de respuesta.

## Fundamentos

Holland (1997) propone seis tipos de intereses (Realista, Investigador, Artístico, Social, Emprendedor, Convencional) dispuestos en un hexágono, y describe personas y ambientes con un **código de tres letras**. La estructura circular es una predicción falsable (clase 024; Rounds y Tracey, 1993) y la teoría tiene respaldo variable según el aspecto (Nauta, 2010). El código exacto es una síntesis inestable: ordenar tres de seis puntajes cercanos es sensible al error.

Laboratorio con `onet-riasec-sf` (60 ítems, motor del repositorio; 500 personas simuladas que responden dos veces):

| Coincidencia entre aplicaciones | Valor |
|---|---:|
| Primera letra | 69,2 % |
| Conjunto de tres letras | 75,6 % |
| Código exacto | 39,4 % |

Ejemplo: SEA en una aplicación y ESA en la otra.

## Ejemplo resuelto

Medias por escala S = 4,1; E = 4,0; A = 3,9; I = 2,5; R = 2,2; C = 2,0: código SEA. Con error de ±0,2, E y S pueden intercambiarse: el conjunto {S, E, A} es estable, el orden no.

## Errores y límites

- Decidir una carrera por el código.
- Interpretar interés como capacidad.
- Usar la adaptación con validación pendiente (ver `DISCLAIMER.md`) para decisiones.
- Datos sintéticos; la estructura hexagonal se asumió en la simulación.

## Ejercicios

- **Inicial.** ¿Qué letras son adyacentes a R en el hexágono? I y C.
- **Intermedio.** ¿Cuántos códigos de tres letras ordenados existen con 6 tipos? 6·5·4 = 120.
- **Avanzado.** Reduce el ruido a 0,5 en `lab.py` y observa las coincidencias.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/151-teoria-de-intereses-de-holland/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo presentarías un perfil a un estudiante? 2. ¿Qué información adicional recogerías? 3. ¿Qué límites tiene un test de intereses?
Se logra si el estudiante usa el motor, cuantifica la estabilidad y matiza el uso.

## Bibliografía

- Holland, J. L. (1997). *Making Vocational Choices* (3.ª ed.). Psychological Assessment Resources.
- Rounds, J., & Tracey, T. J. (1993). Prediger's dimensional representation of Holland's RIASEC circumplex. *Journal of Applied Psychology*, 78(6), 875-890.
- Nauta, M. M. (2010). The development, evolution, and status of Holland's theory of vocational personalities. *Journal of Counseling Psychology*, 57(1), 11-22.
