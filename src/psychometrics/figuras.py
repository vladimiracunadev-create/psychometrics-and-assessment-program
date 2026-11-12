"""Generador minimo de figuras SVG (solo biblioteca estandar) para las clases.

Cada figura incluye <title> y <desc> (accesibilidad) y usa una paleta con contraste suficiente
sobre fondo claro. Las figuras se generan desde datos simulados con semilla fija, de modo que son
reproducibles: el SVG de una clase es el resultado del codigo de su `figuras.py`.
"""
from __future__ import annotations

from html import escape

AZUL, ROJO, VERDE, GRIS = "#1f5fbf", "#b3261e", "#1b7f3b", "#5f6368"
W, H = 640, 360
ML, MR, MT, MB = 64, 20, 40, 56


def _esc(t: object) -> str:
    return escape(str(t), quote=True)


class Lienzo:
    def __init__(self, titulo: str, descripcion: str, xlabel: str, ylabel: str, xr: tuple[float, float], yr: tuple[float, float]):
        self.titulo, self.desc, self.xl, self.yl, self.xr, self.yr = titulo, descripcion, xlabel, ylabel, xr, yr
        self.partes: list[str] = []

    def x(self, v: float) -> float:
        return ML + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * (W - ML - MR)

    def y(self, v: float) -> float:
        return H - MB - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (H - MB - MT)

    def ejes(self, n: int = 5) -> None:
        p = self.partes
        p.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
        for i in range(n + 1):
            vy = self.yr[0] + (self.yr[1] - self.yr[0]) * i / n
            vx = self.xr[0] + (self.xr[1] - self.xr[0]) * i / n
            p.append(f'<line x1="{ML}" x2="{W - MR}" y1="{self.y(vy):.1f}" y2="{self.y(vy):.1f}" stroke="#e3e3e3"/>')
            p.append(f'<text x="{ML - 8}" y="{self.y(vy) + 4:.1f}" text-anchor="end" font-size="11" fill="{GRIS}">{vy:.3g}</text>')
            p.append(f'<text x="{self.x(vx):.1f}" y="{H - MB + 16}" text-anchor="middle" font-size="11" fill="{GRIS}">{vx:.3g}</text>')
        p.append(f'<line x1="{ML}" x2="{ML}" y1="{MT}" y2="{H - MB}" stroke="#333"/>')
        p.append(f'<line x1="{ML}" x2="{W - MR}" y1="{H - MB}" y2="{H - MB}" stroke="#333"/>')
        p.append(f'<text x="{(ML + W - MR) / 2}" y="{H - 12}" text-anchor="middle" font-size="12" fill="#222">{_esc(self.xl)}</text>')
        p.append(f'<text transform="translate(16 {(MT + H - MB) / 2}) rotate(-90)" text-anchor="middle" font-size="12" fill="#222">{_esc(self.yl)}</text>')
        p.append(f'<text x="{ML}" y="22" font-size="14" font-weight="bold" fill="#111">{_esc(self.titulo)}</text>')

    def linea(self, xs, ys, color: str = AZUL, etiqueta: str | None = None, punteada: bool = False) -> None:
        pts = " ".join(f"{self.x(a):.1f},{self.y(b):.1f}" for a, b in zip(xs, ys, strict=True))
        dash = ' stroke-dasharray="6 4"' if punteada else ""
        self.partes.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.2"{dash}/>')
        if etiqueta:
            self.partes.append(f'<text x="{self.x(xs[-1]) - 4:.1f}" y="{self.y(ys[-1]) - 8:.1f}" text-anchor="end" font-size="11" fill="{color}">{_esc(etiqueta)}</text>')

    def puntos(self, xs, ys, color: str = AZUL, r: float = 2.4, opacidad: float = 0.55) -> None:
        for a, b in zip(xs, ys, strict=True):
            self.partes.append(f'<circle cx="{self.x(a):.1f}" cy="{self.y(b):.1f}" r="{r}" fill="{color}" fill-opacity="{opacidad}"/>')

    def barras(self, xs, ys, ancho: float, color: str = AZUL) -> None:
        for a, b in zip(xs, ys, strict=True):
            x0, x1 = self.x(a - ancho / 2), self.x(a + ancho / 2)
            self.partes.append(f'<rect x="{x0:.1f}" y="{self.y(b):.1f}" width="{x1 - x0 - 1:.1f}" height="{self.y(self.yr[0]) - self.y(b):.1f}" fill="{color}"/>')

    def vertical(self, x: float, color: str = ROJO, etiqueta: str | None = None) -> None:
        self.partes.append(f'<line x1="{self.x(x):.1f}" x2="{self.x(x):.1f}" y1="{MT}" y2="{H - MB}" stroke="{color}" stroke-width="1.6" stroke-dasharray="5 4"/>')
        if etiqueta:
            self.partes.append(f'<text x="{self.x(x) + 5:.1f}" y="{MT + 12}" font-size="11" fill="{color}">{_esc(etiqueta)}</text>')

    def texto(self, x: float, y: float, t: str, color: str = "#222") -> None:
        self.partes.append(f'<text x="{self.x(x):.1f}" y="{self.y(y):.1f}" font-size="11" fill="{color}">{_esc(t)}</text>')

    def svg(self) -> str:
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
                f'aria-labelledby="t d" font-family="Segoe UI, Arial, sans-serif"><title id="t">{_esc(self.titulo)}</title>'
                f'<desc id="d">{_esc(self.desc)}</desc>' + "".join(self.partes) + "</svg>\n")


def guardar(ruta, lienzo: Lienzo) -> None:
    import pathlib
    pathlib.Path(ruta).write_text(lienzo.svg(), encoding="utf-8")
