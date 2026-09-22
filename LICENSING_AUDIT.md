# Auditoría crítica de licencias psicométricas

**Repositorio:** `vladimiracunadev-create/psychometrics-and-assessment-program`

**Fecha de corte:** 22 de septiembre de 2026

**Commit auditado antes de los cambios:** `f6800b2770eba9a0cf4aec38c1f4833861c8008c`

**Alcance:** licencias y procedencia; no es un dictamen jurídico ni una
certificación psicométrica.

## 1. Conclusión ejecutiva

La licencia anterior mezclaba en un único archivo MIT software, documentación e
ítems propios, y remitía los bancos de terceros a metadatos demasiado gruesos.
La separación era jurídicamente insuficiente, aunque el repositorio sí contenía
advertencias de procedencia y bloqueaba instrumentos marcados como propietarios.

Hallazgos principales:

1. **MIT histórico irrevocable para las copias ya entregadas.** Todo el contenido
   actual, incluidos los 68 ítems propios, fue añadido en el commit inicial con
   una nota que lo incluía bajo MIT. La nueva política no revoca ese permiso.
2. **IPIP correctamente abierto.** La fuente oficial confirma que los materiales
   IPIP están en dominio público y autorizados para cualquier uso, comercial o
   no comercial. Las traducciones y glosas propias deben distinguirse del inglés.
3. **O*NET estaba mal clasificado.** El O*NET® Interest Profiler está sujeto a
   licencias específicas. La versión del repositorio es una adaptación por su
   traducción propia y otras modificaciones, por lo que corresponde la O*NET
   Tools Developer License, no “dominio público”.
4. **O*NET mantiene un riesgo crítico abierto.** La Developer License exige un
   estudio de validación para contenido modificado. No existe. Añadir avisos
   mejora atribución, pero no subsana la condición pendiente.
5. **Sin evidencia de bancos comerciales incorporados.** Los nombres comerciales
   sólo aparecen en advertencias o bibliografía; no hay manuales, claves, baremos
   ni archivos que se presenten como sus bancos. La ausencia no puede probarse
   de forma absoluta sin acceso legal a los corpus propietarios completos.
6. **Titularidad limitada.** El historial muestra un autor Git humano y trailers
   de coautoría de una IA. Sólo se reivindica trabajo original identificable;
   teorías, hechos, marcas y terceros quedan fuera.

## 2. Método y evidencia

Se inspeccionaron:

- todos los archivos rastreados y los cinco commits de todas las refs locales;
- `LICENSE`, `pyproject.toml`, README, documentación, currículo y bibliografía;
- los cinco YAML de `instruments/`, sus 344 ítems y 81 escalas;
- código de carga y puntuación, scripts de ingesta/construcción, pruebas y CI;
- autores, correos, fechas, trailers y blobs históricos de Git;
- términos oficiales de IPIP, O*NET, Creative Commons y U.S. Copyright Office;
- coincidencias textuales muestrales de enunciados propios y referencias a
  pruebas comerciales.

Fuentes primarias principales:

- IPIP Permission: <https://ipip.ori.org/newPermission.htm>;
- O*NET Career Exploration Tools License:
  <https://www.onetcenter.org/license_tools.html>;
- O*NET Tools Developer License:
  <https://www.onetcenter.org/license_toolsdev.html>;
- Creative Commons, tipos de licencia y FAQ:
  <https://creativecommons.org/cc-licenses/> y
  <https://creativecommons.org/faq/>;
- U.S. Copyright Office: <https://www.copyright.gov/what-is-copyright/>.

No existe directorio `datasets/`, `dataset/` ni `data/` rastreado. Los JSON
`scripts/ipip120.json` y `scripts/ipip_via_r.json` son datos intermedios IPIP y
quedan incluidos en el inventario de terceros.

## 3. Matriz de alcance actual

| Superficie | Estado anterior | Estado resultante | Riesgo residual |
|---|---|---|---|
| Código, algoritmos y tests | MIT mezclado con contenido | MIT, alcance explícito | Bajo; patentes y regulación no se resuelven con copyright |
| Documentación educativa | MIT | CC BY-NC-SA 4.0, excluyendo terceros | La copia histórica sigue disponible bajo MIT |
| Ítems propios existentes | MIT | MIT histórico reconocido; sin nueva CC automática | No puede recuperarse exclusividad sobre copias MIT existentes |
| Nuevos ítems propios | Sin política diferenciada | Decisión expresa pendiente | Se requiere acuerdo del titular/contribuyente |
| IPIP inglés | “dominio público” | Dominio público confirmado | Marcas, publicaciones y pruebas homónimas no quedan incluidas |
| Traducciones IPIP | Mencionadas como propias, sin alcance | Modificaciones propias separadas; sin equivalencia | MIT histórico de la versión existente; validez transcultural pendiente |
| O*NET | “dominio público” | O*NET Tools Developer License | **Crítico:** falta estudio de validación para la adaptación |
| Metodologías y teorías | Tratadas informalmente como públicas | Ideas/hechos separados de la expresión protegida | La etiqueta de una teoría no autoriza una prueba comercial |
| Bibliografía | Listado de fuentes | Citas, no relicenciamiento | Verificar permisos si se añaden extractos extensos |

## 4. LICENSE y empaquetado

`LICENSE` contenía el texto MIT seguido de una nota española que ampliaba MIT a
documentación e ítems propios y afirmaba que O*NET era dominio público. El texto
MIT se conserva y la nota se sustituye por un aviso de alcance que remite a los
inventarios. `pyproject.toml` mantiene `license = {text = "MIT"}` y el classifier
MIT porque el paquete Python distribuido contiene el motor de software, no los
YAML externos ni las clases.

No se cambió a Apache-2.0: MIT ya era la licencia histórica, es compatible con
la instrucción “MIT o Apache-2.0” y evita una transición innecesaria. Apache-2.0
aportaría una licencia expresa de patentes, pero requeriría revisar titularidad y
compatibilidad de cada contribución; no soluciona los bancos de ítems.

## 5. Documentación educativa

Se adopta CC BY-NC-SA 4.0 para la oferta actual de contenido educativo original.
Ventajas: atribución, adaptación docente no comercial y obligación de compartir
adaptaciones en condiciones equivalentes. Riesgos: el término no comercial puede
ser incierto en formación remunerada, editoriales, consultoría o plataformas; la
licencia es irrevocable para quien ya la recibe; y no debe aplicarse al software
ni a material de terceros.

Creative Commons recomienda licencias de software para el código y permite CC
para documentación. Esa separación se refleja en `LICENSE-CONTENT.md`.

## 6. Ítems propios: análisis de opciones

No se elige automáticamente entre CC BY-NC-ND, CC BY-NC-SA y derechos reservados.
La comparación completa está en `LICENSE-CONTENT.md`.

Punto decisivo: `disc-abierto.yaml` y `valores-spranger.yaml` ya se ofrecieron
bajo MIT, sin cambios desde el commit inicial. Una licencia más restrictiva sólo
puede gobernar aportes futuros o una oferta alternativa; no elimina las copias y
permisos MIT ya obtenidos. Si la finalidad es proteger integridad psicométrica,
ND reduce la difusión de adaptaciones pero también bloquea traducción y mejora.
Si la finalidad es ciencia abierta no comercial, SA facilita validación. Si la
finalidad es control y licenciamiento comercial, derechos reservados ofrecen más
control futuro, a costa de adopción y replicabilidad.

## 7. Instrumentos de terceros

### 7.1 IPIP-NEO-120

La declaración oficial de IPIP permite cualquier propósito, comercial o no. El
repositorio conserva los textos ingleses y genera YAML mediante un parser y un
diccionario de traducciones. Modificaciones: traducción, estructura, IDs y glosas.
No se encontraron contenidos del NEO-PI-R comercial. Riesgo principal: confusión
de nombres y extrapolación de evidencia/baremos a la traducción española.

### 7.2 IPIP-VIA-R

Mismo fundamento de dominio público IPIP. No es el VIA-IS. Modificaciones:
traducción, jerarquía de virtudes, glosas, IDs y renombre técnico `HUM_H`. Riesgo
principal: confusión con la prueba VIA propietaria y fiabilidades modestas.

### 7.3 O*NET® Interest Profiler

La página oficial vigente distingue:

- CC BY-ND 4.0 para copiar/publicar la herramienta sin modificaciones;
- O*NET Tools Developer License para modificar, editar, extender o traducir.

El repositorio tradujo los 60 ítems por cuenta propia y cambió presentación y
contexto. La propia fuente oficial considera una traducción “Adapted Material”.
La Developer License permite reproducir y compartir adaptaciones, pero exige:

- atribución, vínculo y aviso de licencia;
- indicación de modificaciones;
- aviso visible de que USDOL/ETA no aprobó ni probó las modificaciones;
- descripción accesible de las modificaciones;
- estudio de validación para contenido modificado antes de introducir el producto.

Se incorporan los avisos exigibles en documentos y metadatos. No hay evidencia
de un estudio de validación. El resultado de la auditoría es una no conformidad
abierta, no una aprobación. La opción de menor riesgo operativo es retirar la
adaptación de usos reales hasta validar, sustituirla por una integración oficial
o recibir autorización escrita. Esa decisión excede una corrección documental.

## 8. Scoring, algoritmos, escalas y metodología

`src/psychometrics/motor/puntuacion.py` implementa reflejo de ítems invertidos,
agregación por escalas, manejo de omisiones, medias por ítem y alertas. La
implementación concreta es MIT. Las ideas matemáticas, fórmulas, hechos y métodos
no se convierten por ello en propiedad exclusiva.

Las claves IPIP/O*NET y estructuras de escalas derivadas de terceros conservan
su estatus de origen. Las glosas y descripciones originales del repositorio son
contenido, no código. No se alteraron fórmulas, claves, opciones ni resultados de
puntuación durante esta auditoría.

## 9. Historial y contributors

- Cinco commits auditados, todos en `main`, sin tags locales.
- Autor Git de los cinco: Vladimir Acuña `<vladimir.acuna.dev@gmail.com>`.
- Todos los mensajes incluyen `Co-Authored-By: Claude Opus 5
  <noreply@anthropic.com>`.
- El commit inicial añadió todos los instrumentos y la licencia; los YAML no
  cambiaron posteriormente.
- No hay evidencia en Git de cesiones, CLA, contratos de trabajo o permisos
  adicionales. La coautoría declarada de IA no acredita por sí sola derechos.

Se normaliza el aviso de copyright sólo para el trabajo realmente original de
Vladimir Acuña y contribuyentes que hayan concedido derechos. No se atribuye al
proyecto la autoría de IPIP, O*NET, teorías, marcas o publicaciones citadas.

## 10. Búsqueda de instrumentos comerciales

Se buscaron nombres y variantes de Everything DiSC, DiSC Classic, Thomas PPA,
VIA-IS, NEO-PI-R, Study of Values, Hogan, MMPI, 16PF y MBTI en archivos
rastreados. Los seis primeros aparecen sólo para negar derivación o como fuentes
bibliográficas; los demás no aparecen. No hay PDFs/manuales comerciales ni
directorios ocultos rastreados con bancos adicionales.

Las fuentes institucionales consultadas confirman que Everything DiSC® se ofrece
bajo licencia de contenido de Wiley, VIA Survey/VIA-IS se declara protegido por
VIA Institute, PAR licencia traducciones NEO y el catálogo WorldCat registra
*Study of Values* (3.ª edición) con copyright de 1960. Los enlaces y avisos están
en `THIRD_PARTY_NOTICES.md`.

Se hicieron búsquedas exactas muestrales de enunciados distintivos de los bancos
propios. No aparecieron coincidencias públicas atribuibles a las pruebas
comerciales nombradas. Limitación: una comparación forense exhaustiva exigiría
acceso legal a los corpus completos y versiones históricas de cada prueba. La
conclusión prudente es “no se encontró evidencia”, no “imposible que exista”.

## 11. Cambios realizados

- `LICENSE`: MIT limitado al software y enlaces al mapa de licencias.
- `LICENSE-CONTENT.md`: alcance de contenido, CC BY-NC-SA y opciones de ítems.
- `INSTRUMENT_LICENSES.md`: inventario instrumento por instrumento.
- `THIRD_PARTY_NOTICES.md`: atribuciones y condiciones de terceros.
- `docs/LICENSING_HISTORY.md`: continuidad histórica y contributors.
- `DISCLAIMER.md`: no diagnóstico, no sustitución, límites y uso investigativo.
- metadatos y documentación: reclasificación O*NET y cifras de dominio público.
- validación: nuevo valor de licencia conocido para O*NET y pruebas de
  coherencia para evitar que vuelva a declararse como dominio público.

## 12. Riesgos y acciones pendientes

| Prioridad | Riesgo | Acción recomendada | Responsable sugerido |
|---|---|---|---|
| Crítica | Adaptación O*NET sin validación exigida por licencia | Suspender uso real; validar, integrar versión oficial, pedir permiso o retirar | Titular + asesoría jurídica/psicométrica |
| Alta | Copias históricas de ítems propios permanecen bajo MIT | Aceptar la continuidad y definir política sólo para aportes/versiones futuros | Titular |
| Alta | Falta política explícita de contribución de ítems | Exigir declaración de autoría/licencia y consentimiento expreso por PR | Maintainer |
| Media | Traducciones IPIP sin equivalencia | Validación transcultural antes de interpretación individual | Equipo investigador |
| Media | Riesgo de confusión con marcas comerciales | Mantener avisos y revisar nombres en UI/publicación | Maintainer |
| Media | No hay corpus propietario para comparación exhaustiva | Revisión legal con acceso autorizado si se pretende certificación | Asesor jurídico |

## 13. Criterio de aceptación

La auditoría documental queda completa cuando los nuevos archivos existen, las
afirmaciones del README y YAML coinciden con el modelo de licencia, los tests y
validadores pasan sin cambios de resultados, no hay mojibake y el diff no altera
ítems ni reglas de puntuación. La conformidad de O*NET no se considera cerrada
hasta resolver la validación o retirar/reemplazar la adaptación.
