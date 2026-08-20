# 004 — Puntaje bruto, media por ítem y por qué no son lo mismo

> [Clase anterior](../003-*/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../005-*/README.md)

**Parte:** 00 — Fundamentos de la medición psicológica
**Horas estimadas:** 3 · **Estado:** `escrita`

## Propósito

Explicar por qué el puntaje bruto es engañoso, qué lo reemplaza dentro de este
motor, y por qué ninguno de los dos basta sin una referencia externa.

## Resultados de aprendizaje

1. Calcular bruto y media por ítem, y decir cuándo usar cada uno.
2. Detectar el error de comparar brutos entre escalas de distinta longitud.
3. Explicar por qué agregar promediando promedios está mal.
4. Reconocer que ninguna de las dos cifras es interpretable sin baremo.

## Conceptos centrales

`puntaje bruto` · `media por ítem` · `agregación ponderada` · `baremo`

## Fundamentos

### El bruto depende de cuántos ítems haya

En el IPIP-NEO-120, el dominio Responsabilidad tiene 24 ítems y la faceta Orden
tiene 4. Con respuestas en el punto medio (3):

- Responsabilidad: bruto = 72
- Orden: bruto = 12

Si alguien concluye "es seis veces más responsable que ordenado", ha comparado
longitudes de escala, no rasgos.

### La media por ítem

```
media_item = suma de respuestas efectivas / número de ítems respondidos
```

En el ejemplo anterior, ambas dan **3.00**. Ahora sí son comparables entre sí,
y además quedan en la misma unidad que la escala de respuesta: un 4.2 significa
"en promedio, algo más que *moderadamente exacto*".

Por eso `PuntajeEscala` expone las dos cifras, y todo lo que el motor compara
—el código Holland, las fortalezas de firma, el orden de facetas— usa
`media_item`, nunca `bruto`.

### El error del promedio de promedios

Al calcular un dominio a partir de sus facetas, hay dos formas y **no dan lo
mismo**:

```
A: media de las medias de las facetas
B: media de todos los ítems de todas las facetas
```

Coinciden solo si todas las facetas tienen el mismo número de ítems. Cuando no,
A da a cada faceta el mismo peso con independencia de cuántos ítems la midan, lo
que equivale a decidir en silencio que una faceta de 2 ítems pesa tanto como una
de 10.

Este motor usa **B**, y `tests/test_puntuacion.py` lo fija con un caso donde
ambas difieren: 2.0 contra 1.8.

> **En el catálogo actual, A y B coinciden siempre.** Todas las escalas hoja
> —las 30 facetas del IPIP-NEO-120 y las 24 fortalezas del IPIP-VIA-R— tienen
> exactamente 4 ítems, así que ponderar por ítem no cambia nada.
>
> Que una virtud del VIA agrupe 3 fortalezas y otra 5 es irrelevante aquí: lo
> que importa no es cuántas hijas tiene el padre, sino cuántos ítems tiene cada
> hija. El laboratorio verifica esa coincidencia sobre los datos reales y
> construye un instrumento sintético de facetas desiguales (2 ítems frente a 6)
> para exhibir la divergencia, que allí llega a un punto entero de diferencia.

### Lo que ninguna de las dos cifras dice

Una media por ítem de 4.2 en Responsabilidad **no** significa "alto". Significa
que respondió, en promedio, algo más que *moderadamente exacto*. Si la población
de referencia promedia 4.4, esa persona está por debajo del promedio.

Convertir una media en un percentil requiere una muestra normativa. Eso es la
parte 06, y es la razón de que `PuntajeEscala` traiga los campos `percentil`,
`z` y `baremo` todavía en `None`: la estructura está, los datos no.

## Laboratorio

`lab.py` puntúa el mismo protocolo de las dos formas sobre todo el catálogo
—donde coinciden— y sobre un instrumento sintético de facetas desiguales, donde
la diferencia alcanza un punto entero.

```bash
python classes/part-00-fundamentos-de-la-medicion/004-puntaje-bruto-y-media-por-item/lab.py
```

## Para pensar

1. ¿En qué caso el bruto sí es la cifra correcta que informar?
2. Si una escala tiene 3 de 10 ítems omitidos, ¿la media por ítem sigue siendo
   comparable con la de alguien que respondió los 10?
3. ¿Por qué `PuntajeEscala` guarda `items_respondidos` **e** `items_totales`?

## Bibliografía

- AERA, APA & NCME (2014). *Standards*. Cap. 5, "Scores, Scales, Norms".
- Johnson, J. A. (2014). IPIP-NEO-120. *Journal of Research in Personality*, 51.
