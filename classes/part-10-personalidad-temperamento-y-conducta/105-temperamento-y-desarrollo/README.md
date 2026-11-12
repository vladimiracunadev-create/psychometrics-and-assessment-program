# 105 — Temperamento y desarrollo

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 024 y 039.

## Objetivos

1. Distinguir estabilidad de rango y estabilidad absoluta.
2. Interpretar un patrón simplex.
3. Corregir por atenuación el efecto del error de medida.

## Fundamentos

El temperamento (diferencias tempranas de reactividad y autorregulación; Thomas y Chess, 1977; Rothbart y Bates, 2006) muestra estabilidad moderada que **decae con el intervalo**: patrón *simplex*. La consistencia de rango (orden relativo de las personas) aumenta con la edad (Roberts y DelVecchio, 2000). La correlación observada subestima la estabilidad por el error de medida.

Laboratorio (rasgo autorregresivo con paso 0,85 por intervalo de 2 años; fiabilidad 0,80; N = 5 000):

| Distancia (pasos) | r observada | r verdadera | Corregida (obs/fiab.) |
|---:|---:|---:|---:|
| 1 | 0,683 | 0,850 | 0,853 |
| 2 | 0,572 | 0,722 | 0,714 |
| 3 | 0,470 | 0,614 | 0,587 |
| 4 | 0,400 | 0,522 | 0,500 |

Las cifras son del modelo, no estimaciones del temperamento real.

## Ejemplo resuelto

Con r observada = 0,57 y fiabilidad 0,80: corregida = 0,57/0,80 = 0,71, cercana a la verdadera 0,72.

## Errores y límites

- Interpretar baja estabilidad observada como «el niño cambió» sin descontar el error.
- Etiquetar tempranamente a un niño por un puntaje de temperamento.
- Usar la misma escala en edades distintas sin evidencia de equivalencia (clase 070).
- Informantes (padres, docentes) agregan sesgos propios.

## Ejercicios

- **Inicial.** ¿Qué es un patrón simplex?
- **Intermedio.** Si el paso es 0,9, ¿cuál es la estabilidad verdadera a 3 pasos? 0,9³ = 0,729.
- **Avanzado.** Baja la fiabilidad a 0,6 en `lab.py` y observa las correlaciones observadas.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/105-temperamento-y-desarrollo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué implica la estabilidad moderada para el uso de predicciones tempranas? 2. ¿Cómo comunicarías esto a una familia? 3. ¿Qué diseño separa error de cambio?
Se logra si el estudiante interpreta estabilidad corrigiendo por error de medida.

## Bibliografía

- Thomas, A., & Chess, S. (1977). *Temperament and Development*. Brunner/Mazel. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Rothbart, M. K., & Bates, J. E. (2006). Temperament. En N. Eisenberg (Ed.), *Handbook of Child Psychology* (6.ª ed., Vol. 3). Wiley. ✅ [DOI](https://doi.org/10.1002/9780470147658.chpsy0303)
- Roberts, B. W., & DelVecchio, W. F. (2000). The rank-order consistency of personality traits from childhood to old age. *Psychological Bulletin*, 126(1), 3-25. ✅ [DOI](https://doi.org/10.1037/0033-2909.126.1.3)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
