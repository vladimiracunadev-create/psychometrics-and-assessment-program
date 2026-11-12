# 135 — Cribado frente a diagnóstico en la infancia

![Portada de la clase 135](portada.svg)

<!-- NAV -->
[← 134 — Observación sistemática y registros anecdótic…](../134-observacion-sistematica-y-registros-anecdoticos/README.md) · [📚 Parte 13](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [136 — Evaluar con la familia: entrevista y devoluci… →](../136-evaluar-con-la-familia-entrevista-y-devolucion/README.md)
<!-- /NAV -->

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 100 y 131.

## Objetivos

1. Distinguir el propósito de un cribado del de un diagnóstico.
2. Interpretar una curva ROC y elegir un punto de corte.
3. Calcular cuántos niños se derivan por cada caso verdadero.

## Fundamentos

El **cribado** identifica riesgo en una población aparentemente sana, con pruebas breves; el **diagnóstico** es un proceso profesional, individual y más amplio (Glascoe, 2005; Lipkin y Macias, 2020). Un cribado se evalúa con sensibilidad, especificidad, valor predictivo y el área bajo la curva ROC (Hanley y McNeil, 1982). El corte «óptimo» (Youden) puede no ser el viable si la red de derivación es limitada.

Laboratorio (prevalencia 5 %; puntaje de casos ~N(0; 1) y de no casos ~N(1,5; 1); AUC ≈ 0,86):

| Corte | Sens. | Espec. | VPP | Derivar por cada 100 | Derivados por caso |
|---:|---:|---:|---:|---:|---:|
| 0,00 | 0,50 | 0,93 | 0,28 | 8,9 | 3,5 |
| 0,75 (Youden) | 0,77 | 0,77 | 0,15 | 25,3 | 6,6 |
| 1,50 | 0,93 | 0,50 | 0,09 | 52,1 | 11,2 |

## Ejemplo resuelto

Con corte 0,75, por cada 100 niños se derivan 25; ≈ 3,9 son casos (77 % de 5) y ≈ 21 no lo son: 6,6 derivados por caso.

## Errores y límites

- Llamar «diagnóstico» a un resultado de cribado.
- Elegir el corte por estadística sin considerar capacidad y costos.
- No ofrecer apoyo mientras se espera la evaluación.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué es el índice de Youden?
- **Intermedio.** Sens. 0,6 y esp. 0,9 → Youden 0,5.
- **Avanzado.** Cambia la prevalencia a 15 % en `lab.py` y observa el VPP.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/135-cribado-frente-a-diagnostico-en-la-infancia/lab.py
```

## Autoevaluación y criterios

1. ¿Qué capacidad de derivación tiene tu servicio? 2. ¿Cómo comunicas «riesgo»? 3. ¿Qué seguimiento propones para los no derivados?
Se logra si el estudiante elige un corte justificado y comunica con lenguaje de riesgo.

## Bibliografía

- Glascoe, F. P. (2005). Screening for developmental and behavioral problems. *Mental Retardation and Developmental Disabilities Research Reviews*, 11(3), 173-179. ✅ [DOI](https://doi.org/10.1002/mrdd.20068)
- Hanley, J. A., & McNeil, B. J. (1982). The meaning and use of the area under a receiver operating characteristic (ROC) curve. *Radiology*, 143(1), 29-36. ✅ [DOI](https://doi.org/10.1148/radiology.143.1.7063747)
- Lipkin, P. H., & Macias, M. M. (2020). Promoting optimal development. *Pediatrics*, 145(1), e20193449. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 134 — Observación sistemática y registros anecdótic…](../134-observacion-sistematica-y-registros-anecdoticos/README.md)  
[📚 Parte 13](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[136 — Evaluar con la familia: entrevista y devoluci… →](../136-evaluar-con-la-familia-entrevista-y-devolucion/README.md)
<!-- /NAV -->
