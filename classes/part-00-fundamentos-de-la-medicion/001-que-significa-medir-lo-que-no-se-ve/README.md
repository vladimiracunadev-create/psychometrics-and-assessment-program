# 001 — Qué significa medir lo que no se ve

> Inicio del programa · [Índice de la parte](../README.md) · [Clase siguiente](../002-*/README.md)

**Parte:** 00 — Fundamentos de la medición psicológica
**Horas estimadas:** 4 · **Estado:** `escrita`

## Propósito

Establecer qué se está afirmando cuando se dice que un cuestionario **mide** la
responsabilidad, la ansiedad o el interés vocacional, y por qué esa afirmación
no es evidente.

## Resultados de aprendizaje

Al terminar podrás:

1. Distinguir un **constructo** de su **indicador**, y explicar por qué nunca se
   observa el primero.
2. Enunciar el supuesto central de la medición psicológica y señalar dónde puede
   fallar.
3. Reconocer la diferencia entre medir una longitud y medir un rasgo.
4. Explicar por qué un puntaje sin referencia no significa nada.

## Conceptos centrales

`constructo` · `indicador` · `variable latente` · `operacionalización` · `inferencia`

## Fundamentos

### El problema de partida

Una cinta métrica toca el objeto que mide. Un cuestionario no. Cuando alguien
responde *"Siempre estoy preparado"* con un 4 de 5, no se ha observado su
responsabilidad: se ha observado **una marca en un formulario**.

Todo lo demás es inferencia. La cadena completa es:

```
rasgo no observable  ->  conducta que lo manifiesta  ->  ítem que la interroga
                     ->  respuesta marcada          ->  puntaje agregado
                     ->  interpretación
```

Cada flecha es un supuesto que puede fallar. La psicometría es, en buena medida,
la disciplina que se ocupa de someter esas flechas a prueba.

### Constructo e indicador

Un **constructo** es una abstracción que se postula para explicar regularidades
en la conducta. Nadie ha visto la extraversión; se postula porque quien va a
muchas fiestas también tiende a hablar con desconocidos y a sentirse cómodo en
grupo, y esas conductas covarían.

Un **indicador** es algo observable que se supone relacionado con el constructo.
El ítem *"Hago amigos con facilidad"* es un indicador de cordialidad.

> El error más común es tratar el indicador como si fuera el constructo. Un
> puntaje alto en un test de ansiedad no *es* ansiedad: es un puntaje del que se
> infiere ansiedad, con un margen de error que hay que declarar.

### El supuesto central

La medición psicológica descansa en una idea sencilla y fuerte:

**Si varios indicadores distintos covarían, es razonable postular una causa común
que los explique.**

Ese es el motivo de que un test tenga muchos ítems y no uno solo. Un ítem
aislado mezcla el rasgo con su circunstancia: quien responde *"Siempre estoy
preparado"* puede estar pensando en el examen de ayer. Al promediar veinte ítems,
las circunstancias particulares tienden a cancelarse y lo que comparten —el
rasgo— se acumula.

El supuesto puede fallar de dos maneras, y ambas tienen nombre propio en el
resto del programa:

- Los indicadores covarían pero **no por el constructo** que se cree, sino por
  otra cosa: el estilo de respuesta, la deseabilidad social, el vocabulario.
  Eso es un problema de **validez** (parte 03).
- Los indicadores covarían tan poco que no sostienen la inferencia de una causa
  común. Eso es un problema de **fiabilidad** (parte 02).

### Medir un rasgo no es medir una longitud

| | Longitud | Rasgo psicológico |
|---|---|---|
| Unidad | Definida y constante (el metro) | No existe unidad natural |
| Cero | Absoluto y significativo | Arbitrario: no hay "cero responsabilidad" |
| Acceso | Directo | Solo por indicadores |
| Comparación | Universal | Requiere una muestra de referencia |

De esta tabla se sigue la consecuencia práctica más importante de la clase:

> **Un puntaje psicológico aislado no significa nada.** Sacar 84 en una escala no
> es alto ni bajo hasta saber cuántos ítems tiene, en qué rango, y cómo puntúa la
> población con la que tiene sentido compararse.

Por eso este repositorio nunca informa un bruto sin acompañarlo de la media por
ítem y del número de ítems respondidos, y por eso la parte 06 se dedica entera a
los baremos.

## Laboratorio

`lab.py` simula un rasgo latente en 500 personas, genera respuestas a ítems que
lo reflejan con ruido, y muestra cómo la correlación entre el puntaje observado
y el rasgo verdadero crece al añadir ítems. Es la demostración numérica del
supuesto central.

```bash
python classes/part-00-fundamentos-de-la-medicion/001-que-significa-medir-lo-que-no-se-ve/lab.py
```

## Para pensar

1. La estatura tiene un cero absoluto; la extraversión no. ¿Qué operaciones
   aritméticas deja de autorizar esa diferencia?
2. Si dos personas obtienen el mismo puntaje, ¿son iguales en el rasgo? ¿Qué
   necesitarías saber para responder?
3. Un test de una sola pregunta puede ser válido en algún caso. ¿En cuál?

## Bibliografía

- Borsboom, D. (2005). *Measuring the Mind: Conceptual Issues in Contemporary
  Psychometrics*. Cambridge University Press. Cap. 1.
- Michell, J. (1999). *Measurement in Psychology*. Cambridge University Press.
- AERA, APA & NCME (2014). *Standards for Educational and Psychological
  Testing*. Cap. 1.
