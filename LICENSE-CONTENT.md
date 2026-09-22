# Licencia del contenido

Este documento separa la licencia del software de la licencia del contenido.
No es asesoría jurídica y no sustituye la revisión de un profesional competente
en las jurisdicciones donde se use o distribuya el proyecto.

## 1. Software: MIT

El archivo [`LICENSE`](LICENSE) se aplica a la implementación de software:

- `src/**/*.py`;
- `scripts/**/*.py`;
- `tests/**/*.py`;
- los laboratorios `classes/**/lab.py`;
- `Makefile`, configuración de empaquetado y automatización de CI, salvo que un
  archivo indique expresamente otra procedencia.

La licencia MIT cubre la expresión concreta del código. No convierte en
propiedad exclusiva ideas, fórmulas matemáticas, métodos psicométricos ni hechos.

## 2. Documentación educativa: CC BY-NC-SA 4.0

Salvo las exclusiones de las secciones 3 y 4, el material educativo original se
ofrece bajo [Creative Commons Atribución-NoComercial-CompartirIgual 4.0
Internacional](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es):

- `classes/**/*.md` y el texto educativo original de `classes/**/lesson.yaml`;
- `docs/**/*.md`, excepto `docs/LICENSING_HISTORY.md`, que es un registro factual;
- `README.md`, `INSTALL.md`, `ROADMAP.md`, `SUPPORT.md`, `CONTRIBUTING.md`,
  `GOVERNANCE.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` y `curriculum.yaml`;
- comentarios explicativos y glosas originales no incorporados desde terceros.

La licencia permite copiar y adaptar con atribución, únicamente para fines no
comerciales, y exige compartir las adaptaciones bajo la misma licencia. “No
comercial” no equivale automáticamente a “educativo” o “sin fines de lucro”; si
el uso tiene una finalidad comercial o existe duda, debe solicitarse permiso al
titular.

Atribución sugerida: “Psychometrics and Assessment Program, Vladimir Acuña,
CC BY-NC-SA 4.0; se indicaron los cambios”.

## 3. Bancos de ítems e instrumentos

Los archivos `instruments/*.yaml` son materiales mixtos. La licencia de la
colección o del software no sustituye la licencia de cada banco:

- IPIP-NEO-120 e IPIP-VIA-R: los ítems ingleses del IPIP están declarados en
  dominio público por IPIP. Las traducciones españolas y glosas del repositorio
  son modificaciones identificadas por separado.
- O*NET® Interest Profiler: se rige por la licencia específica de O*NET; no es
  dominio público a efectos de este repositorio. La versión aquí incluida está
  modificada y debe tratarse según la O*NET Tools Developer License.
- DISC Abierto y Valores de Spranger: ítems redactados en el repositorio. Véase
  la decisión pendiente de la sección 5 y el efecto de la licencia MIT histórica.

El detalle, la atribución y las condiciones comerciales están en
[`INSTRUMENT_LICENSES.md`](INSTRUMENT_LICENSES.md). Los materiales de terceros
nunca quedan relicenciados por CC BY-NC-SA 4.0 ni por MIT.

## 4. Exclusiones

No se ofrecen bajo la licencia de contenido:

- ítems, escalas, textos, nombres y marcas de terceros, salvo en los términos de
  su licencia o del dominio público aplicable;
- citas bibliográficas, extractos y enlaces, que conservan su situación propia;
- nombres y marcas, incluidos O*NET®, DiSC®, VIA y nombres de pruebas comerciales;
- contribuciones cuyo autor no haya concedido derechos suficientes.

[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) prevalece para las
atribuciones de terceros.

## 5. Ítems propios: alternativas evaluadas, sin nueva elección automática

Los 68 ítems actuales de `disc-abierto.yaml` y `valores-spranger.yaml` se
publicaron íntegramente en el commit inicial bajo MIT. Esa autorización ya
otorgada no se revoca. Para nuevas versiones o nuevos bancos, el titular debe
adoptar expresamente una política; hasta entonces no se concede aquí una licencia
CC adicional sobre aportes futuros.

| Alternativa futura | Ventajas | Riesgos y límites |
|---|---|---|
| CC BY-NC-ND 4.0 | Permite compartir copias íntegras, exige atribución y bloquea la distribución de adaptaciones; protege mejor la estabilidad del enunciado. | Impide publicar traducciones, correcciones y adaptaciones sin permiso; dificulta validación transcultural y ciencia abierta; CC desaconseja ND para bases científicas. No impide estudiar privadamente una adaptación donde la ley lo permita. |
| CC BY-NC-SA 4.0 | Permite traducción, mejora y validación no comercial; las adaptaciones deben permanecer bajo términos equivalentes. | “No comercial” puede ser ambiguo; no bloquea modificaciones psicométricamente deficientes y el copyleft no sustituye control de calidad. |
| Derechos reservados | Máximo control sobre redistribución, adaptación y explotación comercial; permite licencias caso a caso. | Reduce revisión, replicación y adopción; genera fricción para docencia e investigación; exige gestionar permisos y no recupera derechos ya concedidos bajo MIT. |

Recomendación de la auditoría, no decisión de licencia: antes de escoger, definir
si la prioridad es integridad de los ítems, ciencia abierta o explotación
comercial; consultar asesoría jurídica; y acompañar cualquier licencia con una
política de versiones, atribución y validación. Una cláusula de licencia no
garantiza calidad psicométrica ni impide todo uso amparado por la ley.

## 6. Continuidad de la licencia MIT histórica

El commit inicial `cea8823b5c509e9e99d821910b70c9f93e62b9` (19 de agosto de
2026) publicó código, documentación e ítems propios con una nota que los incluía
bajo MIT. Los receptores de esa versión pueden seguir ejerciendo esos permisos.
Esta separación rige la oferta actual y futura del repositorio; no pretende
anular licencias ya concedidas. Véase [`docs/LICENSING_HISTORY.md`](docs/LICENSING_HISTORY.md).

## 7. Contribuciones futuras

Una contribución sólo puede cambiar la licencia de material del que su autor sea
titular o para el que tenga autorización. Quien aporte material debe identificar
autor, fuente, licencia, modificaciones y evidencia. La aceptación de código se
entiende bajo MIT; la de documentación educativa original, bajo CC BY-NC-SA 4.0;
los ítems requieren una decisión expresa y no se aceptan por inferencia.
