# 072 — Directrices de la International Test Commission

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clase 071.

## Objetivos

1. Reconocer las directrices ITC sobre uso, traducción/adaptación y evaluación por computador e internet.
2. Distinguir lo documentado, lo implementado y lo validado en un catálogo.
3. Auditar un catálogo con criterios de transparencia.

## Fundamentos

La International Test Commission publica directrices internacionales: uso de tests (ITC, 2013), traducción y adaptación (ITC, 2017) y evaluación computarizada y por internet (ITC, 2006), entre otras. Piden competencia del usuario, información al evaluado, control de calidad, seguridad y atención a la equidad. En este repositorio esas ideas se traducen en **estados diferenciados** del catálogo.

Laboratorio (catálogo `catalogo/fichas.yaml`, 140 fichas):

| Medida | Valor |
|---|---:|
| Fichas documentadas / implementadas | 135 / 5 |
| Fichas verificadas contra fuente primaria | 5 de 140 |
| Licencia propietaria | 36 |
| Propietarias de uso clínico (exigen profesional habilitado) | 19 |
| «Validado» sin evidencia declarada | 0 |

## Ejemplo resuelto

La ficha del WISC figura como propietaria de uso clínico y educativo: se estudia su fundamento y se usan alternativas abiertas para practicar; no se reproducen sus ítems ni claves.

## Errores y límites

- Contar fichas como instrumentos disponibles.
- Dejar `verificado: false` indefinidamente sin plan para contrastar con la fuente primaria.
- Citar las directrices sin leer la versión vigente.

## Ejercicios

- **Inicial.** ¿Qué distingue un instrumento documentado de uno implementado?
- **Intermedio.** Calcula el porcentaje de fichas propietarias → 36/140 = 25,7 %.
- **Avanzado.** Elige cinco fichas y verifícalas contra su fuente primaria; actualiza `verificado`.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/072-itc-y-normas-internacionales/lab.py
```

## Autoevaluación y criterios

1. ¿Qué responsabilidad tiene el usuario del test? 2. ¿Qué información entregarías al evaluado? 3. ¿Cómo evitas inflar el recuento del catálogo?
Se logra si el estudiante audita un catálogo con estados diferenciados.

## Bibliografía

- International Test Commission (2013). *ITC Guidelines on Test Use*. ITC. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- International Test Commission (2017). *The ITC Guidelines for Translating and Adapting Tests* (2.ª ed.). ITC. ✅ [DOI](https://doi.org/10.1080/15305058.2017.1398166)
- International Test Commission (2006). International guidelines on computer-based and internet-delivered testing. *International Journal of Testing*, 6(2), 143-171. ✅ [DOI](https://doi.org/10.1207/s15327574ijt0602_4)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
