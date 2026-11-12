# 153 — Valores laborales y de vida

![Portada de la clase 153](portada.svg)

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 107 y 108.

## Objetivos

1. Escalar valores a partir de comparaciones por pares.
2. Estimar el modelo de Bradley–Terry.
3. Evaluar la estabilidad de un ordenamiento de valores.

## Fundamentos

En el modelo de Bradley y Terry (1952), la probabilidad de que el valor *i* supere al *j* en una comparación es wᵢ/(wᵢ + wⱼ). Los pesos se estiman iterativamente (Zermelo, 1929). Las comparaciones por pares evitan la aquiescencia de la Likert, pero son relativas y el número de pares crece con k(k − 1)/2. Los inventarios de valores laborales clásicos (Super, 1970) ordenan valores por importancia.

Laboratorio (6 valores; 15 pares; 60 personas simuladas):

| Valor | w verdadero | w estimado | Puesto estimado |
|---|---:|---:|---:|
| Autonomía | 1,32 | 1,35 | 1 |
| Equilibrio | 1,23 | 1,29 | 2 |
| Seguridad | 1,15 | 1,13 | 3 |
| Ingreso | 0,99 | 0,91 | 4 |
| Servicio | 0,82 | 0,90 | 5 |
| Prestigio | 0,49 | 0,42 | 6 |

Repitiendo el estudio con otra muestra de 60, el top 3 coincide con el orden verdadero en solo 34 % de las repeticiones.

## Ejemplo resuelto

w₁ = 1,6 y w₂ = 1,0: P(1 supera a 2) = 1,6/2,6 = 0,615.

## Errores y límites

- Informar el puesto exacto de cada valor.
- Interpretar «valorar más» como «valorar mucho».
- Usar comparaciones por pares con muchos valores (fatiga).
- Datos sintéticos; los pesos verdaderos son supuestos.

## Ejercicios

- **Inicial.** ¿Cuántos pares hay con 8 valores? → 28.
- **Intermedio.** Si w₁ = 2 y w₂ = 1, P(1 supera a 2) = 0,667.
- **Avanzado.** Aumenta a 200 personas en `lab.py` y observa la estabilidad del top 3.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/153-valores-laborales-y-de-vida/lab.py
```

## Autoevaluación y criterios

1. ¿Cómo usarías los valores en una conversación de orientación? 2. ¿Qué otros métodos hay (ranking, Likert, centrado)? 3. ¿Cómo informarías la incertidumbre?
Se logra si el estudiante estima una escala por pares y comunica un orden con su incertidumbre.

## Bibliografía

- Bradley, R. A., & Terry, M. E. (1952). Rank analysis of incomplete block designs: I. The method of paired comparisons. *Biometrika*, 39(3-4), 324-345. ✅ [DOI](https://doi.org/10.1093/biomet/39.3-4.324)
- Zermelo, E. (1929). Die Berechnung der Turnier-Ergebnisse als ein Maximumproblem der Wahrscheinlichkeitsrechnung. *Mathematische Zeitschrift*, 29, 436-460. ✅ [DOI](https://doi.org/10.1007/bf01180541)
- Super, D. E. (1970). *Work Values Inventory*. Houghton Mifflin. ✅ [DOI](https://doi.org/10.1037/t01584-000)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
