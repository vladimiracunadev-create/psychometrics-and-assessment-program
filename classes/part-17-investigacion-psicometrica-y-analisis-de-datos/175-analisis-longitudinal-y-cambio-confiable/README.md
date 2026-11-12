# 175 — Análisis longitudinal y cambio confiable

![Portada de la clase 175](portada.svg)

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 025 y 162.

## Objetivos

1. Calcular el índice de cambio fiable (RCI).
2. Corregir por efecto de práctica.
3. Distinguir cambio fiable de cambio importante.

## Fundamentos

El RCI (Jacobson y Truax, 1991) compara el cambio observado con el error de la diferencia: RCI = (X₂ − X₁)/EE_dif, con EE_dif = √2·ETM. Cuando hay **efecto de práctica** (mejora por repetir la prueba), se descuenta la mejora esperada (Chelune et al., 1993; Hageman y Arrindell, 1999).

Laboratorio (DE = 10; fiabilidad 0,90; ETM = 3,16; EE_dif = 4,47; práctica +3 puntos; umbral = 8,77):

| Condición | RCI ingenuo: «mejoró» | RCI con práctica: «mejoró» |
|---|---:|---:|
| Sin cambio real (solo práctica) | 10,0 % | 2,6 % |
| Cambio real de +6 puntos | 51,8 % | 27,0 % |

Sin corregir la práctica, un 10 % de personas sin cambio real parece haber mejorado (se espera 2,5 %).

## Ejemplo resuelto

Cambio observado 10 puntos y práctica 3: RCI ingenuo = 10/4,47 = 2,24 (mejoró); RCI corregido = 7/4,47 = 1,57 (sin cambio fiable).

## Errores y límites

- Ignorar la práctica en pruebas repetidas.
- Confundir cambio fiable con cambio clínicamente importante.
- Aplicar el RCI con fiabilidades de otra población.
- Un umbral de 8,77 puntos exige cambios grandes: la sensibilidad es baja (27 % de detección de +6).

## Ejercicios

- **Inicial.** ¿Qué es el efecto de práctica?
- **Intermedio.** Calcula EE_dif con DE = 15 y fiabilidad 0,95 → 15·√0,05·1,414 = 4,74.
- **Avanzado.** Cambia la práctica a 5 puntos y observa el RCI ingenuo.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/175-analisis-longitudinal-y-cambio-confiable/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo estimarías la práctica? 2. ¿Qué formas alternas usarías? 3. ¿Cómo informarías el cambio a la persona?
Se logra si el estudiante corrige por práctica y no sobreinterpreta.

## Bibliografía

- Jacobson, N. S., & Truax, P. (1991). Clinical significance: A statistical approach to defining meaningful change in psychotherapy research. *Journal of Consulting and Clinical Psychology*, 59(1), 12-19. ✅ [DOI](https://doi.org/10.1037/0022-006x.59.1.12)
- Chelune, G. J., et al. (1993). Individual change after epilepsy surgery: Practice effects and base-rate information. *Journal of Clinical and Experimental Neuropsychology*, 15(1), 27-34. ✅ [DOI](https://doi.org/10.1037//0894-4105.7.1.41)
- Hageman, W. J. J. M., & Arrindell, W. A. (1999). Establishing clinically significant change. *Behaviour Research and Therapy*, 37(12), 1169-1193. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
