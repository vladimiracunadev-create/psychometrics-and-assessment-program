# Inventario de licencias de instrumentos

Estado verificado el 22 de septiembre de 2026. “Uso comercial” describe lo que
permite la fuente identificada; no certifica cumplimiento de otras obligaciones,
marcas, privacidad, regulación profesional ni validez psicométrica.

## Resumen

| Instrumento | Creador / procedencia | Situación | Uso comercial | Modificaciones del repositorio | Evidencia |
|---|---|---|---|---|---|
| IPIP-NEO-120 | John A. Johnson; ítems IPIP iniciados por Lewis R. Goldberg | Ítems ingleses IPIP en dominio público | Sí, según declaración expresa de IPIP | Traducción española de trabajo; YAML, IDs, glosas y jerarquía; sin equivalencia transcultural | [Permiso IPIP](https://ipip.ori.org/newPermission.htm), [clave IPIP-NEO-120](https://ipip.ori.org/30FacetNEO-PI-RItems.htm), Johnson (2014) |
| IPIP-VIA-R | Bluemke, Partsch, Saucier y Lechner; ítems IPIP/Goldberg | Ítems ingleses IPIP en dominio público | Sí, según declaración expresa de IPIP | Traducción española; YAML y jerarquía; `HUM` renombrado `HUM_H`; sin equivalencia transcultural | [Permiso IPIP](https://ipip.ori.org/newPermission.htm), [clave IPIP-VIA-R](https://ipip.ori.org/IPIP-VIA-R_Key.html), Bluemke et al. (2021) |
| O*NET® Interest Profiler Short Form | USDOL/ETA; National Center for O*NET Development; Rounds, Su, Lewis y Rivkin | O*NET Tools Developer License para esta versión modificada; **no dominio público** | La licencia no prohíbe por sí misma el uso comercial, pero exige atribución, aviso y validación; el cumplimiento actual está pendiente | Traducción española propia, presentación Likert, YAML, IDs, glosas y puntuación local | [Licencias O*NET](https://www.onetcenter.org/license_tools.html), [Developer License](https://www.onetcenter.org/license_toolsdev.html), [informe fuente](https://www.onetcenter.org/dl_files/IPSF_PP.pdf) |
| DISC Abierto | Ítems redactados por psychometrics-and-assessment-program; marco conceptual atribuido a Marston (1928) | Ítems ya publicados bajo MIT en el commit inicial; no se selecciona automáticamente una nueva CC | Sí para las versiones históricas recibidas bajo MIT; política de aportes futuros pendiente | Banco Likert normativo propio de 32 ítems; no validado; afirma no derivar de pruebas comerciales | Historial Git, blob `b63580f0995024258ec99240b1a7c57c45cc99b0`; Marston (1928) como referencia conceptual |
| Valores de Spranger | Ítems redactados por psychometrics-and-assessment-program; marco conceptual atribuido a Spranger | Ítems ya publicados bajo MIT en el commit inicial; no se selecciona automáticamente una nueva CC | Sí para las versiones históricas recibidas bajo MIT; política de aportes futuros pendiente | Banco Likert normativo propio de 36 ítems; no validado; no reproduce *Study of Values* | Historial Git, blob `5ff840e77c62ac9b0503a8117c7386595f5e9d79`; Spranger (1914/1928) como referencia conceptual |

## 1. IPIP-NEO-120

- **Nombre:** Inventario de personalidad IPIP-NEO-120.
- **Creador:** John A. Johnson desarrolló la forma de 120 ítems; los enunciados
  pertenecen al International Personality Item Pool, iniciativa de Lewis R.
  Goldberg.
- **Procedencia:** `https://ipip.ori.org/30FacetNEO-PI-RItems.htm` y Johnson,
  J. A. (2014), *Journal of Research in Personality*, 51, 78–89.
- **Situación:** IPIP declara en su página de permiso que sus ítems, escalas e
  inventarios están en dominio público.
- **Uso comercial:** permitido expresamente por IPIP, igual que el no comercial.
- **Modificaciones:** traducción española no validada; nombres y descripciones
  españolas; IDs; jerarquía de cinco dominios y treinta facetas; conversión a
  JSON/YAML. El texto inglés se conserva como fuente canónica del generador.
- **Riesgos:** “IPIP-NEO-120” no significa NEO-PI-R. El repositorio no puede
  conceder derechos sobre NEO-PI-R, su manual, marcas, baremos ni otros textos.
  La traducción no hereda los parámetros de la muestra inglesa.

## 2. IPIP-VIA-R

- **Nombre:** Inventario de fortalezas del carácter IPIP-VIA-R.
- **Creadores:** Bluemke, M.; Partsch, M. V.; Saucier, G.; Lechner, C. M.; con
  ítems del IPIP de Goldberg.
- **Procedencia:** `https://ipip.ori.org/IPIP-VIA-R_Key.html`; Bluemke et al.
  (2021), “Circumventing cultural bias in the assessment of character strengths”.
- **Situación:** dominio público según la declaración general de IPIP.
- **Uso comercial:** permitido expresamente por IPIP.
- **Modificaciones:** traducción española no validada; jerarquía de seis
  virtudes y 24 fortalezas; serialización; glosas; cambio del identificador de
  Humor de `HUM` a `HUM_H` para evitar colisión con Humanidad.
- **Riesgos:** no es VIA-IS y no incorpora el banco del VIA Institute. El marco
  académico citado y sus publicaciones no quedan relicenciados.

## 3. O*NET® Interest Profiler Short Form

- **Nombre:** O*NET® Interest Profiler Short Form, 60 ítems.
- **Creadores:** patrocinado por USDOL/ETA y desarrollado por National Center
  for O*NET Development; informe de Rounds, Su, Lewis y Rivkin (2010).
- **Procedencia:** apéndice del informe `IPSF_PP.pdf` y documentación oficial de
  O*NET Career Exploration Tools.
- **Situación:** la fuente oficial vigente ofrece CC BY-ND 4.0 para publicación
  literal o la O*NET Tools Developer License para modificar, editar, extender o
  traducir. La afirmación anterior “obra federal = dominio público” era
  insuficiente y se corrige. Esta versión es adaptada y, por tanto, se clasifica
  bajo la Developer License.
- **Uso comercial:** no aparece prohibido por la Developer License; la concesión
  es mundial y libre de regalías. Sin embargo, deben cumplirse todas sus
  condiciones, incluida la validación de contenido modificado antes de introducir
  el producto. No debe declararse simplemente “uso comercial permitido” mientras
  falte esa validación.
- **Modificaciones:** traducción propia al español (no la traducción oficial de
  Mi Próximo Paso), YAML, IDs, agrupación, glosas, presentación y puntuación local.
- **Estado de cumplimiento:** **riesgo crítico abierto**. Se añadieron atribución,
  vínculo, marca y aviso de modificación. No existe el estudio de validación que
  exige la sección 3(b). La documentación no cura esa carencia.
- **Acción necesaria antes de uso real:** validación conforme a estándares,
  reemplazo por integración oficial/no modificada cuando aplique, autorización
  escrita o retirada de la adaptación.

## 4. DISC Abierto

- **Nombre:** DISC Abierto — Estilos conductuales.
- **Creador:** `psychometrics-and-assessment-program` declara autoría propia de
  los 32 ítems; Vladimir Acuña es el único autor Git observado.
- **Procedencia:** redacción original de 2026; Marston (1928) se cita como
  antecedente conceptual, no como banco de preguntas.
- **Situación:** incorporado completo en el commit inicial bajo MIT. La teoría o
  idea de cuatro dimensiones no otorga derechos sobre instrumentos comerciales.
- **Uso comercial:** permitido respecto de la copia histórica bajo MIT. La
  auditoría no selecciona una licencia nueva para futuros ítems.
- **Modificaciones:** no se observan cambios al YAML desde el commit inicial.
  Banco normativo Likert, equilibrado en clave y sin validación empírica.
- **Evidencia:** historial Git y búsqueda exacta muestral de enunciados; no se
  encontraron coincidencias públicas con los ítems comerciales nombrados.
- **Límite de verificación:** los bancos propietarios completos no están
  públicamente disponibles, por lo que no puede probarse una negativa absoluta.
  No se observan archivos, manuales, claves ni nombres de ítems de Everything
  DiSC, DiSC Classic o Thomas PPA.

## 5. Valores de Spranger

- **Nombre:** Inventario de valores de Spranger.
- **Creador:** `psychometrics-and-assessment-program` declara autoría propia de
  los 36 ítems; Vladimir Acuña es el único autor Git observado.
- **Procedencia:** redacción original de 2026; teoría de Spranger (1914/1928).
  *Study of Values* sólo aparece como referencia histórica no reproducida.
- **Situación:** incorporado completo en el commit inicial bajo MIT.
- **Uso comercial:** permitido respecto de la copia histórica bajo MIT. La
  política para aportes futuros queda pendiente de decisión expresa.
- **Modificaciones:** no se observan cambios al YAML desde el commit inicial.
  Banco Likert normativo y sin validación empírica.
- **Evidencia y límite:** historial Git y búsqueda exacta muestral no revelaron
  coincidencias públicas con *Study of Values*. Sin acceso autorizado al banco
  propietario completo, la conclusión es “sin evidencia de incorporación”, no
  una certificación forense absoluta.

## Instrumentos comerciales no incorporados

Las expresiones Everything DiSC, DiSC Classic, Thomas PPA, VIA-IS, NEO-PI-R y
Study of Values aparecen únicamente en advertencias, comparaciones o citas. La
auditoría no encontró archivos que se presenten como sus manuales, baremos,
claves o bancos. Nadie debe añadirlos, traducirlos ni “adaptarlos” sin permiso
documentado del titular.
