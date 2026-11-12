# 085 — Razonamiento numérico

![Portada de la clase 085](portada.svg)

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 015 y 083.

## Objetivos

1. Diseñar ítems numéricos con distractores basados en errores típicos.
2. Realizar un análisis de distractores con valor diagnóstico.
3. Distinguir razonamiento numérico de cálculo y de conocimiento curricular.

## Fundamentos

Los distractores de opción múltiple no son relleno: representan errores conceptuales (Brown y Burton, 1978, sobre «bugs» procedimentales). Si cada distractor atrae a quienes cometen **ese** error, el ítem entrega información diagnóstica además del acierto (Gierl et al., 2017).

Laboratorio (ítem «X % de N» con errores E1 = dividir, E2 = sumar, E3 = error de decimal; 4 000 respuestas por perfil, sintéticas):

| Perfil | Correcta | E1 | E2 | E3 | Opción más elegida |
|---|---:|---:|---:|---:|---|
| domina | 0,92 | 0,03 | 0,03 | 0,03 | correcta |
| confunde división | 0,08 | 0,77 | 0,07 | 0,07 | E1 |
| suma en vez de multiplicar | 0,08 | 0,07 | 0,78 | 0,07 | E2 |
| error de decimal | 0,08 | 0,07 | 0,07 | 0,78 | E3 |

## Ejemplo resuelto

«40 % de 200» → correcta 80; E1 = 200/40 = 5; E2 = 40 + 200 = 240; E3 = 40·200/10 = 800. Quien marca 5 probablemente dividió.

## Errores y límites

- Perfiles de error sintéticos: en datos reales hay que validar que el distractor mide lo que se supone (entrevistas cognitivas).
- Distractores absurdos que nadie elige no aportan.
- Confundir bajo desempeño numérico con baja capacidad: puede ser falta de instrucción.

## Ejercicios

- **Inicial.** ¿Qué es un distractor funcional?
- **Intermedio.** Diseña los distractores de «15 % de 80» (correcta 12).
- **Avanzado.** Agrega un perfil que adivina al azar y calcula su firma.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/085-razonamiento-numerico/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo se valida un distractor? 2. ¿Qué haces con un distractor que elige menos del 5 %? 3. ¿Cómo evitas sesgo cultural en contextos numéricos?
Se logra si el estudiante diseña distractores con justificación y analiza su funcionamiento.

## Bibliografía

- Brown, J. S., & Burton, R. R. (1978). Diagnostic models for procedural bugs in basic mathematical skills. *Cognitive Science*, 2(2), 155-192. ✅ [DOI](https://doi.org/10.1016/s0364-0213(78)80004-4)
- Gierl, M. J., Bulut, O., Guo, Q., & Zhang, X. (2017). Developing, analyzing, and using distractors for multiple-choice tests in education. *Review of Educational Research*, 87(6), 1082-1116. ✅ [DOI](https://doi.org/10.3102/0034654317726529)
- Haladyna, T. M., & Rodriguez, M. C. (2013). *Developing and Validating Test Items*. Routledge. ✅ [DOI](https://doi.org/10.4324/9780203850381)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
