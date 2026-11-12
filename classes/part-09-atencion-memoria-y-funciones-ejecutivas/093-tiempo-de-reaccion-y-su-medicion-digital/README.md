# 093 — Tiempo de reacción y su medición digital

![Portada de la clase 093](portada.svg)

<!-- NAV -->
[← 092 — Atención selectiva y dividida](../092-atencion-selectiva-y-dividida/README.md) · [📚 Parte 09](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [094 — Memoria visual y auditiva →](../094-memoria-visual-y-auditiva/README.md)
<!-- /NAV -->

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clases 026 y 089.

## Objetivos

1. Describir la distribución ex-Gaussiana de los tiempos de reacción.
2. Evaluar el efecto del ruido del dispositivo.
3. Elegir y declarar de antemano un resumen robusto.

## Fundamentos

Los tiempos de reacción tienen asimetría positiva (cola larga): suelen modelarse con una ex-Gaussiana (normal + exponencial). La media es sensible a la cola; la **mediana** y la **media recortada** son más robustas. El dispositivo agrega error: refresco de pantalla (16,7 ms a 60 Hz), latencia de teclado o pantalla táctil y variabilidad del navegador (la precisión depende del entorno; se calibra y se registra).

Laboratorio (300 personas, 40 ensayos; fiabilidad por mitades con Spearman-Brown):

| Dispositivo | Media | Mediana | Media recortada |
|---|---:|---:|---:|
| Ideal | 0,818 | 0,864 | 0,852 |
| Ruidoso (refresco + latencia) | 0,830 | 0,861 | 0,861 |

La mediana y la media recortada superan a la media; el ruido del dispositivo, en este diseño, cambia poco porque es pequeño frente a la variabilidad de la persona (puede importar más con tareas cortas o comparaciones entre dispositivos).

## Ejemplo resuelto

Con RT 280, 300, 310, 320, 1 400: media = 522; mediana = 310. Un solo ensayo distraído desplaza la media 210 ms.

## Errores y límites

- Elegir el criterio de recorte después de ver los datos.
- Mezclar dispositivos sin registrar su tipo.
- Descartar ensayos sin informar cuántos.
- Los parámetros de la ex-Gaussiana y del ruido del laboratorio son supuestos.

## Ejercicios

- **Inicial.** ¿Por qué la media sobrestima el RT típico?
- **Intermedio.** Calcula la media recortada (150–1 000 ms) de 120, 280, 300, 310, 1 400 → 296,7.
- **Avanzado.** Aumenta el ruido de latencia a 80 ms y reporta el efecto sobre cada resumen.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/093-tiempo-de-reaccion-y-su-medicion-digital/lab.py
```

## Autoevaluación y criterios

1. ¿Qué metadatos del dispositivo registrarías? 2. ¿Cómo justificas el recorte? 3. ¿Qué implica la telemetría para la privacidad (parte 07)?
Se logra si el estudiante elige y justifica un resumen y declara el efecto del dispositivo.

## Bibliografía

- Whelan, R. (2008). Effective analysis of reaction time data. *The Psychological Record*, 58(3), 475-482. ✅ [DOI](https://doi.org/10.1007/bf03395630)
- Ratcliff, R. (1993). Methods for dealing with reaction time outliers. *Psychological Bulletin*, 114(3), 510-532. ✅ [DOI](https://doi.org/10.1037/0033-2909.114.3.510)
- Anwyl-Irvine, A., Dalmaijer, E. S., Hodges, N., & Evershed, J. K. (2021). Realistic precision and accuracy of online experiment platforms, web browsers, and devices. *Behavior Research Methods*, 53, 1407-1425. ✅ [DOI](https://doi.org/10.3758/s13428-020-01501-5)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 092 — Atención selectiva y dividida](../092-atencion-selectiva-y-dividida/README.md)  
[📚 Parte 09](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[094 — Memoria visual y auditiva →](../094-memoria-visual-y-auditiva/README.md)
<!-- /NAV -->
