# Estado de validación de los instrumentos

Este documento responde a una sola pregunta, instrumento por instrumento:
**¿qué autoriza a interpretar este puntaje como aquello que dice medir?**

## Resumen

| Instrumento | Ítems | Estructura | Fiabilidad | Validez | ¿Decidir sobre personas? |
|---|---:|---|---|---|---|
| `ipip-neo-120` | 120 | ✅ publicada | ✅ α .63–.88 por faceta | ✅ extensa | 🟡 en inglés y con baremo |
| `ipip-via-r` | 96 | ✅ publicada | 🟡 α .42–.74 | ✅ publicada | 🟡 solo perfil descriptivo |
| `onet-riasec-sf` | 60 | ✅ publicada en fuente inglesa | ✅ α .90–.93 en fuente | ✅ fuente inglesa | ❌ adaptación española no validada |
| `disc-abierto` | 32 | ❌ ninguna | ❌ ninguna | ❌ ninguna | ❌ **no** |
| `valores-spranger` | 36 | ❌ ninguna | ❌ ninguna | ❌ ninguna | ❌ **no** |

## La advertencia principal

Dos instrumentos del catálogo (`disc-abierto` y `valores-spranger`) tienen ítems
**escritos por este repositorio y sin ningún estudio empírico**. No existe
evidencia de que midan lo que su nombre dice.

Están incluidos deliberadamente, por dos razones:

1. Permiten estudiar el contraste entre un instrumento validado y uno que no lo
   está, que es la lección central de la parte 03.
2. Dan un DISC y un inventario de valores **redistribuibles**, frente a los
   comerciales, que no lo son.

No se deben usar para seleccionar, promover, despedir ni diagnosticar. La CLI lo
advierte en cada informe y `tests/test_estructura.py` verifica que el archivo lo
declare.

## Las traducciones al español

**Ninguna traducción de este repositorio está baremada.**

Los dos bancos IPIP de dominio público y la fuente inglesa de O*NET fueron
estudiados en inglés. Sus coeficientes de fiabilidad y sus percentiles
corresponden a esas versiones. Traducir un instrumento
no transfiere sus propiedades psicométricas: hace falta un estudio de
equivalencia transcultural que demuestre que los ítems funcionan igual en la
nueva población (invarianza de medida, parte 04, clase 25).

Consecuencia práctica: el texto en español sirve para administrar el
instrumento y describir un perfil intraindividual — qué escalas son las más
altas de esta persona — pero **no** para afirmar que alguien está en el
percentil 80 de la población chilena.

En O*NET la limitación también es jurídica: la O*NET Tools Developer License
exige validar el contenido modificado antes de introducir el producto. La
traducción incluida no satisface hoy esa condición. Consulte
[`../INSTRUMENT_LICENSES.md`](../INSTRUMENT_LICENSES.md) y
[`../DISCLAIMER.md`](../DISCLAIMER.md).

## Ausencia de baremos

`PuntajeEscala` declara `percentil`, `z` y `baremo`, y los tres valen siempre
`None`. La estructura está lista; los datos no existen.

Sin muestra normativa, una media por ítem de 4.2 significa "respondió, en
promedio, algo más que *moderadamente exacto*". No significa "alto".

Recoger esos datos es el objetivo del estudio de validación que da nombre a este
repositorio. Ver [`ROADMAP.md`](../ROADMAP.md).

## Qué haría falta para validar los instrumentos propios

Por orden:

1. **Contenido** — panel de expertos que juzgue si los ítems cubren el
   constructo sin contaminarlo (parte 03, clase 17).
2. **Piloto** — n ≥ 200, análisis clásico de ítems, descarte de los que no
   discriminan (parte 01, clase 10).
3. **Estructura** — factorial exploratorio y luego confirmatorio contra la
   estructura declarada (parte 04).
4. **Fiabilidad** — omega de McDonald, no solo alfa; test-retest a 4 semanas
   (parte 02).
5. **Validez de constructo** — convergencia con instrumentos establecidos:
   DISC contra Extraversión y Responsabilidad del IPIP-NEO-120 (parte 03).
6. **Invarianza** — comprobar que la estructura se sostiene por sexo, edad y
   país (parte 04, clase 25).

Hasta el paso 5 no es defendible usarlos para nada consecuente.
