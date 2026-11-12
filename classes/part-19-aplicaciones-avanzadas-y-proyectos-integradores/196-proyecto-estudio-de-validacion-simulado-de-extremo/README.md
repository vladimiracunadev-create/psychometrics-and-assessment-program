# 196 — Proyecto: estudio de validación simulado de extremo a extremo

> [Índice de la parte](../README.md)

**Parte 19 — Aplicaciones avanzadas y proyectos integradores** · Nivel avanzado · 5 h · Estado `escrita`
**Prerrequisitos:** clase 180.

## Objetivos

1. Integrar diseño, datos, fiabilidad, validez e informe.
2. Comprobar que el estudio recupera la verdad simulada.
3. Revisar el informe con la lista de la clase 180.

## Fundamentos

Con datos sintéticos se conoce la verdad del modelo, de modo que se puede comprobar si el análisis la recupera. Se simula un factor de 10 ítems, dos aplicaciones y dos criterios (uno relacionado y uno ajeno).

Laboratorio (n = 300): alfa 0,85 con IC bootstrap [0,83; 0,87]; test-retest r = 0,84; validez convergente r = 0,36 y discriminante r = −0,07; omega teórico 0,88; el informe cumple 4 de 4 criterios de la lista de la clase 180.

## Ejemplo resuelto

El informe califica el «válido» como válido para describir el constructo en datos simulados, no para decisiones sobre personas reales, y declara sus limitaciones.

## Errores y límites

- Creer que el éxito en datos simulados prueba validez en personas.
- Omitir equidad e invarianza.
- El revisor solo comprueba la forma del informe.

## Ejercicios

- **Inicial.** ¿Qué ventaja tiene conocer la verdad simulada?
- **Intermedio.** Reduce a 5 ítems y observa alfa y su intervalo.
- **Avanzado.** Añade DIF por grupo simulado al estudio.

## Laboratorio

```bash
python classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/196-proyecto-estudio-de-validacion-simulado-de-extremo/lab.py
```

## Autoevaluación y criterios

1. ¿Qué decisión de este proyecto es la más discutible? 2. ¿Qué evidencia falta? 3. ¿Qué dato no deberías conservar?
Se logra si el estudiante ejecuta el proyecto, interpreta sus cifras con cautela y declara sus límites.

## Bibliografía

- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
- Appelbaum, M., et al. (2018). Journal article reporting standards for quantitative research in psychology. *American Psychologist*, 73(1), 3-25.
