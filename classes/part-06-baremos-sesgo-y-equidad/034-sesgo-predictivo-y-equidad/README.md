# 034 — Sesgo predictivo y definiciones de equidad

> [Índice de la parte](../README.md) · [Anterior](../033-funcionamiento-diferencial-del-item/README.md) · [Siguiente](../035-adaptacion-transcultural/README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 019 y 020.

## Objetivos

1. Aplicar el modelo de Cleary de sesgo predictivo.
2. Comparar selección, tasa de verdaderos positivos y valor predictivo entre grupos.
3. Explicar por qué las definiciones de equidad no pueden cumplirse a la vez.

## Fundamentos

Modelo de Cleary (1968): un test no tiene sesgo predictivo si la recta de regresión del criterio sobre el test es la misma en todos los grupos. Se comparan intercepto y pendiente por grupo. Aparte, hay definiciones de equidad basadas en resultados: igual tasa de selección, igual tasa de verdaderos positivos (oportunidad igual) e igual valor predictivo (calibración). Si las tasas base difieren, no se pueden igualar todas (Kleinberg et al., 2017; Chouldechova, 2017).

Laboratorio (corte común X ≥ 0,5; «buen desempeño» = Y > 0):

| Mundo | Grupo | Selección | TPR | VPP | Tasa base |
|---|---|---:|---:|---:|---:|
| 1 (misma recta) | A | 0,307 | 0,453 | 0,742 | 0,503 |
| | B | 0,160 | 0,285 | 0,715 | 0,401 |
| 2 (B rinde menos en Y a igual X) | A | 0,307 | 0,453 | 0,742 | 0,503 |
| | B | 0,160 | 0,326 | 0,595 | 0,293 |

En el mundo 1 las rectas coinciden y la calibración es parecida (VPP 0,74 y 0,72), pero la selección y el TPR difieren. En el mundo 2 el VPP cae en B (0,60): el corte común sobre-predice el desempeño de B.

## Ejemplo resuelto

Si la recta común predice Y = 0,5 para X = 1 y el grupo B promedia 0,2 en ese X, el test sobre-predice a B (diferencia de intercepto).

## Errores y límites

- Declarar «el test es justo» porque la recta es común, sin mirar las consecuencias (clase 020).
- Elegir una definición de equidad por conveniencia técnica.
- Ignorar que el criterio (p. ej. evaluación del supervisor) también puede estar sesgado.
- Las decisiones automatizadas requieren revisión humana y derecho a explicación (parte 07).

## Ejercicios

- **Inicial.** ¿Qué compara el modelo de Cleary?
- **Intermedio.** Si las tasas base son iguales, ¿es posible igualar selección y TPR a la vez? Sí, en general.
- **Avanzado.** Cambia la tasa base de B en `lab.py` y observa las tres métricas.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/034-sesgo-predictivo-y-equidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué definición de equidad priorizas en admisión y por qué? 2. ¿Quién decide? 3. ¿Cómo documentas la decisión?
Se logra si el estudiante evalúa sesgo predictivo y discute definiciones de equidad.

## Bibliografía

- Cleary, T. A. (1968). Test bias: Prediction of grades of Negro and white students in integrated colleges. *Journal of Educational Measurement*, 5(2), 115-124. ✅ [DOI](https://doi.org/10.1111/j.1745-3984.1968.tb00613.x)
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2017). Inherent trade-offs in the fair determination of risk scores. *ITCS 2017*. ⚠️ existe, pero Crossref registra 2023 (¿otra edición?; [DOI](https://doi.org/10.1145/3603195.3603206))
- Chouldechova, A. (2017). Fair prediction with disparate impact. *Big Data*, 5(2), 153-163. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
