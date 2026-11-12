# 032 — Validez de contenido y el juicio de expertos

![Portada de la clase 032](portada.svg)

<!-- NAV -->
[← 031 — La validez no es una propiedad del test, es u…](../031-validez-como-argumento/README.md) · [📚 Parte 03](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [033 — Validez de constructo: convergente y discrimi… →](../033-validez-de-constructo/README.md)
<!-- /NAV -->

**Parte 03 — Validez** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 011 y 031.

## Objetivos

1. Explicar la representatividad del contenido frente a la tabla de especificaciones.
2. Calcular el I-CVI, el S-CVI/Ave y la V de Aiken.
3. Reconocer lo que estos índices no miden.

## Fundamentos

La validez de contenido pregunta si los ítems representan el dominio que se quiere cubrir. Se apoya en una **tabla de especificaciones** (clase 016) y en el juicio de expertos.

```
I-CVI = jueces que califican 3 o 4 / total de jueces       (escala 1-4)
V de Aiken = Σ(rᵢ − mínimo) / ( n · (categorías − 1) )     (Aiken, 1985)
S-CVI/Ave = promedio de los I-CVI
```

Un umbral habitual de I-CVI es 0,78 con seis o más jueces (Lynn, 1986; Polit y Beck, 2006): es una convención, no una ley.

Laboratorio (6 jueces, 12 ítems; los ítems 11 y 12 son poco relevantes por diseño):

| Ítems | I-CVI | V de Aiken | Juicio |
|---|---:|---:|---|
| 1–10 | 0,83–1,00 | 0,67–1,00 | ok |
| 11 | 0,17 | 0,33 | revisar |
| 12 | 0,00 | 0,28 | revisar |

S-CVI/Ave = 0,79. Los índices detectan los dos ítems defectuosos.

## Ejemplo resuelto

Cinco jueces califican un ítem con 4, 4, 3, 2, 3. I-CVI = 4/5 = 0,80. V de Aiken = (3+3+2+1+2)/(5·3) = 0,73.

## Errores y límites

- Los índices cuantifican **acuerdo** entre jueces, no **cobertura**: un banco con todos los ítems relevantes puede omitir una faceta completa. Eso se ve contra la tabla de especificaciones.
- Elegir jueces sin experiencia en el dominio o en la población evaluada.
- Aplicar el índice a constructos sin dominio acotado.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre relevancia y claridad como criterios de juicio?
- **Intermedio.** Calcula el I-CVI de un ítem con calificaciones 4, 4, 4, 3, 2, 1 → 4/6 = 0,67.
- **Avanzado.** Añade a `lab.py` un séptimo juez sesgado y observa el efecto sobre el I-CVI.

## Laboratorio

```bash
python classes/part-03-validez/032-validez-de-contenido/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un S-CVI alto no garantiza cobertura? 2. ¿Cómo eliges expertos? 3. ¿Qué haces con un ítem de I-CVI 0,67?
Se logra si el estudiante calcula los índices y propone cómo revisar la cobertura.

## Bibliografía

- Aiken, L. R. (1985). Three coefficients for analyzing the reliability and validity of ratings. *Educational and Psychological Measurement*, 45(1), 131-142. ✅ [DOI](https://doi.org/10.1177/0013164485451012)
- Lynn, M. R. (1986). Determination and quantification of content validity. *Nursing Research*, 35(6), 382-385. ✅ [DOI](https://doi.org/10.1097/00006199-198611000-00017)
- Polit, D. F., & Beck, C. T. (2006). The content validity index: Are you sure you know what's being reported? *Research in Nursing & Health*, 29(5), 489-497. ✅ [DOI](https://doi.org/10.1002/nur.20147)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 031 — La validez no es una propiedad del test, es u…](../031-validez-como-argumento/README.md)  
[📚 Parte 03](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[033 — Validez de constructo: convergente y discrimi… →](../033-validez-de-constructo/README.md)
<!-- /NAV -->
