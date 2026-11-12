# 064 — Análisis de redes psicométricas

> [Índice de la parte](../README.md)

**Parte 04 — Estructura y análisis factorial** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 021 y 052.

## Objetivos

1. Distinguir correlación marginal de correlación parcial.
2. Interpretar una red de correlaciones parciales.
3. Reconocer los límites causales y de estimación de las redes.

## Fundamentos

Una red psicométrica (Borsboom y Cramer, 2013) representa variables como nodos y asociaciones **condicionales** (parciales) como aristas. A diferencia del modelo factorial, no postula una causa común latente. La correlación parcial entre A y C dado el resto se obtiene de la inversa de R: p_ij = −P_ij / √(P_ii·P_jj).

Laboratorio: cadena A → B → C → D (cada eslabón r ≈ 0,6), N = 5 000:

| Par | Correlación marginal | Parcial |
|---|---:|---:|
| A–B | 0,61 | 0,53 |
| A–C | 0,36 | −0,00 |
| A–D | 0,19 | −0,01 |
| B–C | 0,59 | 0,44 |
| B–D | 0,32 | −0,03 |
| C–D | 0,59 | 0,53 |

Las parciales recuperan la cadena; las marginales sugieren aristas espurias.

## Ejemplo resuelto

r_AB = 0,6; r_BC = 0,6; r_AC = 0,36: parcial(A,C | B) = (0,36 − 0,36)/√(0,64·0,64) = 0.

## Errores y límites

- Leer una arista como causalidad o la centralidad como «importancia» sin estudio de estabilidad.
- Estimar redes con muestras pequeñas sin regularización: las parciales son ruidosas (Epskamp y Fried, 2018); aquí no se regulariza.
- Comparar redes entre grupos sin pruebas formales.
- Epskamp, Borsboom y Fried (2018): reportar precisión de aristas y estabilidad.

## Ejercicios

- **Inicial.** ¿Qué indica una arista con parcial 0?
- **Intermedio.** ¿Por qué A y C correlacionan 0,36 si no están conectados directamente? Por B (mediación).
- **Avanzado.** Añade en `lab.py` una causa común E que afecta a A y D y observa la red.

## Laboratorio

```bash
python classes/part-04-estructura-y-analisis-factorial/064-analisis-de-redes-psicometricas/lab.py
```

## Autoevaluación y criterios

1. ¿Qué responde una red que no responde un modelo factorial? 2. ¿Qué no puede responder? 3. ¿Qué precauciones usas con n pequeño?
Se logra si el estudiante calcula parciales e interpreta la red con cautela causal.

## Bibliografía

- Borsboom, D., & Cramer, A. O. J. (2013). Network analysis: An integrative approach to the structure of psychopathology. *Annual Review of Clinical Psychology*, 9, 91-121. ✅ [DOI](https://doi.org/10.1146/annurev-clinpsy-050212-185608)
- Epskamp, S., & Fried, E. I. (2018). A tutorial on regularized partial correlation networks. *Psychological Methods*, 23(4), 617-634. ✅ [DOI](https://doi.org/10.1037/met0000167)
- Epskamp, S., Borsboom, D., & Fried, E. I. (2018). Estimating psychological networks and their accuracy. *Behavior Research Methods*, 50(1), 195-212. ✅ [DOI](https://doi.org/10.3758/s13428-017-0862-1)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
