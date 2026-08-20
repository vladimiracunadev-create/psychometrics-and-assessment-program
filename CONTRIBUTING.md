# Cómo contribuir

Gracias por el interés. Este documento explica qué se acepta y con qué criterio.

## Antes de empezar

```bash
python -m pip install -e ".[dev]"
make test
make lint
make validar
```

Los tres deben pasar en limpio antes de abrir un pull request.

## Aportar un instrumento

Es la contribución más valiosa. Requisitos **no negociables**:

1. **Procedencia declarada.** `procedencia.fuente` debe apuntar a la publicación
   o al repositorio original. El cargador rechaza un archivo sin fuente.
2. **Licencia redistribuible.** Solo `dominio-publico`, `CC-BY-4.0` o
   `autoria-propia`. **No se aceptan ítems de instrumentos comerciales
   protegidos**, ni siquiera "adaptados" o "inspirados en".
3. **Estado de validación honesto.** Si el banco no tiene estudio empírico, debe
   declararlo en `procedencia.notas`. `tests/test_estructura.py` lo verifica.
4. **Texto en español e inglés** cuando la fuente lo permita.
5. **Pasar `make validar`.**

Si el instrumento se deriva de una fuente publicada, añade además un
`scripts/ingest_*.py` que lo reconstruya y **valide su propia salida**. Un parser
que no comprueba lo que produce publicará datos incompletos sin avisar.

## Aportar una clase

Las clases `planificada` de `curriculum.yaml` están abiertas. Una clase completa
lleva:

- `README.md` con propósito, resultados de aprendizaje, fundamentos, laboratorio,
  preguntas y bibliografía.
- `lab.py` **ejecutable, determinista** (semilla fija) y sin dependencias fuera
  de las declaradas.
- `lesson.yaml` con `estado: escrita`.

Regla de oro de los laboratorios: **si la salida del laboratorio contradice el
texto de la clase, se corrige el texto.** Ya ocurrió una vez y quedó documentado.

## Convención de codificación

**Prosa en castellano con tildes. Todo lo estructural en ASCII** — claves YAML,
valores de enumeración, identificadores, códigos de escala.

No es cosmética: una pasada automática de tildes acentuó las claves `codigo` y
`version` y rompió el cargador en silencio. Ver
`tests/test_estructura.py::test_claves_yaml_en_ascii`.

## Estilo

- `ruff` con la configuración de `pyproject.toml`.
- Comentarios que expliquen **por qué**, no qué.
- Mensajes de commit en imperativo y en español.

## Qué no se acepta

- Ítems de instrumentos comerciales protegidos, en cualquier forma.
- Afirmaciones de validez sin referencia verificable.
- Cifras en el README que no se puedan comprobar con un comando.
- Laboratorios no deterministas.
