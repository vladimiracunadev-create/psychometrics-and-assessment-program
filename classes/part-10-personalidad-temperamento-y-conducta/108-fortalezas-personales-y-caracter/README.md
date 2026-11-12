# 108 — Fortalezas personales y carácter

> [Índice de la parte](../README.md)

**Parte 10 — Personalidad, temperamento y conducta** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 009 y 102.

## Objetivos

1. Describir la clasificación de virtudes y fortalezas del carácter.
2. Estimar la estabilidad del «top-5» de fortalezas.
3. Usar un instrumento abierto sin sobreafirmar.

## Fundamentos

Peterson y Seligman (2004) propusieron 6 virtudes y 24 fortalezas del carácter. El instrumento comercial asociado es propietario; en este repositorio se usa **IPIP-VIA-R** (`instruments/ipip-via-r.yaml`; 96 ítems, 24 escalas de 4 ítems; dominio público). Con 4 ítems por escala la fiabilidad es limitada (con r₁ = 0,30 por ítem, ≈ 0,63), y las «fortalezas distintivas» (top-5 de cada persona) son inestables.

Laboratorio (3 000 personas, dos aplicaciones paralelas):

| Medida | Valor |
|---|---:|
| Fiabilidad supuesta por escala | 0,63 |
| Coincidencia media del top-5 entre aplicaciones | 2,54 de 5 |
| Coincidencia por azar puro (5 de 24) | 1,04 |
| Personas con ≥ 4 de 5 coincidentes | 13,6 % |

## Ejemplo resuelto

Dos aplicaciones dan top-5 {A, B, C, D, E} y {A, B, F, G, H}: coinciden 2 de 5. Es lo que cabe esperar con esta fiabilidad.

## Errores y límites

- Comunicar el top-5 como «tus fortalezas» sin matizar.
- Interpretar fortalezas como virtudes morales de la persona.
- Evidencia de intervenciones basadas en fortalezas: mixta; no prometer mejoras sin respaldo.
- Fiabilidad supuesta; en datos reales se estima.

## Ejercicios

- **Inicial.** ¿Cuántas fortalezas hay en el modelo?
- **Intermedio.** Calcula la fiabilidad con r₁ = 0,3 y 6 ítems → 1,8/2,5 = 0,72.
- **Avanzado.** Estima la coincidencia del top-5 con 8 ítems por escala.

## Laboratorio

```bash
python classes/part-10-personalidad-temperamento-y-conducta/108-fortalezas-personales-y-caracter/lab.py
```

## Autoevaluación y criterios

1. ¿Qué lectura útil queda del top-5? 2. ¿Cómo mejorarías la fiabilidad? 3. ¿Qué cautelas éticas tiene darle a un adolescente un «perfil de fortalezas»?
Se logra si el estudiante cuantifica la inestabilidad y matiza la interpretación.

## Bibliografía

- Peterson, C., & Seligman, M. E. P. (2004). *Character Strengths and Virtues: A Handbook and Classification*. Oxford University Press/APA.
- Goldberg, L. R., et al. (2006). The International Personality Item Pool and the future of public-domain personality measures. *Journal of Research in Personality*, 40(1), 84-96.
