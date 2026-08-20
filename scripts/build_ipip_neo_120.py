"""Genera instruments/ipip-neo-120.yaml desde el volcado público del IPIP.

El texto en inglés es el CANÓNICO y de dominio público (ipip.ori.org).
El texto en español es una traducción de trabajo de este repositorio: sirve para
administrar el instrumento en castellano, pero NO hereda los baremos de Johnson
(2014), que se calcularon sobre la versión inglesa. Queda marcado como tal en el
propio archivo para que nadie lo use como si estuviera validado.

CONVENCIÓN: las claves de los diccionarios y los nombres de campo emitidos al
YAML van en ASCII. Solo la prosa lleva tildes.
"""
from __future__ import annotations

import json
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# La clave debe coincidir con el campo "dominio" del JSON: ASCII, sin tildes.
DOMINIOS = {
    "neuroticismo": (
        "N", "Neuroticismo", "Neuroticism",
        "Tendencia a experimentar emociones negativas: ansiedad, ira, tristeza y estrés.",
        "Serena bajo presión, poco reactiva emocionalmente, rara vez se altera.",
        "Reacciona con intensidad ante la amenaza y el contratiempo; el estrés le pesa.",
    ),
    "extraversion": (
        "E", "Extraversión", "Extraversion",
        "Cantidad e intensidad de la interacción social y de la emoción positiva.",
        "Reservada, prefiere entornos tranquilos, grupos pequeños o el trabajo a solas.",
        "Sociable, enérgica y expresiva; se recarga en compañía de otras personas.",
    ),
    "apertura": (
        "O", "Apertura a la experiencia", "Openness to Experience",
        "Amplitud, profundidad y originalidad de la vida mental y experiencial.",
        "Práctica, concreta y convencional; prefiere lo probado a lo novedoso.",
        "Curiosa, imaginativa y receptiva a ideas, arte y formas de vida distintas.",
    ),
    "amabilidad": (
        "A", "Amabilidad", "Agreeableness",
        "Orientación prosocial frente a antagonismo en el trato con los demás.",
        "Competitiva, escéptica y directa; antepone su criterio al consenso.",
        "Cooperativa, confiada y considerada; busca la armonía.",
    ),
    "responsabilidad": (
        "C", "Responsabilidad", "Conscientiousness",
        "Grado de organización, persistencia y control de impulsos dirigido a metas.",
        "Espontánea y flexible; le cuesta la rutina y la planificación sostenida.",
        "Organizada, perseverante y fiable; planifica y termina lo que empieza.",
    ),
}

FACETAS = {
    "N1": ("Ansiedad", "Nivel de preocupación, tensión y anticipación de amenazas."),
    "N2": ("Ira", "Facilidad para sentir enfado y frustración ante la contrariedad."),
    "N3": ("Depresión", "Tendencia al desánimo, la tristeza y el desaliento."),
    "N4": ("Timidez social", "Incomodidad y vergüenza ante la mirada de los demás."),
    "N5": ("Inmoderación", "Dificultad para resistir impulsos, antojos y excesos."),
    "N6": ("Vulnerabilidad", "Capacidad de sostenerse frente a la presión y la urgencia."),
    "E1": ("Cordialidad", "Facilidad y calidez en el trato cercano con otras personas."),
    "E2": ("Gregarismo", "Preferencia por la compañía numerosa frente a la soledad."),
    "E3": ("Asertividad", "Tendencia a tomar la iniciativa, dirigir y hacerse oír."),
    "E4": ("Nivel de actividad", "Ritmo vital, ocupación y necesidad de estar en movimiento."),
    "E5": ("Búsqueda de emociones", "Necesidad de estimulación intensa, riesgo y novedad."),
    "E6": ("Alegría", "Frecuencia e intensidad de la emoción positiva y el entusiasmo."),
    "O1": ("Imaginación", "Riqueza de la fantasía y de la vida interior."),
    "O2": ("Intereses artísticos", "Sensibilidad a la belleza, el arte y la forma."),
    "O3": ("Emotividad", "Conciencia y valoración de las propias emociones y las ajenas."),
    "O4": ("Espíritu aventurero", "Disposición a probar lo nuevo y salir de la rutina."),
    "O5": ("Intelecto", "Gusto por las ideas abstractas, el debate y el desafío mental."),
    "O6": ("Liberalismo", "Disposición a cuestionar la autoridad, la norma y la tradición."),
    "A1": ("Confianza", "Supuesto de buena fe en las intenciones de los demás."),
    "A2": ("Honestidad", "Franqueza y rechazo a la manipulación en beneficio propio."),
    "A3": ("Altruismo", "Disposición activa a ayudar y ocuparse de los demás."),
    "A4": ("Cooperación", "Preferencia por evitar el conflicto y ceder para acordar."),
    "A5": ("Modestia", "Tendencia a no exhibir ni sobrevalorar los propios méritos."),
    "A6": ("Empatía", "Sensibilidad ante el sufrimiento y la desventaja ajena."),
    "C1": ("Autoeficacia", "Confianza en la propia competencia para sacar el trabajo adelante."),
    "C2": ("Orden", "Necesidad de estructura, limpieza y organización del entorno."),
    "C3": ("Sentido del deber", "Apego a los compromisos, las reglas y la palabra dada."),
    "C4": ("Orientación al logro", "Ambición, esfuerzo y exigencia sobre el propio rendimiento."),
    "C5": ("Autodisciplina", "Capacidad de empezar y sostener una tarea hasta terminarla."),
    "C6": ("Cautela", "Deliberación previa a la acción; freno a la decisión impulsiva."),
}

ES = {
    "Worry about things.": "Me preocupo por las cosas.",
    "Fear for the worst.": "Temo que ocurra lo peor.",
    "Am afraid of many things.": "Le tengo miedo a muchas cosas.",
    "Get stressed out easily.": "Me estreso con facilidad.",
    "Get angry easily.": "Me enojo con facilidad.",
    "Get irritated easily.": "Me irrito con facilidad.",
    "Lose my temper.": "Pierdo los estribos.",
    "Am not easily annoyed.": "No me molesto con facilidad.",
    "Often feel blue.": "A menudo me siento decaído.",
    "Dislike myself.": "No me gusto a mí mismo.",
    "Am often down in the dumps.": "A menudo ando por el suelo.",
    "Feel comfortable with myself.": "Me siento a gusto conmigo mismo.",
    "Find it difficult to approach others.": "Me cuesta acercarme a los demás.",
    "Am afraid to draw attention to myself.": "Me da miedo llamar la atención.",
    "Only feel comfortable with friends.": "Solo me siento cómodo con mis amigos.",
    "Am not bothered by difficult social situations.":
        "Las situaciones sociales difíciles no me incomodan.",
    "Go on binges.": "Caigo en excesos.",
    "Rarely overindulge.": "Rara vez me excedo.",
    "Easily resist temptations.": "Resisto las tentaciones con facilidad.",
    "Am able to control my cravings.": "Soy capaz de controlar mis antojos.",
    "Panic easily.": "Entro en pánico con facilidad.",
    "Become overwhelmed by events.": "Los acontecimientos me sobrepasan.",
    "Feel that I am unable to deal with things.":
        "Siento que no soy capaz de manejar las cosas.",
    "Remain calm under pressure.": "Mantengo la calma bajo presión.",
    "Make friends easily.": "Hago amigos con facilidad.",
    "Feel comfortable around people.": "Me siento cómodo rodeado de gente.",
    "Avoid contacts with others.": "Evito el contacto con los demás.",
    "Keep others at a distance.": "Mantengo a los demás a distancia.",
    "Love large parties.": "Me encantan las fiestas multitudinarias.",
    "Talk to a lot of different people at parties.":
        "En las fiestas hablo con mucha gente distinta.",
    "Prefer to be alone.": "Prefiero estar solo.",
    "Avoid crowds.": "Evito las aglomeraciones.",
    "Take charge.": "Tomo el mando.",
    "Try to lead others.": "Trato de liderar a los demás.",
    "Take control of things.": "Tomo el control de las cosas.",
    "Wait for others to lead the way.": "Espero a que otros marquen el camino.",
    "Am always busy.": "Siempre estoy ocupado.",
    "Am always on the go.": "Siempre estoy en movimiento.",
    "Do a lot in my spare time.": "Hago muchas cosas en mi tiempo libre.",
    "Like to take it easy.": "Me gusta tomármelo con calma.",
    "Love excitement.": "Me encanta la emoción fuerte.",
    "Seek adventure.": "Busco la aventura.",
    "Enjoy being reckless.": "Disfruto siendo temerario.",
    "Act wild and crazy.": "Me comporto de forma alocada.",
    "Radiate joy.": "Irradio alegría.",
    "Have a lot of fun.": "Me divierto mucho.",
    "Love life.": "Amo la vida.",
    "Look at the bright side of life.": "Le veo el lado bueno a la vida.",
    "Have a vivid imagination.": "Tengo una imaginación vívida.",
    "Enjoy wild flights of fantasy.": "Disfruto dejando volar la fantasía.",
    "Love to daydream.": "Me encanta soñar despierto.",
    "Like to get lost in thought.": "Me gusta perderme en mis pensamientos.",
    "Believe in the importance of art.": "Creo en la importancia del arte.",
    "See beauty in things that others might not notice.":
        "Veo belleza en cosas que otros no notarían.",
    "Do not like poetry.": "No me gusta la poesía.",
    "Do not enjoy going to art museums.": "No disfruto ir a museos de arte.",
    "Experience my emotions intensely.": "Vivo mis emociones con intensidad.",
    "Feel others emotions.": "Siento las emociones de los demás.",
    "Rarely notice my emotional reactions.": "Rara vez noto mis reacciones emocionales.",
    "Do not understand people who get emotional.":
        "No entiendo a la gente que se pone emotiva.",
    "Prefer variety to routine.": "Prefiero la variedad a la rutina.",
    "Prefer to stick with things that I know.": "Prefiero quedarme con lo que ya conozco.",
    "Dislike changes.": "Me disgustan los cambios.",
    "Am attached to conventional ways.": "Soy apegado a las formas convencionales.",
    "Love to read challenging material.": "Me encanta leer material exigente.",
    "Avoid philosophical discussions.": "Evito las discusiones filosóficas.",
    "Have difficulty understanding abstract ideas.": "Me cuesta entender las ideas abstractas.",
    "Am not interested in theoretical discussions.": "No me interesan las discusiones teóricas.",
    "Tend to vote for liberal political candidates.":
        "Suelo votar por candidatos políticos progresistas.",
    "Believe that there is no absolute right and wrong.":
        "Creo que no existe un bien y un mal absolutos.",
    "Tend to vote for conservative political candidates.":
        "Suelo votar por candidatos políticos conservadores.",
    "Believe that we should be tough on crime.":
        "Creo que hay que ser duro con la delincuencia.",
    "Trust others.": "Confío en los demás.",
    "Believe that others have good intentions.": "Creo que los demás tienen buenas intenciones.",
    "Trust what people say.": "Confío en lo que dice la gente.",
    "Distrust people.": "Desconfío de la gente.",
    "Use others for my own ends.": "Uso a los demás para mis propios fines.",
    "Cheat to get ahead.": "Hago trampa para salir adelante.",
    "Take advantage of others.": "Me aprovecho de los demás.",
    "Obstruct others plans.": "Obstaculizo los planes de los demás.",
    "Am concerned about others.": "Me preocupo por los demás.",
    "Love to help others.": "Me encanta ayudar a los demás.",
    "Am indifferent to the feelings of others.":
        "Me son indiferentes los sentimientos de los demás.",
    "Take no time for others.": "No dedico tiempo a los demás.",
    "Love a good fight.": "Me gusta una buena pelea.",
    "Yell at people.": "Le grito a la gente.",
    "Insult people.": "Insulto a la gente.",
    "Get back at others.": "Me desquito con los demás.",
    "Believe that I am better than others.": "Creo que soy mejor que los demás.",
    "Think highly of myself.": "Tengo un alto concepto de mí mismo.",
    "Have a high opinion of myself.": "Tengo una opinión muy buena de mí mismo.",
    "Boast about my virtues.": "Presumo de mis virtudes.",
    "Sympathize with the homeless.": "Me compadezco de las personas sin hogar.",
    "Feel sympathy for those who are worse off than myself.":
        "Siento compasión por quienes están peor que yo.",
    "Am not interested in other people problems.":
        "No me interesan los problemas de los demás.",
    "Try not to think about the needy.": "Trato de no pensar en los necesitados.",
    "Complete tasks successfully.": "Completo las tareas con éxito.",
    "Excel in what I do.": "Destaco en lo que hago.",
    "Handle tasks smoothly.": "Manejo las tareas sin dificultad.",
    "Know how to get things done.": "Sé cómo sacar las cosas adelante.",
    "Like to tidy up.": "Me gusta ordenar.",
    "Often forget to put things back in their proper place.":
        "A menudo olvido dejar las cosas en su lugar.",
    "Leave a mess in my room.": "Dejo mi habitación hecha un desorden.",
    "Leave my belongings around.": "Dejo mis cosas tiradas por ahí.",
    "Keep my promises.": "Cumplo mis promesas.",
    "Tell the truth.": "Digo la verdad.",
    "Break rules.": "Rompo las reglas.",
    "Break my promises.": "Incumplo mis promesas.",
    "Do more than what is expected of me.": "Hago más de lo que se espera de mí.",
    "Work hard.": "Trabajo duro.",
    "Put little time and effort into my work.":
        "Dedico poco tiempo y esfuerzo a mi trabajo.",
    "Do just enough work to get by.": "Hago solo lo justo para salir del paso.",
    "Am always prepared.": "Siempre estoy preparado.",
    "Carry out my plans.": "Llevo a cabo mis planes.",
    "Waste my time.": "Pierdo el tiempo.",
    "Have difficulty starting tasks.": "Me cuesta empezar las tareas.",
    "Jump into things without thinking.": "Me lanzo a las cosas sin pensar.",
    "Make rash decisions.": "Tomo decisiones precipitadas.",
    "Rush into things.": "Me precipito en las cosas.",
    "Act without thinking.": "Actúo sin pensar.",
}

OPCIONES = [
    (1, "Muy inexacto", "Very Inaccurate"),
    (2, "Moderadamente inexacto", "Moderately Inaccurate"),
    (3, "Ni inexacto ni exacto", "Neither Inaccurate nor Accurate"),
    (4, "Moderadamente exacto", "Moderately Accurate"),
    (5, "Muy exacto", "Very Accurate"),
]


def normaliza(texto: str) -> str:
    """Quita apóstrofos y contracciones para casar con la tabla ES.

    El volcado del IPIP usa apóstrofos en `others'`, `I'm` y `don't`. La tabla de
    traducción los evita para no pelear con el quoting de YAML y de la shell, así
    que aquí se normalizan ambos lados al mismo texto plano.
    """
    t = texto.replace("’", "'")
    for antes, despues in (
        ("I'm", "I am"), ("Don't", "Do not"), ("don't", "do not"),
        ("what's", "what is"), ("others'", "others"), ("people's", "people"),
    ):
        t = t.replace(antes, despues)
    return t


def cita_yaml(texto: str) -> str:
    """Escapa un escalar YAML en comillas dobles."""
    return '"' + texto.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    datos = json.loads((RAIZ / "scripts" / "ipip120.json").read_text(encoding="utf-8"))

    faltan = sorted(
        {i["texto_en"] for f in datos for i in f["items"] if normaliza(i["texto_en"]) not in ES}
    )
    if faltan:
        print("Sin traducción al español:", *faltan, sep="\n  ")
        return 1

    lineas: list[str] = []
    add = lineas.append

    add("# =========================================================================")
    add("# IPIP-NEO-120 - Inventario de personalidad de los Cinco Grandes")
    add("#")
    add("# Los 120 ítems en inglés son DOMINIO PÚBLICO (International Personality")
    add("# Item Pool). Pueden usarse y redistribuirse sin permiso ni pago, con")
    add("# fines comerciales o académicos.")
    add("#")
    add("# La traducción al español es de este repositorio y NO está baremada: los")
    add("# percentiles de Johnson (2014) se calcularon sobre la versión inglesa.")
    add("# Usar el formulario en español para puntuación normativa exige un estudio")
    add("# de validación propio. Ver docs/VALIDACION.md.")
    add("#")
    add("# Generado por scripts/build_ipip_neo_120.py - no editar a mano.")
    add("# =========================================================================")
    add("codigo: ipip-neo-120")
    add('version: "1.0.0"')
    add("nombre:")
    add("  es: Inventario de personalidad IPIP-NEO-120")
    add("  en: IPIP-NEO-120 Personality Inventory")
    add("descripcion:")
    add("  es: >-")
    add("    Mide los cinco grandes factores de personalidad desglosados en 30")
    add("    facetas, cuatro ítems por faceta. Es la versión de dominio público")
    add("    más completa del modelo de los Cinco Grandes y el instrumento con")
    add("    mejor respaldo empírico del catálogo.")
    add("  en: >-")
    add("    Measures the Five Factor Model across 30 facets with four items each.")
    add("tipo_respuesta: likert")
    add("ipsativo: false")
    add("duracion_min: [20, 30]")
    add("procedencia:")
    add("  autores: Johnson, J. A.; International Personality Item Pool (Goldberg)")
    add("  anio: 2014")
    add("  fuente: https://ipip.ori.org/30FacetNEO-PI-RItems.htm")
    add("  licencia: dominio-publico")
    add("  cita: >-")
    add("    Johnson, J. A. (2014). Measuring thirty facets of the Five Factor Model")
    add("    with a 120-item public domain inventory: Development of the")
    add("    IPIP-NEO-120. Journal of Research in Personality, 51, 78-89.")
    add("  notas:")
    add("    muestra: >-")
    add("      Alfas de Cronbach calculados sobre una muestra de internet de")
    add("      N = 619.150 personas.")
    add("    traduccion: >-")
    add("      El texto en español es traducción de trabajo de este repositorio,")
    add("      sin estudio de equivalencia transcultural. No hereda los baremos")
    add("      originales.")

    add("opciones:")
    for valor, es, en in OPCIONES:
        add(f"  - valor: {valor}")
        add(f"    etiqueta: {{es: {cita_yaml(es)}, en: {cita_yaml(en)}}}")

    add("escalas:")
    for clave, (pref, nom_es, nom_en, desc, bajo, alto) in DOMINIOS.items():
        add(f"  - codigo: {pref}")
        add(f"    nombre: {{es: {cita_yaml(nom_es)}, en: {cita_yaml(nom_en)}}}")
        add(f"    descripcion: {{es: {cita_yaml(desc)}}}")
        add(f"    polo_bajo: {{es: {cita_yaml(bajo)}}}")
        add(f"    polo_alto: {{es: {cita_yaml(alto)}}}")
        for faceta in (x for x in datos if x["dominio"] == clave):
            nom_f, desc_f = FACETAS[faceta["codigo"]]
            add(f"  - codigo: {faceta['codigo']}")
            add(f"    padre: {pref}")
            add(f"    nombre: {{es: {cita_yaml(nom_f)}, en: {cita_yaml(faceta['faceta_en'])}}}")
            add(f"    descripcion: {{es: {cita_yaml(desc_f)}}}")
            add(f"    alfa: {faceta['alpha']}")

    add("items:")
    n = 0
    for faceta in datos:
        for item in faceta["items"]:
            n += 1
            add(f"  - id: q{n:03d}")
            add(f"    escala: {faceta['codigo']}")
            add(f"    clave: {item['clave']}")
            add("    texto:")
            add(f"      es: {cita_yaml(ES[normaliza(item['texto_en'])])}")
            add(f"      en: {cita_yaml(item['texto_en'])}")

    destino = RAIZ / "instruments" / "ipip-neo-120.yaml"
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"OK  {destino.relative_to(RAIZ)}  ({n} ítems, {len(datos)} facetas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
