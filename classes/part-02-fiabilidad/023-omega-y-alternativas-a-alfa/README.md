# 023 — Omega de McDonald y por qué alfa se queda corto

![Portada de la clase 023](portada.svg)

> [Índice de la parte](../README.md) · [Anterior](../022-consistencia-interna-alfa/README.md) · [Siguiente](../024-test-retest-y-estabilidad/README.md)

**Parte 02 — Fiabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 022 (se anticipa el modelo factorial de la parte 04).

## Objetivos

1. Explicar la tau-equivalencia y cuándo falla.
2. Calcular omega total desde cargas factoriales.
3. Anticipar cuánto difieren alfa y omega.
4. Reconocer que omega depende de que el modelo factorial sea correcto.

## Fundamentos

Con ítems estandarizados y un factor: carga λᵢ y varianza única ψᵢ = 1 − λᵢ².

```
ω = (Σλᵢ)² / ( (Σλᵢ)² + Σψᵢ )
```

Si las cargas son iguales (tau-equivalencia), ω = α; si no, α es menor (McDonald, 1999; Dunn, Baguley y Brunsden, 2014).

Laboratorio (6 ítems, cargas **verdaderas** conocidas):

| Caso | α | ω | Diferencia |
|---|---:|---:|---:|
| Cargas iguales (0,6 × 6) | 0,770 | 0,771 | 0,001 |
| Desiguales (0,9 … 0,3) | 0,748 | 0,769 | 0,021 |
| Muy desiguales (0,95 × 2; 0,2 × 4) | 0,569 | 0,644 | 0,075 |

**Lo que el laboratorio no puede enseñar:** aquí se usan las cargas verdaderas porque generamos los datos. Con datos reales las cargas se estiman; si el modelo ajusta mal (dos dimensiones, errores correlacionados), omega hereda el error. Con estructura multidimensional corresponde omega jerárquico o por dimensión.

## Ejemplo resuelto

Cargas 0,8; 0,7; 0,6: (Σλ)² = 4,41; Σψ = 0,36 + 0,51 + 0,64 = 1,51; ω = 4,41 / 5,92 = 0,745.

## Errores y límites

- Reportar omega calculado con un modelo que ajusta mal.
- Presentar la brecha alfa–omega como «defecto» de alfa en cualquier caso.
- Creer que un ω alto vuelve unidimensional una escala multidimensional.

## Ejercicios

- **Inicial.** ¿Cuándo coinciden α y ω? → con cargas iguales.
- **Intermedio.** Cuatro cargas de 0,5: (Σλ)² = 4, Σψ = 3, ω = 4/7 = 0,571.
- **Avanzado.** Añade a `lab.py` una carga negativa sin reflejar y explica el efecto en α.

## Laboratorio

```bash
python classes/part-02-fiabilidad/023-omega-y-alternativas-a-alfa/lab.py
```

## Autoevaluación y criterios

1. ¿Qué supuesto sobre las cargas hace alfa? 2. ¿Por qué omega puede engañar con un modelo mal especificado? 3. ¿Qué usarías con dos subdimensiones?
Se logra si el estudiante calcula ω, anticipa la brecha y declara la dependencia del modelo.

## Bibliografía

- McDonald, R. P. (1999). *Test Theory: A Unified Treatment*. Lawrence Erlbaum. ✅ [DOI](https://doi.org/10.2307/2669496)
- Dunn, T. J., Baguley, T., & Brunsden, V. (2014). From alpha to omega. *British Journal of Psychology*, 105(3), 399-412. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Hayes, A. F., & Coutts, J. J. (2020). Use omega rather than Cronbach's alpha for estimating reliability. *Communication Methods and Measures*, 14(1), 1-24. ✅ [DOI](https://doi.org/10.1080/19312458.2020.1718629)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
