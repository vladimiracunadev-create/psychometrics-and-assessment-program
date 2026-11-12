"""Laboratorio 199 - Proyecto: borrador de un instrumento original y su protocolo de validacion.

Se redacta un BANCO de 16 items originales de "organizacion del estudio" (2 escalas de 8 items) y se
audita con reglas automaticas: items por escala, equilibrio de claves positivas/negativas, items de
doble pregunta (contienen " y " o " o "), longitud, y dobles negaciones. Luego se imprime el protocolo
de validacion con PRE-REGISTRO de criterios de decision. El instrumento NO se agrega al catalogo y NO
esta validado: es un borrador que necesita revision de expertos, entrevistas cognitivas y un estudio
con personas reales (clase 193). Items de autoria propia, sin material de terceros.
"""
from __future__ import annotations

BANCO = [
    ("PLAN", 1, "Antes de estudiar, decido que voy a avanzar ese dia."),
    ("PLAN", 1, "Reservo horarios concretos para estudiar cada semana."),
    ("PLAN", 1, "Divido las tareas grandes en partes mas pequenas."),
    ("PLAN", 1, "Reviso mi calendario de entregas con anticipacion."),
    ("PLAN", -1, "Dejo para el ultimo momento lo que tengo que entregar."),
    ("PLAN", -1, "Empiezo a estudiar sin saber que tema me falta."),
    ("PLAN", -1, "Se me pasan las fechas de entrega."),
    ("PLAN", -1, "Me cuesta decidir por donde comenzar."),
    ("FOCO", 1, "Cuando estudio, silencio las notificaciones."),
    ("FOCO", 1, "Puedo mantener la atencion en una tarea durante un rato largo."),
    ("FOCO", 1, "Vuelvo a la tarea con facilidad despues de una interrupcion."),
    ("FOCO", 1, "Elijo un lugar tranquilo para trabajar."),
    ("FOCO", -1, "Reviso el telefono cada pocos minutos mientras estudio."),
    ("FOCO", -1, "Me distraigo con cualquier ruido."),
    ("FOCO", -1, "Abro otras paginas cuando deberia estar leyendo."),
    ("FOCO", -1, "Salto de una tarea a otra sin terminar ninguna."),
]


def auditar() -> list[tuple[str, bool, str]]:
    res = []
    for esc in ("PLAN", "FOCO"):
        its = [b for b in BANCO if b[0] == esc]
        pos = sum(c == 1 for _, c, _ in its)
        res.append((f"{esc}: 8 items", len(its) == 8, f"{len(its)} items"))
        res.append((f"{esc}: claves equilibradas (4/4)", pos == len(its) - pos, f"{pos} positivas y {len(its) - pos} negativas"))
    dobles = [t for _, _, t in BANCO if " y " in t.lower() or " o " in t.lower()]
    res.append(("sin items de doble pregunta", not dobles, f"{len(dobles)} sospechosos: {dobles}"))
    largos = [t for _, _, t in BANCO if len(t.split()) > 16]
    res.append(("items de 16 palabras o menos", not largos, f"{len(largos)} largos"))
    neg2 = [t for _, c, t in BANCO if c == -1 and (" no " in t.lower() or "nunca" in t.lower())]
    res.append(("sin dobles negaciones en items invertidos", not neg2, f"{len(neg2)} casos"))
    return res


PROTOCOLO = [
    ("1 revision de expertos", "6 o mas jueces; I-CVI >= 0.78 por item"),
    ("2 entrevistas cognitivas", "10 personas; reescribir lo que se interprete distinto"),
    ("3 piloto", "n >= 200; alfa >= 0.70 por escala; eliminar items con correlacion item-resto < 0.20"),
    ("4 estructura", "analisis factorial con paralelo: se espera 2 factores; si no, se revisa la teoria"),
    ("5 validez", "convergente con una medida abierta y verificada; discriminante con una no relacionada"),
    ("6 equidad", "DIF por sexo y tipo de colegio; invarianza antes de comparar grupos"),
    ("7 decision", "los umbrales se fijan ANTES de ver los datos y se registran (preregistro)"),
]


def main() -> None:
    print("Auditoria automatica del banco:")
    for nombre, ok, det in auditar():
        print(f"  [{'ok' if ok else 'FALLA'}] {nombre:<44} {det}")
    print("\nProtocolo de validacion (criterios fijados antes de recolectar):")
    for e, c in PROTOCOLO:
        print(f"  {e:<26} {c}")
    print()
    print("Lectura: las reglas automaticas detectan problemas de redaccion y de equilibrio, no calidad psicometrica.")
    print("El borrador esta SIN VALIDAR y no se publica como test. Los umbrales del protocolo son convenciones de uso")
    print("comun, no verdades; se justifican y se fijan antes de ver los datos para evitar decidir segun el resultado.")


if __name__ == "__main__":
    main()
