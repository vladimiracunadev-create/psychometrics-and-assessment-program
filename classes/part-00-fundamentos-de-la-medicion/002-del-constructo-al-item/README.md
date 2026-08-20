# 002 — Del constructo al ítem: cómo nace una pregunta

> [Clase anterior](../001-*/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../003-*/README.md)

**Parte:** 00 — Fundamentos de la medición psicológica
**Horas estimadas:** 4 · **Estado:** `escrita`

## Propósito

Recorrer el camino que va de una idea abstracta —"quiero medir la
responsabilidad"— a una frase concreta que una persona pueda responder, y
mostrar dónde se pierde o se gana calidad en ese trayecto.

## Resultados de aprendizaje

1. Definir un constructo con la precisión suficiente para que sea medible.
2. Construir una **tabla de especificaciones** que delimite el dominio.
3. Reconocer los cuatro defectos clásicos de redacción de ítems.
4. Explicar por qué un banco necesita más ítems de los que acabará usando.

## Conceptos centrales

`definición operacional` · `dominio del constructo` · `tabla de especificaciones`
· `deficiencia` · `contaminación`

## Fundamentos

### Primero la definición, después el ítem

Escribir ítems antes de definir el constructo es el error de origen más caro,
porque no se detecta hasta el análisis factorial, cuando ya hay datos recogidos.

Una definición útil delimita **qué entra y qué no**. Compárense:

- Vaga: *"Responsabilidad es ser responsable en el trabajo."*
- Operativa: *"Grado en que una persona organiza su actividad, persiste ante la
  dificultad y controla sus impulsos para alcanzar metas."*

La segunda ya sugiere sus facetas: orden, perseverancia, autocontrol. No es
casualidad que el IPIP-NEO-120 mida Responsabilidad con seis facetas —
autoeficacia, orden, sentido del deber, orientación al logro, autodisciplina y
cautela. Esa estructura salió de una definición, no de una intuición.

### Los dos fallos del dominio

Un instrumento puede fallar por defecto o por exceso:

| Fallo | Qué ocurre | Ejemplo |
|---|---|---|
| **Deficiencia** | El instrumento no cubre parte del constructo | Medir responsabilidad solo con ítems de orden, sin perseverancia |
| **Contaminación** | El instrumento captura algo ajeno al constructo | Ítems con vocabulario difícil que miden, de paso, nivel educativo |

La **tabla de especificaciones** es la herramienta que previene ambos: una
matriz de facetas por número de ítems previstos, decidida *antes* de escribir.

### Cuatro defectos de redacción

1. **Doble cañón**: dos afirmaciones en un ítem. *"Soy ordenado y puntual"* — no
   se puede responder si se es una cosa y no la otra.
2. **Ambigüedad de frecuencia**: *"A veces me enojo"* — todos a veces se enojan;
   el ítem no discrimina.
3. **Deseabilidad social**: *"¿Es usted una persona honesta?"* — mide la
   disposición a admitir, no el rasgo.
4. **Doble negación**: *"No es raro que no termine lo que empiezo"* — el error de
   comprensión se confunde con el rasgo.

> Obsérvese el ítem real del IPIP-VIA-R `"No abandono una tarea antes de
> terminarla"`. Es una negación simple y directa, no una doble negación: se
> entiende de una lectura.

### Sobreproducir para poder descartar

Un banco parte con dos o tres veces los ítems que sobrevivirán. El pilotaje
(parte 01, clase 10) descarta los que no correlacionan con su escala, los que
correlacionan con la escala equivocada y los que casi nadie responde.

Descartar es parte del método, no una señal de fracaso. Lo que sí es un fracaso
es no tener de dónde descartar.

## Laboratorio

`lab.py` audita los cinco instrumentos del catálogo contra los defectos de
redacción detectables automáticamente: longitud excesiva, conjunciones
sospechosas de doble cañón y negaciones acumuladas. No sustituye al juicio de un
experto, pero encuentra los casos evidentes.

```bash
python classes/part-00-fundamentos-de-la-medicion/002-del-constructo-al-item/lab.py
```

## Para pensar

1. Toma la definición de Apertura a la experiencia del catálogo y propón una
   faceta que el IPIP-NEO-120 no cubra. ¿Es deficiencia o está fuera del
   constructo?
2. El ítem `"Suelo votar por candidatos políticos progresistas"` mide Liberalismo
   en el IPIP. ¿Qué problema tiene fuera de Estados Unidos?
3. ¿Por qué "¿es usted honesto?" mide algo distinto de la honestidad?

## Bibliografía

- DeVellis, R. F. (2016). *Scale Development: Theory and Applications* (4.ª ed.).
  Sage. Caps. 4-5.
- Clark, L. A., & Watson, D. (1995). Constructing validity. *Psychological
  Assessment*, 7(3), 309-319.
