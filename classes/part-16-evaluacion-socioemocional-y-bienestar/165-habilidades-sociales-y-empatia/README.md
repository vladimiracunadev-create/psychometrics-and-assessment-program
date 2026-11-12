# 165 — Habilidades sociales y empatía

![Portada de la clase 165](portada.svg)

> [Índice de la parte](../README.md)

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 045 y 083.

## Objetivos

1. Distinguir empatía cognitiva y afectiva y su medición.
2. Corregir el sesgo de respuesta en una prueba de reconocimiento de emociones.
3. Diferenciar autoinformes de pruebas de desempeño.

## Fundamentos

La empatía es multidimensional (Davis, 1983: toma de perspectiva, fantasía, preocupación empática, malestar personal). Los autoinformes miden el autoconcepto; las pruebas de reconocimiento de emociones miden desempeño perceptivo, pero mezclan percepción, vocabulario y sesgo de respuesta. La **tasa de acierto no sesgada** (Wagner, 1993), Hu = Σ_i [aciertos_i² / (n_i · respuestas_i)]/k, corrige parcialmente la tendencia a usar una respuesta.

Laboratorio (6 emociones × 12 estímulos; misma nitidez perceptiva; sintético):

| Persona | Precisión cruda | Hu |
|---|---:|---:|
| Sin sesgo de respuesta | 0,75 | 0,57 |
| Sesgo a responder «enojo» | 0,56 | 0,37 |

## Ejemplo resuelto

Para «enojo»: 11 aciertos de 12 estímulos, pero la persona responde «enojo» 30 veces: Hu_enojo = 11²/(12·30) = 0,34, muy inferior a la precisión cruda de esa categoría (0,92).

## Errores y límites

- Diagnosticar «falta de empatía».
- Usar pruebas con rostros sin evidencia de equivalencia cultural.
- Tomar el reconocimiento de emociones como habilidad social global.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Qué mide un autoinforme de empatía?
- **Intermedio.** Calcula Hu para 9 aciertos, 12 estímulos y 15 respuestas: 81/(12·15) = 0,45.
- **Avanzado.** Introduce un segundo sesgo (a «miedo») y compara.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/165-habilidades-sociales-y-empatia/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo evalúas habilidades sociales en el aula? 2. ¿Qué observarías en contexto? 3. ¿Qué derivarías y cuándo?
Se logra si el estudiante corrige el sesgo y distingue qué mide cada tipo de instrumento.

## Bibliografía

- Davis, M. H. (1983). Measuring individual differences in empathy: Evidence for a multidimensional approach. *Journal of Personality and Social Psychology*, 44(1), 113-126. ✅ [DOI](https://doi.org/10.1037/0022-3514.44.1.113)
- Wagner, H. L. (1993). On measuring performance in category judgment studies of nonverbal behavior. *Journal of Nonverbal Behavior*, 17(1), 3-28. ✅ [DOI](https://doi.org/10.1007/bf00987006)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
