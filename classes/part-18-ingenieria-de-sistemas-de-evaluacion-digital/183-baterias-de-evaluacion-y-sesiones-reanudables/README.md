# 183 — Baterías de evaluación y sesiones reanudables

![Portada de la clase 183](portada.svg)

<!-- NAV -->
[← 182 — Modelos de ítems y esquemas versionados](../182-modelos-de-items-y-esquemas-versionados/README.md) · [📚 Parte 18](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [184 — Telemetría de interacción y tiempos de respue… →](../184-telemetria-de-interaccion-y-tiempos-de-respuesta/README.md)
<!-- /NAV -->

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 182.

## Objetivos

1. Agrupar instrumentos en una batería.
2. Pausar y reanudar una sesión sin perder datos.
3. Detectar alteraciones del estado guardado.

## Fundamentos

Una batería es una lista de instrumentos aplicados a la misma persona. Guardar solo las respuestas y recalcular al consultar evita puntajes obsoletos. Una huella SHA-256 del estado detecta cambios accidentales o manipulación, pero no controla el acceso.

Laboratorio con el módulo `psychometrics.baterias`: 68 respuestas (36 de valores y 32 de DISC), pausa a las 60, JSON de unos 6,8 kB, reanudación con resultado idéntico al de la sesión continua, alteración detectada, 68 eventos en bitácora sin datos personales ni reloj.

## Ejemplo resuelto

Una persona deja el DISC a medias: la sesión guarda 24 de 32 respuestas, devuelve `('disc-abierto','c01')` como siguiente ítem y, al completar, entrega el mismo resultado que si no hubiera pausado.

## Errores y límites

- Guardar puntajes derivados en vez de respuestas.
- Creer que la huella protege la confidencialidad.
- Los datos del laboratorio son sintéticos.

## Ejercicios

- **Inicial.** ¿Por qué se guardan respuestas y no puntajes?
- **Intermedio.** Añade una tercera pausa y verifica la igualdad.
- **Avanzado.** Propón cómo cifrarías el JSON de sesión y dónde guardarías la clave.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/183-baterias-de-evaluacion-y-sesiones-reanudables/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Ley 19.628 y Ley 21.719 (Chile), sobre protección de datos: verificar el texto vigente en la fuente oficial. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 182 — Modelos de ítems y esquemas versionados](../182-modelos-de-items-y-esquemas-versionados/README.md)  
[📚 Parte 18](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[184 — Telemetría de interacción y tiempos de respue… →](../184-telemetria-de-interaccion-y-tiempos-de-respuesta/README.md)
<!-- /NAV -->
