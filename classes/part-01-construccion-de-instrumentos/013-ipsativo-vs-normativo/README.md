# 013 — Ipsativo frente a normativo: la trampa de la elección forzada

![Portada de la clase 013](portada.svg)

<!-- NAV -->
[← 012 — Formatos de respuesta: Likert, dicotómico, co…](../012-formatos-de-respuesta/README.md) · [📚 Parte 01](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md) · [014 — Longitud del test: el intercambio entre preci… →](../014-longitud-y-costo-de-medida/README.md)
<!-- /NAV -->

**Parte:** 01 — Construcción de instrumentos
**Nivel:** fundamentos · **Horas estimadas:** 4 · **Estado:** `escrita`
**Prerrequisitos:** clases 003, 005 y 012.

## Propósito

La elección forzada resiste el falseamiento y la aquiescencia, pero tiene un
costo matemático que invalida ciertas comparaciones. Esta clase lo demuestra con
datos simulados y enseña cuándo el formato es apropiado.

## Resultados de aprendizaje

1. Definir medida ipsativa y normativa.
2. Demostrar por qué las escalas ipsativas suman una constante.
3. Predecir la correlación media inducida: −1/(k−1).
4. Decidir cuándo usar elección forzada y cuándo no.

## Fundamentos

En un formato **normativo**, cada escala se puntúa con independencia: una persona
puede puntuar alto en todas. En uno **ipsativo** debe repartir una cantidad fija
(ordenar, distribuir puntos, elegir «el más y el menos»): lo que sube una escala
baja otra. El puntaje describe la **jerarquía interna** de la persona, no su
nivel absoluto.

Consecuencias, establecidas desde Hicks (1970):

1. Las *k* escalas suman la misma constante para todos: su varianza total es cero.
2. La correlación media entre escalas es −1/(k−1), **aunque los rasgos sean independientes**.
3. Comparar a dos personas en una escala es ambiguo: una puede ser alta en todo y otra baja en todo y obtener el mismo perfil.
4. El análisis factorial y las correlaciones con criterios externos se distorsionan.

### Cuándo sirve

Para **orientar una conversación individual** («¿qué prefieres tú?») o para
reducir el falseamiento cuando todas las opciones son igual de deseables. No sirve
para rankear personas ni para estimar el nivel absoluto de un rasgo, salvo con
modelos que lo recuperan (modelos de Thurstone para elección forzada, Brown y
Maydeu-Olivares, 2011), que exigen diseños y calibración específicos.

## Ejemplo resuelto

Cuatro escalas independientes. Tras ipsatizar, la correlación media esperada es
−1/3 = −0,333. El laboratorio obtiene −0,333 con 5 000 personas simuladas, y la
suma por persona es del orden de 10⁻¹⁵ (cero numérico).

## Errores frecuentes

- Interpretar una correlación negativa entre escalas ipsativas como «rasgos opuestos».
- Comparar el puntaje ipsativo de dos personas como si fuera normativo.
- Llamar «ipsativo» a cualquier ranking sin revisar si hay suma fija.

## Limitaciones

El resultado exige escalas con varianza similar y sin relación real; con rasgos
correlacionados la cifra cambia, pero el sesgo negativo estructural permanece.

## Ejercicios

- **Inicial.** ¿Es ipsativa una Likert de 1 a 5? ¿Y repartir 100 puntos entre 5 áreas?
- **Intermedio.** Predice la correlación media con 6 escalas ipsativas independientes. (−0,20)
- **Avanzado.** Modifica `lab.py` para correlacionar dos rasgos reales con r = 0,5 antes de ipsatizar y compara con la predicción.

*Solución:* la Likert es normativa; repartir 100 puntos es ipsativo.

## Relación con el catálogo

`ipsativo: false` en los cinco YAML de `instruments/`. El DISC abierto y Valores de
Spranger usan Likert **a propósito** para que las escalas sean comparables entre personas.

## Laboratorio

```bash
python classes/part-01-construccion-de-instrumentos/013-ipsativo-vs-normativo/lab.py
```

## Autoevaluación

1. ¿Por qué la suma constante implica correlaciones negativas?
2. ¿Qué decisión de personal sería indefendible con puntajes ipsativos?
3. ¿Qué ventaja real conserva la elección forzada?

## Criterios de evaluación

El estudiante deriva la propiedad de suma constante, predice la correlación y
rechaza usos de comparación entre personas con datos ipsativos.

## Bibliografía

- Hicks, L. E. (1970). Some properties of ipsative, normative, and forced-choice normative measures. *Psychological Bulletin*, 74(3), 167-184. ✅ [DOI](https://doi.org/10.1037/h0029780)
- Cheung, M. W.-L., & Chan, W. (2002). Reducing uniform response bias with ipsative measurement in multiple-group confirmatory factor analysis. *Structural Equation Modeling*, 9(1), 55-77. ✅ [DOI](https://doi.org/10.1207/s15328007sem0901_4)
- Brown, A., & Maydeu-Olivares, A. (2011). Item response modeling of forced-choice questionnaires. *Educational and Psychological Measurement*, 71(3), 460-502. ✅ [DOI](https://doi.org/10.1177/0013164410375112)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.

---

<!-- NAV -->
[← 012 — Formatos de respuesta: Likert, dicotómico, co…](../012-formatos-de-respuesta/README.md)  
[📚 Parte 01](../README.md) · [🗺️ Índice 001–200](../../../PROGRAMA.md)  
[014 — Longitud del test: el intercambio entre preci… →](../014-longitud-y-costo-de-medida/README.md)
<!-- /NAV -->
