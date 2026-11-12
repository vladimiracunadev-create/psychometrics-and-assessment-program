# 178 — Reproducibilidad: preregistro, datos y código

> [Índice de la parte](../README.md)

**Parte 17 — Investigación psicométrica y análisis de datos** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 171 y 173.

## Objetivos

1. Verificar la reproducibilidad con huellas criptográficas.
2. Reconocer las fuentes de no reproducibilidad (semilla, orden, entorno).
3. Preparar un registro de investigación reutilizable.

## Fundamentos

La investigación reproducible incluye plan previo (**preinscripción**; Nosek et al., 2018), datos (o su generador) y código compartidos con principios FAIR (Wilkinson et al., 2016), semilla, y registro del entorno (Peng, 2011). Una verificación simple: ejecutar dos veces y comparar la huella (SHA-256) del resultado. Este repositorio lo aplica en su CI: regenera los bancos IPIP y exige que el árbol quede limpio.

Laboratorio:

| Situación | Resultado |
|---|---|
| Semilla fija, estructuras ordenadas | 3 huellas idénticas (852ffb6b…) |
| Sin semilla | 3 huellas distintas |
| Semilla fija con iteración sobre un `set` | el orden puede variar entre procesos |

Entorno registrado: versión de Python y plataforma.

## Ejemplo resuelto

`json.dumps(resultado, sort_keys=True)` fija el orden de las claves antes de calcular la huella: sin eso, dos diccionarios iguales podrían serializarse distinto.

## Errores y límites

- Confiar solo en la semilla.
- No registrar las versiones de las librerías.
- Compartir datos con identificadores (clase 078): se comparten datos anonimizados o sintéticos.
- La reproducibilidad no garantiza que el análisis sea correcto.

## Ejercicios

- **Inicial.** ¿Qué es la preinscripción?
- **Intermedio.** ¿Por qué ordenar las claves antes del hash? Para obtener una serialización determinista.
- **Avanzado.** Añade al laboratorio un archivo `requirements` fijado con hashes y verifícalo.

## Laboratorio

```bash
python classes/part-17-investigacion-psicometrica-y-analisis-de-datos/178-reproducibilidad-preregistro-datos-y-codigo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué incluirías en un paquete de reproducibilidad? 2. ¿Qué datos no puedes compartir? 3. ¿Cómo declararías análisis exploratorios?
Se logra si el estudiante verifica reproducibilidad y documenta el entorno.

## Bibliografía

- Nosek, B. A., et al. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. ✅ [DOI](https://doi.org/10.1073/pnas.1708274114)
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. ⚠️ existe, pero Crossref registra 2018 (¿otra edición?; [DOI](https://doi.org/10.3410/f.726216348.793543848))
- Peng, R. D. (2011). Reproducible research in computational science. *Science*, 334, 1226-1227. ✅ [DOI](https://doi.org/10.1126/science.1213847)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
