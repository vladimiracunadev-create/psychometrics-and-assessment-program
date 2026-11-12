# 102 — Banco IPIP: historia y uso abierto

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 005 y 101.

## Objetivos

1. Explicar qué es el International Personality Item Pool (IPIP) y por qué es de dominio público.
2. Auditar la clave de un instrumento real del repositorio.
3. Distinguir «usable» de «validado».

## Fundamentos

El IPIP (Goldberg, 1999; Goldberg et al., 2006) es una colección de ítems y escalas de personalidad de **dominio público**: se pueden usar, traducir y adaptar sin permiso ni pago (la fuente primaria es ipip.ori.org). El IPIP-NEO-120 (Johnson, 2014) mide 30 facetas con 4 ítems cada una. En este repositorio el banco está en `instruments/ipip-neo-120.yaml` con licencia `dominio-publico`.

Laboratorio (estructura real del YAML, 120 ítems y 35 escalas): puntaje de una persona que responde siempre 5, con reflejo de invertidos:

| Faceta | Ítems | Invertidos | Todo 5 | Todo 3 | Todo 1 |
|---|---:|---:|---:|---:|---:|
| A1 | 4 | 1 | 4,00 | 3,00 | 2,00 |
| A2 | 4 | 4 | 1,00 | 3,00 | 5,00 |
| C1 | 4 | 0 | 5,00 | 3,00 | 1,00 |
| N1 | 4 | 0 | 5,00 | 3,00 | 1,00 |
| E1 | 4 | 2 | 3,00 | 3,00 | 3,00 |

Desvío medio de las facetas respecto del punto medio ante aquiescencia pura: 0,97. **El IPIP-NEO-120 no tiene clave equilibrada dentro de cada faceta.**

## Ejemplo resuelto

Persona que marca 5 en todo: N1 (todo directo) → 5,0; A2 (todo invertido) → 1,0. Un perfil así parece «muy neurótica y muy poco amable» solo por estilo de respuesta.

## Errores y límites

- Creer que «dominio público» significa «validado» o «con normas».
- Reportar puntajes de faceta con 4 ítems como si fueran precisos.
- Ignorar que las versiones traducidas necesitan su propia evidencia (clase 035).
- Respetar siempre la procedencia y cita del banco (`procedencia` en el YAML).

## Ejercicios

- **Inicial.** ¿Qué licencia tiene el IPIP?
- **Intermedio.** ¿Qué puntaje da «todo 5» en una faceta con 2 directos y 2 invertidos? 3,0.
- **Avanzado.** Calcula el desvío medio por dominio (no por faceta) y compara con el de facetas.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/102-banco-ipip-historia-y-uso-abierto/lab.py
```

## Autoevaluación y criterios

1. ¿Qué significa «uso abierto»? 2. ¿Qué evidencia local reunirías antes de usarlo en un proceso con consecuencias? 3. ¿Cómo mitigarías la aquiescencia?
Se logra si el estudiante audita la clave y distingue lo abierto de lo validado.

## Bibliografía

- Goldberg, L. R. (1999). A broad-bandwidth, public domain, personality inventory measuring the lower-level facets of several five-factor models. En I. Mervielde et al. (Eds.), *Personality Psychology in Europe* (Vol. 7). Tilburg University Press. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Goldberg, L. R., et al. (2006). The International Personality Item Pool and the future of public-domain personality measures. *Journal of Research in Personality*, 40(1), 84-96. ✅ [DOI](https://doi.org/10.1016/j.jrp.2005.08.007)
- Johnson, J. A. (2014). Measuring thirty facets of the Five Factor Model with a 120-item public domain inventory: Development of the IPIP-NEO-120. *Journal of Research in Personality*, 51, 78-89. ✅ [DOI](https://doi.org/10.1016/j.jrp.2014.05.003)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
