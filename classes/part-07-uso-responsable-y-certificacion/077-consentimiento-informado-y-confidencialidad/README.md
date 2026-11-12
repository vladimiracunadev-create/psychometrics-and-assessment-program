# 077 — Consentimiento informado y confidencialidad

> [Índice de la parte](../README.md)

**Parte 07 — Uso responsable y certificación** · Nivel profesional · 4 h · Estado `escrita`
**Prerrequisitos:** clase 076.

## Objetivos

1. Describir los elementos de un consentimiento informado válido.
2. Implementar un registro de consentimiento que respete finalidad y retiro.
3. Entender la diferencia entre integridad (hash) y confidencialidad.

## Fundamentos

Un consentimiento informado es **libre, específico, informado y revocable**; en menores se suma el asentimiento del niño o niña y la autorización de quien ejerce su cuidado. Debe explicar qué se mide, para qué, quién verá los resultados, cuánto se conservarán y cómo retirarse. En investigación aplican además los principios éticos de la Declaración de Helsinki (WMA, 2013) y las revisiones por comités de ética.

Laboratorio (3 sujetos sintéticos; el s003 retiró su consentimiento):

| Finalidad del análisis | Sujetos que se pueden usar |
|---|---|
| evaluación | s001, s002 |
| investigación | s001 (s002 no autorizó esa finalidad; s003 retiró) |

La huella SHA-256 del registro de auditoría cambia al alterar un solo registro (cfe0e7fd… frente a 2e550769…).

## Ejemplo resuelto

Si un colegio usa los resultados de una evaluación para un estudio externo, necesita un consentimiento específico para investigación: el firmado para «evaluación» no basta.

## Errores y límites

- Consentimiento «paraguas» para cualquier uso.
- Hacer el consentimiento condición de un servicio que no lo requiere.
- Creer que el hash protege el dato: detecta cambios, no impide el acceso.
- La confidencialidad tiene límites legales y éticos (riesgo para la persona o terceros): se explican de antemano.

## Ejercicios

- **Inicial.** ¿Qué diferencia hay entre consentimiento y asentimiento?
- **Intermedio.** Agrega una finalidad «informe a la familia» y modifica el registro.
- **Avanzado.** Implementa que el retiro dispare la eliminación de los datos y deje constancia.

## Laboratorio

```bash
python classes/part-07-uso-responsable-y-certificacion/077-consentimiento-informado-y-confidencialidad/lab.py
```

## Autoevaluación y criterios

1. ¿Qué haces si alguien retira el consentimiento tras el análisis? 2. ¿Quién accede a qué? 3. ¿Cómo pruebas que no hubo uso indebido?
Se logra si el estudiante diseña un consentimiento específico y un registro auditable.

## Bibliografía

- World Medical Association (2013). Declaration of Helsinki: Ethical principles for medical research involving human subjects. *JAMA*, 310(20), 2191-2194.
- American Psychological Association (2017). *Ethical Principles of Psychologists and Code of Conduct*.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
