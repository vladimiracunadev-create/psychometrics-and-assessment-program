# 117 — Percepción y prevención de riesgos laborales

> [Índice de la parte](../README.md)

**Parte 11 — Psicometría laboral y empleabilidad** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 091 y 112.

## Objetivos

1. Medir la detección de peligros con teoría de detección de señales.
2. Entender el problema estadístico de validar contra accidentes.
3. Ubicar la evaluación individual dentro de un enfoque de sistema.

## Fundamentos

La percepción de riesgos se puede evaluar con tareas de detección de peligros (d′ separa capacidad de cautela, clase 091). Validar contra **accidentes** es difícil porque son eventos raros: una tasa de 0,05 por trabajador-año da una correlación mínima y pide miles de casos. Los criterios **proximales** (conductas seguras observadas, cuasi-accidentes, clima de seguridad) son más frecuentes y fiables (Clarke, 2006). Y Reason (1990) recuerda que los accidentes se explican principalmente por fallas de sistema, no solo por «errores humanos».

Laboratorio:

| Medida | Valor |
|---|---:|
| d′ estimado (20 + 20 imágenes): media / DE | 1,51 / 0,70 (DE verdadera de d′ = 0,5) |
| N = 200: r con accidentes / con conductas seguras / potencia | −0,079 / 0,468 / 20 % |
| N = 2 000: r con accidentes / con conductas seguras / potencia | −0,071 / 0,449 / 87 % |

Con 200 trabajadores casi nunca se detecta la relación con accidentes (20 %).

## Ejemplo resuelto

Para detectar una correlación de −0,07 con 80 % de potencia se requieren cerca de 1 600 personas (n ≈ 7,85/r² + 3).

## Errores y límites

- Culpar al trabajador con base en un puntaje de percepción.
- Validar solo con accidentes.
- Cribar a postulantes por «propensión a accidentes» sin evidencia: la evidencia de ese constructo es limitada.
- La normativa de prevención (p. ej. Ley 16.744 y reglamentos) se consulta en su texto vigente.

## Ejercicios

- **Inicial.** ¿Por qué es difícil usar accidentes como criterio?
- **Intermedio.** Calcula n para r = 0,10 y 80 % de potencia → ≈ 785 + 3.
- **Avanzado.** Aumenta la tasa a 0,5 accidentes por trabajador-año y observa la potencia.

## Laboratorio

```bash
python classes/part-11-psicometria-laboral-y-empleabilidad/117-percepcion-y-prevencion-de-riesgos-laborales/lab.py
```

## Autoevaluación y criterios

1. ¿Qué criterio proximal propones? 2. ¿Qué parte de la prevención no es individual? 3. ¿Qué cautelas éticas hay?
Se logra si el estudiante elige criterios viables y ubica la evaluación en un enfoque de sistema.

## Bibliografía

- Reason, J. (1990). *Human Error*. Cambridge University Press.
- Clarke, S. (2006). The relationship between safety climate and safety performance: A meta-analytic review. *Journal of Occupational Health Psychology*, 11(4), 315-327.
- Macmillan, N. A., & Creelman, C. D. (2005). *Detection Theory: A User's Guide* (2.ª ed.). Lawrence Erlbaum.
