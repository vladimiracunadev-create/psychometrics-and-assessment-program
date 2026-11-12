# 177 — Funcionamiento diferencial del ítem en la práctica

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 063 y 053.

## Objetivos

1. Distinguir DIF uniforme y no uniforme.
2. Comparar Mantel–Haenszel con la regresión logística.
3. Elegir el método según el tipo de DIF sospechado.

## Fundamentos

El **DIF uniforme** desplaza la curva del ítem de un grupo (la diferencia no depende del nivel de habilidad); el **no uniforme** cambia su pendiente (las curvas se cruzan). Mantel–Haenszel (Holland y Thayer, 1988) está diseñado para DIF uniforme. La regresión logística (Swaminathan y Rogers, 1990) ajusta ítem ~ total + grupo + total×grupo y permite contrastar ambos tipos (Zumbo, 1999).

Laboratorio (20 ítems, 2 grupos de 600, 40 réplicas; un ítem con y sin DIF; criterio interno = total sin el ítem):

| Escenario | MH (1 gl) | RL con interacción (2 gl) | RL solo grupo |
|---|---:|---:|---:|
| Sin DIF | 0 % | 5 % | 0 % |
| Uniforme | 100 % | 100 % | 100 % |
| No uniforme | 10 % | 95 % | 10 % |

## Ejemplo resuelto

Con DIF no uniforme el grupo focal rinde mejor en habilidad baja y peor en alta (o al revés); el efecto promedio del grupo es cercano a 0 y MH no lo ve.

## Errores y límites

- Usar MH y concluir «no hay DIF» sin considerar el no uniforme.
- Eliminar ítems por significación estadística sin revisar la magnitud ni el contenido.
- Muestras pequeñas: poca potencia.
- Pocas réplicas (40): las tasas son aproximadas.

## Ejercicios

- **Inicial.** ¿Qué es el DIF no uniforme?
- **Intermedio.** ¿Qué gl tiene la prueba conjunta de grupo e interacción? 2.
- **Avanzado.** Aumenta el DIF uniforme (shift 0,3) y estima la potencia.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/177-funcionamiento-diferencial-del-item-en-la-practica/lab.py
```

## Autoevaluación y criterios

1. ¿Qué haces con un ítem con DIF? 2. ¿Cómo eliges el grupo focal? 3. ¿Cómo informas la magnitud?
Se logra si el estudiante selecciona el método según el DIF y distingue significación de magnitud.

## Bibliografía

- Holland, P. W., & Thayer, D. T. (1988). Differential item performance and the Mantel-Haenszel procedure. En H. Wainer & H. I. Braun (Eds.), *Test Validity*. Lawrence Erlbaum. ⚠️ existe, pero Crossref registra 2013 (¿otra edición?; [DOI](https://doi.org/10.4324/9780203056905-19))
- Swaminathan, H., & Rogers, H. J. (1990). Detecting differential item functioning using logistic regression procedures. *Journal of Educational Measurement*, 27(4), 361-370. ✅ [DOI](https://doi.org/10.1111/j.1745-3984.1990.tb00754.x)
- Zumbo, B. D. (1999). *A Handbook on the Theory and Methods of Differential Item Functioning (DIF)*. National Defense Headquarters, Ottawa. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
