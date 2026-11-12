# 062 — La muestra normativa: a quién se compara la persona

> [Índice de la parte](../README.md) · [Anterior](../061-baremos-y-percentiles/README.md) · [Siguiente](../063-funcionamiento-diferencial-del-item/README.md)

**Parte 06 — Baremos, sesgo y equidad** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clase 061.

## Objetivos

1. Explicar cómo la composición de la muestra normativa cambia el percentil de una persona.
2. Aplicar la reponderación por estratos (post-estratificación).
3. Listar lo que debe declarar la ficha de un baremo.

## Fundamentos

El baremo responde «¿comparado con quién?». Una muestra de conveniencia (voluntarios, una universidad) no representa a la población. Si se conocen los pesos reales de los estratos (educación, sexo, región), se puede **reponderar** cada observación por (peso poblacional del estrato)/(peso muestral) (post-estratificación; Lumley, 2010). Corrige la composición en esas variables, **no** otras diferencias entre la muestra y la población.

Laboratorio (3 niveles educativos 40/40/20 % en la población, 5/25/70 % en la muestra de conveniencia):

| Baremo | Percentil del puntaje 105 |
|---|---:|
| Poblacional | 64,7 |
| Conveniencia (universidad) | 41,5 |
| Conveniencia reponderada | 63,0 |

La misma persona queda «sobre la media» o «bajo la media» según con quién se la compare.

## Ejemplo resuelto

Estrato «superior»: 20 % en la población y 70 % en la muestra → peso 0,20/0,70 = 0,29 por observación. El estrato «básica»: 0,40/0,05 = 8,0.

## Errores y límites

- Reponderar con pocas observaciones por estrato (pesos extremos inestables).
- Creer que la reponderación vuelve representativa una muestra autoseleccionada.
- Usar normas de otro país o época sin evidencia de equivalencia (contexto chileno: no asumir equivalencia con normas extranjeras).
- Las *ITC Guidelines* piden documentar la muestra normativa (ITC, 2013).

## Ejercicios

- **Inicial.** Nombra cuatro datos obligatorios en la ficha de un baremo.
- **Intermedio.** Peso de un estrato con 30 % poblacional y 10 % muestral → 3,0.
- **Avanzado.** Cambia la composición de la muestra de conveniencia en `lab.py` y observa cuándo la reponderación falla.

## Laboratorio

```bash
python classes/part-06-baremos-sesgo-y-equidad/062-elegir-la-muestra-normativa/lab.py
```

## Autoevaluación y criterios

1. ¿Qué corrige y qué no la post-estratificación? 2. ¿Qué haces cuando no existe baremo local? 3. ¿Cómo informar a la persona evaluada?
Se logra si el estudiante compara baremos y declara las limitaciones de una norma.

## Bibliografía

- International Test Commission (2013). *ITC Guidelines on Test Use*. ITC. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Lumley, T. (2010). *Complex Surveys: A Guide to Analysis Using R*. Wiley. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
