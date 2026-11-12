# 063 — Funcionamiento diferencial del ítem (DIF)

![Portada de la clase 063](portada.svg)

<!-- NAV -->
[← 062 — La muestra normativa: a quién se compara la p…](../062-elegir-la-muestra-normativa/README.md) · [📚 Parte 06](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [064 — Sesgo predictivo y definiciones de equidad →](../064-sesgo-predictivo-y-equidad/README.md)
<!-- /NAV -->

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clases 015 y 052.

## Objetivos

1. Distinguir impacto de DIF.
2. Calcular el estadístico de Mantel-Haenszel y la clasificación ETS.
3. Decidir qué hacer con un ítem con DIF.

## Fundamentos

**Impacto:** los grupos difieren en el puntaje. **DIF:** a igual nivel del rasgo, los grupos difieren en la probabilidad de acierto de un ítem. El método de Mantel-Haenszel (Holland y Thayer, 1988) compara a personas con el mismo puntaje total:

```
α_MH = Σ(Aₛ·Dₛ/Tₛ) / Σ(Bₛ·Cₛ/Tₛ)          Δ_MH = −2,35·ln(α_MH)
```

Clasificación ETS (Zwick, 2012) por magnitud: A (|Δ| < 1), B (1 a 1,5), C (> 1,5, con significación). Se basa en el criterio interno (puntaje total), que puede contaminarse si hay muchos ítems con DIF.

Laboratorio (2 grupos, 20 ítems; grupo focal con habilidad −0,5; ítem 7 con DIF uniforme +0,8):

| Ítem | α_MH | Δ | χ² | Clase |
|---:|---:|---:|---:|---|
| 1 | 0,93 | 0,17 | 1,5 | A |
| 3 | 0,86 | 0,35 | 7,0 | A |
| **7** | **2,38** | **−2,03** | **281,3** | **C** |

Puntaje total medio: 10,1 (referencia) y 8,1 (focal) = impacto. Solo el ítem 7 se señala.

## Ejemplo resuelto

Estrato con A = 30, B = 20, C = 20, D = 30: α = (30·30)/(20·20) = 2,25; Δ = −2,35·ln 2,25 = −1,91 → magnitud C si es significativo.

## Errores y límites

- Eliminar automáticamente ítems con DIF: se revisa el contenido, la relevancia para el constructo y el efecto sobre el puntaje.
- Confundir DIF con diferencia de grupos.
- Usar MH con muestras pequeñas (poca potencia) o DIF no uniforme (requiere regresión logística u otro método).
- Un DIF «estadístico» puede ser irrelevante en lo práctico.

## Ejercicios

- **Inicial.** ¿Qué compara MH que no compara una diferencia de medias?
- **Intermedio.** α = 0,5: Δ = −2,35·ln 0,5 = 1,63 → C.
- **Avanzado.** Añade en `lab.py` un segundo ítem con DIF en dirección contraria y observa el efecto sobre el criterio interno.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/063-funcionamiento-diferencial-del-item/lab.py
```

## Autoevaluación y criterios

1. ¿Qué es impacto? 2. ¿Qué haces con un ítem C? 3. ¿Qué grupos eliges como focal y por qué?
Se logra si el estudiante distingue impacto de DIF y decide con criterio sustantivo.

## Bibliografía

- Mantel, N., & Haenszel, W. (1959). Statistical aspects of the analysis of data from retrospective studies of disease. *Journal of the National Cancer Institute*, 22(4), 719-748. ✅ [DOI](https://doi.org/10.1093/jnci/22.4.719)
- Holland, P. W., & Thayer, D. T. (1988). Differential item performance and the Mantel-Haenszel procedure. En H. Wainer & H. I. Braun (Eds.), *Test Validity*. Lawrence Erlbaum. ⚠️ existe, pero Crossref registra 2013 (¿otra edición?; [DOI](https://doi.org/10.4324/9780203056905-19))
- Zwick, R. (2012). *A Review of ETS Differential Item Functioning Assessment Procedures*. ETS Research Report RR-12-08. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 062 — La muestra normativa: a quién se compara la p…](../062-elegir-la-muestra-normativa/README.md)  
[📚 Parte 06](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[064 — Sesgo predictivo y definiciones de equidad →](../064-sesgo-predictivo-y-equidad/README.md)
<!-- /NAV -->
