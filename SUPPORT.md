# Soporte

## Dónde preguntar

| Necesidad | Dónde |
|---|---|
| Fallo del software | [Issues](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/issues) |
| Duda de uso o de psicometría | [Discussions](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/discussions) |
| Vulnerabilidad | [Security advisory](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/security/advisories/new) |
| Aportar instrumento o clase | [CONTRIBUTING.md](CONTRIBUTING.md) |

## Antes de abrir un issue

```bash
python --version
psychometrics validar
make test
```

Incluye la salida de esos tres comandos.

## Lo que este proyecto no puede darte

- **Interpretación clínica o laboral de un perfil.** El software calcula
  puntajes; interpretarlos para decidir sobre una persona requiere formación y,
  según la jurisdicción, habilitación profesional.
- **Baremos.** No hay datos normativos. Ver [`docs/VALIDACION.md`](docs/VALIDACION.md).
- **Aval de los instrumentos sin validar.** `disc-abierto` y
  `valores-spranger` no tienen evidencia empírica y no deben usarse para
  decisiones sobre personas.
