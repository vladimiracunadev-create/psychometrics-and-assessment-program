# 188 — Seguridad y privacidad por diseño

> [Índice de la parte](../README.md)

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 187.

## Objetivos

1. Seudonimizar con HMAC en lugar de un hash simple.
2. Aplicar retención por categoría.
3. Reconocer que esto no es asesoría jurídica.

## Fundamentos

Un hash simple de un identificador acotado puede revertirse probando todos los candidatos; un HMAC con clave secreta guardada aparte lo impide (Krawczyk et al., 1997, RFC 2104). La privacidad por diseño integra minimización, seudonimización y plazos de retención desde el origen; los plazos concretos dependen de la finalidad y de la normativa vigente (Ley 19.628 y Ley 21.719), que debe verificarse en la fuente oficial. Este material no es asesoría jurídica.

Laboratorio (1.000 identificadores ficticios): el hash simple se revierte; el HMAC sin clave no; es estable con la misma clave y distinto con otra; de 5 registros se conservan 3 y se eliminan 2 según el plazo.

## Ejemplo resuelto

Se guardan los resultados con el seudónimo HMAC y la clave en un gestor aparte; la telemetría detallada no se conserva.

## Errores y límites

- Guardar la clave junto con los datos.
- Olvidar copias de seguridad al eliminar.
- La clave del laboratorio es de demostración.

## Ejercicios

- **Inicial.** ¿Por qué un HMAC es mejor que un hash simple?
- **Intermedio.** Propón un procedimiento de rotación de clave.
- **Avanzado.** Redacta una política de retención para tres categorías de datos.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/188-seguridad-y-privacidad-por-diseno/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- Krawczyk, H., Bellare, M., & Canetti, R. (1997). *HMAC: Keyed-Hashing for Message Authentication*. RFC 2104. ✅ [DOI](https://doi.org/10.17487/rfc2104)
- Ley 19.628 y Ley 21.719 (Chile): verificar en bcn.cl. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
