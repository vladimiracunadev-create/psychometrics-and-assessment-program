# Guía de conceptos: qué es cada cosa

Si algo de este repositorio te resulta confuso, empieza aquí. Está escrita para cualquier persona, sin conocimientos previos.

## 1. Las palabras de la evaluación

Piensa en un **cuestionario de personalidad** que alguien contesta en una pantalla:

```
INSTRUMENTO  (el cuestionario completo, por ejemplo «IPIP-NEO-120»)
 ├── ESCALA «Responsabilidad»   ← lo que se quiere medir (un rasgo)
 │     ├── ÍTEM  «Termino lo que empiezo»                → respuesta: 1, 2, 3, 4 o 5
 │     ├── ÍTEM  «Dejo mis cosas desordenadas»  (invertido) → respuesta: 1, 2, 3, 4 o 5
 │     └── …
 ├── ESCALA «Amabilidad»
 │     └── …
 └── PUNTAJE: con las respuestas se calcula un número por escala
```

| Palabra | Qué es, en simple | Ejemplo |
|---|---|---|
| **Instrumento** (o test, o cuestionario) | El conjunto completo de preguntas más las reglas para puntuarlas. | IPIP-NEO-120 (120 preguntas) |
| **Ítem** | Una sola pregunta o afirmación del instrumento. | «Hago amigos con facilidad.» |
| **Escala** | Un grupo de ítems que apuntan al mismo rasgo; de ahí sale un puntaje. | «Extraversión» |
| **Constructo** | La idea abstracta que se quiere medir; no se ve directamente. | «Responsabilidad» |
| **Respuesta** | Lo que marca la persona (por ejemplo, de 1 a 5). | 4 |
| **Puntaje** | Número que resume las respuestas de una escala. | media 3,8 |
| **Baremo (o norma)** | Tabla que dice si un puntaje es alto o bajo comparado con un grupo. | «percentil 70» |
| **Evaluado** | La persona que contesta el instrumento. | tú, un estudiante, un postulante |

## 2. Dos palabras que se confunden: «dominio»

- **Dominio de un constructo** (clase 002): el conjunto de contenidos que un rasgo abarca. Ejemplo: el dominio de «responsabilidad» incluye orden, perseverancia y autocontrol.
- **Dominio público** (licencia): significa que **nadie es dueño de los derechos** de esas preguntas y cualquiera puede usarlas, copiarlas y modificarlas sin pedir permiso. No tiene nada que ver con el constructo.

Cuando el README dice «216 ítems de dominio público», se refiere a lo segundo: son preguntas que se pueden usar libremente.

## 3. Licencias: por qué importan

Un instrumento puede tener distintos estados legales:

| Estado | Significa | Ejemplo en el repositorio |
|---|---|---|
| **Dominio público** | Se usa libre y gratis. | IPIP-NEO-120, IPIP-VIA-R |
| **Autoría propia** | Lo escribió este proyecto; se publica bajo licencia MIT. | DISC Abierto, Valores de Spranger |
| **Licencia específica** | Se puede usar con condiciones de quien lo publicó. | O*NET Interest Profiler (forma breve) |
| **Propietaria** | Tiene dueño comercial; **no se copian sus preguntas**. | Tests comerciales: solo se describen en una ficha |

Que algo sea de «dominio público» **no** significa que esté validado ni que sirva para decidir sobre personas: son dos asuntos distintos (ver el punto siguiente).

## 4. «Validado» no es lo mismo que «disponible»

- **Disponible legalmente:** se puede usar sin problema legal.
- **Validado:** existen estudios que muestran que el instrumento mide lo que dice, en una población y para un fin concretos.

Este repositorio tiene instrumentos disponibles que **no están validados**, y lo declara en cada uno. Por eso no deben usarse para decidir sobre personas.

## 5. Las piezas del repositorio

| Pieza | Qué es | Dónde está |
|---|---|---|
| **Programa** | Las 200 clases para aprender el tema. | `classes/` |
| **Clase** | Una lección con explicación, ejemplos, laboratorio y fuentes. | `classes/part-XX/NNN-…/README.md` |
| **Laboratorio** (`lab.py`) | Un programa corto que simula datos para ver una idea con números. Los datos son inventados (sintéticos). | dentro de cada clase |
| **Instrumentos ejecutables** | Los 5 cuestionarios que el programa sí puede mostrar y puntuar. Cada uno es un archivo de datos. | `instruments/` |
| **Catálogo** | La lista de instrumentos que el proyecto conoce. Tiene dos niveles: los 5 ejecutables y las **fichas**. | `instruments/` y `catalogo/fichas.yaml` |
| **Ficha** | Una descripción informativa de un instrumento o técnica (qué es, para qué se usa, qué estado tiene). **No contiene las preguntas** ni sirve para aplicarlo. | `catalogo/fichas.yaml` (140) |
| **Motor** | El código que carga un instrumento, calcula los puntajes y genera el informe. | `src/psychometrics/` |
| **Estado verificable** | La tabla del README que dice, con cifras reales, qué está hecho y qué no. | `README.md` |

## 6. Cómo leer los símbolos del estado

- ✅ hecho y comprobado por una prueba automática o por el validador.
- 🟡 hecho en parte, o hecho pero falta algo (se dice qué).
- ⚠️ existe, pero con una condición o un riesgo que debes conocer.
- ⚪ no existe todavía.
- 🔎 fuente bibliográfica que aún no se ha podido comprobar.

## 7. Qué hacer a continuación

1. Lee la [guía de la parte 00](../classes/part-00-fundamentos-de-la-medicion/README.md).
2. Empieza por la [clase 001](../classes/part-00-fundamentos-de-la-medicion/001-que-significa-medir-lo-que-no-se-ve/README.md).
3. Si quieres ver un instrumento real, ejecuta `psychometrics catalogo` (instrucciones en el [README](../README.md#-empezar)).
