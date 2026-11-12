# 120 — Impacto adverso y defensa legal de una decisión de selección

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 035, 068 y 112.

> Material educativo, **no asesoría jurídica**. El marco chileno (principio de no discriminación laboral del Código del Trabajo y normas conexas) se consulta en su texto vigente (bcn.cl) con un profesional del derecho.

## Objetivos

1. Calcular razón de tasas y significación (Fisher exacto).
2. Distinguir alerta estadística de conclusión de discriminación.
3. Organizar la documentación que respalda un proceso.

## Fundamentos

La «regla de los cuatro quintos» (razón de tasas < 0,80) proviene de las *Uniform Guidelines* de EE. UU. (1978) y se usa como **alerta** orientativa; **no** es norma chilena. Para ver si la diferencia es compatible con el azar se usa una prueba de significación (Fisher exacto, bilateral) o intervalos para la razón (Morris y Lobsenz, 2000). Ninguna de las dos concluye por sí sola que haya discriminación: importa si el proceso está justificado por el puesto (validez) y si existen alternativas con menor impacto.

Laboratorio:

| Escenario | Tasa G1 | Tasa G2 | Razón | Alerta 4/5 | p (Fisher) |
|---|---:|---:|---:|---|---:|
| n = 20 y 20 | 0,450 | 0,300 | 0,67 | SÍ | 0,5145 |
| n = 100 y 100 | 0,450 | 0,300 | 0,67 | SÍ | 0,0405 |
| n = 3 000 y 3 000 | 0,500 | 0,450 | 0,90 | no | 0,0001 |
| n = 300 y 300 | 0,300 | 0,300 | 1,00 | no | 1,0000 |

## Ejemplo resuelto

Con n = 20 por grupo, 9 de 20 frente a 6 de 20: la razón es 0,67 pero p = 0,51, plenamente compatible con el azar.

## Errores y límites

- Declarar discriminación solo por una razón < 0,80 (o descartarla solo por p > 0,05).
- Ignorar que con muestras grandes diferencias pequeñas son «significativas».
- No monitorear el impacto del proceso en el tiempo.
- Documentación esencial: análisis del puesto, evidencia de validez, decisiones de corte, alternativas consideradas.

## Ejercicios

- **Inicial.** ¿Qué dice la regla de los 4/5?
- **Intermedio.** Tasas 0,60 y 0,50 → razón 0,83; ¿alerta? No.
- **Avanzado.** Calcula el p de Fisher para 12/40 frente a 6/40 en `lab.py`.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/120-impacto-adverso-y-defensa-legal-de-una/lab.py
```

## Autoevaluación y criterios

1. ¿Qué diferencia hay entre impacto adverso y discriminación? 2. ¿Qué documentación conservarías? 3. ¿A quién consultarías?
Se logra si el estudiante calcula e interpreta los indicadores sin sobreafirmar.

## Bibliografía

- Uniform Guidelines on Employee Selection Procedures (1978), 29 CFR Part 1607 (EE. UU.). 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Morris, S. B., & Lobsenz, R. E. (2000). Significance tests and confidence intervals for the adverse impact ratio. *Personnel Psychology*, 53(1), 89-111. ✅ [DOI](https://doi.org/10.1111/j.1744-6570.2000.tb00195.x)
- SIOP (2018). *Principles for the Validation and Use of Personnel Selection Procedures* (5.ª ed.). ⚠️ existe, pero Crossref registra 1975 (¿otra edición?; [DOI](https://doi.org/10.1037/e475802008-001))

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
