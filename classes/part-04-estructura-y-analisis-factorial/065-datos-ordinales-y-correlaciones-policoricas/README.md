# 065 — Datos ordinales y correlaciones policóricas

> [Índice de la parte](../README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 007 y 052.

## Objetivos

1. Explicar por qué Pearson subestima el vínculo latente de variables ordinales.
2. Distinguir correlaciones tetracórica y policórica.
3. Reconocer los «factores de dificultad».

## Fundamentos

Si dos variables continuas se registran en pocas categorías, Pearson (phi, en el caso binario) subestima la correlación entre los rasgos latentes, y más cuanto más asimétricas las categorías. Ferguson (1941) describió el artefacto de **factores de dificultad**: ítems de dificultad similar se agrupan en un factor espurio. La **correlación tetracórica** (dos categorías) y la **policórica** (más; Olsson, 1979) estiman la correlación latente suponiendo normalidad bivariada. Flora y Curran (2004) muestran que estimadores para datos ordinales (p. ej. WLSMV) tienen ventajas con pocas categorías.

Laboratorio (correlación latente verdadera 0,60; N = 60 000):

| Corte (z) | % de unos | Pearson/phi | Tetracórica (aprox.) |
|---:|---:|---:|---:|
| 0,0 | 50,2 % | 0,406 | 0,595 |
| 0,5 | 30,9 % | 0,401 | 0,622 |
| 1,0 | 16,0 % | 0,358 | 0,666 |
| 1,5 | 6,7 % | 0,293 | 0,734 |
| 2,0 | 2,4 % | 0,249 | 0,839 |

La aproximación (Bonett y Price, 2005) es buena en cortes centrales y burda en los extremos; la estimación correcta es por máxima verosimilitud.

## Ejemplo resuelto

Dicotomizar ambas variables en la mediana da, en teoría, phi = (2/π)·arcsen(ρ) = 0,637 · arcsen(0,6) = 0,41, coherente con el 0,406 observado: ya cuesta ~0,19 de correlación.

## Errores y límites

- Usar Pearson en ítems binarios o con 2–4 categorías sin considerar el artefacto.
- Aplicar policóricas con muestras pequeñas (inestables) o cuando la normalidad latente es inverosímil.
- Creer que la policórica «arregla» ítems malos.

## Ejercicios

- **Inicial.** ¿Por qué phi baja cuando los ítems son muy fáciles?
- **Intermedio.** Con 5 categorías simétricas, ¿esperas mayor o menor sesgo que con 2? Menor.
- **Avanzado.** Cambia RHO a 0,3 en `lab.py` y compara el sesgo relativo.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/065-datos-ordinales-y-correlaciones-policoricas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es un factor de dificultad? 2. ¿Qué supuesto exige la policórica? 3. ¿Cuándo basta Pearson?
Se logra si el estudiante elige el coeficiente según categorías y asimetría.

## Bibliografía

- Ferguson, G. A. (1941). The factorial interpretation of test difficulty. *Psychometrika*, 6(5), 323-329.
- Olsson, U. (1979). Maximum likelihood estimation of the polychoric correlation coefficient. *Psychometrika*, 44(4), 443-460.
- Flora, D. B., & Curran, P. J. (2004). An empirical evaluation of alternative methods of estimation for confirmatory factor analysis with ordinal data. *Psychological Methods*, 9(4), 466-491.
- Bonett, D. G., & Price, R. M. (2005). Inferential methods for the tetrachoric correlation coefficient. *Journal of Educational and Behavioral Statistics*, 30(2), 213-225.
