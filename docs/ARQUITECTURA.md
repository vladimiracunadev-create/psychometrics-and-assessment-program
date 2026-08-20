# Arquitectura

## La decisión de fondo

**Un instrumento es dato, no código.** Un test se declara en un YAML y el motor
lo interpreta. Agregar uno nuevo no requiere tocar Python.

De ahí se siguen las demás decisiones.

## Capas

```
        instruments/*.yaml
                |
                v
        motor/cargador.py      valida y construye
                |
                v
        motor/modelos.py       dataclasses inmutables
                |
                v
        motor/puntuacion.py    respuestas -> perfil
                |
                v
        cli.py                 presentación
```

Cada capa depende solo de la anterior. `puntuacion.py` no sabe leer archivos y
`cargador.py` no sabe puntuar.

## Por qué la validación es agresiva

Un instrumento mal declarado no falla al cargarse: falla al puntuar, o peor, no
falla y produce un informe plausible y equivocado sobre una persona real.

El cargador rechaza, entre otras cosas: campos obligatorios ausentes, `licencia`
o `tipo_respuesta` desconocidos, procedencia sin fuente, escalas huérfanas,
escalas hoja sin ítems, ids repetidos, ítems que apuntan a una escala
inexistente, claves distintas de ±1, y un instrumento Likert sin opciones.

## La convención de codificación

**Prosa en castellano con tildes. Todo lo estructural en ASCII.**

Es una regla nacida de un fallo real: una pasada automática de tildes acentuó
las claves `codigo` y `version`, y el cargador dejó de encontrarlas. La
regresión está fijada en `tests/test_estructura.py::test_claves_yaml_en_ascii`.

## El flujo de ingesta

Los tres bancos de dominio público no se transcriben a mano:

```
fuente original (HTML o PDF)
        |
        v
scripts/ingest_*.py     -> scripts/*.json     estructura + validación
        |
        v
scripts/build_*.py      -> instruments/*.yaml traducción + metadatos
```

Los `ingest_*` **validan su propia salida y abortan** si no cuadra: 30 facetas
por 4 ítems, 24 fortalezas con clave equilibrada, 6 dominios. En el desarrollo
inicial esa comprobación detectó cinco errores de parseo que habrían pasado
inadvertidos.

El CI regenera los YAML y falla si el árbol de trabajo queda sucio: el archivo
publicado siempre coincide con lo que produce su generador.

## Tres decisiones de puntuación

1. **El reflejo va antes de la suma.** Reflejar después de agregar da un
   resultado distinto y equivocado.
2. **Las omisiones no valen cero.** Un cero no existe en una Likert de 1 a 5.
   Se excluyen del cálculo y se informan.
3. **Las escalas compuestas agregan desde los ítems**, no promediando promedios.
   Lo segundo daría a cada faceta el mismo peso sin declararlo.

Las tres están fijadas en `tests/test_puntuacion.py`.

## Qué no está implementado

- Puntuación ipsativa (elección forzada, ranking, suma constante). El modelo
  declara los tipos; el motor lanza `NotImplementedError`.
- Baremos y percentiles.
- Teoría de respuesta al ítem.
- Persistencia y multiusuario.
