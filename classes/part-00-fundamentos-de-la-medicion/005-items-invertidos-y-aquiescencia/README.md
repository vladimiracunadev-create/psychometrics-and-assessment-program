# 005 — Ítems invertidos y sesgo de aquiescencia

> [Clase anterior](../004-*/README.md) · [Índice de la parte](../README.md) · [Clase siguiente](../006-*/README.md)

**Parte:** 00 — Fundamentos de la medición psicológica
**Horas estimadas:** 4 · **Estado:** `escrita`

## Propósito

Explicar qué es el sesgo de aquiescencia, por qué los ítems invertidos son la
defensa clásica contra él, y qué precio se paga por usarlos.

## Resultados de aprendizaje

1. Definir aquiescencia y describir cómo distorsiona un perfil.
2. Reflejar correctamente un ítem invertido y justificar el orden de operaciones.
3. Explicar el costo psicométrico de los ítems invertidos.
4. Medir el equilibrio de clave de un instrumento.

## Conceptos centrales

`aquiescencia` · `clave invertida` · `reflejo` · `clave equilibrada` · `estilo de respuesta`

## Fundamentos

### El sesgo

La **aquiescencia** es la tendencia a estar de acuerdo con lo que se afirme, con
independencia del contenido. Existe en todas las poblaciones y varía entre
personas y entre culturas.

Si todos los ítems de una escala apuntan en la misma dirección, quien tiende a
asentir puntúa alto en todo. El instrumento habrá medido, en parte, un estilo de
respuesta y no el rasgo.

### La defensa

Se escribe la mitad de los ítems en dirección contraria:

| Clave | Ítem | Responder 5 significa |
|---|---|---|
| Directo (+) | *"No abandono una tarea antes de terminarla"* | mucha perseverancia |
| Invertido (−) | *"Me rindo con facilidad"* | poca perseverancia |

Quien asiente a todo obtiene ahora 5 y 5, que tras reflejar el segundo dan 5 y 1:
media 3, el punto medio. **El sesgo se cancela.**

### El reflejo, y por qué el orden importa

```
valor_reflejado = mínimo + máximo − valor_observado
```

En una Likert de 1 a 5: 1↔5, 2↔4, 3↔3.

La regla no negociable es que **el reflejo va antes de la suma**. Reflejar
después de agregar da un número distinto y equivocado. `puntuacion.py` lo hace
en el paso 1, antes de cualquier agregación, y `test_puntuacion.py` lo fija con
`test_item_invertido_se_refleja_antes_de_sumar`.

### El precio

Los ítems invertidos no son gratis:

1. **Cuestan comprensión.** Quien lee rápido o no domina el idioma se equivoca
   más en ellos. Ese error entra como ruido.
2. **Producen un factor artificial.** En análisis factorial, los invertidos
   suelen agruparse entre sí formando un factor que no corresponde a ningún
   constructo: es un artefacto del método (parte 04).
3. **Redactarlos bien es difícil.** El negativo de un rasgo no siempre es su
   ausencia. Lo contrario de "confío en los demás" no es "desconfío": puede ser
   "no me planteo la cuestión".

### El equilibrio en el catálogo

| Instrumento | Ítems | Invertidos | Proporción |
|---|---:|---:|---:|
| IPIP-NEO-120 | 120 | 55 | 46 % |
| IPIP-VIA-R | 96 | 48 | 50 % |
| DISC Abierto | 32 | 16 | 50 % |
| Valores de Spranger | 36 | 12 | 33 % |
| O*NET RIASEC SF | 60 | 0 | 0 % |

El RIASEC no tiene ninguno, y con razón: pregunta si una actividad concreta
gusta o no. Su contrario —"me disgustaría reparar cerraduras"— no aporta
información nueva y confundiría más de lo que corrige. **La técnica se aplica
donde resuelve un problema, no por costumbre.**

## Laboratorio

`lab.py` simula personas con distinta aquiescencia y muestra el perfil con y sin
ítems invertidos, cuantificando cuánto sesgo elimina la clave equilibrada.

```bash
python classes/part-00-fundamentos-de-la-medicion/005-items-invertidos-y-aquiescencia/lab.py
```

## Para pensar

1. ¿Por qué el RIASEC puede prescindir de invertidos sin quedar expuesto?
2. Si los invertidos forman un factor artificial, ¿conviene igual usarlos?
3. Escribe el invertido de *"Sé cómo sacar las cosas adelante"*. ¿Qué mide
   exactamente el que escribiste?

## Bibliografía

- Weijters, B., Baumgartner, H., & Schillewaert, N. (2013). Reversed item bias.
  *Psychological Methods*, 18(3), 320-334.
- Bluemke, M., et al. (2021). IPIP-VIA-R short scales.
