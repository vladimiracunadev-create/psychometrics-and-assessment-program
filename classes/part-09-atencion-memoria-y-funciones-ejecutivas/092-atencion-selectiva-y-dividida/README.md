# 092 — Atención selectiva y dividida

> [Índice de la parte](../README.md)

**Parte 09 — Atención, memoria y funciones ejecutivas** · Nivel intermedio · 4 h · Estado `escrita`
**Prerrequisitos:** clase 091.

## Objetivos

1. Distinguir búsqueda de rasgo y de conjunción.
2. Calcular pendientes tiempo–tamaño del conjunto.
3. Interpretar el costo de doble tarea.

## Fundamentos

En la búsqueda visual, el tiempo de respuesta puede crecer con el número de elementos (búsqueda serial) o ser casi plano (búsqueda en paralelo) (Treisman y Gelade, 1980). La **pendiente** (ms por elemento) es el indicador. En atención dividida, el **costo de doble tarea** es el aumento relativo del tiempo cuando se realizan dos tareas a la vez; es mayor si compiten por el mismo recurso (Wickens, 2002).

Laboratorio (100 personas simuladas):

| Medida | Valor |
|---|---:|
| Pendiente de búsqueda de rasgo | 0,40 ms/elemento (DE entre personas 0,87) |
| Pendiente de búsqueda de conjunción | 12,45 ms/elemento (DE 0,72) |
| Costo de doble tarea con recursos distintos | 4,0 % |
| Costo de doble tarea con el mismo recurso | 35,4 % |

## Ejemplo resuelto

Con pendiente 12 ms/elemento, pasar de 8 a 32 elementos suma 24·12 = 288 ms.

## Errores y límites

- Hablar de «atención» como un solo constructo.
- Usar una tarea de laboratorio para inferir conducta en el aula sin evidencia ecológica (clase 057).
- Las pendientes son medidas diferenciales con fiabilidad individual limitada (clase 097).
- Los parámetros son ilustrativos.

## Ejercicios

- **Inicial.** ¿Qué indica una pendiente cercana a 0?
- **Intermedio.** Si el RT base es 500 ms y la pendiente 12 ms, ¿RT esperado con 20 elementos? 740 ms.
- **Avanzado.** Añade en `lab.py` un costo asimétrico (tarea A cuesta más que B) y descríbelo.

## Laboratorio

```bash
python classes/part-09-atencion-memoria-y-funciones-ejecutivas/092-atencion-selectiva-y-dividida/lab.py
```

## Autoevaluación y criterios

1. ¿Qué tareas de la vida diaria requieren atención dividida? 2. ¿Qué prueba de «atención» usarías para una pregunta concreta? 3. ¿Qué limita la generalización?
Se logra si el estudiante vincula cada indicador con un tipo de atención.

## Bibliografía

- Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97-136. ✅ [DOI](https://doi.org/10.1016/0010-0285(80)90005-5)
- Wickens, C. D. (2002). Multiple resources and performance prediction. *Theoretical Issues in Ergonomics Science*, 3(2), 159-177. ✅ [DOI](https://doi.org/10.1080/14639220210123806)

Leyenda: ✅ existe en Crossref con título y año coincidentes (enlace al DOI); ⚠️ el título existe pero con otro año (reedición); 🔎 no verificada automáticamente. Crossref confirma la existencia de la fuente, no que respalde cada afirmación de la clase.
