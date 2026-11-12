# 131 — Hitos del desarrollo y sus rangos normales

![Portada de la clase 131](portada.svg)

> [Índice de la parte](../README.md)

**Parte 13 — Desarrollo infantil y evaluación psicoeducativa** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 061 y 100.

## Objetivos

1. Entender los hitos como distribuciones de edad, no como edades únicas.
2. Calcular la probabilidad de hallazgos aislados en una lista de verificación.
3. Interpretar patrones y trayectorias, no ítems sueltos.

## Fundamentos

Los hitos (sentarse, caminar, primeras palabras) se alcanzan en **ventanas** amplias y asimétricas (WHO Multicentre Growth Reference Study Group, 2006, para seis hitos motores). Una edad «promedio» no es un plazo. En una lista de *k* hitos, la probabilidad de que un niño típico tenga al menos uno por sobre el percentil 95 es 1 − 0,95ᵏ.

Laboratorio (hito simulado, mediana 12 meses; parámetros ilustrativos):

| Percentil | 1 | 5 | 50 | 95 | 99 |
|---|---:|---:|---:|---:|---:|
| Edad (meses) | 8,5 | 9,4 | 12,0 | 15,4 | 17,1 |

Niños sanos que aún no lo logran a los 14 meses: 15,4 %; a los 16 meses: 2,8 %. Con 10 hitos independientes, 40,4 % de los niños típicos tiene al menos uno «atrasado» (≥ 2: 8,8 %).

## Ejemplo resuelto

Con 10 hitos: 1 − 0,95¹⁰ = 0,401.

## Errores y límites

- Tomar la mediana como fecha límite.
- Derivar por un solo hito sin considerar el patrón global.
- Aplicar ventanas de otra población o cultura sin evidencia.
- Los parámetros del laboratorio son ilustrativos; las ventanas reales se consultan en las fuentes.

## Ejercicios

- **Inicial.** ¿Por qué la distribución es asimétrica?
- **Intermedio.** 1 − 0,95⁶ = 0,265 con 6 hitos.
- **Avanzado.** Usa σ = 0,25 en `lab.py` y describe el cambio de la ventana.

## Laboratorio

```bash
python classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/131-hitos-del-desarrollo-y-sus-rangos-normales/lab.py
```

## Autoevaluación y criterios

1. ¿Qué dirías a una familia preocupada por un solo hito? 2. ¿Qué es vigilancia del desarrollo? 3. ¿Cuándo derivarías?
Se logra si el estudiante interpreta hitos como rangos y calcula el efecto de revisar muchos.

## Bibliografía

- WHO Multicentre Growth Reference Study Group (2006). WHO Motor Development Study: Windows of achievement for six gross motor development milestones. *Acta Paediatrica*, Suppl. 450, 86-95. ⚠️ existe, pero Crossref registra 2006 (¿otra edición?; [DOI](https://doi.org/10.1111/j.1651-2227.2006.tb02379.x))
- Lipkin, P. H., & Macias, M. M. (2020). Promoting optimal development: Identifying infants and young children with developmental disorders through developmental surveillance and screening. *Pediatrics*, 145(1), e20193449. ✅ [DOI](https://doi.org/10.1542/9781610025034-part03-promoting)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
