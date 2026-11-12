# Changelog

Todas las modificaciones relevantes de este proyecto se documentan aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el versionado sigue [SemVer](https://semver.org/lang/es/).

## [No publicado]

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
- **Clases 006-010 escritas** (parte 01) con README, laboratorio ejecutable y bibliografía.
- `docs/AUDITORIA_INICIAL.md` y `docs/COBERTURA_CURRICULAR.md`.

### Planificado
- Redacción de las 195 clases pendientes (190 restantes; ver ROADMAP).
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
