# 123 — Roles en equipos: modelo Belbin y su evidencia

![Portada de la clase 123](portada.svg)

<!-- NAV -->
[← 122 — Evaluación de la efectividad del liderazgo](../122-evaluacion-de-la-efectividad-del-liderazgo/README.md) · [📚 Parte 12](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [124 — Comportamiento en equipos de trabajo →](../124-comportamiento-en-equipos-de-trabajo/README.md)
<!-- /NAV -->

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 040 y 068.

## Objetivos

1. Describir el modelo de roles de equipo y su estado de evidencia.
2. Calcular la tasa de falsos positivos por comparaciones múltiples.
3. Aplicar la corrección de Bonferroni.

## Fundamentos

El modelo de nueve roles de equipo de Belbin (1981) es propietario y muy usado. Las revisiones psicométricas del inventario de autopercepción cuestionan su estructura y fiabilidad (Furnham, Steele y Pendleton, 1993), aunque hay trabajos que buscan sustento (Aritzeta, Swailes y Senior, 2007). Aquí solo se usa la estructura «nueve roles» como pretexto estadístico: **al probar muchos roles, algo sale «significativo» por azar** (Simmons, Nelson y Simonsohn, 2011).

Laboratorio (sin ningún efecto real; 40 equipos; 2 000 estudios simulados; prueba z aproximada):

| Medida | Valor |
|---|---:|
| Estudios con ≥ 1 rol «significativo» (p < 0,05) | 43,3 % (teórico 1 − 0,95⁹ = 37,0 %) |
| Con corrección de Bonferroni (p < 0,05/9) | 8,6 % |

El exceso sobre el 37 % teórico viene de la aproximación normal con muestras chicas; con Bonferroni la tasa baja pero no llega a 5 % por la misma razón.

## Ejemplo resuelto

Con 9 comparaciones independientes al 5 %, P(al menos una significativa) = 1 − 0,95⁹ = 0,37.

## Errores y límites

- Decidir sobre personas por su «rol Belbin».
- Concluir que un equipo «equilibrado» rinde más a partir de un solo estudio.
- Bonferroni es conservador; hay alternativas (Holm, control de la tasa de descubrimientos falsos).
- Se trata de una simulación estadística, no de una evaluación empírica del modelo.

## Ejercicios

- **Inicial.** ¿Por qué aparecen hallazgos por azar?
- **Intermedio.** Con 20 comparaciones: 1 − 0,95²⁰ = 0,64.
- **Avanzado.** Aumenta a 200 equipos en `lab.py` y observa la tasa sin corrección.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/123-roles-en-equipos-modelo-belbin-y-su/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es preinscribir hipótesis? 2. ¿Cómo evaluarías el modelo de roles con rigor? 3. ¿Qué alternativa abierta usarías para enseñar roles?
Se logra si el estudiante cuantifica y corrige los falsos positivos y desaconseja el uso en decisiones.

## Bibliografía

- Belbin, R. M. (1981). *Management Teams: Why They Succeed or Fail*. Heinemann. ✅ [DOI](https://doi.org/10.2307/2581652)
- Furnham, A., Steele, H., & Pendleton, D. (1993). A psychometric assessment of the Belbin Team-Role Self-Perception Inventory. *Journal of Occupational and Organizational Psychology*, 66(3), 245-257. ✅ [DOI](https://doi.org/10.1111/j.2044-8325.1993.tb00535.x)
- Aritzeta, A., Swailes, S., & Senior, B. (2007). Belbin's team role model: Development, validity and applications for team building. *Journal of Management Studies*, 44(1), 96-118. ✅ [DOI](https://doi.org/10.1111/j.1467-6486.2007.00666.x)
- Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology. *Psychological Science*, 22(11), 1359-1366. ✅ [DOI](https://doi.org/10.1177/0956797611417632)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 122 — Evaluación de la efectividad del liderazgo](../122-evaluacion-de-la-efectividad-del-liderazgo/README.md)  
[📚 Parte 12](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[124 — Comportamiento en equipos de trabajo →](../124-comportamiento-en-equipos-de-trabajo/README.md)
<!-- /NAV -->
