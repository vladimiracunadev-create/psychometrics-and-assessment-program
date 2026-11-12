# Changelog

Todas las modificaciones relevantes de este proyecto se documentan aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el versionado sigue [SemVer](https://semver.org/lang/es/).

## [No publicado]

### Cambiado
- **Numeración consecutiva 001-200 en el orden de estudio.** Las clases 001-080 cambiaron de número (las partes 02 a 19 ya coincidían); el número anterior queda en `curriculum.yaml` (`id_original`). Se renombraron carpetas y se actualizaron las referencias cruzadas. Las entradas históricas de este archivo usan la numeración anterior. Se retiró `scripts/expand_curriculum.py` (habría regenerado la numeración antigua).

### Añadido
- **Currículo ampliado a 20 partes y 200 clases** (`scripts/expand_curriculum.py`,
  aditivo e idempotente). Las 40 clases originales conservan su identificador;
  las 160 nuevas (041-200) están **planificadas**, no escritas.
- **Catálogo ampliado** `catalogo/fichas.yaml`: 140 fichas documentales de
  instrumentos, familias y técnicas (8 familias A-H), incluidos 15 instrumentos
  laborales universales y las familias psicoeducativas. Todas `verificado: false`
  salvo los 5 instrumentos implementados; ninguna validada.
- Módulo `psychometrics.fichas` con validación de estados, licencias y
  consistencia con `instruments/`, y pruebas (`test_fichas.py`, `test_curriculo.py`).
- **Clases 036-040, 076-130 escritas** (partes 07 a 12: uso responsable y certificacion con la vigencia de la Ley 21.719 verificada el 2026-11-12, inteligencia, atencion-memoria-funciones ejecutivas, personalidad, psicometria laboral y liderazgo-equipos-sociometria), con README, laboratorio determinista y bibliografia. Dato corregido por la ejecucion: la clave del IPIP-NEO-120 no esta equilibrada por faceta.
- **Clases 011-035 y 051-075 escritas** (partes 02 a 06 completas: fiabilidad, validez, estructura factorial, TRI, baremos y equidad), cada una con README, laboratorio determinista solo con biblioteca estandar y bibliografia.
- **Clases 006-010 escritas** (parte 01) con README, laboratorio ejecutable y bibliografía.
- `docs/AUDITORIA_INICIAL.md` y `docs/COBERTURA_CURRICULAR.md`.

- **Clases 041-050 y 191-200 escritas** (partes 00 y 01 ampliadas y parte 19 de proyectos integradores): con ellas las 200 clases del currículo están redactadas.
- **Clases 131-190 escritas** (partes 13 a 18: desarrollo infantil, aprendizaje y dificultades, orientación vocacional, socioemocional y bienestar con protocolos de seguridad probados, investigación psicométrica e ingeniería de sistemas de evaluación), cada una con README, laboratorio determinista y bibliografía (de memoria, sin contrastar con fuentes primarias).
- Módulo `psychometrics.baterias` (baterías y sesiones reanudables con huella de integridad) y `tests/test_baterias.py` (8 pruebas).

### Planificado
- Contraste de bibliografías con fuentes primarias y revisión por pares de las 200 clases (ver ROADMAP).
- Módulo de fiabilidad: alfa de Cronbach, omega de McDonald, error típico.
- Baremos y percentiles a partir de datos propios.

## [0.1.0] - 2026-08-19

Primera versión pública.

### Añadido
- **Motor psicométrico**: modelo de dominio, cargador con validación estricta y
  puntuación con reflejo de clave invertida, agregación jerárquica ponderada por
  ítem y control de calidad del protocolo.
- **Catálogo de 5 instrumentos, 344 ítems, 81 escalas**:
  - `ipip-neo-120` — Cinco Grandes, 120 ítems, 5 dominios y 30 facetas (dominio público).
  - `ipip-via-r` — Fortalezas del carácter, 96 ítems, 6 virtudes y 24 fortalezas (dominio público).
  - `onet-riasec-sf` — Intereses vocacionales RIASEC, 60 ítems (dominio público).
  - `disc-abierto` — Estilos conductuales, 32 ítems propios, **sin validar**.
  - `valores-spranger` — Seis valores rectores, 36 ítems propios, **sin validar**.
- **Ingesta reproducible** de los tres bancos públicos desde su fuente original,
  con validación estructural que aborta la escritura si el resultado no cuadra.
- **CLI** `psychometrics` con `catalogo`, `ficha`, `rendir`, `puntuar` y `validar`.
- **Programa de aprendizaje**: 8 partes y 40 clases en el currículo;
  la parte 00 completa con 5 clases y 5 laboratorios ejecutables.
- **57 tests** de invariantes del catálogo y del comportamiento del motor.
- CI en Python 3.11, 3.12 y 3.13, con lint, validación del catálogo y
  comprobación de que los YAML generados coinciden con su generador.

### Notas de esta versión
- Sin datos normativos: los campos `percentil`, `z` y `baremo` existen pero
  siempre valen `None`.
- Las traducciones al español no están baremadas ni tienen estudio de
  equivalencia transcultural.

[No publicado]: https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/releases/tag/v0.1.0
