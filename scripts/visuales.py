"""Genera las portadas, mapas de ruta e iconos SVG del programa (solo biblioteca estandar).

Lo usa scripts/sync_indices.py, de modo que las imagenes siempre reflejan curriculum.yaml y
el estado real de cada clase (formato pedagogico o compacto). Cada SVG lleva <title> y <desc>.
"""
from __future__ import annotations

import textwrap
from html import escape

# (color oscuro, nombre de seccion) por parte; todos con contraste suficiente con texto blanco.
SECCION = {
    "fund": ("#1f4e8c", "Fundamentos"),
    "tec": ("#0b6e69", "Núcleo técnico"),
    "uso": ("#9b2226", "Uso responsable"),
    "dom": ("#5a3d99", "Dominios de evaluación"),
    "apl": ("#a4561b", "Infancia, educación y bienestar"),
    "ing": ("#374151", "Investigación e ingeniería"),
    "pro": ("#7a5a00", "Proyectos"),
}
PARTE_SECCION = {"00": "fund", "01": "fund", "02": "tec", "03": "tec", "04": "tec", "05": "tec", "06": "tec", "07": "uso",
                 "08": "dom", "09": "dom", "10": "dom", "11": "dom", "12": "dom", "13": "apl", "14": "apl", "15": "apl",
                 "16": "apl", "17": "ing", "18": "ing", "19": "pro"}
EMOJI = {"00": "📏", "01": "📝", "02": "📶", "03": "✅", "04": "🧩", "05": "📈", "06": "⚖️", "07": "🛡️", "08": "💡", "09": "⏱️",
         "10": "🙂", "11": "💼", "12": "👥", "13": "🧸", "14": "📖", "15": "🧭", "16": "❤️", "17": "🔬", "18": "⚙️", "19": "🏁"}

# Glifos monocromos (blancos) dibujados en un recuadro de 48 x 48.
GLIFOS = {
    "00": '<rect x="4" y="18" width="40" height="12" rx="2"/><path d="M12 18v6M20 18v8M28 18v6M36 18v8" stroke="#000" stroke-opacity=".45" stroke-width="2"/>',
    "01": '<rect x="10" y="4" width="28" height="40" rx="3"/><path d="M16 15h16M16 22h16M16 29h10" stroke="#000" stroke-opacity=".45" stroke-width="2.5"/>',
    "02": '<path d="M3 24c5-14 9-14 14 0s9 14 14 0 7-8 14-4" fill="none" stroke="#fff" stroke-width="3.5"/><path d="M3 24h42" stroke="#fff" stroke-width="1.5" stroke-dasharray="3 3"/>',
    "03": '<circle cx="24" cy="24" r="20"/><path d="M14 25l8 8 14-16" fill="none" stroke="#000" stroke-opacity=".5" stroke-width="5"/>',
    "04": '<circle cx="12" cy="12" r="6"/><circle cx="36" cy="14" r="6"/><circle cx="24" cy="38" r="6"/><path d="M12 12L36 14L24 38z" fill="none" stroke="#fff" stroke-width="2.5"/>',
    "05": '<path d="M4 40C16 40 16 8 44 8" fill="none" stroke="#fff" stroke-width="4"/><path d="M4 42h40M4 42V6" fill="none" stroke="#fff" stroke-width="1.5"/>',
    "06": '<path d="M2 40C14 40 14 8 24 8s10 32 22 32z"/>',
    "07": '<path d="M24 3l17 6v13c0 11-7 19-17 23C14 41 7 33 7 22V9z"/><path d="M16 24l6 6 11-12" fill="none" stroke="#000" stroke-opacity=".5" stroke-width="4"/>',
    "08": '<circle cx="24" cy="19" r="14"/><rect x="18" y="35" width="12" height="4" rx="2"/><rect x="20" y="41" width="8" height="3" rx="1.5"/>',
    "09": '<circle cx="24" cy="25" r="19" fill="none" stroke="#fff" stroke-width="4"/><path d="M24 25V12M24 25l9 5" stroke="#fff" stroke-width="4" stroke-linecap="round"/><rect x="19" y="2" width="10" height="4" rx="1"/>',
    "10": '<circle cx="24" cy="24" r="20"/><circle cx="17" cy="20" r="2.5" fill="#000" fill-opacity=".5"/><circle cx="31" cy="20" r="2.5" fill="#000" fill-opacity=".5"/><path d="M14 29c5 8 15 8 20 0" fill="none" stroke="#000" stroke-opacity=".5" stroke-width="3.5"/>',
    "11": '<rect x="4" y="15" width="40" height="26" rx="4"/><path d="M16 15v-4a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v4" fill="none" stroke="#fff" stroke-width="3.5"/>',
    "12": '<circle cx="24" cy="10" r="6"/><circle cx="8" cy="36" r="6"/><circle cx="40" cy="36" r="6"/><path d="M24 10L8 36L40 36z" fill="none" stroke="#fff" stroke-width="2.5"/>',
    "13": '<rect x="4" y="28" width="18" height="16" rx="2"/><rect x="26" y="28" width="18" height="16" rx="2"/><rect x="15" y="8" width="18" height="16" rx="2"/>',
    "14": '<path d="M24 12C18 7 10 7 4 9v30c6-2 14-2 20 3zM24 12c6-5 14-5 20-3v30c-6-2-14-2-20 3z"/>',
    "15": '<circle cx="24" cy="24" r="20" fill="none" stroke="#fff" stroke-width="3.5"/><path d="M24 8l7 16-7 16-7-16z"/>',
    "16": '<path d="M24 42S4 30 4 17a10 10 0 0 1 20-3 10 10 0 0 1 20 3c0 13-20 25-20 25z"/>',
    "17": '<circle cx="20" cy="20" r="14" fill="none" stroke="#fff" stroke-width="4.5"/><path d="M31 31l13 13" stroke="#fff" stroke-width="6" stroke-linecap="round"/>',
    "18": '<circle cx="24" cy="24" r="10" fill="none" stroke="#fff" stroke-width="5"/><path d="M24 2v8M24 38v8M2 24h8M38 24h8M8.5 8.5l5.5 5.5M34 34l5.5 5.5M39.5 8.5L34 14M14 34l-5.5 5.5" stroke="#fff" stroke-width="5" stroke-linecap="round"/>',
    "19": '<path d="M24 3l6.2 13.4 14.6 1.7-10.9 9.9 3 14.4L24 34.9 11.1 42.4l3-14.4L3.2 18.1l14.6-1.7z"/>',
}
FUENTE = "Segoe UI, Arial, sans-serif"


def _e(t: object) -> str:
    return escape(str(t), quote=True)


def glifo(pid: str, x: float, y: float, escala: float = 1.0) -> str:
    return f'<g transform="translate({x} {y}) scale({escala})" fill="#ffffff">{GLIFOS[pid]}</g>'


def _lineas(texto: str, ancho: int, maximo: int) -> list[str]:
    ls = textwrap.wrap(texto, ancho)
    if len(ls) > maximo:
        ls = ls[:maximo]
        ls[-1] = ls[-1].rstrip(" .,;:") + "…"
    return ls


def _marco(w: int, h: int, titulo: str, desc: str, cuerpo: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-labelledby="t d" font-family="{FUENTE}"><title id="t">{_e(titulo)}</title><desc id="d">{_e(desc)}</desc>{cuerpo}</svg>\n')


def portada_parte(p: dict) -> str:
    color, sec = SECCION[PARTE_SECCION[p["id"]]]
    n = len(p["clases"])
    ped = sum(1 for c in p["clases"] if c.get("pedagogico"))
    t = _lineas(p["titulo"], 34, 2)
    cuerpo = (f'<rect width="900" height="190" rx="14" fill="{color}"/>'
              f'<circle cx="780" cy="40" r="150" fill="#ffffff" fill-opacity=".07"/><circle cx="860" cy="170" r="110" fill="#ffffff" fill-opacity=".06"/>'
              f'<g transform="translate(40 52) scale(2.2)">{GLIFOS[p["id"]]}</g>'
              f'<text x="180" y="52" font-size="16" fill="#ffffff" fill-opacity=".85" letter-spacing="2">PARTE {p["id"]} · {_e(sec.upper())}</text>')
    for i, ln in enumerate(t):
        cuerpo += f'<text x="180" y="{96 + i * 38}" font-size="32" font-weight="bold" fill="#ffffff">{_e(ln)}</text>'
    cuerpo += (f'<text x="180" y="{96 + len(t) * 38 + 8}" font-size="16" fill="#ffffff" fill-opacity=".9">'
               f'Nivel {_e(p["nivel"])} · {n} clases · {_e(p["semanas"])} semanas · {ped} con formato pedagógico completo</text>')
    return _marco(900, 190, f"Parte {p['id']}: {p['titulo']}", f"Portada de la parte {p['id']}, sección {sec}, con {n} clases.", cuerpo)


def ruta_parte(p: dict) -> str:
    color, _ = SECCION[PARTE_SECCION[p["id"]]]
    cs = p["clases"]
    w, h = 900, 330
    filas = [cs[:5], cs[5:]]
    cuerpo = [f'<rect width="{w}" height="{h}" rx="14" fill="#f7f8fa" stroke="#d9dde3"/>',
              f'<text x="24" y="32" font-size="16" font-weight="bold" fill="#111">Ruta de estudio · de la clase {cs[0]["id"]} a la {cs[-1]["id"]}</text>']
    for r, fila in enumerate(filas):
        y = 90 + r * 125
        cuerpo.append(f'<line x1="70" y1="{y}" x2="{w - 70}" y2="{y}" stroke="{color}" stroke-width="4" stroke-opacity=".35"/>')
        for i, c in enumerate(fila):
            x = 70 + i * (w - 140) / 4
            lleno = bool(c.get("pedagogico"))
            fill, txt = (color, "#ffffff") if lleno else ("#ffffff", color)
            cuerpo.append(f'<circle cx="{x:.1f}" cy="{y}" r="26" fill="{fill}" stroke="{color}" stroke-width="3"/>')
            cuerpo.append(f'<text x="{x:.1f}" y="{y + 6}" text-anchor="middle" font-size="16" font-weight="bold" fill="{txt}">{c["id"]}</text>')
            for j, ln in enumerate(_lineas(c["titulo"], 22, 3)):
                cuerpo.append(f'<text x="{x:.1f}" y="{y + 48 + j * 15}" text-anchor="middle" font-size="12" fill="#222">{_e(ln)}</text>')
    cuerpo.append(f'<circle cx="30" cy="{h - 18}" r="7" fill="{color}"/><text x="44" y="{h - 13}" font-size="12" fill="#333">formato pedagógico completo</text>'
                  f'<circle cx="260" cy="{h - 18}" r="7" fill="#fff" stroke="{color}" stroke-width="2.5"/><text x="274" y="{h - 13}" font-size="12" fill="#333">formato compacto (en reescritura)</text>')
    return _marco(w, h, f"Ruta de la parte {p['id']}", "Diez clases en secuencia; el círculo lleno indica formato pedagógico completo.", "".join(cuerpo))


def portada_clase(p: dict, c: dict) -> str:
    color, _ = SECCION[PARTE_SECCION[p["id"]]]
    t = _lineas(c["titulo"], 52, 2)
    cuerpo = (f'<rect width="900" height="120" rx="12" fill="{color}"/>'
              f'<circle cx="840" cy="20" r="90" fill="#ffffff" fill-opacity=".07"/>'
              f'<g transform="translate(26 34) scale(1.1)">{GLIFOS[p["id"]]}</g>'
              f'<text x="100" y="30" font-size="14" fill="#ffffff" fill-opacity=".85" letter-spacing="1.5">CLASE {c["id"]} · PARTE {p["id"]} · {_e(p["titulo"].upper()[:48])}</text>')
    for i, ln in enumerate(t):
        cuerpo += f'<text x="100" y="{62 + i * 28}" font-size="24" font-weight="bold" fill="#ffffff">{_e(ln)}</text>'
    cuerpo += f'<text x="100" y="{62 + len(t) * 28 + 6}" font-size="13" fill="#ffffff" fill-opacity=".9">{c["horas_estimadas"]} h · nivel {_e(p["nivel"])}</text>'
    return _marco(900, 120, f"Clase {c['id']}: {c['titulo']}", f"Portada de la clase {c['id']} de la parte {p['id']}.", cuerpo)


def mapa_programa(partes: list[dict]) -> str:
    w, h = 900, 565
    cuerpo = [f'<rect width="{w}" height="{h}" rx="14" fill="#ffffff" stroke="#d9dde3"/>',
              '<text x="24" y="34" font-size="18" font-weight="bold" fill="#111">Mapa del programa · 20 partes · 200 clases</text>']
    for i, p in enumerate(partes):
        col, fila = i % 5, i // 5
        x, y = 24 + col * 174, 56 + fila * 114
        color, _ = SECCION[PARTE_SECCION[p["id"]]]
        ids = p["clases"]
        cuerpo.append(f'<rect x="{x}" y="{y}" width="162" height="102" rx="10" fill="{color}"/>')
        cuerpo.append(glifo(p["id"], x + 10, y + 10, 0.7))
        cuerpo.append(f'<text x="{x + 52}" y="{y + 28}" font-size="12" fill="#fff" fill-opacity=".85">PARTE {p["id"]}</text>')
        cuerpo.append(f'<text x="{x + 52}" y="{y + 44}" font-size="11" fill="#fff" fill-opacity=".85">{ids[0]["id"]}–{ids[-1]["id"]}</text>')
        for j, ln in enumerate(_lineas(p["titulo"], 22, 3)):
            cuerpo.append(f'<text x="{x + 10}" y="{y + 66 + j * 14}" font-size="12" font-weight="bold" fill="#fff">{_e(ln)}</text>')
    lx = 24
    for k, (c, nombre) in SECCION.items():
        cuerpo.append(f'<rect x="{lx}" y="{h - 34}" width="14" height="14" rx="3" fill="{c}"/><text x="{lx + 20}" y="{h - 22}" font-size="11" fill="#333">{_e(nombre)}</text>')
        lx += 20 + 7 * len(nombre) + 14
    return _marco(w, h, "Mapa del programa", "Veinte partes agrupadas en siete secciones, con su rango de clases.", "".join(cuerpo))
