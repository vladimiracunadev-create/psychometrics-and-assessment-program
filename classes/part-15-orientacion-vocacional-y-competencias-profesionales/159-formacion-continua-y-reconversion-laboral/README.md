# 159 — Formación continua y reconversión laboral

![Portada de la clase 159](portada.svg)

> [Índice de la parte](../README.md)

**Parte 15 — Orientación vocacional y competencias profesionales** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 111 y 155.

## Objetivos

1. Calcular una brecha ponderada de habilidades hacia ocupaciones destino.
2. Propagar la incertidumbre de la autoevaluación.
3. Planificar una ruta de formación con supuestos explícitos.

## Fundamentos

Los análisis de brechas comparan las habilidades actuales con las requeridas por una ocupación (OECD, 2019). La brecha ponderada es Σwᵢ·max(0, requeridoᵢ − actualᵢ)/Σwᵢ. La autoevaluación tiene error; incorporarlo muestra qué tan estable es el «mejor destino». La reconversión también depende de factores no medidos: mercado local, redes, costos y apoyo (Savickas, 2005).

Laboratorio (ocupaciones **ficticias**; error de autoevaluación DE 1,2; 6 horas por punto de brecha como supuesto):

| Destino | Brecha ponderada | Horas estimadas | Prob. de menor brecha |
|---|---:|---:|---:|
| Soporte técnico | 1,08 | 52 | 93,6 % |
| Coordinación de proyectos | 1,67 | 80 | 6,3 % |
| Analista de datos junior | 2,33 | 112 | 0,1 % |

El mejor destino es estable aquí porque su ventaja es amplia; con brechas más parejas no lo sería.

## Ejemplo resuelto

Habilidad requerida 8 con peso 3, actual 3: brecha = 3·5 = 15 (antes de dividir por Σw).

## Errores y límites

- Prometer horas o empleabilidad que dependen del mercado.
- Usar solo autoevaluación para decisiones costosas.
- Ignorar la brecha de apoyo y de tiempo disponible.
- Las ocupaciones, requisitos y horas son ficticios.

## Ejercicios

- **Inicial.** ¿Qué es una brecha ponderada?
- **Intermedio.** Con requerido 7, actual 9: brecha 0 (no se compensa).
- **Avanzado.** Reduce el error de autoevaluación a 0,5 y observa las probabilidades.

## Laboratorio

```bash
python classes/part-15-orientacion-vocacional-y-competencias-profesionales/159-formacion-continua-y-reconversion-laboral/lab.py
```

## Autoevaluación y criterios

1. ¿Qué evidencia de habilidades usarías además de la autoevaluación? 2. ¿Qué apoyos financieros y de tiempo existen (a verificar)? 3. ¿Cómo evalúas el avance?
Se logra si el estudiante calcula brechas, incorpora incertidumbre y planifica una ruta realista.

## Bibliografía

- OECD (2019). *OECD Skills Outlook 2019: Thriving in a Digital World*. OECD Publishing. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)
- Savickas, M. L. (2005). The theory and practice of career construction. En S. D. Brown & R. W. Lent (Eds.), *Career Development and Counseling*. Wiley. 🔎 sin verificar (libro, norma o sitio no hallado en Crossref: comprobar a mano)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
