"""Puntuación de instrumentos: de respuestas crudas a un perfil interpretable.

Tres decisiones de diseño que conviene tener presentes al leer este módulo:

1. Los ítems invertidos se reflejan ANTES de sumar, usando el rango declarado de
   la escala de respuesta. Reflejar después de agregar da un resultado distinto
   y silenciosamente equivocado.

2. Las omisiones no valen cero. Un cero en una Likert de 1 a 5 no existe, y
   tratarlo así arrastra el puntaje hacia abajo. Se excluyen del cálculo y se
   informan; si superan un umbral, la escala se marca como poco fiable.

3. El puntaje comparable es la MEDIA POR ÍTEM, no el bruto. El bruto depende de
   cuántos ítems tenga la escala, así que comparar un dominio de 24 ítems con
   una faceta de 4 usando brutos no significa nada.
"""

from __future__ import annotations

from .modelos import Instrumento, PuntajeEscala, Respuesta, Resultado, TipoRespuesta

# Si falta más de un tercio de los ítems de una escala, el puntaje se emite
# igual pero acompañado de una advertencia: es un dato, no un veredicto.
UMBRAL_OMISION = 1 / 3


class RespuestaFueraDeRango(ValueError):
    """Se recibió un valor que la escala de respuesta del instrumento no admite."""


def _rango(instrumento: Instrumento) -> tuple[int, int]:
    if not instrumento.opciones:
        raise ValueError(f"{instrumento.codigo}: no declara opciones de respuesta")
    valores = [o.valor for o in instrumento.opciones]
    return min(valores), max(valores)


def _reflejar(valor: int, minimo: int, maximo: int) -> int:
    """Invierte un valor dentro del rango declarado: 1<->5, 2<->4, 3<->3."""
    return minimo + maximo - valor


def puntuar(
    instrumento: Instrumento,
    respuestas: list[Respuesta],
    *,
    estricto: bool = True,
) -> Resultado:
    """Convierte respuestas en un perfil de puntajes por escala.

    Args:
        instrumento: el test administrado.
        respuestas: una por ítem respondido; las ausentes cuentan como omitidas.
        estricto: si True, un valor fuera de rango lanza excepción. Si False, se
            trata como omisión y se anota una advertencia.
    """
    if instrumento.tipo_respuesta is not TipoRespuesta.LIKERT:
        raise NotImplementedError(
            f"{instrumento.codigo}: la puntuación de {instrumento.tipo_respuesta.value} "
            "vive en scoring/ipsativo.py; este módulo solo cubre Likert"
        )

    minimo, maximo = _rango(instrumento)
    advertencias: list[str] = []

    por_id = {r.item_id: r for r in respuestas}
    desconocidas = sorted(set(por_id) - {i.id for i in instrumento.items})
    if desconocidas:
        advertencias.append(
            f"{len(desconocidas)} respuestas no corresponden a ningún ítem y se "
            f"ignoraron: {', '.join(desconocidas[:5])}"
            + ("..." if len(desconocidas) > 5 else "")
        )

    # Paso 1: valor efectivo de cada ítem, ya reflejado si es de clave invertida.
    efectivo: dict[str, int] = {}
    omitidas = 0
    for item in instrumento.items:
        r = por_id.get(item.id)
        if r is None or r.valor is None:
            omitidas += 1
            continue
        if not minimo <= r.valor <= maximo:
            if estricto:
                raise RespuestaFueraDeRango(
                    f"ítem {item.id}: valor {r.valor} fuera del rango "
                    f"[{minimo}, {maximo}] declarado por {instrumento.codigo}"
                )
            advertencias.append(
                f"ítem {item.id}: valor {r.valor} fuera de rango, tratado como omisión"
            )
            omitidas += 1
            continue
        efectivo[item.id] = r.valor if item.clave == 1 else _reflejar(r.valor, minimo, maximo)

    # Paso 2: agregación por escala hoja.
    puntajes: dict[str, PuntajeEscala] = {}
    for escala in instrumento.escalas:
        if instrumento.hijas_de(escala.codigo):
            continue  # las compuestas se resuelven en el paso 3
        items = instrumento.items_de(escala.codigo)
        valores = [efectivo[i.id] for i in items if i.id in efectivo]
        puntajes[escala.codigo] = _construir(escala.codigo, valores, len(items), advertencias)

    # Paso 3: escalas compuestas. Se agregan desde los ÍTEMS de sus hojas, no
    # promediando medias: si las facetas tuvieran distinto número de ítems, el
    # promedio de promedios daría un peso artificialmente igual a cada faceta.
    for escala in instrumento.escalas:
        hijas = instrumento.hijas_de(escala.codigo)
        if not hijas:
            continue
        ids = [i.id for h in hijas for i in instrumento.items_de(h.codigo)]
        valores = [efectivo[i] for i in ids if i in efectivo]
        puntajes[escala.codigo] = _construir(escala.codigo, valores, len(ids), advertencias)

    # Paso 4: control de calidad del protocolo completo.
    if efectivo and len(set(efectivo.values())) == 1:
        advertencias.append(
            "todas las respuestas son idénticas: el protocolo sugiere respuesta "
            "en línea recta y no debería interpretarse"
        )
    if instrumento.items and omitidas / len(instrumento.items) > UMBRAL_OMISION:
        advertencias.append(
            f"se omitió el {omitidas / len(instrumento.items):.0%} del instrumento; "
            "el perfil completo es poco fiable"
        )

    return Resultado(
        instrumento=instrumento.codigo,
        version=instrumento.version,
        puntajes=puntajes,
        omitidas=omitidas,
        advertencias=tuple(advertencias),
    )


def _construir(
    codigo: str, valores: list[int], total: int, advertencias: list[str]
) -> PuntajeEscala:
    respondidos = len(valores)
    bruto = float(sum(valores))
    media = bruto / respondidos if respondidos else 0.0
    if total and respondidos / total < 1 - UMBRAL_OMISION:
        advertencias.append(
            f"escala {codigo}: solo {respondidos} de {total} ítems respondidos"
        )
    return PuntajeEscala(
        codigo=codigo,
        bruto=bruto,
        items_respondidos=respondidos,
        items_totales=total,
        media_item=round(media, 4),
    )


def ordenar_por_media(resultado: Resultado, codigos: list[str]) -> list[tuple[str, float]]:
    """Devuelve (código, media) ordenado de mayor a menor.

    Es la operación base del código Holland de tres letras y de cualquier
    ranking de escalas dentro de una misma persona.
    """
    pares = [(c, resultado[c].media_item) for c in codigos if c in resultado.puntajes]
    return sorted(pares, key=lambda p: (-p[1], p[0]))
