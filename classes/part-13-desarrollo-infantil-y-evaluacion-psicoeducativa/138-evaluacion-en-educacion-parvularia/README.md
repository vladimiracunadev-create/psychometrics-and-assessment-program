# 138 — Evaluación en educación parvularia

![Portada de la clase 138](portada.svg)

<!-- NAV -->
[← 137 — Atención temprana y apoyos](../137-atencion-temprana-y-apoyos/README.md) · [📚 Parte 13](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [139 — Cribado del neurodesarrollo: alcances y deriv… →](../139-cribado-del-neurodesarrollo-alcances-y-derivacion/README.md)
<!-- /NAV -->

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 029 y 134.

## Objetivos

1. Evaluar con rúbricas de niveles observables.
2. Calcular kappa simple y ponderado.
3. Entender la calibración entre educadoras como parte del instrumento.

## Fundamentos

En educación parvularia la evaluación es sobre todo **formativa y de observación**, referida a los objetivos de las bases curriculares (consultar la versión vigente del Ministerio de Educación). Una rúbrica de 4 niveles es ordinal; el acuerdo entre educadoras se mide con kappa, y el **kappa ponderado** (Cohen, 1968) penaliza más los desacuerdos lejanos.

Laboratorio (120 niños; dos educadoras; datos sintéticos):

| Rúbrica / condición | κ simple | κ ponderado |
|---|---:|---:|
| Descriptores ambiguos | 0,14 | 0,33 |
| Descriptores observables | 0,46 | 0,73 |
| Observables + una educadora indulgente (+0,6) | 0,30 | 0,65 |

## Ejemplo resuelto

Dos niveles de diferencia (1 frente a 3) pesan (2/3)² = 0,44 y uno de diferencia (1 frente a 2), (1/3)² = 0,11, en el kappa cuadrático de 4 niveles.

## Errores y límites

- Clasificar al niño en vez de describir lo observado en un periodo.
- Descriptores ambiguos («adecuado», «bueno») sin conductas.
- Comparar educadoras sin calibrar.
- Los niveles no son edades de desarrollo ni diagnósticos.

## Ejercicios

- **Inicial.** ¿Qué hace observable un descriptor?
- **Intermedio.** Redacta un descriptor observable para «sigue instrucciones de dos pasos».
- **Avanzado.** Simula tres educadoras y calcula el kappa por pares.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/138-evaluacion-en-educacion-parvularia/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo calibrarías al equipo? 2. ¿Qué evidencias (fotos, producciones) recoges y con qué consentimiento? 3. ¿Cómo informas a las familias?
Se logra si el estudiante mejora una rúbrica y mide el acuerdo.

## Bibliografía

- Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213-220. ✅ [DOI](https://doi.org/10.1037/h0026256)
- Ministerio de Educación de Chile. *Bases Curriculares de la Educación Parvularia* (versión vigente: verificar en mineduc.cl). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 137 — Atención temprana y apoyos](../137-atencion-temprana-y-apoyos/README.md)  
[📚 Parte 13](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[139 — Cribado del neurodesarrollo: alcances y deriv… →](../139-cribado-del-neurodesarrollo-alcances-y-derivacion/README.md)
<!-- /NAV -->
