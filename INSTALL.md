# Instalación

## Requisitos

- Python 3.11, 3.12 o 3.13
- `pip`

La única dependencia de ejecución es `PyYAML`.

## Instalación

```bash
git clone https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program.git
cd psychometrics-and-assessment-program
python -m pip install -e ".[dev]"
```

El modo editable (`-e`) es el recomendado: el catálogo de `instruments/` se
resuelve respecto a la raíz del repositorio.

## Comprobar que funciona

```bash
psychometrics validar
```

Debe listar los cinco instrumentos y terminar en `TODO CORRECTO`.

```bash
make test
```

## Uso sin instalar

```bash
PYTHONPATH=src python -m psychometrics.cli catalogo
```

En PowerShell:

```powershell
$env:PYTHONPATH = "src"; python -m psychometrics.cli catalogo
```

## Codificación en Windows

La consola de Windows abre en `cp1252` y rompe las tildes. La CLI reconfigura su
salida a UTF-8 automáticamente. Para scripts propios:

```bash
set PYTHONIOENCODING=utf-8
```

## Catálogo en otra ubicación

```bash
export PSYCHOMETRICS_INSTRUMENTS=/ruta/a/mis/instrumentos
```

## Extras opcionales

```bash
python -m pip install -e ".[analisis]"
```

`numpy` y `scipy`, necesarios a partir de la parte 04 del programa.
