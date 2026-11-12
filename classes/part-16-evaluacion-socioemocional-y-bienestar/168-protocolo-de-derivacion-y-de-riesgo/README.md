# 168 — Protocolo de derivación y de riesgo

> [Índice de la parte](../README.md)

**Parte 16 — Evaluación socioemocional y bienestar** · Nivel avanzado · 4 h · Estado `escrita`
**Prerrequisitos:** clases 135 y 167.

> **Seguridad.** Ejemplo didáctico. Un protocolo real lo define cada institución con profesionales de salud mental y la normativa vigente; los canales y plazos se verifican en fuentes oficiales.

## Objetivos

1. Modelar un protocolo de derivación como máquina de estados.
2. Verificar sus invariantes de seguridad de forma exhaustiva.
3. Definir roles, plazos y registro.

## Fundamentos

Un protocolo responde: ¿qué señal activa qué acción?, ¿quién actúa?, ¿en qué plazo?, ¿qué se registra? Como el espacio de entradas es pequeño, se puede **probar** que cumple sus invariantes en todas las combinaciones, en vez de confiar en la revisión visual (Reason, 1990: las defensas del sistema importan más que la vigilancia individual).

Invariantes del laboratorio:
- **I1.** Riesgo inmediato ⇒ contacto humano inmediato.
- **I2.** Alerta alta o riesgo ⇒ el caso no se cierra sin revisión humana.
- **I3.** Si hay alerta, nunca se responde «sin acción».
- **I4.** Si no hay profesional disponible, se escala.

Resultado: 12 combinaciones verificadas, 0 violaciones.

| Alerta | Riesgo | Profesional | Acción | Plazo |
|---:|---|---|---|---|
| 2 | sí | sí | contacto humano inmediato y acompañamiento | inmediato |
| 2 | sí | no | escalar de inmediato a la jefatura de turno | inmediato |
| 2 | no | sí | derivar a profesional y contactar a la familia | 24 h |
| 0 | no | — | sin acción específica; monitoreo universal | — |

## Ejemplo resuelto

Alerta 0 con riesgo = sí: el nivel de alerta del cribado no importa; el indicador de riesgo manda (I1).

## Errores y límites

- Depender de que alguien «recuerde» el protocolo.
- Sin registro, no hay aprendizaje ni responsabilidad.
- Automatizar la decisión humana: el sistema alerta y registra, el equipo actúa.
- Plazos del laboratorio ilustrativos.

## Ejercicios

- **Inicial.** ¿Qué es un invariante?
- **Intermedio.** Agrega una invariante nueva (p. ej. «todo caso inmediato queda registrado») y compruébala.
- **Avanzado.** Añade un nivel de alerta intermedio con reglas propias y verifica las invariantes.

## Laboratorio

```bash
python classes/part-16-evaluacion-socioemocional-y-bienestar/168-protocolo-de-derivacion-y-de-riesgo/lab.py
```

## Autoevaluación y criterios

1. ¿Quién es responsable en cada paso? 2. ¿Cómo se informa a la familia? 3. ¿Cómo se cuida a quien aplica la evaluación?
Se logra si el estudiante modela un protocolo y prueba sus invariantes.

## Bibliografía y fuentes

- Reason, J. (1990). *Human Error*. Cambridge University Press.
- American Psychological Association (2017). *Ethical Principles of Psychologists and Code of Conduct*.
- Ministerio de Salud de Chile: orientaciones vigentes de prevención y respuesta (verificar en minsal.cl).
