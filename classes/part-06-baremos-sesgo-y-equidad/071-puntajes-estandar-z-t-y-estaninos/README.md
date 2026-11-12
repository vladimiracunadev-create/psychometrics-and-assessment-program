# 071 — Puntajes estándar: z, T y estaninos

> [Índice de la parte](../README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 3 h · Estado `escrita`
**Prerrequisitos:** clase 031.

## Objetivos

1. Convertir un bruto a z, T y estanino.
2. Distinguir la transformación lineal de la normalizada.
3. Decidir cuándo normalizar y cómo declararlo.

## Fundamentos

- **Lineal:** z = (x − M)/DE; T = 50 + 10z; estanino ≈ 5 + 2z (acotado a 1–9). Conserva la forma de la distribución.
- **Normalizada (de área):** bruto → rango percentil → cuantil de la normal → escala deseada. Fuerza forma normal.
- **Estaninos por percentil acumulado:** cortes en 4, 11, 23, 40, 60, 77, 89 y 96 %.

Laboratorio (prueba fácil con techo, media 32,9 y DE 5,4):

| Bruto | Percentil | T lineal | T normalizado | Estanino lineal | Estanino normalizado |
|---:|---:|---:|---:|---:|---:|
| 20 | 2,4 | 26,0 | 30,1 | 1 | 1 |
| 34 | 50,2 | 52,0 | 50,0 | 5 | 5 |
| 38 | 81,9 | 59,5 | 59,1 | 7 | 7 |
| 40 | 97,8 | 63,2 | 70,1 | 8 | 9 |

La diferencia aparece en la cola larga: el puntaje máximo es T = 63 lineal o 70 normalizado.

## Ejemplo resuelto

z = −1 → T = 40; estanino lineal = 5 − 2 = 3. Percentil 84 → z = 1 → T = 60.

## Errores y límites

- Normalizar sin justificar que el rasgo sea normal: una asimetría puede ser real.
- Comparar T de pruebas con transformaciones distintas.
- Informar estaninos como si tuvieran precisión de puntaje bruto: agrupan.
- Los estaninos esconden diferencias pequeñas; es una ventaja cuando la medida es imprecisa (clase 015).

## Ejercicios

- **Inicial.** ¿Qué puntaje T equivale al percentil 50 normalizado? → 50.
- **Intermedio.** z = 1,5 → T = 65; estanino = 8.
- **Avanzado.** Cambia la forma de la distribución en `lab.py` a una asimétrica positiva y compara las dos transformaciones.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/071-puntajes-estandar-z-t-y-estaninos/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo normalizar? 2. ¿Qué cambia en la cola? 3. ¿Cómo se declara en el manual?
Se logra si el estudiante transforma y justifica la elección.

## Bibliografía

- Angoff, W. H. (1984). *Scales, Norms, and Equivalent Scores*. Educational Testing Service. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Anastasi, A., & Urbina, S. (1997). *Psychological Testing* (7.ª ed.). Prentice Hall. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
