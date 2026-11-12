# 065 — Adaptación transcultural y equivalencia

![Portada de la clase 065](portada.svg)

> [Índice de la parte](../README.md) · [Anterior](../064-sesgo-predictivo-y-equidad/README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 045 y 063.

## Objetivos

1. Describir el proceso de adaptación de un instrumento.
2. Calcular la congruencia de Tucker entre cargas de dos versiones.
3. Reconocer que la similitud factorial no implica comparabilidad de medias.

## Fundamentos

Adaptar un test es más que traducirlo: se decide la equivalencia conceptual, lingüística y métrica (Hambleton, Merenda y Spielberger, 2005). Las *ITC Guidelines* (2017) recomiendan traducción y retraducción con revisión de expertos, prueba piloto cognitiva, estudios de equivalencia y documentación. La **congruencia de Tucker** φ = Σxy/√(Σx²·Σy²) mide la similitud de dos vectores de cargas; φ > 0,95 es una regla citada para «similitud factorial» (Lorenzo-Seva y ten Berge, 2006).

Laboratorio (8 ítems; ítem 3 mal traducido, carga 0,35; ítem 5 desplazado 0,6; mismo rasgo medio):

| Medida | Valor |
|---|---:|
| Congruencia de Tucker de las cargas | 0,986 |
| Diferencia de medias de la escala | 0,71 (DE 5,89) |

φ es alto aunque hay un ítem defectuoso y un ítem que desplaza la media de la escala en una diferencia que no existe en el rasgo.

## Ejemplo resuelto

Cargas (0,7; 0,7; 0,7) y (0,7; 0,35; 0,7): numerador = 0,49 + 0,245 + 0,49 = 1,225; denominador = √(1,47·1,1025) = 1,273; φ = 0,962: «similar» pese a un ítem a la mitad de carga.

## Errores y límites

- Declarar equivalencia por φ alto o por alfa similar.
- Traducir sin retraducir ni piloto cognitivo.
- Usar normas del país de origen sin estudio local (contexto chileno).
- Un instrumento adaptado necesita su propio estudio de fiabilidad y validez.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre traducir y adaptar?
- **Intermedio.** Calcula φ para (0,6; 0,6) y (0,6; 0,3) → 0,36 + 0,18 = 0,54; √(0,72·0,45) = 0,569; φ = 0,949.
- **Avanzado.** Añade un tercer ítem con carga baja y observa φ.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/065-adaptacion-transcultural/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia mínima pedirías para comparar medias entre idiomas? 2. ¿Qué es una prueba piloto cognitiva? 3. ¿Cómo documentarías el proceso?
Se logra si el estudiante diseña un plan de adaptación y evaluación de equivalencia.

## Bibliografía

- Hambleton, R. K., Merenda, P. F., & Spielberger, C. D. (Eds.) (2005). *Adapting Educational and Psychological Tests for Cross-Cultural Assessment*. Lawrence Erlbaum. ✅ [DOI](https://doi.org/10.4324/9781410611758)
- International Test Commission (2017). *The ITC Guidelines for Translating and Adapting Tests* (2.ª ed.). ITC. ✅ [DOI](https://doi.org/10.1080/15305058.2017.1398166)
- Lorenzo-Seva, U., & ten Berge, J. M. F. (2006). Tucker's congruence coefficient as a meaningful index of factor similarity. *Methodology*, 2(2), 57-64. ✅ [DOI](https://doi.org/10.1027/1614-2241.2.2.57)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
