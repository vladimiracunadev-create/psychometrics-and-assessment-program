# 010 — Pilotaje y análisis de ítems

> [Clase anterior](../009-longitud-y-costo-de-medida/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../../part-02-fiabilidad/011-teoria-clasica-del-error/README.md)

**Parte:** 01 — Construcción de instrumentos
**Nivel:** fundamentos · **Horas estimadas:** 4 · **Estado:** `escrita`
**Prerrequisitos:** clases 004, 006 y 009.

## Propósito

Antes de usar un instrumento se prueba con una muestra pequeña. Esta clase enseña
el análisis clásico de ítems —dificultad y discriminación— y cómo decidir qué
ítems se revisan, se reescriben o se descartan.

## Resultados de aprendizaje

1. Calcular dificultad (proporción de aciertos) y discriminación (correlación ítem-resto).
2. Explicar por qué se excluye el propio ítem del total.
3. Detectar ítems defectuosos y justificar la decisión sin descartar a ciegas.
4. Diseñar un piloto y declarar sus límites.

## Fundamentos

**Dificultad (p).** En ítems dicotómicos, proporción que acierta o asiente. Valores
cercanos a 0 o 1 aportan poca información: casi todos responden igual. En
rendimiento máximo suele buscarse un rango intermedio; en cribado puede
convenir p extrema a propósito.

**Discriminación (r ítem-resto).** Correlación entre el ítem y el total **sin ese
ítem**. Si se deja el ítem dentro, se correlaciona consigo mismo y la cifra se
infla, sobre todo en escalas cortas. Una regla de lectura habitual es revisar r < 0,20.

### Qué pasa en el laboratorio

Se simulan 300 personas y 12 ítems, con dos defectos sembrados:

| Ítem | p | r | Resultado |
|---:|---:|---:|---|
| 1–10 | 0,25–0,70 | 0,30–0,53 | ok |
| 11 | 0,95 | 0,27 | marcado: p extrema (demasiado fácil) |
| 12 | 0,50 | 0,06 | marcado: discrimina poco (azar) |

El análisis encuentra los dos ítems defectuosos sin marcar ninguno de los sanos.

### Decidir con criterio

Un indicador marcado es una **alerta, no un veredicto**. Un ítem con r baja puede
medir otra faceta legítima; uno muy fácil puede ser necesario por cobertura del
contenido (clase 017). Se revisa su redacción (clase 006), su clave y su aporte
a la tabla de especificaciones antes de eliminarlo.

### Diseño del piloto

- Tamaño: lo bastante grande para que los índices no oscilen; una muestra de 300 es una referencia didáctica, no una norma universal.
- Población: similar a la destinataria, o el análisis no se transfiere.
- Registro: tiempos, omisiones y comentarios de las personas.
- Datos personales: sin identificadores; consentimiento (parte 07).

## Errores frecuentes

- Correlacionar el ítem con el total que lo incluye.
- Eliminar ítems por un solo índice.
- Pilotar con estudiantes cercanos al autor y generalizar a toda la población.
- Reportar un piloto como validación.

## Limitaciones

Los índices clásicos dependen de la muestra. Con ítems politómicos o rasgos
multidimensionales hay que adaptarlos (partes 04 y 05). Un piloto no establece validez.

## Ejercicios

- **Inicial.** Un ítem lo acierta el 98 %. ¿Qué información aporta?
- **Intermedio.** ¿Por qué r ítem-resto es menor que r ítem-total?
- **Avanzado.** Añade a `lab.py` un ítem con correlación negativa (clave mal puesta) y explica cómo lo detectas.

*Solución intermedio:* el total incluye al ítem, y esa parte siempre correlaciona consigo misma.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/010-pilotaje-y-analisis-de-items/lab.py
```

## Autoevaluación

1. ¿Qué dos indicadores usarías primero y por qué?
2. ¿Cuándo conservarías un ítem con r < 0,20?
3. ¿Qué no puedes concluir de un piloto?

## Criterios de evaluación

El estudiante calcula los índices, detecta defectos sembrados y redacta una decisión por ítem con justificación.

## Bibliografía

- Crocker, L., & Algina, J. (1986). *Introduction to Classical and Modern Test Theory*. Holt, Rinehart & Winston. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Nunnally, J. C., & Bernstein, I. H. (1994). *Psychometric Theory* (3.ª ed.). McGraw-Hill. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
