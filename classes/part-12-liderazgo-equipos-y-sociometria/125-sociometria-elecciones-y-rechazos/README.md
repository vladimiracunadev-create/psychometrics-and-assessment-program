# 125 — Sociometría: elecciones y rechazos

![Portada de la clase 125](portada.svg)

<!-- NAV -->
[← 124 — Comportamiento en equipos de trabajo](../124-comportamiento-en-equipos-de-trabajo/README.md) · [📚 Parte 12](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [126 — Análisis de redes sociométricas →](../126-analisis-de-redes-sociometricas/README.md)
<!-- /NAV -->

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 061 y 066.

> **Ética.** La sociometría con niños, niñas y adolescentes exige consentimiento informado y asentimiento, confidencialidad estricta, no mostrar al grupo quién rechaza o es rechazado y un propósito de apoyo a la convivencia con profesionales. Este laboratorio usa un curso **ficticio** y solo enseña el cálculo.

## Objetivos

1. Calcular preferencia social e impacto social.
2. Clasificar el estatus sociométrico con la convención de Coie et al. (1982).
3. Interpretar el estatus como relativo y cambiante.

## Fundamentos

Moreno (1934) introdujo la sociometría: cada persona nomina a quienes elegiría (y, a veces, rechazaría) en una actividad. Se cuentan las nominaciones recibidas (LM, «me gusta más»; LL, «me gusta menos»), se estandarizan en el grupo y se calculan **preferencia social** SP = zLM − zLL e **impacto social** SI = zLM + zLL. Clasificación habitual (Coie, Dodge y Coppotelli, 1982; Cillessen, 2009): *popular* (SP alto, LM alto, LL bajo), *rechazado* (SP bajo, LL alto, LM bajo), *ignorado* (SI bajo, LM y LL bajos), *controvertido* (SI alto, LM y LL altos) y *promedio*. Los umbrales son convenciones.

Laboratorio (curso ficticio de 30; 3 elecciones positivas y 3 negativas):

| Estatus | Estudiantes |
|---|---:|
| Promedio | 20 |
| Popular | 3 |
| Rechazado | 3 |
| Ignorado | 4 |

Ejemplos: estudiante 14 (LM 19, LL 0, SP 3,05) → popular; estudiante 25 (LM 0, LL 17, SP −2,80) → rechazado.

## Ejemplo resuelto

zLM = 1,2 y zLL = −0,5: SP = 1,7 (alto) y SI = 0,7; con LM > 0 y LL < 0 → popular.

## Errores y límites

- Etiquetar a un niño o niña con un estatus.
- Usar la sociometría sin protocolo de apoyo posterior.
- Olvidar que los resultados dependen del grupo y la ola de medición (clase 127).
- Reducir la convivencia a un puntaje.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre preferencia e impacto social?
- **Intermedio.** zLM = −0,4 y zLL = 1,1: SP = −1,5 → candidato a «rechazado» si LL > 0 y LM < 0.
- **Avanzado.** Cambia el número de elecciones a 5 en `lab.py` y observa la distribución.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/125-sociometria-elecciones-y-rechazos/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo explicas la actividad a los estudiantes? 2. ¿Quién ve los resultados y cómo se resguardan? 3. ¿Qué haces ante un patrón de rechazo?
Se logra si el estudiante calcula el estatus y propone un protocolo ético de uso.

## Bibliografía

- Moreno, J. L. (1934). *Who Shall Survive?* Nervous and Mental Disease Publishing. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Coie, J. D., Dodge, K. A., & Coppotelli, H. (1982). Dimensions and types of social status: A cross-age perspective. *Developmental Psychology*, 18(4), 557-570. ✅ [DOI](https://doi.org/10.1037/0012-1649.18.4.557)
- Cillessen, A. H. N. (2009). Sociometric methods. En K. H. Rubin, W. M. Bukowski, & B. Laursen (Eds.), *Handbook of Peer Interactions, Relationships, and Groups*. Guilford. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 124 — Comportamiento en equipos de trabajo](../124-comportamiento-en-equipos-de-trabajo/README.md)  
[📚 Parte 12](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[126 — Análisis de redes sociométricas →](../126-analisis-de-redes-sociometricas/README.md)
<!-- /NAV -->
