# 028 — Modelos de dos y tres parámetros

> [Índice de la parte](../README.md) · [Anterior](../027-modelo-de-rasch/README.md) · [Siguiente](../029-informacion-del-item/README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 027.

## Objetivos

1. Interpretar a (discriminación), b (dificultad) y c (adivinación).
2. Recuperar parámetros con una regresión logística cuando θ se conoce.
3. Mostrar la distorsión de ignorar c.

## Fundamentos

```
P(θ) = c + (1 − c) · logística( a·(θ − b) )          (Birnbaum, 1968)
```

La pendiente a hace que la curva sea más o menos empinada en b; c es la asíntota inferior (opción múltiple: acierto por azar). En 2PL, c = 0.

Curvas (a, b, c):

| (a, b, c) | θ = −3 | −1 | 0 | 1 | 3 |
|---|---:|---:|---:|---:|---:|
| (1, 0, 0) | 0,05 | 0,27 | 0,50 | 0,73 | 0,95 |
| (2, 0, 0) | 0,00 | 0,12 | 0,50 | 0,88 | 1,00 |
| (1, 0, 0,2) | 0,24 | 0,42 | 0,60 | 0,78 | 0,96 |

Laboratorio (30 000 personas, θ conocido): ítem 2PL (a = 1,5; b = 0,5) → estimado a = 1,50; b = 0,50. Ítem 3PL (a = 1,5; b = 0,5; c = 0,2) ajustado como 2PL → a = 0,96; b = 0,04: la curva se aplana y se desplaza.

## Ejemplo resuelto

a = 2, θ − b = 0,5: logística(1) = 0,731. Con c = 0,2: 0,2 + 0,8 · 0,731 = 0,785.

## Errores y límites

- Ajustar 2PL a ítems de opción múltiple con adivinación notable.
- Estimar c con muestras pequeñas (inestable; a menudo se fija o se usa un prior).
- Interpretar b como «dificultad» sin considerar a y c.
- θ se conoce solo en la simulación.

## Ejercicios

- **Inicial.** ¿Cuánto vale P en θ = b para un ítem 3PL con c = 0,25? → c + (1 − c)·0,5 = 0,625.
- **Intermedio.** Compara P en θ = −1 para a = 1 y a = 2 (b = 0): 0,27 y 0,12.
- **Avanzado.** Ajusta en `lab.py` un c fijo conocido y comprueba que recuperas a y b.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/028-modelos-de-dos-y-tres-parametros/lab.py
```

## Autoevaluación y criterios

1. ¿Qué cambia al aumentar a? 2. ¿Cuándo es defendible el 3PL? 3. ¿Qué datos exige?
Se logra si el estudiante interpreta los parámetros y justifica el modelo.

## Bibliografía

- Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. En F. M. Lord & M. R. Novick, *Statistical Theories of Mental Test Scores*. Addison-Wesley. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Baker, F. B., & Kim, S.-H. (2004). *Item Response Theory: Parameter Estimation Techniques* (2.ª ed.). CRC Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
