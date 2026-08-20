# Gobernanza

## Modelo

Proyecto de mantenedor único (BDFL) en su etapa actual. Las decisiones técnicas
las toma quien mantiene el repositorio, con discusión pública en los issues.

**Mantenedor:** Vladimir Acuña ([@vladimiracunadev-create](https://github.com/vladimiracunadev-create))

## Cómo se decide

1. Toda propuesta relevante se discute en un issue antes del pull request.
2. Los cambios que afectan al formato de `instruments/*.yaml` requieren una nota
   de migración en el `CHANGELOG.md`.
3. Los cambios que afectan a la puntuación requieren un test que fije el
   comportamiento anterior y otro que fije el nuevo.

## Principios no negociables

Estos no se someten a discusión caso por caso:

1. **Sin procedencia no hay instrumento.** El cargador rechaza un archivo que no
   declare fuente y licencia.
2. **Nunca se publican ítems de instrumentos comerciales protegidos.**
3. **El estado de validación se declara siempre**, y se declara a la baja cuando
   hay duda.
4. **Las cifras publicadas deben ser comprobables con un comando.** Si el README
   dice 344 ítems, `make validar` debe poder confirmarlo.
5. **Si el laboratorio contradice al texto, gana el laboratorio.**

## Versionado

[SemVer](https://semver.org/lang/es/). Para este proyecto:

- **Mayor**: cambio incompatible del formato de instrumento o de la API del motor.
- **Menor**: instrumento nuevo, clase nueva, funcionalidad nueva.
- **Parche**: correcciones que no cambian puntajes.

Un cambio que **altere el puntaje** de un instrumento existente es siempre, como
mínimo, una versión menor, y debe documentarse en el `CHANGELOG.md` con el
efecto numérico.
