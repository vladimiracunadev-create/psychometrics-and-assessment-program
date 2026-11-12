# 036 — Los Standards de AERA, APA y NCME

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clases 016 a 020.

## Objetivos

1. Describir la estructura y el espíritu de los *Standards*.
2. Distinguir responsabilidades del desarrollador, del usuario y de quien comunica resultados.
3. Auditar la documentación de un instrumento con una lista de verificación propia.

## Fundamentos

Los *Standards for Educational and Psychological Testing* (AERA, APA y NCME, 2014) son el marco de referencia profesional sobre validez, fiabilidad, equidad, desarrollo, administración, informes y uso. No son una ley: son criterios de buena práctica que se citan en la evaluación de instrumentos y en la defensa de decisiones. Sus principios transversales: la validez es de **interpretaciones y usos**, la documentación es una obligación del desarrollador y la responsabilidad del uso concreto recae en quien lo decide.

Laboratorio: lista de verificación propia (autores, año, fuente, licencia, cita, tipo de respuesta, duración y declaración de estado de validación) aplicada a los cinco instrumentos del repositorio:

| Instrumento | Criterios cumplidos |
|---|---:|
| disc-abierto, ipip-via-r, onet-riasec-sf, valores-spranger | 8 / 8 |
| ipip-neo-120 | 7 / 8 (no declara su estado de validación en el archivo) |

Hallazgo real de la auditoría: el YAML de `ipip-neo-120` no dice que carece de estudio de validación propio; sí lo dice la ficha del catálogo. Es una mejora pendiente.

## Ejemplo resuelto

Un cuestionario de «liderazgo» sin manual: no declara población, normas ni evidencia. Según los *Standards*, el usuario no debería basar decisiones en él hasta contar con esa información.

## Errores y límites

- Citar los *Standards* como si «certificaran» un test.
- Creer que la lista del laboratorio mide calidad psicométrica: mide si el instrumento declara lo necesario.
- Aplicar criterios de un contexto (educación) a otro (clínico) sin adaptarlos.

## Ejercicios

- **Inicial.** ¿Quién es responsable del uso concreto de un test?
- **Intermedio.** Agrega a `revisa()` un criterio de «población objetivo declarada» y aplica la lista.
- **Avanzado.** Corrige la documentación de `ipip-neo-120` sin cambiar sus ítems y verifica con la lista.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/036-estandares-aera-apa-ncme/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diferencia hay entre estándar y ley? 2. ¿Qué evidencia mínima exigirías? 3. ¿Cómo comunicas una limitación?
Se logra si el estudiante audita documentación y distingue lo declarado de lo demostrado.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. American Educational Research Association. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- American Psychological Association (2017). *Ethical Principles of Psychologists and Code of Conduct*. APA. ⚠️ existe, pero Crossref registra 2002 (¿otra edición?; [DOI](https://doi.org/10.1037/e300672004-001))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
