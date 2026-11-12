# 059 — Equiparación y vinculación de puntajes

![Portada de la clase 059](portada.svg)

<!-- NAV -->
[← 058 — Modelos de respuesta graduada](../058-modelos-de-respuesta-graduada/README.md) · [📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [060 — Diseño de bancos para pruebas adaptativas →](../060-diseno-de-bancos-para-pruebas-adaptativas/README.md)
<!-- /NAV -->

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 061 y 052.

## Objetivos

1. Distinguir equiparación de otras formas de vinculación.
2. Aplicar media, lineal y equipercentil en un diseño de grupos aleatorios.
3. Evaluar el efecto sobre decisiones con corte.

## Fundamentos

Equiparar es hacer intercambiables los puntajes de formas distintas del mismo test (Kolen y Brennan, 2014; Holland y Dorans, 2006). Exige: mismo constructo, misma fiabilidad, simetría y equidad. Los diseños comunes: grupos aleatorios, grupo único contrabalanceado, grupos no equivalentes con ítems ancla. Si las formas miden contenidos distintos, solo hay **vinculación**, no equiparación.

Laboratorio (formas de 40 ítems; Y es más difícil en 0,4; 6 000 personas por forma; corte 22 en la escala X):

| Método | Aprobados con Y equiparada |
|---|---:|
| Forma X (referencia) | 0,303 |
| Sin equiparar | 0,068 |
| Media | 0,209 |
| Lineal | 0,209 |
| Equipercentil | 0,325 |

Sin equiparar, el grupo que rindió la forma difícil aprueba mucho menos solo por la forma. El equipercentil se acerca a la referencia porque iguala toda la distribución.

## Ejemplo resuelto

Medias X = 20,01 e Y = 17,23: la equiparación de medias suma 2,78; un puntaje 15 en Y equivale a 17,78 en X.

## Errores y límites

- Equiparar con grupos no equivalentes sin ítems ancla.
- Aplicar equipercentil con muestras pequeñas sin suavizado.
- Usar el mismo corte sin equiparar cuando las formas difieren.
- La equiparación no corrige un constructo distinto.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre equiparar y vincular?
- **Intermedio.** Medias 30 y 26: ¿qué puntaje en X corresponde a 28 en Y por media? 32.
- **Avanzado.** Disminuye N a 300 en `lab.py` y describe la inestabilidad del equipercentil.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/059-equiparacion-y-vinculacion-de-puntajes/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es un diseño de ítems ancla? 2. ¿Por qué importa la equivalencia de grupos? 3. ¿Qué riesgo hay si no se equipara?
Se logra si el estudiante equipara y evalúa el efecto sobre un corte.

## Bibliografía

- Kolen, M. J., & Brennan, R. L. (2014). *Test Equating, Scaling, and Linking* (3.ª ed.). Springer. ✅ [DOI](https://doi.org/10.1007/978-1-4939-0317-7)
- Holland, P. W., & Dorans, N. J. (2006). Linking and equating. En R. L. Brennan (Ed.), *Educational Measurement* (4.ª ed.). ACE/Praeger. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 058 — Modelos de respuesta graduada](../058-modelos-de-respuesta-graduada/README.md)  
[📚 Parte 05](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[060 — Diseño de bancos para pruebas adaptativas →](../060-diseno-de-bancos-para-pruebas-adaptativas/README.md)
<!-- /NAV -->
