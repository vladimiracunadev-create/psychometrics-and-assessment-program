"""Genera instruments/ipip-via-r.yaml desde el volcado público del IPIP-VIA-R.

Los 96 ítems en inglés son DOMINIO PÚBLICO (International Personality Item Pool).
La traducción al español es de este repositorio y no está baremada.

El archivo generado declara la jerarquía completa del marco VIA: 6 virtudes
como escalas padre y 24 fortalezas del carácter como escalas hijas. El motor
agrega las virtudes desde los ítems de sus fortalezas, no promediando promedios.

CONVENCIÓN: los códigos de escala y las claves de diccionario van en ASCII.
"""
from __future__ import annotations

import json
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# Marco VIA (Peterson & Seligman, 2004): 6 virtudes universales.
VIRTUDES = {
    "SAB": (
        "Sabiduría y conocimiento", "Wisdom and Knowledge",
        "Fortalezas cognitivas: adquirir y usar el conocimiento.",
        ["ORI", "CUR", "JUD", "LOV", "PER"],
    ),
    "COR": (
        "Coraje", "Courage",
        "Fortalezas emocionales para perseguir metas frente a la oposición.",
        ["VAL", "IND", "INT", "ZES"],
    ),
    "HUM": (
        "Humanidad", "Humanity",
        "Fortalezas interpersonales de cuidado y cercanía con otras personas.",
        ["CAP", "KIN", "SOC"],
    ),
    "JUS": (
        "Justicia", "Justice",
        "Fortalezas cívicas que sostienen una vida comunitaria sana.",
        ["CIT", "EQU", "LEA"],
    ),
    "TEM": (
        "Templanza", "Temperance",
        "Fortalezas que protegen contra el exceso.",
        ["FOR", "MOD", "PRU", "SEL"],
    ),
    "TRA": (
        "Trascendencia", "Transcendence",
        "Fortalezas que conectan con algo más grande y dan sentido.",
        ["APP", "GRA", "HOP", "HUM_H", "SPI"],
    ),
}

# El código HUM del IPIP (humor) choca con el que asignamos a la virtud
# Humanidad. Se renombra la fortaleza a HUM_H y se documenta el cambio.
RENOMBRES = {"HUM": "HUM_H"}

FORTALEZAS = {
    "APP": ("Apreciación de la belleza", "Notar y valorar la belleza y la excelencia."),
    "CAP": ("Capacidad de amar", "Valorar y sostener vínculos afectivos cercanos."),
    "CIT": ("Trabajo en equipo", "Lealtad y compromiso con el grupo del que se forma parte."),
    "CUR": ("Curiosidad", "Interés abierto por la experiencia y la novedad."),
    "EQU": ("Equidad", "Tratar a todas las personas según el mismo criterio."),
    "FOR": ("Perdón", "Disposición a dar una segunda oportunidad."),
    "GRA": ("Gratitud", "Reconocer y agradecer lo bueno que se recibe."),
    "HOP": ("Esperanza", "Esperar lo mejor y trabajar para conseguirlo."),
    "HUM_H": ("Humor", "Disposición al juego, la risa y aligerar el ambiente."),
    "IND": ("Perseverancia", "Terminar lo empezado pese a los obstáculos."),
    "INT": ("Integridad", "Decir la verdad y presentarse de forma auténtica."),
    "JUD": ("Juicio crítico", "Pensar las cosas a fondo y examinarlas desde varios lados."),
    "KIN": ("Amabilidad", "Hacer favores y buenas obras sin que se los pidan."),
    "LEA": ("Liderazgo", "Organizar actividades de grupo y lograr que ocurran."),
    "LOV": ("Amor por aprender", "Dominar nuevas destrezas y cuerpos de conocimiento."),
    "MOD": ("Modestia", "Dejar que los logros hablen por sí solos."),
    "ORI": ("Creatividad", "Pensar formas nuevas y productivas de hacer las cosas."),
    "PER": ("Perspectiva", "Ofrecer consejo sensato y ver el cuadro completo."),
    "PRU": ("Prudencia", "Elegir con cuidado; no decir ni hacer lo que luego se lamenta."),
    "SEL": ("Autorregulación", "Regular lo que se siente y lo que se hace."),
    "SOC": ("Inteligencia social", "Leer los motivos y sentimientos propios y ajenos."),
    "SPI": ("Espiritualidad", "Tener creencias coherentes sobre el propósito y el sentido."),
    "VAL": ("Valentía", "No retroceder ante la amenaza, el reto o el dolor."),
    "ZES": ("Vitalidad", "Encarar la vida con energía y entusiasmo."),
}

ES = {
    "Feel it's important to live in a world of beauty.":
        "Siento que es importante vivir en un mundo bello.",
    "Experience deep emotions when I see beautiful things.":
        "Experimento emociones profundas cuando veo cosas bellas.",
    "Am rarely aware of the natural beauty in the environment.":
        "Rara vez reparo en la belleza natural del entorno.",
    "Fail to notice beauty until others comment on it.":
        "No noto la belleza hasta que otros la comentan.",
    "Know that there are people in my life who care as much for me as for themselves.":
        "Sé que hay personas en mi vida que me quieren tanto como a sí mismas.",
    "Can express love to someone else.": "Soy capaz de expresarle amor a otra persona.",
    "Do not easily share my feelings with others.":
        "No comparto fácilmente mis sentimientos con los demás.",
    "Have difficulty accepting love from anyone.":
        "Me cuesta aceptar el cariño de cualquier persona.",
    "Am an extremely loyal person.": "Soy una persona extremadamente leal.",
    "Support my teammates or fellow group members.":
        "Apoyo a mis compañeros de equipo o de grupo.",
    "Am not good at working with a group.": "No se me da bien trabajar en grupo.",
    "Prefer to do everything alone.": "Prefiero hacerlo todo solo.",
    "Am excited by many different activities.":
        "Me entusiasman actividades muy distintas entre sí.",
    "Can find something of interest in any situation.":
        "Encuentro algo interesante en cualquier situación.",
    "Am not all that curious about the world.": "No soy tan curioso respecto del mundo.",
    "Have few interests.": "Tengo pocos intereses.",
    "Treat all people equally.": "Trato a todas las personas por igual.",
    "Believe that everyone's rights are equally important.":
        "Creo que los derechos de todas las personas valen lo mismo.",
    "Take advantage of others.": "Me aprovecho de los demás.",
    "Treat others differently if I don't like them.":
        "Trato distinto a quienes no me caen bien.",
    "Try to respond with understanding when someone treats me badly.":
        "Trato de responder con comprensión cuando alguien me trata mal.",
    "Allow others to make a fresh start.":
        "Le doy a los demás la oportunidad de empezar de nuevo.",
    "Hold grudges.": "Guardo rencor.",
    "Find it hard to forgive others.": "Me cuesta perdonar a los demás.",
    "Express my thanks to those who care about me.":
        "Le expreso mi agradecimiento a quienes se preocupan por mí.",
    "Am an extremely grateful person.": "Soy una persona extremadamente agradecida.",
    "Feel no gratitude to others.": "No siento gratitud hacia los demás.",
    "Find few things in my life to be grateful for.":
        "Encuentro pocas cosas que agradecer en mi vida.",
    "Can find the positive in what seems negative to others.":
        "Encuentro lo positivo en lo que a otros les parece negativo.",
    "Remain hopeful despite challenges.":
        "Mantengo la esperanza a pesar de las dificultades.",
    "Expect the worst.": "Espero lo peor.",
    "Often think about the possibility of negative outcomes that are not likely to occur.":
        "A menudo pienso en desenlaces malos que es poco probable que ocurran.",
    "Use laughter to brighten the days of others.":
        "Uso la risa para alegrarle el día a los demás.",
    "Keep my sense of humor even in gloomy situations.":
        "Conservo el sentido del humor incluso en situaciones sombrías.",
    "Am not known for my sense of humor.": "No soy conocido por mi sentido del humor.",
    "Am not fun to be with.": "No soy una compañía divertida.",
    "Don't quit a task before it is finished.": "No abandono una tarea antes de terminarla.",
    "Finish things despite obstacles in the way.":
        "Termino las cosas a pesar de los obstáculos.",
    "Don't finish what I start.": "No termino lo que empiezo.",
    "Give up easily.": "Me rindo con facilidad.",
    "Am trusted to keep secrets.": "Confían en mí para guardar secretos.",
    "Keep my promises.": "Cumplo mis promesas.",
    "Lie to get myself out of trouble.": "Miento para librarme de un problema.",
    "Cheat on people who have trusted me.": "Traiciono a quienes han confiado en mí.",
    "Weigh the pro's and the con's.": "Sopeso los pros y los contras.",
    "Am valued by my friends for my good judgment.":
        "Mis amigos valoran mi buen criterio.",
    "Don't tend to think things through critically.":
        "No suelo analizar las cosas con espíritu crítico.",
    "Don't think about different possibilities when making decisions.":
        "No considero distintas posibilidades al tomar decisiones.",
    "Am never too busy to help a friend.":
        "Nunca estoy demasiado ocupado para ayudar a un amigo.",
    "Go out of my way to cheer up people who appear down.":
        "Hago un esfuerzo por animar a quien veo decaído.",
    "Get impatient when others talk to me about their problems.":
        "Me impaciento cuando otros me hablan de sus problemas.",
    "Am only kind to others if they have been kind to me.":
        "Solo soy amable con quienes han sido amables conmigo.",
    "Am good at helping people work well together.":
        "Se me da bien lograr que la gente trabaje bien junta.",
    "Am told that I am a strong but fair leader.":
        "Me dicen que soy un líder firme pero justo.",
    "Have difficulty getting others to work together.":
        "Me cuesta conseguir que los demás trabajen juntos.",
    "Am not good at taking charge of a group.": "No se me da bien dirigir un grupo.",
    "Am a true life-long learner.": "Soy alguien que aprende durante toda la vida.",
    "Am thrilled when I learn something new.": "Me emociona aprender algo nuevo.",
    "Don't like to learn new things.": "No me gusta aprender cosas nuevas.",
    "Don't read nonfiction books for fun.": "No leo libros de no ficción por gusto.",
    "Don't brag about my accomplishments.": "No presumo de mis logros.",
    "Would never be described as arrogant.": "Nadie me describiría como arrogante.",
    "Like to stand out in a crowd.": "Me gusta destacar entre la gente.",
    "Like to talk about myself.": "Me gusta hablar de mí mismo.",
    "Come up with new ways to do things.": "Se me ocurren formas nuevas de hacer las cosas.",
    "Am an original thinker.": "Pienso de forma original.",
    "Am not considered to have new and different ideas.":
        "No se me considera alguien con ideas nuevas y distintas.",
    "Have no special urge to do something original.":
        "No siento una necesidad especial de hacer algo original.",
    "Have a mature view on life.": "Tengo una visión madura de la vida.",
    "Am considered to be a wise person.": "Se me considera una persona sabia.",
    "Am not good at figuring out what really matters.":
        "No se me da bien distinguir lo que de verdad importa.",
    "Am rarely consulted for advice by others.": "Rara vez me piden consejo.",
    "Believe it is always better to be safe than sorry.":
        "Creo que siempre es mejor prevenir que lamentar.",
    "Make careful choices.": "Tomo decisiones con cuidado.",
    "Act before thinking through the consequences.":
        "Actúo antes de pensar en las consecuencias.",
    "Like taking risks.": "Me gusta correr riesgos.",
    "Am a highly disciplined person.": "Soy una persona muy disciplinada.",
    "Forego things that are bad for me in the long run even if they make me feel good in "
    "the short run.":
        "Renuncio a lo que me perjudica a largo plazo aunque a corto plazo me haga "
        "sentir bien.",
    "Let myself be taken over by urges to spend or eat too much.":
        "Dejo que me dominen las ganas de gastar o comer en exceso.",
    "Give in to my urges.": "Cedo ante mis impulsos.",
    "Am good at sensing what others are feeling.":
        "Se me da bien percibir lo que sienten los demás.",
    "Know what to say to make people feel good.":
        "Sé qué decir para que la gente se sienta bien.",
    "Don't know how to handle myself in a new social situation.":
        "No sé cómo comportarme en una situación social nueva.",
    "Have trouble guessing how others will react.":
        "Me cuesta anticipar cómo van a reaccionar los demás.",
    "Am a spiritual person.": "Soy una persona espiritual.",
    "Believe that each person has a purpose in life.":
        "Creo que cada persona tiene un propósito en la vida.",
    "Feel that life has no meaning.": "Siento que la vida no tiene sentido.",
    "Do not believe in a universal power or a God.":
        "No creo en un poder universal ni en un Dios.",
    "Have taken frequent stands in the face of strong opposition.":
        "He tomado postura muchas veces frente a una fuerte oposición.",
    "Don't hesitate to express an unpopular opinion.":
        "No dudo en expresar una opinión impopular.",
    "Do not stand up for my beliefs.": "No defiendo mis convicciones.",
    "Don't speak my mind freely when there might be negative results.":
        "No digo lo que pienso cuando podría traerme consecuencias negativas.",
    "Awaken with a sense of excitement about the day's possibilities.":
        "Despierto entusiasmado por lo que el día puede traer.",
    "Look forward to each new day.": "Espero cada nuevo día con ganas.",
    "Am described as grumpy.": "Me describen como gruñón.",
    "Don't have much energy.": "No tengo mucha energía.",
}

OPCIONES = [
    (1, "Muy inexacto", "Very Inaccurate"),
    (2, "Moderadamente inexacto", "Moderately Inaccurate"),
    (3, "Ni inexacto ni exacto", "Neither Inaccurate nor Accurate"),
    (4, "Moderadamente exacto", "Moderately Accurate"),
    (5, "Muy exacto", "Very Accurate"),
]


def limpia(texto: str) -> str:
    """Normaliza espacios sobrantes antes de la puntuación final."""
    return re.sub(r"\s+([.,;])", r"\1", texto).strip()


def cita_yaml(texto: str) -> str:
    return '"' + texto.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    datos = json.loads((RAIZ / "scripts" / "ipip_via_r.json").read_text(encoding="utf-8"))
    por_codigo = {RENOMBRES.get(e["codigo"], e["codigo"]): e for e in datos}

    faltan = sorted(
        {limpia(i["texto_en"]) for e in datos for i in e["items"]
         if limpia(i["texto_en"]) not in ES}
    )
    if faltan:
        print("Sin traducción al español:", *faltan, sep="\n  ")
        return 1

    declaradas = {c for _, _, _, cs in VIRTUDES.values() for c in cs}
    if declaradas != set(por_codigo):
        print("Desalineación virtud/fortaleza:")
        print("  solo en VIRTUDES:", sorted(declaradas - set(por_codigo)))
        print("  solo en el banco:", sorted(set(por_codigo) - declaradas))
        return 1

    lineas: list[str] = []
    add = lineas.append
    add("# =========================================================================")
    add("# IPIP-VIA-R - Fortalezas del carácter (24 escalas breves)")
    add("#")
    add("# Los 96 ítems en inglés son DOMINIO PÚBLICO (International Personality")
    add("# Item Pool). El marco conceptual es la clasificación VIA de Peterson y")
    add("# Seligman (2004); estos ítems son la operacionalización abierta de")
    add("# Goldberg, revisada por Bluemke et al. (2021), NO el VIA-IS comercial.")
    add("#")
    add("# Cada fortaleza tiene 4 ítems con clave equilibrada: 2 directos y 2")
    add("# invertidos. Ese equilibrio es lo que contiene el sesgo de aquiescencia,")
    add("# y se verifica en tests/test_instrumentos.py.")
    add("#")
    add("# La traducción al español es de este repositorio y no está baremada.")
    add("# Generado por scripts/build_ipip_via_r.py - no editar a mano.")
    add("# =========================================================================")
    add("codigo: ipip-via-r")
    add('version: "1.0.0"')
    add("nombre:")
    add("  es: Inventario de fortalezas del carácter IPIP-VIA-R")
    add("  en: IPIP-VIA-R Character Strengths Inventory")
    add("descripcion:")
    add("  es: >-")
    add("    Mide las 24 fortalezas del carácter de la clasificación VIA,")
    add("    agrupadas en 6 virtudes. No evalúa rendimiento ni patología:")
    add("    describe qué cualidades del carácter están más presentes en la")
    add("    persona. El resultado útil son las fortalezas de firma, es decir las")
    add("    más altas del propio perfil, no la comparación escala por escala con")
    add("    otras personas.")
    add("  en: >-")
    add("    Measures the 24 VIA character strengths grouped into 6 virtues.")
    add("tipo_respuesta: likert")
    add("ipsativo: false")
    add("duracion_min: [12, 18]")
    add("procedencia:")
    add("  autores: Bluemke, M.; Partsch, M. V.; Saucier, G.; Lechner, C. M.; Goldberg, L. R.")
    add("  anio: 2021")
    add("  fuente: https://ipip.ori.org/IPIP-VIA-R_Key.html")
    add("  licencia: dominio-publico")
    add("  cita: >-")
    add("    Bluemke, M., Partsch, M. V., Saucier, G., & Lechner, C. M. (2021).")
    add("    Circumventing cultural bias in the assessment of character strengths:")
    add("    IPIP-VIA-R short scales. Marco: Peterson, C., & Seligman, M. E. P.")
    add("    (2004). Character Strengths and Virtues.")
    add("  notas:")
    add("    no_es_via_is: >-")
    add("      Este NO es el VIA-IS del VIA Institute, que es propietario. Es la")
    add("      medida abierta del IPIP sobre el mismo marco conceptual.")
    add("    codigo_humor: >-")
    add("      El código original de Humor es HUM y colisiona con el que este")
    add("      archivo asigna a la virtud Humanidad; la fortaleza se declara")
    add("      como HUM_H.")
    add("    fiabilidad: >-")
    add("      Los alfas de varias escalas rondan .50-.60. Con 4 ítems es lo")
    add("      esperable y sirve para describir un perfil, no para decidir sobre")
    add("      una persona. Ver docs/VALIDACION.md.")

    add("opciones:")
    for valor, es, en in OPCIONES:
        add(f"  - valor: {valor}")
        add(f"    etiqueta: {{es: {cita_yaml(es)}, en: {cita_yaml(en)}}}")

    add("escalas:")
    for cod_v, (nom_es, nom_en, desc, hijas) in VIRTUDES.items():
        add(f"  - codigo: {cod_v}")
        add(f"    nombre: {{es: {cita_yaml(nom_es)}, en: {cita_yaml(nom_en)}}}")
        add(f"    descripcion: {{es: {cita_yaml(desc)}}}")
        for cod_f in hijas:
            e = por_codigo[cod_f]
            nom_f, desc_f = FORTALEZAS[cod_f]
            add(f"  - codigo: {cod_f}")
            add(f"    padre: {cod_v}")
            add(f"    nombre: {{es: {cita_yaml(nom_f)}, en: {cita_yaml(e['fortaleza_en'])}}}")
            add(f"    descripcion: {{es: {cita_yaml(desc_f)}}}")

    add("items:")
    n = 0
    for _, _, _, hijas in VIRTUDES.values():
        for cod_f in hijas:
            for item in por_codigo[cod_f]["items"]:
                n += 1
                texto_en = limpia(item["texto_en"])
                add(f"  - id: v{n:03d}")
                add(f"    escala: {cod_f}")
                add(f"    clave: {item['clave']}")
                add("    texto:")
                add(f"      es: {cita_yaml(ES[texto_en])}")
                add(f"      en: {cita_yaml(texto_en)}")

    destino = RAIZ / "instruments" / "ipip-via-r.yaml"
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"OK  {destino.relative_to(RAIZ)}  ({n} ítems, {len(por_codigo)} fortalezas, "
          f"{len(VIRTUDES)} virtudes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
