# 056 — Estimación de parámetros y de habilidad

![Portada de la clase 056](portada.svg)

<!-- NAV -->
[← 055 — Testing adaptativo informatizado](../055-testing-adaptativo/README.md) · [📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [057 — Curvas características e información del test →](../057-curvas-caracteristicas-e-informacion-del-test/README.md)
<!-- /NAV -->

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 052 a 054.

## Objetivos

1. Comparar estimación ML y EAP de θ.
2. Explicar por qué ML no existe con puntajes extremos.
3. Reconocer el sesgo hacia la media del EAP.

## Fundamentos

Con ítems conocidos, **ML** maximiza la verosimilitud del patrón de respuestas; **EAP** (Bock y Mislevy, 1982) promedia θ con la distribución a posteriori bajo un prior (aquí N(0, 1)). ML no tiene máximo finito con 0 o todos los aciertos; EAP siempre existe pero encoge hacia el prior.

Laboratorio (10 ítems 2PL):

| Patrón | ML | EAP |
|---|---:|---:|
| Todo mal | indefinido | −1,92 |
| 1 acierto (el más fácil) | −2,35 | −1,46 |
| 5 aciertos (los 5 fáciles) | 0,08 | 0,06 |
| 9 aciertos (falla el más fácil) | 2,45 | 1,49 |
| Todo bien | indefinido | 1,96 |

RMSE sobre 3 000 personas: EAP 0,572 (todas); ML 0,699 (solo 2 918 con estimación finita).

## Ejemplo resuelto

Patrón «5 aciertos»: ML ≈ 0,08 y EAP ≈ 0,06 apenas difieren (el patrón es consistente con el centro del prior); en patrones extremos EAP se acerca a 0 más que ML.

## Errores y límites

- Reportar θ de ML sin tratar los extremos.
- Usar un prior inadecuado para una población distinta (p. ej. grupos de media −1).
- Comparar EAP entre grupos con priors distintos.
- Elegir estimador es elegir un sesgo: se declara y se justifica.

## Ejercicios

- **Inicial.** ¿Por qué ML falla con puntaje perfecto?
- **Intermedio.** Si el prior es N(0, 1) y los datos informan poco, ¿hacia dónde se acerca θ̂? A 0.
- **Avanzado.** Cambia el prior a N(1, 1) en `lab.py` y observa la estimación de «todo mal».

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/056-estimacion-de-parametros-y-de-habilidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es un prior y quién lo elige? 2. ¿Qué estimador usarías para una admisión y por qué? 3. ¿Qué reportarías además de θ̂?
Se logra si el estudiante compara estimadores y declara el sesgo elegido.

## Bibliografía

- Bock, R. D., & Mislevy, R. J. (1982). Adaptive EAP estimation of ability in a microcomputer environment. *Applied Psychological Measurement*, 6(4), 431-444. ✅ [DOI](https://doi.org/10.1177/014662168200600405)
- Baker, F. B., & Kim, S.-H. (2004). *Item Response Theory: Parameter Estimation Techniques* (2.ª ed.). CRC Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 055 — Testing adaptativo informatizado](../055-testing-adaptativo/README.md)  
[📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[057 — Curvas características e información del test →](../057-curvas-caracteristicas-e-informacion-del-test/README.md)
<!-- /NAV -->
