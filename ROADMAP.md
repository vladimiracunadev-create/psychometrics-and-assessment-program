# Roadmap

Estado actual en [`README.md`](README.md#-estado-verificable). Aquí está lo que
falta y en qué orden.

## v0.2.0 — Fiabilidad medible

- [ ] Módulo `psychometrics.analisis.fiabilidad`: alfa de Cronbach, omega de
      McDonald, correlación ítem-total corregida, error típico de medida.
- [ ] Comando `psychometrics analizar <codigo> --datos respuestas.csv`.
- [ ] Parte 02 del programa (5 clases).
- [ ] Reproducir los alfas publicados del IPIP-NEO-120 sobre datos abiertos,
      como prueba de que la implementación es correcta.

## v0.3.0 — Estructura

- [ ] Matriz de correlaciones y correlaciones policóricas.
- [ ] Análisis factorial exploratorio.
- [ ] Verificador de estructura circumpleja: someter a prueba el hexágono de
      Holland sobre datos reales, que es la predicción falsable del modelo.
- [ ] Partes 01 y 04 del programa.

## v0.4.0 — Baremos

- [ ] `psychometrics.normas`: percentiles, puntajes z y T, tablas por grupo.
- [ ] Formato declarativo de baremo, versionado junto al instrumento.
- [ ] Parte 06 del programa.
- [ ] **Estudio de validación propio**: recogida de datos en población
      hispanohablante para los instrumentos traducidos. Es el objetivo que da
      nombre al repositorio.

## v0.5.0 — TRI

- [ ] Modelo de Rasch y modelos de 2 y 3 parámetros.
- [ ] Función de información del ítem.
- [ ] Testing adaptativo sobre el catálogo existente.
- [ ] Parte 05 del programa.

## v1.0.0 — Programa completo

- [ ] Las 40 clases escritas con laboratorio.
- [ ] Partes 03 y 07.
- [ ] Sitio de estudio en GitHub Pages.
- [ ] Instrumentos propios (`disc-abierto`, `valores-spranger`) con estudio de
      validación completo, o retirados del catálogo si la evidencia no acompaña.

## Sin fecha

- Puntuación ipsativa (elección forzada, ranking, suma constante).
- Ajuste persona-puesto contra descripciones ocupacionales de O*NET.
- API HTTP y frontend web.
- Detección de funcionamiento diferencial del ítem (DIF).

## Lo que no se hará

- Publicar ítems de instrumentos comerciales protegidos.
- Ofrecer interpretación clínica automatizada.
- Presentar como validado un instrumento que no lo esté.
