# 076 — Ley 19.628 y Ley 21.719: datos personales en evaluación

![Portada de la clase 076](portada.svg)

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clases 071 y 073.

> **Aviso.** Esta clase es material educativo, **no asesoría jurídica**. La normativa cambia: antes de aplicar nada, consulte el texto vigente en la Biblioteca del Congreso Nacional (bcn.cl) y a un profesional del derecho.

## Objetivos

1. Ubicar el marco chileno de protección de datos personales y su estado de vigencia.
2. Inventariar los datos de una evaluación y justificar cada uno por su finalidad.
3. Distinguir identificadores, cuasi-identificadores y datos sensibles.

## Fundamentos

- **Ley 19.628** (1999): sobre protección de la vida privada; régimen que rigió el tratamiento de datos personales en Chile.
- **Ley 21.719**: publicada el 13 de diciembre de 2024; modifica íntegramente el régimen de la 19.628 y crea la Agencia de Protección de Datos Personales.
- **Estado de vigencia verificado el 12 de noviembre de 2026** (en fuentes secundarias: estudios jurídicos y prensa especializada): la fecha de entrada en vigencia establecida por la ley es el **1 de diciembre de 2026**; existe un proyecto de ley (Boletín 18.623-07) que la posterga, aprobado en primer trámite por el Senado el 28 de octubre de 2026 con nueva fecha propuesta de 15 de octubre de 2027, **aún no publicado como ley**. Verifique el estado actual de la tramitación antes de tomar decisiones.
- Ideas generales de los regímenes modernos de datos personales (a confirmar en el texto legal): licitud, finalidad, proporcionalidad, calidad, seguridad, transparencia, derechos del titular (acceso, rectificación, supresión, oposición, portabilidad) y protección reforzada de datos sensibles.

Laboratorio: inventario de una evaluación con 9 campos; 4 de 9 no tienen finalidad declarada (comuna, diagnóstico previo, pertenencia étnica, IP de origen) y se marcan para eliminar (minimización); los identificadores directos se separan del resultado (seudonimización).

## Ejemplo resuelto

Para elegir el baremo por edad basta con la fecha de nacimiento (o la edad). El diagnóstico previo, sin finalidad, no se recolecta: reduce riesgo y deber de custodia.

## Errores y límites

- Recolectar «por si sirve más adelante».
- Creer que seudonimizar equivale a anonimizar (clase 078).
- Tratar los textos del laboratorio como interpretación jurídica.
- No todo dato de evaluación es sensible; sí lo pueden ser salud, origen étnico u otros de las categorías legales.

## Ejercicios

- **Inicial.** ¿Qué es un cuasi-identificador?
- **Intermedio.** Agrega los campos «curso» y «establecimiento» al inventario y decide su finalidad.
- **Avanzado.** Redacta una política de retención para el inventario (qué se guarda, cuánto y quién accede).

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/076-ley-19-628-y-ley-21-719/lab.py
```

## Autoevaluación y criterios

1. ¿Qué principio justifica eliminar un campo sin finalidad? 2. ¿Qué cambia con la nueva ley respecto de la 19.628 (verificar en el texto)? 3. ¿Qué datos tuyos evaluarías con protección reforzada?
Se logra si el estudiante inventaría datos y justifica minimización con base en finalidad.

## Bibliografía y fuentes

- Biblioteca del Congreso Nacional de Chile (bcn.cl). Ley 19.628 sobre protección de la vida privada y Ley 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (texto vigente: verificar). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Academia Judicial de Chile. *Ley 21.719* (actualización normativa). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing* (privacidad y confidencialidad). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
