# 024 — Modelos circumplejos: el hexágono de Holland como predicción falsable

> [Índice de la parte](../README.md) · [Anterior](../023-analisis-factorial-confirmatorio/README.md) · [Siguiente](../025-invarianza-de-medida/README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 018.

## Objetivos

1. Explicar el modelo circumplejo y la predicción de orden de las correlaciones.
2. Calcular el índice de satisfacción de predicciones.
3. Relacionar el hexágono R-I-A-S-E-C con el instrumento RIASEC del catálogo.

## Fundamentos

Holland (1997) ordena los tipos Realista, Investigador, Artístico, Social, Emprendedor y Convencional en un hexágono. La predicción: las correlaciones **decrecen con la distancia** en el círculo (adyacentes > alternos > opuestos). Hay 72 comparaciones de orden (6 pares a distancia 1 × 6 a distancia 2; 6 × 3; 6 × 3). El índice de satisfacción (Hubert y Arabie, 1987; Tracey y Rounds, 1993) es la proporción que se cumple. Es una **predicción falsable**: los datos pueden contradecirla.

Laboratorio (N = 1 500):

| Datos | Predicciones cumplidas |
|---|---:|
| Estructura circular simulada | 72 / 72 = 1,00 |
| Seis variables independientes | 41 / 72 = 0,57 (azar ≈ 0,5) |

En los datos circulares se observan correlaciones ≈ 0,28 entre adyacentes y ≈ −0,58 entre opuestos.

## Ejemplo resuelto

Distancias: R–I = 1; R–A = 2; R–S = 3. Predicción: r(R,I) > r(R,A) > r(R,S). Si el instrumento da 0,45; 0,30; 0,10, se cumplen las 3 comparaciones.

## Errores y límites

- Declarar «hexágono confirmado» con un índice calculado en una sola muestra.
- Ignorar que muchas muestras reales muestran estructura circular imperfecta y que existen modelos alternativos (p. ej. con dimensiones «personas-cosas» y «datos-ideas»).
- Aplicarlo a un instrumento sin saber si sus escalas cubren el círculo.

## Ejercicios

- **Inicial.** ¿Cuántos pares de escalas hay en un hexágono? → 15 (6 a dist. 1, 6 a dist. 2, 3 a dist. 3).
- **Intermedio.** Cuenta cuántas comparaciones de orden hay → 6·6 + 6·3 + 6·3 = 72.
- **Avanzado.** Aplica el índice a los datos del instrumento `onet-riasec-sf` cuando tengas respuestas propias (con datos sintéticos).

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/024-modelos-circumplejos/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué es una predicción falsable? 2. ¿Qué evidencia contradiría el hexágono? 3. ¿Qué limita un índice calculado en una muestra?
Se logra si el estudiante calcula el índice y discute su alcance.

## Bibliografía

- Holland, J. L. (1997). *Making Vocational Choices* (3.ª ed.). Psychological Assessment Resources. ⚠️ existe, pero Crossref registra 1975 (¿otra edición?; [DOI](https://doi.org/10.1207/s15327752jpa3901_15))
- Hubert, L., & Arabie, P. (1987). Evaluating order hypotheses within proximity matrices. *Psychological Bulletin*, 102(1), 172-178. ✅ [DOI](https://doi.org/10.1037//0033-2909.102.1.172)
- Tracey, T. J., & Rounds, J. (1993). Evaluating Holland's and Gati's vocational-interest models: A structural meta-analysis. *Psychological Bulletin*, 113(2), 229-246. ✅ [DOI](https://doi.org/10.1037/0033-2909.113.2.229)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
