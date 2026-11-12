# 055 — Testing adaptativo informatizado

![Portada de la clase 055](portada.svg)

<!-- NAV -->
[← 054 — Función de información: dónde mide bien cada…](../054-informacion-del-item/README.md) · [📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [056 — Estimación de parámetros y de habilidad →](../056-estimacion-de-parametros-y-de-habilidad/README.md)
<!-- /NAV -->

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 053 y 054.

## Objetivos

1. Describir el ciclo de un CAT: estimar, seleccionar, administrar, detener.
2. Comparar un CAT con un test fijo en precisión y longitud.
3. Identificar los costos y riesgos del CAT.

## Fundamentos

Un CAT (Weiss, 1982; Wainer et al., 2000) elige cada ítem para dar la máxima información en la estimación actual de θ, y termina al alcanzar una precisión (o un largo máximo). Requiere un banco calibrado y reglas de selección, estimación y parada (van der Linden y Glas, 2010).

Laboratorio (banco de 300 ítems 2PL; 300 examinados; EAP con prior normal; parada con EE < 0,30 o 30 ítems):

| Test | Ítems (media) | RMSE de θ |
|---|---:|---:|
| CAT | 14,7 | 0,295 |
| Fijo de 20 ítems al azar | 20,0 | 0,438 |

El CAT alcanza mayor precisión con menos ítems. Los parámetros del banco se conocen (caso ideal).

## Ejemplo resuelto

Con θ̂ = 0,8 el CAT elige el ítem no usado con mayor a²P(1−P) en θ = 0,8, normalmente uno con b cerca de 0,8 y a alto.

## Errores y límites

- Creer que el CAT es «más justo» por defecto: cada persona ve un test distinto; hay que controlar exposición (clase 060), cobertura de contenido y equidad.
- No poder revisar o saltar ítems (en CAT clásico) afecta a la experiencia y a los grupos con ansiedad ante la prueba.
- Banco mal calibrado = estimaciones sesgadas.
- No hay CAT sin infraestructura digital, seguridad y accesibilidad (parte 18).

## Ejercicios

- **Inicial.** ¿Por qué el CAT puede ser más corto?
- **Intermedio.** ¿Qué EE exige una parada con I ≥ 16? → 0,25.
- **Avanzado.** Cambia la regla de parada a EE < 0,20 y compara ítems y RMSE.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/055-testing-adaptativo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué componentes tiene un CAT? 2. ¿Qué riesgos de seguridad aparecen? 3. ¿Cuándo no usarías CAT?
Se logra si el estudiante implementa o simula el ciclo y compara con un test fijo.

## Bibliografía

- Weiss, D. J. (1982). Improving measurement quality and efficiency with adaptive testing. *Applied Psychological Measurement*, 6(4), 473-492. ✅ [DOI](https://doi.org/10.1177/014662168200600408)
- Wainer, H., et al. (2000). *Computerized Adaptive Testing: A Primer* (2.ª ed.). Lawrence Erlbaum. ✅ [DOI](https://doi.org/10.4324/9781410605931)
- van der Linden, W. J., & Glas, C. A. W. (2010). *Elements of Adaptive Testing*. Springer. ✅ [DOI](https://doi.org/10.1007/978-0-387-85461-8)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 054 — Función de información: dónde mide bien cada…](../054-informacion-del-item/README.md)  
[📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[056 — Estimación de parámetros y de habilidad →](../056-estimacion-de-parametros-y-de-habilidad/README.md)
<!-- /NAV -->
