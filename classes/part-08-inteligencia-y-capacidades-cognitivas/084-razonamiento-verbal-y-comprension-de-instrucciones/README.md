# 084 — Razonamiento verbal y comprensión de instrucciones

> [Índice de la parte](../README.md)

**Parte 08 — Inteligencia y capacidades cognitivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 016 y 006.

## Objetivos

1. Distinguir razonamiento verbal de dominio lector.
2. Evaluar la legibilidad de instrucciones con un índice en español.
3. Identificar varianza irrelevante al constructo por redacción compleja.

## Fundamentos

Una prueba de comprensión de instrucciones o de razonamiento verbal no debe medir, sin quererlo, la capacidad de descifrar textos enrevesados (varianza irrelevante al constructo; clase 016). Un índice de legibilidad para español es el de **Szigriszt-Pazos** (escala INFLESZ):

```
IFSZ = 206,835 − 62,3 · (sílabas/palabras) − (palabras/frases)
```

Escala orientativa: > 80 muy fácil; 65–80 bastante fácil; 55–65 normal; 40–55 algo difícil; < 40 muy difícil (Barrio-Cantalejo et al., 2008).

Laboratorio (contador de sílabas **heurístico**, aproximado):

| Versión de la instrucción | IFSZ | Lectura |
|---|---:|---|
| A. simple («Lea cada pregunta. Elija una respuesta. …») | 61,6 | normal |
| B. intermedia | 67,6 | bastante fácil |
| C. enrevesada («Previamente a la consignación…») | 9,1 | muy difícil |

## Ejemplo resuelto

Texto de 20 palabras, 2 frases, 42 sílabas: IFSZ = 206,835 − 62,3·2,1 − 10 = 65,99 → «bastante fácil».

## Errores y límites

- Tratar el índice como medida de dificultad cognitiva: ignora vocabulario técnico y estructura.
- Simplificar tanto que cambie el constructo (si el objetivo es comprender textos complejos, la complejidad es parte del constructo).
- El contador de sílabas del laboratorio no resuelve todos los diptongos e hiatos.
- No se aplica igual a lectores de distintas edades o lengua materna.

## Ejercicios

- **Inicial.** ¿Qué dos variables entran en el índice?
- **Intermedio.** Reescribe la versión C en lenguaje claro y recalcula.
- **Avanzado.** Mejora `silabas()` para manejar hiatos con tilde (p. ej. «día») y compara.

## Laboratorio

```bash
python classes/part-08-inteligencia-y-capacidades-cognitivas/084-razonamiento-verbal-y-comprension-de-instrucciones/lab.py
```

## Autoevaluación y criterios

1. ¿Cuándo la complejidad textual es parte del constructo? 2. ¿Cómo probarías si la redacción afecta a un grupo? 3. ¿Qué haces con instrucciones en segunda lengua?
Se logra si el estudiante evalúa legibilidad y decide si la complejidad es pertinente.

## Bibliografía

- Szigriszt Pazos, F. (1993). *Sistemas predictivos de legibilidad del mensaje escrito: fórmula de perspicuidad*. Tesis doctoral, Universidad Complutense de Madrid.
- Barrio-Cantalejo, I. M., et al. (2008). Validación de la escala INFLESZ para evaluar la legibilidad de los textos dirigidos a pacientes. *Anales del Sistema Sanitario de Navarra*, 31(2), 135-152.
- Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.
