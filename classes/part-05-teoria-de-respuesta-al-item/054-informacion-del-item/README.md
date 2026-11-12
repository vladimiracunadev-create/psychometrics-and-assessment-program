# 054 — Función de información: dónde mide bien cada ítem

![Portada de la clase 054](portada.svg)

> [Índice de la parte](../README.md) · [Anterior](../053-modelos-de-dos-y-tres-parametros/README.md) · [Siguiente](../055-testing-adaptativo/README.md)

**Parte 05 — Teoría de respuesta al ítem** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clase 053.

## Objetivos

1. Calcular la información de un ítem 2PL y la del test.
2. Convertir información en error típico de estimación.
3. Elegir ítems según el rango del rasgo que interesa.

## Fundamentos

```
Iᵢ(θ) = a² · P(θ) · (1 − P(θ))          I_test(θ) = Σ Iᵢ(θ)          EE(θ) = 1 / √I_test(θ)
```

La información es máxima en θ = b y crece con a². A diferencia del alfa, la precisión **es una curva**, no un número (Lord, 1980; Hambleton, Swaminathan y Rogers, 1991).

Laboratorio (5 ítems):

| Ítem | θ = −2 | −1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|
| A (a 0,6; b −2) | 0,09 | 0,08 | 0,06 | 0,04 | 0,03 |
| B (a 1,0; b 0) | 0,10 | 0,20 | 0,25 | 0,20 | 0,10 |
| C (a 2,0; b 0) | 0,07 | 0,42 | 1,00 | 0,42 | 0,07 |
| D (a 1,5; b 1,5) | 0,01 | 0,05 | 0,19 | 0,49 | 0,49 |
| E (a 2,0; b −1) | 0,42 | 1,00 | 0,42 | 0,07 | 0,01 |
| **Test** | 0,70 | 1,75 | 1,93 | 1,22 | 0,70 |
| Error típico | 1,20 | 0,76 | 0,72 | 0,90 | 1,19 |

C aporta cuatro veces la información de B en su zona; A casi no aporta en ninguna.

## Ejemplo resuelto

a = 2, b = 0 en θ = 0: P = 0,5; I = 4 · 0,25 = 1,0. Para EE = 0,30 se necesita I = 1/0,09 = 11,1.

## Errores y límites

- Tratar la información como fija: depende de que los parámetros estén bien estimados.
- Suponer que más información siempre es mejor: también hay que cubrir el contenido.
- Olvidar que la información de un ítem 3PL es menor que la de un 2PL con los mismos a y b.

## Ejercicios

- **Inicial.** ¿Dónde es máxima la información de un ítem 2PL? → en θ = b.
- **Intermedio.** Si I_test(θ) = 16, EE = 0,25.
- **Avanzado.** Elige en `lab.py` el ítem adicional que más reduzca el error en θ = 1,5.

## Laboratorio

```bash
python classes/part-05-teoria-de-respuesta-al-item/054-informacion-del-item/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un ítem de a alto es más informativo? 2. ¿Cómo diseñarías un test para un corte en θ = 1? 3. ¿Cuál es la relación entre información y fiabilidad?
Se logra si el estudiante calcula la información y elige ítems para un rango.

## Bibliografía

- Lord, F. M. (1980). *Applications of Item Response Theory to Practical Testing Problems*. Lawrence Erlbaum. ⚠️ existe, pero Crossref registra 2012 (¿otra edición?; [DOI](https://doi.org/10.4324/9780203056615))
- Hambleton, R. K., Swaminathan, H., & Rogers, H. J. (1991). *Fundamentals of Item Response Theory*. Sage. ✅ [DOI](https://doi.org/10.2307/2075521)
- Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
