# Auditoría inicial (antes de la expansión)

Contrastada con el repositorio real, no con el README.

| Línea base verificada | Valor |
|---|---|
| Partes / clases | 8 / 40 (5 escritas: 001-005, con README, `lab.py` y `lesson.yaml`) |
| Instrumentos / ítems / escalas | 5 / 344 / 81 |
| Motor | `src/psychometrics/motor` (cargador, modelos, puntuación); CLI; informes |
| Pruebas | 57 en verde; `ruff` limpio; CI en Python 3.11-3.13 |
| Gobernanza | licencias y procedencia por instrumento, `LICENSING_AUDIT.md`, `DISCLAIMER.md` |

## Qué debe conservarse intacto
Identificadores 001-040, los 5 YAML de `instruments/` (344 ítems), el motor y su CLI,
el test de claves ASCII, el chequeo de reproducibilidad de bancos IPIP.

## Cambios aditivos de esta expansión
- `curriculum.yaml`: 12 partes nuevas y 5 clases nuevas en cada parte 00-07 (IDs 041-200). Sin migración: nada se renumera.
- `catalogo/fichas.yaml` + `psychometrics.fichas`: capa documental separada del motor.

## Riesgos y huecos detectados
- 35 de las 40 clases originales siguen sin redactar; las 160 nuevas también.
- No hay módulo de fiabilidad, baremos ni IRT (ver `ROADMAP.md`).
- Sin tipos de ítem de rendimiento (clave correcta, tiempos, adaptativo): requiere extensión del esquema y estudio de consumidores antes de tocar el motor.
- Dos instrumentos de autoría propia sin validar; O*NET con validación de licencia pendiente.
- Las 140 fichas son preliminares: titular, licencia, versión y evidencia deben contrastarse con fuente primaria antes de pasar de `verificado: false`.
- No duplicado relevante detectado; las fichas de instrumentos implementados apuntan al YAML, no lo copian.

## No logrado en esta pasada (declarado, no fingido)
Redacción de clases nuevas, instrumentos ejecutables nuevos, laboratorios de IRT/AFC, extensión del motor a ítems de rendimiento, baterías y matriz de evidencia de validación. Ver `ROADMAP.md`.
