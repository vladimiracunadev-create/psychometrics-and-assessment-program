# 150 — Evaluación de apoyos educativos y evaluación inclusiva

> [Índice de la parte](../README.md)

**Parte 14 — Aprendizaje, aptitudes y dificultades escolares** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 074 y 137.

## Objetivos

1. Calcular el puntaje T de escalamiento de logro de metas (GAS).
2. Entender su sensibilidad a los pesos y su no comparabilidad entre estudiantes.
3. Relacionar la evaluación con el diseño universal para el aprendizaje.

## Fundamentos

El diseño universal para el aprendizaje (CAST, 2018) busca ofrecer múltiples formas de representación, acción y compromiso para reducir la necesidad de ajustes individuales. Para seguir metas individualizadas se usa el **escalamiento de logro de metas** (Kiresuk y Sherman, 1968; Turner-Stokes, 2009): cada meta tiene niveles de −2 a +2 y un peso.

```
T = 50 + 10·Σ(wᵢxᵢ) / √( (1 − ρ)Σwᵢ² + ρ(Σwᵢ)² ),   ρ = 0,3
```

Laboratorio:

| Caso | T |
|---|---:|
| A: logros (0, +1, 0), pesos iguales | 54,6 |
| A: logros (0, +1, 0), peso 3 en la meta 2 | 57,7 |
| B: 5 metas, todas «lo esperado» | 50,0 |
| B: +1 en una sola meta | 53,0 |
| B: +1 en todas | 65,1 |

## Ejemplo resuelto

Tres metas con pesos 1, y logros (0, +1, 0): numerador = 1; denominador = √(0,7·3 + 0,3·9) = √4,8 = 2,19; T = 50 + 10·0,456 = 54,6.

## Errores y límites

- Comparar el T de dos estudiantes: las metas y su dificultad son distintas.
- Fijar metas poco observables o inalcanzables.
- Cambiar los pesos después de ver los resultados.
- ρ = 0,3 es una convención histórica.

## Ejercicios

- **Inicial.** ¿Qué significa T = 50 en GAS?
- **Intermedio.** Calcula T con un solo logro +2 y una sola meta de peso 1 → 50 + 10·2/√(0,7 + 0,3) = 70.
- **Avanzado.** Redacta tres metas observables con niveles −2 a +2 para un estudiante.

## Laboratorio

```bash
python classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/150-evaluacion-de-apoyos-educativos-y-evaluacion-inclusiva/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo acuerdas las metas con la familia y el estudiante? 2. ¿Cómo evitas el efecto techo? 3. ¿Qué apoyos universales reducirían los ajustes individuales?
Se logra si el estudiante redacta metas medibles y calcula e interpreta el T con cautela.

## Bibliografía

- Kiresuk, T. J., & Sherman, R. E. (1968). Goal attainment scaling: A general method for evaluating comprehensive community mental health programs. *Community Mental Health Journal*, 4(6), 443-453. ✅ [DOI](https://doi.org/10.1007/bf01530764)
- Turner-Stokes, L. (2009). Goal attainment scaling (GAS) in rehabilitation: A practical guide. *Clinical Rehabilitation*, 23(4), 362-370. ✅ [DOI](https://doi.org/10.1177/0269215508101742)
- CAST (2018). *Universal Design for Learning Guidelines* (versión 2.2). CAST. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
