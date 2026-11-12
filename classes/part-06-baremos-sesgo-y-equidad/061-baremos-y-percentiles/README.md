# 061 — Baremos, percentiles y puntajes tipificados

> [Índice de la parte](../README.md) · [Siguiente](../062-elegir-la-muestra-normativa/README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 004, 025 y 026.

## Objetivos

1. Calcular rango percentil, z y T desde una muestra normativa.
2. Explicar por qué los percentiles no son equidistantes.
3. Estimar la incertidumbre del propio baremo.

## Fundamentos

Un **baremo** (norma) traduce un puntaje bruto a la posición de la persona respecto de un grupo de referencia. Rango percentil: porcentaje del grupo por debajo (con la mitad de los empates). z = (x − media)/DE; T = 50 + 10z. Los percentiles son ordinales: sirven para ordenar, no para sumar.

Laboratorio (norma de 5 000 personas, media 100,2, DE 14,8):

| Bruto | Percentil | z | T |
|---:|---:|---:|---:|
| 70 | 2,2 | −2,03 | 29,7 |
| 100 | 49,9 | −0,01 | 49,9 |
| 115 | 84,0 | 1,00 | 60,0 |
| 130 | 97,7 | 2,01 | 70,1 |

Salto de percentil para la misma diferencia de 5 puntos brutos: 97 → 102 = 13,5; 127 → 132 = 2,0. Incertidumbre del percentil del puntaje 120: error típico 2,53 con n = 100 y 0,61 con n = 2 000.

## Ejemplo resuelto

z = 1,00 → percentil 84 → T = 60. Un salto de 5 puntos en el centro mueve el percentil mucho más que el mismo salto en una cola.

## Errores y límites

- Sumar o promediar percentiles.
- Reportar un percentil sin la muestra normativa (n, año, lugar, criterios).
- Aplicar un baremo a una población distinta de la normativa (clase 062).
- Tratar un baremo viejo como vigente: los baremos envejecen.

## Ejercicios

- **Inicial.** ¿Qué T corresponde a z = −1? → 40.
- **Intermedio.** Puntaje 118 con media 100 y DE 15 → z = 1,2; T = 62; percentil ≈ 88.
- **Avanzado.** Calcula el error típico del percentil para n = 500 en `lab.py`.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/061-baremos-y-percentiles/lab.py
```

## Autoevaluación y criterios

1. ¿Por qué un percentil exagera diferencias en el centro? 2. ¿Qué informa un manual normativo mínimo? 3. ¿Cómo comunicarías un percentil a una familia?
Se logra si el estudiante transforma puntajes y reporta la incertidumbre del baremo.

## Bibliografía

- Angoff, W. H. (1984). *Scales, Norms, and Equivalent Scores*. Educational Testing Service. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Anastasi, A., & Urbina, S. (1997). *Psychological Testing* (7.ª ed.). Prentice Hall. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Crocker, L., & Algina, J. (1986). *Introduction to Classical and Modern Test Theory*. Holt, Rinehart & Winston. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
