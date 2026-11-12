# 139 — Cribado del neurodesarrollo: alcances y derivación

> [Índice de la parte](../README.md)

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 100 y 135.

## Objetivos

1. Calcular el valor predictivo de un cribado en dos etapas.
2. Reconocer el efecto del error compartido entre pruebas.
3. Diseñar una ruta de derivación con apoyos mientras se espera.

## Fundamentos

Un cribado en dos etapas (cuestionario breve → prueba directa) reduce derivaciones innecesarias. El cálculo habitual multiplica razones de verosimilitud suponiendo independencia entre pruebas; si comparten error (sueño, timidez, contexto), la segunda aporta menos (Glascoe, 2005). Un resultado positivo es «riesgo», y la evaluación diagnóstica corresponde a un equipo habilitado, con consentimiento de la familia (Lipkin y Macias, 2020).

Laboratorio (prevalencia 4 %; punto de corte 1,2 en ambas etapas):

| Peso del error compartido | VPP etapa 1 | VPP tras 2 etapas | VPP si independientes |
|---:|---:|---:|---:|
| 0,0 | 0,19 | 0,59 | 0,57 |
| 0,5 | 0,19 | 0,44 | 0,57 |
| 0,9 | 0,19 | 0,26 | 0,57 |

## Ejemplo resuelto

Odds previos = 0,04/0,96 = 0,042; razón de verosimilitud de cada etapa ≈ sens/FPR; con dos etapas independientes, odds = 0,042·RV² → VPP ≈ 0,57 en este diseño.

## Errores y límites

- Multiplicar razones de verosimilitud sin comprobar independencia.
- Perder niños entre etapas (seguimiento).
- Ruta de derivación sin tiempos ni apoyos intermedios.
- Datos sintéticos.

## Ejercicios

- **Inicial.** ¿Por qué un segundo cribado mejora el VPP?
- **Intermedio.** Con VPP 0,19 y una razón de verosimilitud 4: odds 0,235·4 = 0,94 → VPP 0,48.
- **Avanzado.** Cambia la prevalencia a 10 % en `lab.py`.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/139-cribado-del-neurodesarrollo-alcances-y-derivacion/lab.py
```

## Autoevaluación y criterios

1. ¿Qué apoyos das mientras esperan? 2. ¿Quién deriva y a quién? 3. ¿Cómo evalúas el programa de cribado?
Se logra si el estudiante evalúa una secuencia de cribado con supuestos explícitos.

## Bibliografía

- Glascoe, F. P. (2005). Screening for developmental and behavioral problems. *Mental Retardation and Developmental Disabilities Research Reviews*, 11(3), 173-179. ✅ [DOI](https://doi.org/10.1002/mrdd.20068)
- Lipkin, P. H., & Macias, M. M. (2020). Promoting optimal development. *Pediatrics*, 145(1), e20193449. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Streiner, D. L., & Norman, G. R. (2008). *Health Measurement Scales* (4.ª ed.). Oxford University Press. ✅ [DOI](https://doi.org/10.1093/acprof:oso/9780199231881.001.0001)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
