# 003 — Escalas de medida y qué operaciones permiten

> [Clase anterior](../002-*/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../004-*/README.md)

**Parte:** 00 — Fundamentos de la medición psicológica
**Horas estimadas:** 3 · **Estado:** `escrita`

## Propósito

Determinar qué operaciones aritméticas están autorizadas sobre un conjunto de
puntajes, según el tipo de escala que los produjo — y por qué la psicometría
aplicada vive incómodamente con esa respuesta.

## Resultados de aprendizaje

1. Clasificar una variable en nominal, ordinal, de intervalo o de razón.
2. Decir qué estadísticos son legítimos en cada nivel.
3. Explicar la controversia sobre promediar respuestas Likert.
4. Justificar la posición que adopta este repositorio.

## Conceptos centrales

`nominal` · `ordinal` · `intervalo` · `razón` · `equidistancia` · `Stevens`

## Fundamentos

### Los cuatro niveles de Stevens

S. S. Stevens (1946) propuso una jerarquía que sigue siendo el marco de
referencia:

| Nivel | Qué permite | Estadístico central | Ejemplo |
|---|---|---|---|
| **Nominal** | Igualdad | Moda | Código Holland (`IAS`) |
| **Ordinal** | Orden | Mediana | Ranking de valores |
| **Intervalo** | Distancias iguales | Media | Puntaje CI |
| **Razón** | Cero absoluto | Media geométrica | Tiempo de reacción |

Cada nivel hereda lo que permite el anterior y añade una operación.

### El problema incómodo

Una respuesta Likert es, estrictamente, **ordinal**. Sabemos que "Muy exacto" es
más que "Moderadamente exacto", pero nada garantiza que la distancia entre esos
dos puntos sea la misma que entre "Moderadamente inexacto" y "Ni inexacto ni
exacto".

Si es ordinal, la media no está autorizada. Y sin embargo **todo el campo
promedia respuestas Likert**, incluido este repositorio.

### Por qué se hace igual

Tres argumentos sostienen la práctica:

1. **Robustez empírica.** Las simulaciones muestran que, con cinco o más puntos
   y distribuciones no muy asimétricas, tratar el ordinal como intervalo
   distorsiona poco las conclusiones.
2. **Agregación.** Se promedian *escalas*, no ítems sueltos. La suma de veinte
   ítems ordinales se comporta bastante como una variable continua.
3. **La alternativa cuesta.** Los métodos correctos (correlaciones policóricas,
   TRI) existen y este programa los cubre en la parte 05, pero exigen más datos
   y más supuestos.

> La postura defendible no es "da igual", sino: **se sabe que es una
> aproximación, se conocen sus condiciones de validez, y se declara.**

### Qué hace este repositorio

`motor/puntuacion.py` promedia respuestas Likert. La decisión está documentada y
sus condiciones son las anteriores. Cuando la parte 05 introduzca la TRI, el
mismo catálogo podrá puntuarse con el método correcto y comparar ambos
resultados sobre los mismos datos.

Lo que el motor **no** hace es promediar puntajes ipsativos entre personas, que
es un error de otra categoría: allí la aritmética falla por construcción, no por
aproximación. Ver parte 01, clase 8.

## Laboratorio

`lab.py` toma un conjunto de respuestas y compara tres tratamientos: media
aritmética (intervalo), mediana (ordinal) y puntaje normalizado por rango. Mide
cuánto cambia el orden de las personas según el tratamiento elegido.

```bash
python classes/part-00-fundamentos-de-la-medicion/003-escalas-de-medida-y-sus-operaciones/lab.py
```

## Para pensar

1. El código Holland `IAS` es nominal. ¿Qué se pierde al reducir seis puntajes
   continuos a tres letras?
2. Si las distancias Likert no son iguales, ¿por qué la agregación las vuelve
   *más* parecidas a una escala de intervalo?
3. ¿Qué tendría que ocurrir en los datos para que la aproximación falle?

## Bibliografía

- Stevens, S. S. (1946). On the theory of scales of measurement. *Science*,
  103(2684), 677-680.
- Norman, G. (2010). Likert scales, levels of measurement and the "laws" of
  statistics. *Advances in Health Sciences Education*, 15(5), 625-632.
