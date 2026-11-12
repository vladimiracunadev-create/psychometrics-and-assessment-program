<div align="center">

# 🧠 Psychometrics and Assessment Program

## **20 partes · 200 clases · 5 instrumentos · 344 ítems · de qué significa medir a cómo se certifica**

**Programa de aprendizaje y motor ejecutable de psicometría: cómo se construye,
se puntúa, se valida y se audita un instrumento de medición psicológica —
con bancos públicos, material propio y licencias trazables.**

[![CI](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/ci.yml)
[![Security](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/security.yml)

[![Version](https://img.shields.io/badge/version-0.1.0-orange?style=for-the-badge)](CHANGELOG.md)
[![Instrumentos](https://img.shields.io/badge/instrumentos-5%20·%20344%20ítems-7c5cff?style=for-the-badge)](instruments/)
[![Dominio público](https://img.shields.io/badge/dominio%20público-216%20de%20344%20ítems-2e8b57?style=for-the-badge)](#-procedencia-y-licencias)
[![Clases](https://img.shields.io/badge/clases-90%20de%20200%20escritas-c9184a?style=for-the-badge)](classes/)
[![Tests](https://img.shields.io/badge/tests-70%20en%20verde-3fb950?style=for-the-badge)](tests/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=for-the-badge)](classes/)
[![License](https://img.shields.io/badge/code-MIT-3fb950?style=for-the-badge)](LICENSE)
[![Content](https://img.shields.io/badge/docs-CC%20BY--NC--SA%204.0-7c5cff?style=for-the-badge)](LICENSE-CONTENT.md)

[![Python](https://img.shields.io/badge/Python-3.11%20·%203.12%20·%203.13-3776AB?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

[📚 **Currículo**](curriculum.yaml) ·
[🧪 Instrumentos](instruments/) ·
[🎓 Clases](classes/) ·
[⚖️ Validación](docs/VALIDACION.md) ·
[🏗️ Arquitectura](docs/ARQUITECTURA.md) ·
[📖 Glosario](docs/GLOSARIO.md) ·
[📕 Bibliografía](sources/BIBLIOGRAFIA.md) ·
[🗺️ Roadmap](ROADMAP.md) ·
[🤝 Contribuir](CONTRIBUTING.md)

<br>

| 🧪 Instrumentos | 📝 Ítems | 📐 Escalas | 📘 Clases | 🔬 Laboratorios | ✅ Tests |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **5** | **344** | **81** | **90 / 200** | **90** | **70** |
</div>

---

> [!IMPORTANT]
> Este repositorio **enseña y ejecuta** psicometría, no la sustituye. Dos de sus
> cinco instrumentos llevan ítems propios **sin estudio de validación**, y así
> se declaran en el archivo, en la CLI y en el informe. No se deben usar para
> decidir sobre personas. Ver [`docs/VALIDACION.md`](docs/VALIDACION.md).
> Además, la adaptación española de O*NET® tiene una obligación de validación
> pendiente bajo su licencia. Ver [`DISCLAIMER.md`](DISCLAIMER.md).

## ✅ Estado verificable

| Superficie | Estado |
|---|---|
| Catálogo | ✅ 5/5 instrumentos cargan y validan (`make validar`) |
| Ítems | ✅ 344 ítems: 216 IPIP de dominio público, 60 O*NET bajo licencia específica y 68 de autoría propia |
| Bancos de terceros | ⚠️ IPIP-NEO-120 e IPIP-VIA-R son públicos; la adaptación O*NET tiene validación de licencia pendiente |
| Motor | ✅ carga, valida, refleja clave invertida, agrega jerárquicamente y audita el protocolo |
| CLI | ✅ `catalogo`, `ficha`, `rendir`, `puntuar`, `validar` |
| Clases | 🟡 90 de 200 escritas; las 110 restantes están **planificadas** (carpeta y `lesson.yaml`, sin contenido) en `curriculum.yaml` |
| Fichas | 🟡 140 fichas documentales en [`catalogo/fichas.yaml`](catalogo/fichas.yaml): 5 implementadas, 0 validadas; el resto solo documentadas y `verificado: false` |
| Laboratorios | ✅ 5/5 ejecutables, deterministas y sin dependencias externas |
| Tests | ✅ 70 en verde |
| CI | ✅ pruebas en 3 versiones de Python, lint, validación del catálogo y comprobación de reproducibilidad |
| Baremos | ⚪ la estructura existe (`percentil`, `z`, `baremo`); **no hay datos normativos** |
| TRI / análisis factorial | ⚪ planificados (partes 04 y 05); no implementados |

## 🌟 Qué hace diferente a este programa

- **Los instrumentos son datos, no código.** Un test es un archivo YAML. Agregar
  uno nuevo no requiere tocar Python.
- **Sin procedencia no hay instrumento.** El cargador **rechaza** un archivo que
  no declare fuente y licencia. Un test sin origen verificable no es un test.
- **Los bancos públicos se reconstruyen desde su fuente.** Los parsers validan su
  propia salida y fallan si no cuadra; el CI comprueba que el YAML publicado
  coincida con lo que produce el generador.
- **Lo que no está validado lo dice.** En el archivo, en la CLI y en el informe.
- **Los laboratorios demuestran, no ilustran.** Cada uno produce números y el
  texto de la clase se corrige si no coinciden — [ya ocurrió una vez](classes/part-00-fundamentos-de-la-medicion/004-puntaje-bruto-y-media-por-item/lab.py).

## 🧪 El catálogo

| Código | Instrumento | Ítems | Escalas | Licencia | ¿Validado? |
|---|---|---:|---:|---|---|
| [`disc-abierto`](instruments/disc-abierto.yaml) | DISC Abierto - Estilos conductuales | 32 | 4 | ⚠️ autoría propia | **no** |
| [`ipip-neo-120`](instruments/ipip-neo-120.yaml) | Inventario de personalidad IPIP-NEO-120 | 120 | 35 | ✅ dominio público | sí |
| [`ipip-via-r`](instruments/ipip-via-r.yaml) | Inventario de fortalezas del carácter IPIP-VIA-R | 96 | 30 | ✅ dominio público | sí |
| [`onet-riasec-sf`](instruments/onet-riasec-sf.yaml) | Perfil de intereses vocacionales O*NET (forma breve) | 60 | 6 | ⚠️ O*NET Tools Developer License | adaptación no validada |
| [`valores-spranger`](instruments/valores-spranger.yaml) | Inventario de valores de Spranger | 36 | 6 | ⚠️ autoría propia | **no** |

### 📜 Procedencia y licencias

**216 de 344 ítems (63%) son de dominio público** y proceden de IPIP:

- **IPIP-NEO-120** — [ipip.ori.org](https://ipip.ori.org/30FacetNEO-PI-RItems.htm).
  Johnson (2014). Dominio público explícito, sin permiso ni pago.
- **IPIP-VIA-R** — [ipip.ori.org](https://ipip.ori.org/IPIP-VIA-R_Key.html).
  Bluemke, Partsch, Saucier & Lechner (2021). **No** es el VIA-IS comercial.
- **O*NET® Interest Profiler SF** — [fuente](https://www.onetcenter.org/dl_files/IPSF_PP.pdf)
  y [licencia](https://www.onetcenter.org/license_toolsdev.html). Esta traducción
  propia es material adaptado bajo O*NET Tools Developer License, no dominio
  público. Falta el estudio de validación exigido para contenido modificado;
  no debe usarse como producto validado ni para decisiones reales.

Los 68 ítems restantes (DISC y Valores de Spranger) son **originales de este
repositorio**, escritos sobre modelos teóricos de dominio público. Aquí **no hay
ítems de instrumentos comerciales protegidos** — Everything DiSC, DiSC Classic,
Thomas PPA, VIA-IS, NEO-PI-R ni Study of Values.

## 🚀 Empezar

```bash
git clone https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program.git
cd psychometrics-and-assessment-program
python -m pip install -e ".[dev]"
```

```bash
psychometrics catalogo
```

```bash
psychometrics ficha ipip-neo-120
```

```bash
psychometrics rendir onet-riasec-sf --salida mi-perfil.json
```

```bash
make test
```

Ver [`INSTALL.md`](INSTALL.md) para el detalle.

## 🎓 El programa

<!-- PROGRAMA:INICIO -->
| Parte | Título | Nivel | Clases escritas |
|---|---|---|---|
| 00 | [Fundamentos de la medición psicológica](classes/part-00-fundamentos-de-la-medicion/) | fundamentos | 5 / 10 🟡 |
| 01 | [Construcción de instrumentos](classes/part-01-construccion-de-instrumentos/) | fundamentos | 5 / 10 🟡 |
| 02 | [Fiabilidad](classes/part-02-fiabilidad/) | intermedio | 10 / 10 ✅ |
| 03 | [Validez](classes/part-03-validez/) | intermedio | 10 / 10 ✅ |
| 04 | [Estructura y análisis factorial](classes/part-04-estructura-y-analisis-factorial/) | avanzado | 10 / 10 ✅ |
| 05 | [Teoría de respuesta al ítem](classes/part-05-teoria-de-respuesta-al-item/) | avanzado | 10 / 10 ✅ |
| 06 | [Baremos, sesgo y equidad](classes/part-06-baremos-sesgo-y-equidad/) | avanzado | 10 / 10 ✅ |
| 07 | [Uso responsable y certificación](classes/part-07-uso-responsable-y-certificacion/) | profesional | 10 / 10 ✅ |
| 08 | [Inteligencia y capacidades cognitivas](classes/part-08-inteligencia-y-capacidades-cognitivas/) | intermedio | 10 / 10 ✅ |
| 09 | [Atención, memoria y funciones ejecutivas](classes/part-09-atencion-memoria-y-funciones-ejecutivas/) | intermedio | 10 / 10 ✅ |
| 10 | [Personalidad, temperamento y conducta](classes/part-10-personalidad-temperamento-y-conducta/) | intermedio | 0 / 10 ⬜ |
| 11 | [Psicometría laboral y empleabilidad](classes/part-11-psicometria-laboral-y-empleabilidad/) | intermedio | 0 / 10 ⬜ |
| 12 | [Liderazgo, equipos y sociometría](classes/part-12-liderazgo-equipos-y-sociometria/) | intermedio | 0 / 10 ⬜ |
| 13 | [Desarrollo infantil y evaluación psicoeducativa](classes/part-13-desarrollo-infantil-y-evaluacion-psicoeducativa/) | avanzado | 0 / 10 ⬜ |
| 14 | [Aprendizaje, aptitudes y dificultades escolares](classes/part-14-aprendizaje-aptitudes-y-dificultades-escolares/) | avanzado | 0 / 10 ⬜ |
| 15 | [Orientación vocacional y competencias profesionales](classes/part-15-orientacion-vocacional-y-competencias-profesionales/) | intermedio | 0 / 10 ⬜ |
| 16 | [Evaluación socioemocional y bienestar](classes/part-16-evaluacion-socioemocional-y-bienestar/) | avanzado | 0 / 10 ⬜ |
| 17 | [Investigación psicométrica y análisis de datos](classes/part-17-investigacion-psicometrica-y-analisis-de-datos/) | avanzado | 0 / 10 ⬜ |
| 18 | [Ingeniería de sistemas de evaluación digital](classes/part-18-ingenieria-de-sistemas-de-evaluacion-digital/) | avanzado | 0 / 10 ⬜ |
| 19 | [Aplicaciones avanzadas y proyectos integradores](classes/part-19-aplicaciones-avanzadas-y-proyectos-integradores/) | avanzado | 0 / 10 ⬜ |
| | **Total** | | **90 / 200** |
<!-- PROGRAMA:FIN -->

Cada clase escrita trae README con fundamentos y bibliografía, un `lab.py`
ejecutable y determinista, y `lesson.yaml` con su estado real.

## 🏗️ Arquitectura

```
instruments/*.yaml        el catálogo: un archivo por test, formato declarativo
src/psychometrics/
  motor/modelos.py        modelo de dominio (Instrumento, Escala, Ítem, Resultado)
  motor/cargador.py       YAML -> objeto, con validación estricta
  motor/puntuacion.py     respuestas -> perfil
  cli.py                  interfaz de línea de comandos
scripts/ingest_*.py       fuente original -> JSON estructurado (con validación)
scripts/build_*.py        JSON -> YAML del catálogo (con traducción)
classes/                  el programa de aprendizaje
tests/                    invariantes del catálogo y del motor
```

Detalle en [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md).

## 🤝 Contribuir

Se aceptan instrumentos nuevos siempre que declaren procedencia y licencia
redistribuible. Ver [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 📄 Licencia

MIT para el código; CC BY-NC-SA 4.0 para la documentación educativa original
actual, con exclusiones. Cada banco conserva su situación propia y los 68 ítems
propios actuales mantienen los permisos MIT históricos ya concedidos; no se ha
elegido automáticamente una licencia CC nueva para aportes futuros.

Ver [`LICENSE`](LICENSE), [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md),
[`INSTRUMENT_LICENSES.md`](INSTRUMENT_LICENSES.md),
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) y
[`DISCLAIMER.md`](DISCLAIMER.md).
