# 186 — Accesibilidad de evaluaciones digitales

![Portada de la clase 186](portada.svg)

<!-- NAV -->
[← 185 — Evaluación adaptativa: implementación](../185-evaluacion-adaptativa-implementacion/README.md) · [📚 Parte 18](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [187 — Auditoría de cálculo y trazabilidad →](../187-auditoria-de-calculo-y-trazabilidad/README.md)
<!-- /NAV -->

**Parte 18 — Ingeniería de sistemas de evaluación digital** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 185.

## Objetivos

1. Calcular la relación de contraste WCAG.
2. Distinguir lo verificable automáticamente de lo que exige usuarios.
3. Relacionar accesibilidad con validez.

## Fundamentos

Las pautas WCAG 2.x (W3C) fijan relaciones de contraste mínimas: 4,5:1 para texto normal y 3:1 para texto grande y componentes de interfaz (nivel AA). Una barrera de acceso introduce varianza irrelevante al constructo (AERA et al., 2014).

Laboratorio: negro sobre blanco = 21:1 (verificado); texto principal 17,40:1; gris #767676 4,54:1 (cumple por poco); gris #aaaaaa 2,32:1 y botón deshabilitado 2,19:1 no cumplen.

## Ejemplo resuelto

Un gris #aaaaaa sobre blanco parece legible para quien tiene visión típica, pero con 2,32:1 no cumple AA; se oscurece hasta superar 4,5:1.

## Errores y límites

- Creer que el contraste agota la accesibilidad.
- No probar con lectores de pantalla, teclado y tiempos ajustables.
- Excluir ajustes razonables por «estandarización».

## Ejercicios

- **Inicial.** ¿Cuál es el contraste mínimo AA para texto normal?
- **Intermedio.** Busca un gris que quede justo sobre 4,5:1.
- **Avanzado.** Elabora una lista de verificación de accesibilidad para una evaluación en línea.

## Laboratorio

```bash
python classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/186-accesibilidad-de-evaluaciones-digitales/lab.py
```

## Autoevaluación y criterios

1. ¿Qué parte del diseño podría fallar sin que nadie lo note? 2. ¿Qué evidencia guardarías? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante implementa la idea, la prueba con datos sintéticos y declara sus límites.

## Bibliografía

- W3C. *Web Content Accessibility Guidelines (WCAG) 2.x*. w3.org/TR/WCAG2. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 185 — Evaluación adaptativa: implementación](../185-evaluacion-adaptativa-implementacion/README.md)  
[📚 Parte 18](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[187 — Auditoría de cálculo y trazabilidad →](../187-auditoria-de-calculo-y-trazabilidad/README.md)
<!-- /NAV -->
