# 130 — Gestión de conflictos y toma de decisiones

> [Índice de la parte](../README.md)

**Parte 12 — Liderazgo, equipos y sociometría** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 122 y 124.

## Objetivos

1. Verificar el teorema de la predicción de la diversidad.
2. Comparar juicios independientes con juicios influidos.
3. Relacionar procedimientos de decisión con la calidad del resultado.

## Fundamentos

Para estimaciones numéricas, el error del promedio del grupo es igual al error individual medio menos la **diversidad** (varianza de las estimaciones) (Page, 2007):

```
(media − verdad)² = media[(estimación_i − verdad)²] − varianza(estimaciones)
```

Cuando los juicios son independientes, los errores se cancelan (Surowiecki, 2004). Cuando la discusión los alinea con una figura influyente, baja la diversidad y se hereda su sesgo (Janis, 1972, sobre pensamiento de grupo). Procedimientos como Delphi (Dalkey y Helmer, 1963) buscan juicios independientes iterados. Las escalas de «estilo de manejo de conflictos» son autoinformes de evidencia limitada.

Laboratorio (9 integrantes; verdad 100; error individual DE 20; el líder estima +25 y los demás se acercan 70 %; 4 000 repeticiones):

| Condición | Error colectivo (MSE) | RMSE |
|---|---:|---:|
| Independientes | 45,7 | 6,8 |
| Influidos por el líder sesgado | 325,9 | 18,1 |

La identidad del teorema se cumple con diferencia máxima de 8·10⁻¹³.

## Ejemplo resuelto

Estimaciones 90, 100 y 130 con verdad 100: media 106,67 → error colectivo = 44,4; error individual medio = (100 + 0 + 900)/3 = 333,3; diversidad (varianza poblacional) = 288,9; 333,3 − 288,9 = 44,4.

## Errores y límites

- Suponer que discutir siempre mejora la decisión.
- Aplicar el teorema a decisiones no numéricas sin cuidado.
- Ignorar el conflicto afectivo: la calidad de la relación también importa.
- Modelo simple: el sesgo del líder y la influencia son supuestos.

## Ejercicios

- **Inicial.** ¿Qué es la diversidad en el teorema?
- **Intermedio.** Con estimaciones 80, 100, 120 y verdad 100: error colectivo = 0; error individual = 266,7; diversidad = 266,7.
- **Avanzado.** Reduce la influencia a 0,3 en `lab.py` y observa el error.

## Laboratorio

```bash
python classes/part-12-liderazgo-equipos-y-sociometria/130-gestion-de-conflictos-y-toma-de-decisiones/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo diseñarías una decisión que conserve la diversidad? 2. ¿Qué papel tiene la jefatura? 3. ¿Cómo evalúas la calidad de una decisión?
Se logra si el estudiante verifica el teorema y diseña un procedimiento que conserve la diversidad.

## Bibliografía

- Page, S. E. (2007). *The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies*. Princeton University Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Janis, I. L. (1972). *Victims of Groupthink*. Houghton Mifflin. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Dalkey, N., & Helmer, O. (1963). An experimental application of the Delphi method to the use of experts. *Management Science*, 9(3), 458-467. ✅ [DOI](https://doi.org/10.1287/mnsc.9.3.458)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
