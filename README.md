<div align="center">

# 🧠 Psychometrics and Assessment Program

## **8 partes · 40 clases · 5 instrumentos · 344 ítems · de qué significa medir a cómo se certifica**

**Programa de aprendizaje y motor ejecutable de psicometría: cómo se construye,
se puntúa, se valida y se audita un instrumento de medición psicológica —
con un catálogo real de tests de dominio público, no de juguete.**

[![CI](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/ci.yml)
[![Security](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/actions/workflows/security.yml)

[![Version](https://img.shields.io/badge/version-0.1.0-orange?style=for-the-badge)](CHANGELOG.md)
[![Instrumentos](https://img.shields.io/badge/instrumentos-5%20·%20344%20ítems-7c5cff?style=for-the-badge)](instruments/)
[![Dominio público](https://img.shields.io/badge/dominio%20público-276%20de%20344%20ítems-2e8b57?style=for-the-badge)](#-procedencia-y-licencias)
[![Clases](https://img.shields.io/badge/clases-5%20de%2040%20escritas-c9184a?style=for-the-badge)](classes/)
[![Tests](https://img.shields.io/badge/tests-57%20en%20verde-3fb950?style=for-the-badge)](tests/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=for-the-badge)](classes/)
[![License](https://img.shields.io/badge/license-MIT-3fb950?style=for-the-badge)](LICENSE)

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
| **5** | **344** | **81** | **5 / 40** | **5** | **57** |
</div>

---

> [!IMPORTANT]
> Este repositorio **enseña y ejecuta** psicometría, no la sustituye. Dos de sus
> cinco instrumentos llevan ítems propios **sin estudio de validación**, y así
> se declaran en el archivo, en la CLI y en el informe. No se deben usar para
> decidir sobre personas. Ver [`docs/VALIDACION.md`](docs/VALIDACION.md).

## ✅ Estado verificable

| Superficie | Estado |
|---|---|
| Catálogo | ✅ 5/5 instrumentos cargan y validan (`make validar`) |
| Ítems | ✅ 344 ítems, 276 de dominio público y 68 de autoría propia |
| Bancos públicos | ✅ IPIP-NEO-120, IPIP-VIA-R y O*NET RIASEC reproducibles desde su fuente |
| Motor | ✅ carga, valida, refleja clave invertida, agrega jerárquicamente y audita el protocolo |
| CLI | ✅ `catalogo`, `ficha`, `rendir`, `puntuar`, `validar` |
| Clases | 🟡 5 de 40 escritas; el temario de las 35 restantes está fijado en `curriculum.yaml` |
| Laboratorios | ✅ 5/5 ejecutables, deterministas y sin dependencias externas |
| Tests | ✅ 57 en verde |
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
| [`onet-riasec-sf`](instruments/onet-riasec-sf.yaml) | Perfil de intereses vocacionales O*NET (forma breve) | 60 | 6 | ✅ dominio público | sí |
| [`valores-spranger`](instruments/valores-spranger.yaml) | Inventario de valores de Spranger | 36 | 6 | ⚠️ autoría propia | **no** |

### 📜 Procedencia y licencias

**276 de 344 ítems (80%) son de dominio público** y se
redistribuyen íntegros:

- **IPIP-NEO-120** — [ipip.ori.org](https://ipip.ori.org/30FacetNEO-PI-RItems.htm).
  Johnson (2014). Dominio público explícito, sin permiso ni pago.
- **IPIP-VIA-R** — [ipip.ori.org](https://ipip.ori.org/IPIP-VIA-R_Key.html).
  Bluemke, Partsch, Saucier & Lechner (2021). **No** es el VIA-IS comercial.
- **O*NET Interest Profiler SF** — [onetcenter.org](https://www.onetcenter.org/dl_files/IPSF_PP.pdf).
  Obra del gobierno federal de EE. UU.

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

| Parte | Título | Nivel | Clases |
|---|---|---|---|
| 00 | [Fundamentos de la medición](classes/part-00-fundamentos-de-la-medicion/) | fundamentos | 5 ✅ |
| 01 | [Construcción de instrumentos](classes/part-01-construccion-de-instrumentos/) | fundamentos | 5 ⬜ |
| 02 | [Fiabilidad](classes/part-02-fiabilidad/) | intermedio | 5 ⬜ |
| 03 | [Validez](classes/part-03-validez/) | intermedio | 5 ⬜ |
| 04 | [Estructura y análisis factorial](classes/part-04-estructura-y-analisis-factorial/) | avanzado | 5 ⬜ |
| 05 | [Teoría de respuesta al ítem](classes/part-05-teoria-de-respuesta-al-item/) | avanzado | 5 ⬜ |
| 06 | [Baremos, sesgo y equidad](classes/part-06-baremos-sesgo-y-equidad/) | avanzado | 5 ⬜ |
| 07 | [Uso responsable y certificación](classes/part-07-uso-responsable-y-certificacion/) | profesional | 5 ⬜ |

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

MIT para el código, la documentación y los ítems propios. Cada banco de terceros
conserva su propia situación legal, declarada en su archivo. Ver [`LICENSE`](LICENSE).
