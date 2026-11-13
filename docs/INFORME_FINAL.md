# Informe final de la expansión

Cifras calculadas del repositorio al momento de generar este informe (no estimadas).

## Antes y después

| Medida | Antes (ver `AUDITORIA_INICIAL.md`) | Después |
|---|---:|---:|
| Partes / clases en el currículo | 8 / 40 | 20 / 200 |
| Clases escritas (README + laboratorio + bibliografía) | 5 | 200 |
| Clases solo planificadas | 35 | 0 |
| Laboratorios ejecutables | 5 | 200 |
| Fichas documentales | 0 | 140 |
| Fichas `implementado` | 0 | 5 |
| Fichas `validado-uso-especifico` | 0 | 0 |
| Fichas con `verificado: true` | 0 | 5 |
| Instrumentos ejecutables (YAML) | 5 | 5 |
| Pruebas automáticas | 57 | 78 |

## Qué se añadió

- Currículo de 20 partes y 200 clases con los 40 identificadores originales intactos.
- 200 laboratorios deterministas, de biblioteca estándar y datos **sintéticos**, ejecutados por `make validar`.
- Catálogo `catalogo/fichas.yaml` con estados separados (documentado, disponible legalmente, implementado, en investigación, validado) y módulo `psychometrics.fichas`.
- Módulo `psychometrics.baterias` (baterías, sesiones reanudables con huella de integridad) y sus pruebas.
- Scripts de coherencia: `scripts/sync_indices.py` (índices y cifras del README) y `scripts/validate_repository.py`.

## Qué NO se logró (declarado)

- **Ningún instrumento nuevo ejecutable**: el catálogo sigue con 5 instrumentos, 344 ítems y 81 escalas. El instrumento original de la clase 199 es un borrador dentro del laboratorio, sin validar y fuera del catálogo.
- **Ninguna ficha contrastada con fuente primaria** (135 de 140 siguen `verificado: false`): titulares, licencias y versiones de los 135 instrumentos documentados no están verificados. Los 15 instrumentos laborales se documentan solo por su denominación.
- **Bibliografías solo contrastadas con Crossref**: de 412 referencias únicas, 288 existen con título y año coincidentes, 33 aparecen con otro año (se comprueba la edición) y 91 (libros sin DOI, normas, sitios web) quedan por comprobar a mano. Crossref confirma que la obra existe, no que respalde lo que dice la clase (`docs/VERIFICACION_BIBLIOGRAFIA.md`).
- **Sin revisión por pares**: las 200 clases tienen formato pedagógico (explicación, figura, ejercicios y glosario), pero no han sido revisadas por especialistas; las cifras de los laboratorios son de simulación.
- **Sin baremos ni estudios de validación propios**: todos los datos de los laboratorios son simulados; no se inventaron normas ni estudios.
- **Motor sin ítems de rendimiento** (clave correcta, tiempos, adaptativo): los laboratorios enseñan las técnicas, pero no hay módulo reutilizable en `src/` para fiabilidad, TRI ni análisis factorial.
- Las referencias legales chilenas (Ley 19.628 y Ley 21.719) se verificaron en fuentes públicas el 2026-11-12 y no constituyen asesoría jurídica.

## Riesgos

1. Que se lea una ficha documentada como un instrumento validado (mitigación: estados separados y campo `verificado`).
2. Que las cifras de los laboratorios se tomen como evidencia empírica (son simulaciones).
3. Que el contenido se use para decisiones sobre personas sin la formación y las autorizaciones que exige la normativa.

## Prioridades siguientes

1. Contrastar bibliografías y fichas con fuentes primarias, familia por familia.
2. Revisión por especialistas de las partes de uso sensible (7, 15, 16).
3. Módulos reutilizables de fiabilidad y TRI en `src/` con pruebas.
4. Estudio de validación real de los instrumentos de autoría propia o su retiro del catálogo.
