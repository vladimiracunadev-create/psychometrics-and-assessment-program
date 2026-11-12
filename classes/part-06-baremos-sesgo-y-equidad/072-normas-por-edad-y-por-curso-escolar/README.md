# 072 — Normas por edad y por curso escolar

> [Índice de la parte](../README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 031 y 071.

## Objetivos

1. Comparar normas por bandas y normalización continua.
2. Reconocer el «salto» artificial en los bordes de banda.
3. Distinguir norma por edad de norma por curso.

## Fundamentos

En infancia y adolescencia el rendimiento cambia con la edad. **Bandas:** un baremo por tramo (p. ej. por año). **Continua:** media (y DE) como función suave de la edad, con regresión (Zachary y Gorsuch, 1985; Oosterhuis, van der Ark y Sijtsma, 2016). Una **norma por curso** refleja instrucción recibida; una **por edad**, desarrollo: según el constructo conviene una u otra (o ambas).

Laboratorio (6–13 años, N = 3 000, media cuadrática, DE 6):

| Niño con bruto 30 | Banda | Continua |
|---|---:|---:|
| 6;11 | T = 76,0 | T = 70,1 |
| 7;00 | T = 62,2 | T = 69,0 |

Con bandas, dos niños casi de la misma edad difieren 14 puntos T solo por el lado del corte. Error de la media en el borde e = 7,0: bandas 4,17 y 4,14; continua 0,05.

## Ejemplo resuelto

Media real a los 7;0 = 10 + 9 − 0,45 = 18,55 → T = 50 + 10·(30 − 18,55)/6 = 69,1 (continua: 69,0). La banda de 6 años promedia ~14,4 en el borde: T = 50 + 10·(30 − 14,4)/6 = 76,0, es decir, 7 puntos T más solo por quedar en la banda anterior.

## Errores y límites

- Usar una banda ancha en una edad de cambio rápido.
- Extrapolar la curva fuera de la edad de la muestra normativa.
- Suponer que la DE no cambia con la edad.
- Aplicar una norma de otro curso o país a estudiantes chilenos sin evidencia de equivalencia.

## Ejercicios

- **Inicial.** ¿Qué es mejor para una prueba de lectura inicial: edad o curso?
- **Intermedio.** Si el rendimiento medio sube 5 puntos/año, ¿qué error introduce una banda anual a mitad de año? ≈ 2,5.
- **Avanzado.** Modifica la curva de `media_real` para un tramo plano y observa si la regresión cuadrática ajusta.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/072-normas-por-edad-y-por-curso-escolar/lab.py
```

## Autoevaluación y criterios

1. ¿Qué datos necesita una norma continua? 2. ¿Qué riesgo trae el ajuste paramétrico? 3. ¿Cómo decidirías edad o curso?
Se logra si el estudiante construye y compara ambas normas.

## Bibliografía

- Zachary, R. A., & Gorsuch, R. L. (1985). Continuous norming: Implications for the WAIS-R. *Journal of Clinical Psychology*, 41(1), 86-94.
- Oosterhuis, H. E. M., van der Ark, L. A., & Sijtsma, K. (2016). Sample size requirements for traditional and regression-based norms. *Assessment*, 23(2), 191-202.
