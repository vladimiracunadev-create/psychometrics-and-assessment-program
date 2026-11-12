# 080 — Seguridad de bancos de ítems y de resultados

![Portada de la clase 080](portada.svg)

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clases 060 y 077.

## Objetivos

1. Detectar la filtración de ítems con evidencia estadística.
2. Verificar la integridad de archivos con huellas SHA-256.
3. Distinguir integridad, confidencialidad y disponibilidad.

## Fundamentos

Un banco de ítems es un activo: si se filtra, los puntajes dejan de significar lo que significaban. Medidas: control de acceso, cifrado, rotación de ítems, límites de exposición (clase 060), marcas de agua, y detección estadística (Cizek y Wollack, 2017; Impara y Foster, 2006). La **tríada** seguridad de la información: confidencialidad, integridad, disponibilidad.

Laboratorio (1 000 examinados, 40 ítems; 25 % con acceso previo a 10 ítems filtrados):

| Medida | Valor |
|---|---:|
| Cambio medio de p en ítems no filtrados | +0,007 (DE 0,016) |
| Cambio medio de p en los 10 filtrados | +0,069 |
| Ítems marcados (> 3 DE) | 8 de 10 filtrados, 0 de los 30 restantes |

La detección no es perfecta (dos ítems filtrados, con p alta de partida, no se destacan). Además se genera un manifiesto SHA-256 de `instruments/*.yaml`; agregar un byte cambia la huella.

## Ejemplo resuelto

Un ítem pasa de p = 0,50 a 0,58 en un periodo en que los demás suben 0,01 ± 0,016: (0,08 − 0,01)/0,016 = 4,4 DE → se revisa.

## Errores y límites

- Interpretar todo aumento de p como filtración (puede ser aprendizaje o cambio de población).
- Creer que el hash protege el contenido: solo detecta modificaciones.
- Almacenar claves de corrección junto al banco público.
- Un banco abierto (como los de este repositorio) no tiene este problema; los de alto impacto sí.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre integridad y confidencialidad?
- **Intermedio.** ¿Qué umbral usarías con 100 ítems para limitar falsos positivos? Justifícalo (p. ej. corrección por múltiples comparaciones).
- **Avanzado.** Añade un ítem filtrado que siempre se acierta y verifica su detección.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/080-seguridad-de-bancos-de-items-y-de/lab.py
```

## Autoevaluación y criterios

1. ¿Qué señales además de p indican filtración? (tiempos, patrones de respuesta) 2. ¿Cómo rotas ítems? 3. ¿Qué haces tras confirmar una filtración?
Se logra si el estudiante detecta anomalías y propone un plan de seguridad por capas.

## Bibliografía

- Cizek, G. J., & Wollack, J. A. (Eds.) (2017). *Handbook of Quantitative Methods for Detecting Cheating on Tests*. Routledge. ✅ [DOI](https://doi.org/10.4324/9781315743097)
- Impara, J. C., & Foster, D. (2006). Item and test development strategies to minimize test fraud. En S. M. Downing & T. M. Haladyna (Eds.), *Handbook of Test Development*. Lawrence Erlbaum. ⚠️ existe, pero Crossref registra None (¿otra edición?; [DOI](https://doi.org/10.4324/9780203874776.ch5))
- Way, W. D. (1998). Protecting the integrity of computerized testing item pools. *Educational Measurement: Issues and Practice*, 17(4), 17-27. ✅ [DOI](https://doi.org/10.1111/j.1745-3992.1998.tb00632.x)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
