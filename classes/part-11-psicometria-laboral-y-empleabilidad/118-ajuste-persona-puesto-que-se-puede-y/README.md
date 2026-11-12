# 118 — Ajuste persona-puesto: qué se puede y qué no afirmar

![Portada de la clase 118](portada.svg)

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 031, 074 y 112.

## Objetivos

1. Calcular distintos índices de ajuste y compararlos.
2. Demostrar que un «porcentaje de ajuste» depende de la fórmula elegida.
3. Formular reglas para no inventar porcentajes ni pesos.

## Fundamentos

El ajuste persona-puesto compara el perfil de una persona con el requerido. Existen muchos índices de similitud de perfiles y la elección **cambia** las conclusiones (Edwards, 1993). Un metaanálisis encuentra asociaciones del ajuste con actitudes y desempeño, de magnitud variable según el tipo de ajuste y de medida (Kristof-Brown, Zimmerman y Johnson, 2005). Un «porcentaje» solo tiene sentido si se calibró contra un criterio.

Laboratorio (perfil requerido de 8 competencias; 3 candidatos):

| Candidato | A: distancia | B: % que cumple | C: correlación |
|---|---:|---:|---:|
| Ana | 76 | 75 | 83 |
| Beto | 76 | 88 | 88 |
| Carla | 60 | 0 | 96 |

Los órdenes difieren: A: Ana > Beto > Carla; B: Beto > Ana > Carla; C: Carla > Beto > Ana. Carla obtiene 60, 0 o 96 puntos de ajuste según el índice.

## Ejemplo resuelto

El índice C (correlación) mide *forma* del perfil, no nivel: un candidato con competencias bajas pero proporcionales al requerido parece «muy ajustado».

## Errores y límites

- Presentar «85 % de ajuste» como probabilidad de éxito.
- Ponderar competencias sin evidencia ni justificación.
- Comparar candidatos con índices distintos entre puestos.
- Lo defendible: mostrar qué competencias se cumplen y con qué margen y usar el ajuste como insumo de una conversación.

## Ejercicios

- **Inicial.** ¿Qué mide el índice B?
- **Intermedio.** Calcula el índice B de un candidato que cumple 5 de 8 → 62,5 %.
- **Avanzado.** Define un índice D con pesos y discute cómo lo validarías.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/118-ajuste-persona-puesto-que-se-puede-y/lab.py
```

## Autoevaluación y criterios

1. ¿Qué estudio necesitas para calibrar un porcentaje? 2. ¿Qué información mostrarías en lugar de un porcentaje? 3. ¿Cómo evitar discriminación por «ajuste»?
Se logra si el estudiante muestra la dependencia del índice y propone un informe sin porcentajes inventados.

## Bibliografía

- Edwards, J. R. (1993). Problems with the use of profile similarity indices in the study of congruence in organizational research. *Personnel Psychology*, 46(3), 641-665. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.1993.tb00889.x)
- Kristof-Brown, A. L., Zimmerman, R. D., & Johnson, E. C. (2005). Consequences of individuals' fit at work. *Personnel Psychology*, 58(2), 281-342. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
