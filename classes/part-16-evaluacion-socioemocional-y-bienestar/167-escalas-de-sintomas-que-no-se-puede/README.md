# 167 — Escalas de síntomas: qué no se puede hacer sin un profesional

![Portada de la clase 167](portada.svg)

<!-- NAV -->
[← 166 — Satisfacción académica y laboral](../166-satisfaccion-academica-y-laboral/README.md) · [📚 Parte 16](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [168 — Protocolo de derivación y de riesgo →](../168-protocolo-de-derivacion-y-de-riesgo/README.md)
<!-- /NAV -->

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 100 y 135.

> **Seguridad.** Esta clase no es un protocolo clínico ni sustituye la formación profesional. Si alguien expresa riesgo para sí o para otros, se activa el protocolo de la institución y se contacta a un profesional o a los servicios de emergencia. Los canales de ayuda vigentes en Chile se verifican en las fuentes oficiales del Ministerio de Salud.

## Objetivos

1. Calcular el valor predictivo de un cribado de síntomas según la prevalencia.
2. Diseñar una regla de seguridad independiente del puntaje total y probarla.
3. Delimitar qué puede hacer cada rol (docente, orientador, psicólogo, equipo de salud).

## Fundamentos

Las escalas de síntomas (por ejemplo, el PHQ-9; Kroenke, Spitzer y Williams, 2001) son instrumentos de **cribado y seguimiento**, no de diagnóstico. Con prevalencia baja la mayoría de los positivos son falsos positivos (clase 100). Los ítems de **seguridad** se tratan de forma separada: cualquier respuesta de riesgo dispara contacto humano, sin importar el total.

Laboratorio (escala sintética de 9 ítems; corte ≥ 10):

| Prevalencia | Positivos | VPP |
|---:|---:|---:|
| 2 % | 2 890 | 0,17 |
| 5 % | 3 495 | 0,34 |
| 10 % | 4 667 | 0,54 |
| 20 % | 6 780 | 0,72 |

Respuestas con ítem de riesgo > 0 sin alerta de seguridad, en 100 000 protocolos: **0** (propiedad probada).

## Ejemplo resuelto

Total = 4 (por debajo del corte) pero ítem de riesgo = 1: no hay «positivo de cribado», pero sí alerta de seguridad: se activa el contacto humano.

## Errores y límites

- Interpretar un puntaje como diagnóstico o reportarlo a terceros sin necesidad.
- Aplicar escalas de síntomas sin un protocolo de respuesta definido de antemano.
- Promediar el ítem de riesgo con los demás.
- Escala y datos sintéticos: no se usa para decidir sobre personas.

## Ejercicios

- **Inicial.** ¿Qué significa «positivo» en un cribado?
- **Intermedio.** VPP con S = 0,85, E = 0,90, p = 0,05 → 0,31.
- **Avanzado.** Añade una prueba automática que falle si el ítem de riesgo se omite sin alerta.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/167-escalas-de-sintomas-que-no-se-puede/lab.py
```

## Autoevaluación y criterios

1. ¿Quién puede aplicar e interpretar estas escalas en tu contexto? 2. ¿Qué haces ante una respuesta de riesgo? 3. ¿Qué datos se guardan y quién accede?
Se logra si el estudiante calcula el VPP y diseña una regla de seguridad verificada por pruebas.

## Bibliografía y fuentes

- Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001). The PHQ-9: Validity of a brief depression severity measure. *Journal of General Internal Medicine*, 16(9), 606-613. ✅ [DOI](https://doi.org/10.1097/00006842-200203000-00008)
- Streiner, D. L., & Norman, G. R. (2008). *Health Measurement Scales* (4.ª ed.). Oxford University Press. ✅ [DOI](https://doi.org/10.1093/acprof:oso/9780199231881.001.0001)
- Ministerio de Salud de Chile: orientaciones de prevención del suicidio y canales de ayuda (versión vigente: verificar en minsal.cl). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 166 — Satisfacción académica y laboral](../166-satisfaccion-academica-y-laboral/README.md)  
[📚 Parte 16](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[168 — Protocolo de derivación y de riesgo →](../168-protocolo-de-derivacion-y-de-riesgo/README.md)
<!-- /NAV -->
