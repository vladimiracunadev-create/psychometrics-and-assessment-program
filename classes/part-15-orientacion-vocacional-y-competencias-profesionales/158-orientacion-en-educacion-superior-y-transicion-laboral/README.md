# 158 — Orientación en educación superior y transición laboral

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 034, 100 y 135.

## Objetivos

1. Evaluar un sistema de alerta temprana con AUC y calibración.
2. Auditar su desempeño por grupo.
3. Definir un uso de apoyo, no de etiquetado.

## Fundamentos

La deserción se relaciona con factores académicos y sociales (Tinto, 1993). Los modelos de alerta temprana tienen capacidad predictiva modesta (Bowers, Sprott y Taff, 2013) y pueden distribuir desigualmente cargas y errores (Barocas, Hardt y Narayanan, 2019). Se evalúan con AUC, calibración y tasas por grupo.

Laboratorio (6 000 estudiantes; regresión logística sin usar el grupo; alerta al 20 % de mayor riesgo; datos sintéticos):

| Medida | Valor |
|---|---:|
| Deserción observada / media predicha | 21,8 % / 21,8 % |
| AUC aproximado | 0,69 |

| Grupo | Deserción | Alertados | TPR | FPR |
|---|---:|---:|---:|---:|
| G0 | 14,6 % | 18,1 % | 0,37 | 0,15 |
| G1 | 32,2 % | 22,8 % | 0,39 | 0,15 |

Sin usar el grupo, TPR y FPR son parecidas, pero se alerta a más estudiantes de G1 y en ambos grupos se detectan solo ~4 de cada 10 desertores.

## Ejemplo resuelto

Con 1 000 estudiantes, 218 desertarán; el modelo detecta ≈ 0,38·218 = 83 y alerta a 200: 117 alertados no desertarán.

## Errores y límites

- Etiquetar a estudiantes como «de riesgo» en registros visibles.
- Usar la alerta sin una oferta de apoyo concreta.
- Calibrar en una cohorte y aplicar en otra sin reevaluar.
- Datos sintéticos; las causas de deserción reales son múltiples.

## Ejercicios

- **Inicial.** ¿Qué es la calibración?
- **Intermedio.** TPR 0,39 con 322 desertores en G1 → ≈ 126 detectados.
- **Avanzado.** Cambia el corte al 10 % superior y compara TPR y FPR.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/158-orientacion-en-educacion-superior-y-transicion-laboral/lab.py
```

## Autoevaluación y criterios

1. ¿Qué apoyos ofrecerías? 2. ¿Quién ve las alertas? 3. ¿Cómo evalúas si el apoyo funciona?
Se logra si el estudiante evalúa un modelo de alerta, lo audita por grupo y define un uso respetuoso.

## Bibliografía

- Tinto, V. (1993). *Leaving College: Rethinking the Causes and Cures of Student Attrition* (2.ª ed.). University of Chicago Press. ⚠️ existe, pero Crossref registra 1987 (¿otra edición?; [DOI](https://doi.org/10.2307/40250027))
- Bowers, A. J., Sprott, R., & Taff, S. A. (2013). Do we know who will drop out? *The High School Journal*, 96(2), 77-100. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*. fairmlbook.org. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
