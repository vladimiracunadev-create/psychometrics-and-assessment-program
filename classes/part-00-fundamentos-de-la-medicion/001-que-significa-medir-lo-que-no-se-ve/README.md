# 001 — Qué significa medir lo que no se ve

![Portada de la clase 001](portada.svg)

> Inicio del programa · [Índice de la parte](../README.md) · [Clase siguiente](../002-del-constructo-al-item/README.md)

**Parte 00 — Fundamentos de la medición psicológica** · Nivel fundamentos · 4 h · Estado `escrita`
**Pensada para:** quien construye un instrumento, quien lo interpreta y quien es evaluado.
**Prerrequisitos:** ninguno.

## ¿Para qué te sirve esto?

Alguien te entrega un informe que dice «responsabilidad: 84 puntos». ¿Es mucho? ¿Quién lo midió y con qué? ¿Qué cambiaría si respondieras de nuevo mañana? Estas preguntas valen igual para quien diseña la prueba, para quien la interpreta en un colegio o una empresa y para quien la contesta. Esta clase explica **qué se afirma realmente** cuando se dice que un cuestionario «mide» algo que nadie puede ver, y por qué esa afirmación necesita pruebas.

## Al terminar esta clase podrás

- Distinguir un constructo (la idea) de su indicador (lo que se observa).
- Explicar por qué un puntaje aislado no significa nada sin una referencia.
- Reconocer los dos modos en que falla la medición psicológica: ruido y desvío.
- Explicar por qué un test usa muchos ítems y no uno solo.

## La idea en palabras simples

Una cinta métrica toca el objeto que mide. Un cuestionario no toca la responsabilidad de nadie. Cuando una persona responde «Siempre estoy preparado» con un 4 de 5, lo único observado es **una marca en un formulario**. Todo lo demás es inferencia: de la marca a la conducta, de la conducta al rasgo.

Piensa en un médico que no puede ver la fiebre, pero ve el termómetro, la piel enrojecida y el cansancio. Ninguna señal es la fiebre; juntas la hacen creíble. La psicometría hace lo mismo con rasgos como la ansiedad o el interés vocacional: **reúne varias señales y examina si apuntan a una misma causa**.

![Cadena de inferencia de seis pasos, del rasgo no observable a la interpretación del puntaje](figura-1.svg)

*Figura 1.* La cadena completa. Cada flecha es un supuesto que puede fallar; la psicometría se ocupa de ponerlos a prueba.

## Cómo funciona, paso a paso

**1. Constructo.** Es una abstracción que se postula para explicar regularidades. Nadie ha visto la extraversión; se postula porque quien va a muchas fiestas también tiende a hablar con desconocidos, y esas conductas covarían.

**2. Indicador.** Es algo observable que se supone relacionado con el constructo. El ítem «Hago amigos con facilidad» es un indicador de cordialidad. El error más común es tratar el indicador como si fuera el constructo: un puntaje alto en un test de ansiedad *no es* ansiedad, es un puntaje del que se infiere ansiedad, con un margen de error.

**3. El supuesto central.** Si varios indicadores distintos covarían, es razonable postular una causa común. Por eso un test tiene muchos ítems: un ítem aislado mezcla el rasgo con su circunstancia (quien responde «Siempre estoy preparado» puede estar pensando en el examen de ayer). Al promediar muchos ítems, las circunstancias particulares tienden a cancelarse y lo compartido, el rasgo, se acumula.

**4. Cómo puede fallar.** De dos maneras, y cada una tiene su parte en este programa:

- Los indicadores covarían **por otra cosa** (el estilo de respuesta, la deseabilidad social, el vocabulario): problema de **validez** (parte 03).
- Los indicadores covarían tan poco que no sostienen una causa común: problema de **fiabilidad** (parte 02).

**5. Medir un rasgo no es medir una longitud.**

| | Longitud | Rasgo psicológico |
|---|---|---|
| Unidad | Definida y constante (el metro) | No existe unidad natural |
| Cero | Absoluto y significativo | Arbitrario: no hay «cero responsabilidad» |
| Acceso | Directo | Solo por indicadores |
| Comparación | Universal | Requiere una muestra de referencia |

De la tabla se sigue la consecuencia más importante: **un puntaje psicológico aislado no significa nada**. Sacar 84 no es alto ni bajo hasta saber cuántos ítems tiene la escala, en qué rango se mueve y con quién se compara (parte 06).

## Si construyes el instrumento

- Define primero el constructo con palabras, antes de escribir un solo ítem (clase 002).
- Escribe varios indicadores por constructo; un ítem aislado casi nunca basta.
- Declara cuántos ítems tiene cada puntaje y cómo se calcula. Este repositorio nunca informa un puntaje bruto sin su media por ítem y su número de ítems respondidos.
- Anticipa las dos fallas: planifica cómo estimar la fiabilidad y cómo reunir evidencia de validez.

## Si eres evaluado

- Tu puntaje es una **inferencia**, no una medida directa. Es razonable preguntar con qué grupo te comparan y cuántos ítems respaldan cada resultado.
- Un solo número no resume quién eres. Pide siempre el contexto: para qué se usará y qué otra información existe.
- Si una persona sin formación te «lee» tu perfil como una verdad, desconfía: el perfil es una hipótesis que hay que contrastar.

## Qué muestra el laboratorio

`lab.py` simula un rasgo latente en 500 personas, genera respuestas a ítems que lo reflejan con ruido y calcula cuánto se parece el puntaje observado al rasgo verdadero a medida que se agregan ítems.

![Curva que sube de 0,68 con un ítem a 0,995 con 120 ítems](figura-2.svg)

| Ítems | Correlación con el rasgo | r² |
|---:|---:|---:|
| 1 | 0,677 | 0,458 |
| 4 | 0,881 | 0,777 |
| 16 | 0,967 | 0,935 |
| 120 | 0,995 | 0,990 |

**Análisis.** (1) Con un solo ítem, el puntaje comparte menos de la mitad de su varianza con el rasgo (r² = 0,46): más de la mitad es ruido. (2) Cada duplicación de ítems ayuda menos que la anterior (rendimientos decrecientes): de 1 a 4 ítems se gana 0,20; de 16 a 120, solo 0,03. (3) Por eso el IPIP-NEO-120 tiene 120 ítems, pero también por eso no tiene 1.000: el costo es el tiempo y el cansancio de la persona (clase 014). (4) Es una simulación con ruido independiente; en la vida real, ítems mal redactados pueden compartir un error que no se cancela por más que se agreguen.

## Errores frecuentes

- Confundir el indicador con el constructo.
- Creer que un número tiene sentido sin su referencia.
- Pensar que más ítems arreglan cualquier problema: no corrigen un desvío sistemático.
- Tratar la medición psicológica como «menos científica» por no ser directa: lo que exige es declarar y probar los supuestos.

## Lo mínimo que debes llevarte

1. Lo observado es una respuesta; el rasgo se infiere.
2. Varios indicadores que covarían sostienen mejor una causa común que uno solo.
3. La medición puede fallar por ruido (fiabilidad) o por desvío (validez).
4. Un puntaje sin referencia no significa nada.

## Ejercicios

- **Inicial.** Nombra un constructo y dos indicadores observables. *Ej.: «curiosidad»: preguntas que hace en clase; libros que pide prestados.*
- **Intermedio.** Un test de una sola pregunta («¿Eres feliz?») puede servir en algún caso. ¿En cuál? *Respuesta guía: cuando se busca un cribado rápido y se acepta un margen de error grande, y el constructo es simple y comprensible por todos.*
- **Avanzado.** Cambia el ruido de `lab.py` a 2,0 y estima cuántos ítems necesitas para alcanzar r = 0,95.
- **Aplicación.** Revisa un informe de evaluación real (anonimizado) y marca qué afirmaciones son observaciones y cuáles son inferencias.

## Glosario

- **Constructo:** idea abstracta que se postula para explicar conductas.
- **Indicador:** algo observable que se supone relacionado con el constructo.
- **Variable latente:** variable que no se observa y se infiere de indicadores.
- **Operacionalización:** decidir cómo se observará un constructo.
- **Inferencia:** conclusión que va más allá de lo directamente observado.

## Laboratorio

```bash
python classes/part-00-fundamentos-de-la-medicion/001-que-significa-medir-lo-que-no-se-ve/lab.py
python classes/part-00-fundamentos-de-la-medicion/001-que-significa-medir-lo-que-no-se-ve/figuras.py
```

## Autoevaluación y criterios

1. La estatura tiene un cero absoluto; la extraversión no. ¿Qué operaciones aritméticas deja de autorizar esa diferencia? 2. Si dos personas obtienen el mismo puntaje, ¿son iguales en el rasgo? ¿Qué necesitarías saber? 3. ¿Por qué un test usa muchos ítems?
Se logra la clase si puedes explicar la cadena de inferencia a alguien sin formación y dar un ejemplo de cada modo de falla.

## Fuentes

**Libros y artículos**
- Borsboom, D. (2005). *Measuring the Mind: Conceptual Issues in Contemporary Psychometrics*. Cambridge University Press. 🔎 sin verificar automáticamente (libro).
- Michell, J. (1999). *Measurement in Psychology*. Cambridge University Press. ✅ [DOI](https://doi.org/10.1017/cbo9780511490040)
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*. 🔎 sin verificar automáticamente (norma).

Leyenda: ✅ existe en Crossref con título y año coincidentes; ⚠️ año o edición distinta; 🔎 pendiente de comprobar a mano. Confirmar la existencia de una fuente no prueba que respalde cada afirmación de la clase. Estado general en [`docs/VERIFICACION_BIBLIOGRAFIA.md`](../../../docs/VERIFICACION_BIBLIOGRAFIA.md).
