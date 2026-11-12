# 107 — Motivación, valores y preferencias

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 005, 008 y 024.

## Objetivos

1. Describir modelos de valores (Spranger, Schwartz).
2. Reconocer el efecto del estilo de respuesta en la estructura de valores.
3. Decidir entre puntaje bruto y centrado.

## Fundamentos

Spranger (1928) describió seis tipos de valor; Allport, Vernon y Lindzey (1960) los operacionalizaron; Schwartz (1992) propuso una estructura circular de valores universales con motivaciones compatibles adyacentes y opuestas enfrentadas. El **centrado por persona** (restar su media) corrige el estilo de respuesta que hace correlacionar positivamente todos los valores (Schwartz, 1992), pero vuelve los puntajes relativos y parcialmente ipsativos (clase 008). El instrumento `valores-spranger` del repositorio usa ítems propios y está sin validar.

Laboratorio (6 valores circulares, 4 000 personas, correlación media por distancia en el círculo):

| | Distancia 1 | Distancia 2 | Distancia 3 (opuestos) |
|---|---:|---:|---:|
| Sin corregir | 0,80 | 0,64 | 0,56 |
| Centrado por persona | 0,22 | −0,38 | −0,69 |

## Ejemplo resuelto

Persona con respuestas 5, 5, 4, 3, 3, 4: media 4; centradas 1, 1, 0, −1, −1, 0. Tras centrar, solo informa qué valora *más* que su propio promedio.

## Errores y límites

- Comparar el nivel absoluto de valores entre personas tras centrar.
- Interpretar «sin corregir» como estructura real.
- Reducir las motivaciones laborales a valores sin considerar contexto.
- Los resultados son de simulación.

## Ejercicios

- **Inicial.** ¿Qué corrige el centrado?
- **Intermedio.** Centra las respuestas 2, 3, 4, 5 → −1,5; −0,5; 0,5; 1,5.
- **Avanzado.** Incorpora un segundo estilo (extremismo) en `lab.py` y propón una corrección.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/107-motivacion-valores-y-preferencias/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo prefieres puntajes brutos? 2. ¿Cómo enseñarías la estructura circular? 3. ¿Qué limita su uso en selección?
Se logra si el estudiante corrige por estilo y explica el costo.

## Bibliografía

- Schwartz, S. H. (1992). Universals in the content and structure of values. *Advances in Experimental Social Psychology*, 25, 1-65. ✅ [DOI](https://doi.org/10.1016/s0065-2601(08)60281-6)
- Allport, G. W., Vernon, P. E., & Lindzey, G. (1960). *Study of Values* (3.ª ed.). Houghton Mifflin. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Spranger, E. (1928). *Types of Men*. Niemeyer. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
