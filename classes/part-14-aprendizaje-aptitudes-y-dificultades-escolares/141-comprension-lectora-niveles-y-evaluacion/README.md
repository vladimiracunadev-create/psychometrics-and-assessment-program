# 141 — Comprensión lectora: niveles y evaluación

![Portada de la clase 141](portada.svg)

<!-- NAV -->
[← 140 — Contexto chileno: referentes curriculares y n…](../../part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/140-contexto-chileno-referentes-curriculares-y-normativos/README.md) · [📚 Parte 14](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [142 — Fluidez y precisión lectora →](../142-fluidez-y-precision-lectora/README.md)
<!-- /NAV -->

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 084 y 088.

## Objetivos

1. Describir niveles de comprensión (literal, inferencial, crítico).
2. Comprobar la jerarquía de dificultad y la fiabilidad de subpuntajes.
3. Decidir qué se informa: total o perfil por nivel.

## Fundamentos

La comprensión lectora se modela como la construcción de una representación mental del texto, que integra información explícita, inferencias y conocimiento previo (Kintsch, 1998; Snow, 2002). Las pruebas suelen clasificar los ítems por nivel, pero los niveles **no son habilidades independientes**: correlacionan alto, de modo que los subpuntajes (pocos ítems) son poco fiables y sus diferencias, aún menos (clases 087 y 088).

Laboratorio (24 ítems, 8 por nivel; 2 000 estudiantes simulados con una habilidad única):

| Nivel | % de aciertos | Alfa (8 ítems) |
|---|---:|---:|
| Literal | 66,8 % | 0,62 |
| Inferencial | 50,3 % | 0,63 |
| Crítico | 33,6 % | 0,62 |
| Total (24) | 50,2 % | 0,83 |

Correlación literal–inferencial = 0,60; fiabilidad de la diferencia (inferencial − literal) = 0,07.

## Ejemplo resuelto

Con ρ = 0,62 y r = 0,60 entre subpuntajes de igual varianza, la fiabilidad de la diferencia es (0,62 + 0,62 − 1,20)/(2 − 1,20) = 0,05 (≈ 0,07 en la simulación).

## Errores y límites

- Informar un «perfil por niveles» con 8 ítems por nivel.
- Confundir dificultad del texto con dificultad de la tarea.
- Ignorar el conocimiento previo del tema.
- Datos sintéticos con habilidad única por construcción.

## Ejercicios

- **Inicial.** ¿Qué es una inferencia?
- **Intermedio.** Calcula la fiabilidad de una diferencia con ρ = 0,7 y r = 0,5 → (1,4 − 1,0)/(2 − 1,0) = 0,40.
- **Avanzado.** Sube a 16 ítems por nivel en `lab.py` y observa los alfas.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/141-comprension-lectora-niveles-y-evaluacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué informarías a un docente? 2. ¿Cómo distinguirías un problema de decodificación de uno de comprensión? 3. ¿Cómo controlas la dificultad del texto?
Se logra si el estudiante verifica la jerarquía y decide con criterio qué reportar.

## Bibliografía

- Kintsch, W. (1998). *Comprehension: A Paradigm for Cognition*. Cambridge University Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Snow, C. E. (2002). *Reading for Understanding: Toward an R&D Program in Reading Comprehension*. RAND. ✅ [DOI](https://doi.org/10.7249/mr1465.0)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 140 — Contexto chileno: referentes curriculares y n…](../../part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/140-contexto-chileno-referentes-curriculares-y-normativos/README.md)  
[📚 Parte 14](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[142 — Fluidez y precisión lectora →](../142-fluidez-y-precision-lectora/README.md)
<!-- /NAV -->
