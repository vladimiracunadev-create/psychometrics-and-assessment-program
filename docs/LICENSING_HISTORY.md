# Historial de licenciamiento

Registro factual de la evolución de licencias. No reescribe el historial Git ni
revoca permisos ya concedidos.

## 19 de agosto de 2026 — publicación inicial bajo MIT

El commit `cea8823b5c509e9e99d821910b70c9f93e62b9` añadió todo el catálogo,
el motor, las clases y la documentación. El archivo `LICENSE` de ese commit
incluía el texto MIT y una nota expresa: MIT cubría código, documentación e
ítems propios; los bancos de terceros conservarían su situación propia.

La huella Git del blob histórico de `LICENSE` es
`9939a05d9d096a99b0778e7758636c0c14eab81c`. Los cinco YAML de instrumentos
actuales también estaban íntegros en ese primer commit y no fueron modificados
entre dicho commit y `f6800b2770eba9a0cf4aec38c1f4833861c8008c`.

Consecuencia: los permisos MIT recibidos sobre aquellas versiones permanecen.
Cambiar la oferta posterior no obliga a borrar, devolver ni relicenciar copias
obtenidas válidamente bajo MIT.

## 22 de septiembre de 2026 — separación por capas

La auditoría introducida por el commit que contiene este documento:

- conserva MIT para el software;
- ofrece la documentación educativa original actual bajo CC BY-NC-SA 4.0,
  sin afectar materiales de terceros;
- deja sin elección CC automática los nuevos ítems propios y compara las
  alternativas CC BY-NC-ND, CC BY-NC-SA y derechos reservados;
- reconoce expresamente la continuidad de la licencia MIT histórica;
- corrige O*NET Interest Profiler de “dominio público” a O*NET Tools Developer
  License y registra el riesgo de validación pendiente;
- documenta IPIP como dominio público según la declaración oficial de IPIP;
- crea inventarios, avisos de terceros y un descargo psicométrico.

## Titularidad y contribuciones observadas

El historial auditado contiene cinco commits, todos con autor Git Vladimir
Acuña `<vladimir.acuna.dev@gmail.com>`. Los cinco mensajes contienen el trailer
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`; se conserva esa
atribución, pero el historial por sí solo no demuestra titularidad humana,
cesión contractual ni derechos sobre material de terceros.

La titularidad sólo se afirma sobre redacción e implementación originales
identificables del proyecto. Las teorías, ítems de terceros, publicaciones,
marcas, hechos y material de dominio público quedan expresamente excluidos.

## Regla para cambios futuros

Toda modificación de licencia debe añadirse como una entrada nueva, con fecha,
alcance, titular habilitado y evidencia. Las referencias históricas anteriores
no se “actualizan” como si describieran el estado presente.
