"""Interfaz de línea de comandos del programa.

    psychometrics catalogo              lista los instrumentos disponibles
    psychometrics ficha <codigo>        detalle de un instrumento y su procedencia
    psychometrics rendir <codigo>       administra el test en la terminal
    psychometrics puntuar <codigo> -e   puntúa respuestas desde un JSON
    psychometrics validar               valida todo el catálogo
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

from .motor import (
    Instrumento,
    InstrumentoInvalido,
    Respuesta,
    Resultado,
    cargar,
    catalogo,
    ordenar_por_media,
    puntuar,
)

IDIOMA = "es"


def _salida_utf8() -> None:
    """Windows abre la consola en cp1252 y rompe las tildes al imprimir."""
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8", errors="replace")


def cmd_catalogo(_: argparse.Namespace) -> int:
    instrumentos = catalogo()
    print(f"{len(instrumentos)} instrumentos en el catálogo\n")
    for i in instrumentos:
        dur = f"{i.duracion_min[0]}-{i.duracion_min[1]} min" if i.duracion_min else "-"
        aviso = "" if i.procedencia.licencia.value != "autoria-propia" else "  [SIN VALIDAR]"
        print(f"  {i.codigo:18} {len(i.items):3} ítems  {dur:>10}  "
              f"{i.procedencia.licencia.value:16}{aviso}")
        print(f"  {'':18} {i.nombre.get(IDIOMA, i.codigo)}")
    return 0


def cmd_ficha(args: argparse.Namespace) -> int:
    i = cargar(args.codigo)
    print(f"\n{i.nombre.get(IDIOMA, i.codigo)}  (v{i.version})")
    print("=" * 72)
    print(i.descripcion.get(IDIOMA, "").strip())
    print()
    print(f"  Ítems            {len(i.items)}")
    print(f"  Escalas          {len(i.escalas)} "
          f"({len(i.raices)} raíz + {len(i.escalas) - len(i.raices)} derivadas)")
    print(f"  Formato          {i.tipo_respuesta.value}, "
          f"{len(i.opciones)} puntos" if i.opciones else f"  Formato          {i.tipo_respuesta.value}")
    if i.duracion_min:
        print(f"  Duración         {i.duracion_min[0]}-{i.duracion_min[1]} minutos")
    print(f"  Ipsativo         {'sí (no comparable entre personas)' if i.ipsativo else 'no'}")
    print()
    print("PROCEDENCIA")
    print(f"  Autores          {i.procedencia.autores}")
    print(f"  Año              {i.procedencia.anio}")
    print(f"  Fuente           {i.procedencia.fuente}")
    print(f"  Licencia         {i.procedencia.licencia.value}")
    if i.procedencia.cita:
        print(f"  Cita             {' '.join(i.procedencia.cita.split())}")
    for clave, valor in i.procedencia.notas.items():
        print(f"  · {clave}: {' '.join(valor.split())}")
    print()
    print("ESCALAS")
    for raiz in i.raices:
        n = len(i.items_de(raiz.codigo)) or sum(
            len(i.items_de(h.codigo)) for h in i.hijas_de(raiz.codigo)
        )
        print(f"  {raiz.codigo:8} {raiz.rotulo(IDIOMA):34} {n:3} ítems")
        for hija in i.hijas_de(raiz.codigo):
            alfa = f"α={hija.alfa:.2f}" if hija.alfa else ""
            print(f"    {hija.codigo:6} {hija.rotulo(IDIOMA):32} "
                  f"{len(i.items_de(hija.codigo)):3} ítems  {alfa}")
    return 0


def cmd_rendir(args: argparse.Namespace) -> int:
    i = cargar(args.codigo)
    print(f"\n{i.nombre.get(IDIOMA, i.codigo)}")
    print("=" * 72)
    print(i.descripcion.get(IDIOMA, "").strip())
    print("\nResponde con el número. Enter en blanco = omitir. 'x' = salir.\n")
    for o in i.opciones:
        print(f"  {o.valor} = {o.etiqueta.get(IDIOMA, o.valor)}")
    print()

    respuestas: list[Respuesta] = []
    validos = {o.valor for o in i.opciones}
    for n, item in enumerate(i.items, 1):
        while True:
            crudo = input(f"[{n:3}/{len(i.items)}] {item.enunciado(IDIOMA)}\n  > ").strip()
            if crudo.lower() == "x":
                print("\nInterrumpido.")
                return 130
            if not crudo:
                respuestas.append(Respuesta(item.id, None))
                break
            if crudo.isdigit() and int(crudo) in validos:
                respuestas.append(Respuesta(item.id, int(crudo)))
                break
            print(f"  valor inválido; usa {sorted(validos)}")

    resultado = puntuar(i, respuestas)
    _imprimir(i, resultado)
    if args.salida:
        ruta = pathlib.Path(args.salida)
        ruta.write_text(
            json.dumps(
                {"instrumento": i.codigo, "version": i.version,
                 "respuestas": [{"item_id": r.item_id, "valor": r.valor} for r in respuestas]},
                ensure_ascii=False, indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nRespuestas guardadas en {ruta}")
    return 0


def cmd_puntuar(args: argparse.Namespace) -> int:
    i = cargar(args.codigo)
    datos = json.loads(pathlib.Path(args.entrada).read_text(encoding="utf-8"))
    crudas = datos.get("respuestas", datos) if isinstance(datos, dict) else datos
    if isinstance(crudas, dict):
        respuestas = [Respuesta(k, v) for k, v in crudas.items()]
    else:
        respuestas = [Respuesta(r["item_id"], r.get("valor")) for r in crudas]
    _imprimir(i, puntuar(i, respuestas, estricto=False))
    return 0


def cmd_validar(_: argparse.Namespace) -> int:
    fallos = 0
    for ruta in sorted((pathlib.Path(__file__).resolve().parents[2] / "instruments").glob("*.yaml")):
        try:
            i = cargar(ruta.stem)
        except InstrumentoInvalido as err:
            fallos += 1
            print(f"FALLA  {ruta.stem}")
            for e in err.errores:
                print(f"       - {e}")
            continue
        print(f"OK     {ruta.stem:18} {len(i.items):3} ítems, {len(i.escalas):2} escalas")
    print()
    print(f"{'TODO CORRECTO' if not fallos else f'{fallos} instrumento(s) inválido(s)'}")
    return 1 if fallos else 0


def _imprimir(i: Instrumento, r: Resultado) -> None:
    print("\n" + "=" * 72)
    print(f"RESULTADO  {i.nombre.get(IDIOMA, i.codigo)}")
    print("=" * 72)
    raices = [e.codigo for e in i.raices]
    for codigo, media in ordenar_por_media(r, raices):
        escala = i.escala(codigo)
        p = r[codigo]
        barra = "█" * round(media * 8) + "·" * (40 - round(media * 8))
        print(f"\n  {escala.rotulo(IDIOMA):36} {media:.2f}")
        print(f"  {barra}  bruto {p.bruto:.0f} ({p.items_respondidos}/{p.items_totales})")
        glosa = escala.polo_alto if media >= 3.5 else escala.polo_bajo if media <= 2.5 else {}
        if glosa.get(IDIOMA):
            print(f"    {glosa[IDIOMA]}")
        hijas = ordenar_por_media(r, [h.codigo for h in i.hijas_de(codigo)])
        for cod_h, media_h in hijas:
            print(f"      {i.escala(cod_h).rotulo(IDIOMA):32} {media_h:.2f}")
    if len(raices) == 6 and set(raices) == set("RIASEC"):
        print(f"\n  Código Holland: {''.join(c for c, _ in ordenar_por_media(r, raices)[:3])}")
    if r.advertencias:
        print("\n  ADVERTENCIAS")
        for a in r.advertencias:
            print(f"    · {a}")
    if i.procedencia.licencia.value == "autoria-propia":
        print("\n  Este instrumento NO está validado. El resultado es orientativo y no "
              "debe usarse\n  para decidir sobre personas.")


def main(argv: list[str] | None = None) -> int:
    _salida_utf8()
    p = argparse.ArgumentParser(
        prog="psychometrics",
        description="Motor de evaluación psicométrica: catálogo, administración y puntuación.",
    )
    sub = p.add_subparsers(dest="comando", required=True)

    sub.add_parser("catalogo", help="lista los instrumentos disponibles").set_defaults(
        func=cmd_catalogo)

    f = sub.add_parser("ficha", help="detalle de un instrumento")
    f.add_argument("codigo")
    f.set_defaults(func=cmd_ficha)

    r = sub.add_parser("rendir", help="administra el test en la terminal")
    r.add_argument("codigo")
    r.add_argument("-s", "--salida", help="archivo JSON donde guardar las respuestas")
    r.set_defaults(func=cmd_rendir)

    q = sub.add_parser("puntuar", help="puntúa respuestas desde un JSON")
    q.add_argument("codigo")
    q.add_argument("-e", "--entrada", required=True)
    q.set_defaults(func=cmd_puntuar)

    sub.add_parser("validar", help="valida todo el catálogo").set_defaults(func=cmd_validar)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except (FileNotFoundError, InstrumentoInvalido) as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
