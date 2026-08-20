# Política de seguridad

## Versiones con soporte

| Versión | Soporte |
|---|---|
| 0.1.x | ✅ |

## Reportar una vulnerabilidad

Usa el reporte privado de GitHub:
[Security → Report a vulnerability](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/security/advisories/new).

No abras un issue público para una vulnerabilidad sin corregir.

Tiempos esperados: acuse en 5 días hábiles, evaluación inicial en 10.

## Superficie de ataque

Este proyecto es una biblioteca y una CLI sin servicio de red, sin persistencia y
sin autenticación. La superficie principal es la **carga de archivos YAML**:

- Se usa `yaml.safe_load` siempre. Nunca `yaml.load` sin `Loader` seguro.
- Un instrumento de una fuente no confiable es, a efectos de seguridad, entrada
  no confiable: revísalo antes de cargarlo.

## Consideración de privacidad

Las respuestas a un instrumento psicométrico son **datos personales sensibles**
en la mayoría de las jurisdicciones, incluida la Ley 19.628 de Chile y el RGPD
europeo.

Este repositorio **no almacena ni transmite** respuestas: la CLI las guarda en
disco solo si se le pasa `--salida`. Quien monte un servicio sobre este motor
asume las obligaciones de tratamiento de esos datos: base de licitud,
minimización, plazo de conservación y derecho de acceso y supresión.

`.gitignore` excluye `respuestas-*.json` para reducir el riesgo de commitear
datos de una persona por accidente.
