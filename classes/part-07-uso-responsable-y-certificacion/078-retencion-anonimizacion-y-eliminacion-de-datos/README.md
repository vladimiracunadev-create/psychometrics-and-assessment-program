# 078 — Retención, anonimización y eliminación de datos

![Portada de la clase 078](portada.svg)

<!-- NAV -->
[← 077 — Consentimiento informado y confidencialidad](../077-consentimiento-informado-y-confidencialidad/README.md) · [📚 Parte 07](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [079 — Decisiones automatizadas y derecho a explicac… →](../079-decisiones-automatizadas-y-derecho-a-explicacion/README.md)
<!-- /NAV -->

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clases 076 y 077.

## Objetivos

1. Explicar por qué quitar el nombre no anonimiza.
2. Calcular k-anonimato y el porcentaje de personas únicas.
3. Diseñar una política de retención y eliminación.

## Fundamentos

Los **cuasi-identificadores** (edad, comuna, sexo, fecha) combinados pueden singularizar a una persona. El **k-anonimato** (Sweeney, 2002) exige que cada combinación de cuasi-identificadores se comparta con al menos *k* personas. La generalización (tramos de edad, macrozonas) aumenta *k* a costa de resolución. Los datos seudonimizados siguen siendo personales mientras la reidentificación sea razonablemente posible (Ohm, 2010; Rocher et al., 2019 estiman riesgos altos con pocos atributos).

Laboratorio (2 000 personas sintéticas, 3 cuasi-identificadores):

| Generalización | k | Únicos | Grupos < 5 |
|---|---:|---:|---:|
| Ninguna (edad, comuna, sexo) | 1 | 61,5 % | 99,8 % |
| Edad en tramos de 10 | 1 | 3,6 % | 32,3 % |
| Tramos de 10 + macrozona | 3 | 0,0 % | 1,4 % |
| Tramos de 20 + macrozona | 4 | 0,0 % | 0,4 % |

## Ejemplo resuelto

Con 40 comunas, 53 edades y 2 sexos hay 4 240 combinaciones para 2 000 personas: la mayoría quedan solas. Generalizando a 4 zonas, 4 tramos y 2 sexos hay 32 combinaciones: grupos de ~60.

## Errores y límites

- Suponer que un conjunto «sin nombre» es anónimo.
- Publicar tablas con celdas pequeñas.
- Conservar datos «para siempre»: la política debe fijar plazos y eliminación segura.
- k-anonimato no protege frente a inferencia de atributos (todos los de un grupo con el mismo diagnóstico).

## Ejercicios

- **Inicial.** ¿Qué es un cuasi-identificador?
- **Intermedio.** Calcula combinaciones posibles con 5 tramos de edad, 10 zonas y 2 sexos → 100.
- **Avanzado.** Aplica supresión de celdas < 5 en `lab.py` y reporta cuántas personas se pierden.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/078-retencion-anonimizacion-y-eliminacion-de-datos/lab.py
```

## Autoevaluación y criterios

1. ¿Qué plazo de retención justificarías para resultados de un diagnóstico escolar? 2. ¿Cómo eliminas un dato de un respaldo? 3. ¿Cómo evalúas el riesgo antes de publicar?
Se logra si el estudiante mide riesgo de reidentificación y propone generalización y plazos.

## Bibliografía

- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(5), 557-570. ✅ [DOI](https://doi.org/10.1142/s0218488502001648)
- Ohm, P. (2010). Broken promises of privacy. *UCLA Law Review*, 57, 1701-1777. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Rocher, L., Hendrickx, J. M., & de Montjoye, Y.-A. (2019). Estimating the success of re-identifications in incomplete datasets using generative models. *Nature Communications*, 10, 3069. ✅ [DOI](https://doi.org/10.1038/s41467-019-10933-3)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 077 — Consentimiento informado y confidencialidad](../077-consentimiento-informado-y-confidencialidad/README.md)  
[📚 Parte 07](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[079 — Decisiones automatizadas y derecho a explicac… →](../079-decisiones-automatizadas-y-derecho-a-explicacion/README.md)
<!-- /NAV -->
