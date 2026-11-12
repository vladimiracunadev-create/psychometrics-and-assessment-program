"""Amplia curriculum.yaml a 20 partes y 200 clases de forma aditiva.

Conserva intactas las clases 001-040 (identificadores estables). Las clases
nuevas nacen con estado `planificada`: tienen carpeta y lesson.yaml, pero NO
se declaran escritas hasta que existan README, lab.py y bibliografia.
Es idempotente: si una clase ya existe en el curriculo, no la toca.
"""
from __future__ import annotations

import pathlib
import re
import unicodedata

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent

NUEVAS_EN_EXISTENTES = {
    "00": ["Historia de la psicometría: de Galton a la medición moderna",
           "Constructos, variables latentes y definiciones operacionales",
           "Tipos de test: rendimiento máximo frente a desempeño típico",
           "Pruebas de velocidad, de potencia y tareas cronometradas",
           "Introducción a la estadística descriptiva para evaluación"],
    "01": ["Especificaciones de test y tablas de contenido",
           "Ítems de opción múltiple: distractores y clave",
           "Ítems abiertos, rúbricas y acuerdo entre jueces",
           "Juicio de expertos y revisión cognitiva de ítems",
           "Bancos de ítems, versiones y control de cambios"],
    "02": ["Estadística descriptiva aplicada a puntajes",
           "Correlación de Pearson, Spearman y sus supuestos",
           "Fiabilidad de pruebas dicotómicas: KR-20",
           "Fiabilidad entre evaluadores: kappa y CCI",
           "Intervalos de confianza para puntajes individuales"],
    "03": ["Validez convergente y discriminante: matriz multirrasgo-multimétodo",
           "Validez ecológica y generalización",
           "Evidencia basada en procesos de respuesta",
           "Metaanálisis de validez y corrección por atenuación",
           "Amenazas a la validez: falseamiento y deseabilidad social"],
    "04": ["Rotaciones y criterios de retención de factores",
           "Ajuste en modelos de ecuaciones estructurales",
           "Modelos bifactor y jerárquicos",
           "Análisis de redes psicométricas",
           "Datos ordinales y correlaciones policóricas"],
    "05": ["Estimación de parámetros y de habilidad",
           "Curvas características e información del test",
           "Modelos de respuesta graduada",
           "Equiparación y vinculación de puntajes",
           "Diseño de bancos para pruebas adaptativas"],
    "06": ["Puntajes estándar: z, T y estaninos",
           "Normas por edad y por curso escolar",
           "Equidad en evaluaciones de alto impacto",
           "Acomodaciones y diseño universal de la evaluación",
           "Estudios de invarianza entre grupos"],
    "07": ["Ley 19.628 y Ley 21.719: datos personales en evaluación",
           "Consentimiento informado y confidencialidad",
           "Retención, anonimización y eliminación de datos",
           "Decisiones automatizadas y derecho a explicación",
           "Seguridad de bancos de ítems y de resultados"],
}

# (id, slug, titulo, nivel, semanas, descripcion, [clases])
PARTES_NUEVAS = [
    ("08", "inteligencia-y-capacidades-cognitivas", "Inteligencia y capacidades cognitivas",
     "intermedio", "3-4",
     "Modelos de la inteligencia y cómo se evalúan las capacidades cognitivas, con sus límites.",
     ["Modelos de la inteligencia: Spearman, Thurstone, CHC",
      "Inteligencia fluida y cristalizada",
      "Razonamiento abstracto: matrices y series",
      "Razonamiento verbal y comprensión de instrucciones",
      "Razonamiento numérico",
      "Razonamiento espacial",
      "Resolución de problemas y aprendizaje",
      "Aptitudes mentales primarias",
      "Velocidad de procesamiento",
      "Familias de evaluación cognitiva individual: uso, restricciones y alternativas abiertas"]),
    ("09", "atencion-memoria-y-funciones-ejecutivas", "Atención, memoria y funciones ejecutivas",
     "intermedio", "3-4",
     "Tareas experimentales de atención, memoria y control ejecutivo y su traducción a pruebas.",
     ["Atención sostenida y vigilancia",
      "Atención selectiva y dividida",
      "Tiempo de reacción y su medición digital",
      "Memoria visual y auditiva",
      "Memoria de trabajo",
      "Memoria verbal y aprendizaje de listas",
      "Flexibilidad cognitiva e inhibición",
      "Planificación y control ejecutivo",
      "Tareas clásicas: Stroop, Go/No-Go, n-back",
      "Límites de la evaluación neuropsicológica no clínica"]),
    ("10", "personalidad-temperamento-y-conducta", "Personalidad, temperamento y conducta",
     "intermedio", "3-4",
     "Modelos de rasgos, tipologías y estilos conductuales, con su evidencia y sus usos indebidos.",
     ["Modelo de los cinco factores y sus facetas",
      "Banco IPIP: historia y uso abierto",
      "Tipologías frente a rasgos: crítica a MBTI",
      "Modelos de estilos conductuales: DISC y sus límites",
      "Temperamento y desarrollo",
      "Autorregulación e impulsividad",
      "Motivación, valores y preferencias",
      "Fortalezas personales y carácter",
      "Estados frente a rasgos de personalidad",
      "Falseamiento, deseabilidad social y escalas de validez"]),
    ("11", "psicometria-laboral-y-empleabilidad", "Psicometría laboral y empleabilidad",
     "intermedio", "3-4",
     "Evaluación en contextos de trabajo: predicción del desempeño, competencias y ajuste.",
     ["Análisis de puestos y modelos de competencias",
      "Validez predictiva de los métodos de selección",
      "Pruebas de comprensión de instrucciones escritas",
      "Evaluación de desempeño y criterios",
      "Juicio situacional",
      "Personalidad de vendedores y evaluación comercial",
      "Percepción y prevención de riesgos laborales",
      "Ajuste persona-puesto: qué se puede y qué no afirmar",
      "Dominio del inglés laboral: evaluación de idioma",
      "Impacto adverso y defensa legal de una decisión de selección"]),
    ("12", "liderazgo-equipos-y-sociometria", "Liderazgo, equipos y sociometría",
     "intermedio", "3-4",
     "Evaluación del liderazgo, el trabajo en equipo y las relaciones sociales en grupos.",
     ["Teorías del liderazgo: Lewin y estilos",
      "Evaluación de la efectividad del liderazgo",
      "Roles en equipos: modelo Belbin y su evidencia",
      "Comportamiento en equipos de trabajo",
      "Sociometría: elecciones y rechazos",
      "Análisis de redes sociométricas",
      "Cohesión, aislamiento y liderazgo informal",
      "Clima organizacional y escolar",
      "Evaluación 360 y sesgos de los evaluadores",
      "Gestión de conflictos y toma de decisiones"]),
    ("13", "desarrollo-infantil-y-evaluacion-psicoeducativa",
     "Desarrollo infantil y evaluación psicoeducativa", "avanzado", "4-5",
     "Evaluación en la infancia: desarrollo, lenguaje y señales de alerta, con ética reforzada.",
     ["Hitos del desarrollo y sus rangos normales",
      "Desarrollo cognitivo infantil: Piaget y Vygotsky",
      "Desarrollo del lenguaje",
      "Observación sistemática y registros anecdóticos",
      "Cribado frente a diagnóstico en la infancia",
      "Evaluar con la familia: entrevista y devolución",
      "Atención temprana y apoyos",
      "Evaluación en educación parvularia",
      "Cribado del neurodesarrollo: alcances y derivación",
      "Contexto chileno: referentes curriculares y normativos"]),
    ("14", "aprendizaje-aptitudes-y-dificultades-escolares",
     "Aprendizaje, aptitudes y dificultades escolares", "avanzado", "4-5",
     "Lectura, escritura, matemática y dificultades de aprendizaje desde una óptica pedagógica.",
     ["Comprensión lectora: niveles y evaluación",
      "Fluidez y precisión lectora",
      "Escritura y producción textual con rúbricas",
      "Razonamiento matemático y cálculo",
      "Dificultades específicas de aprendizaje: cribado y derivación",
      "Hábitos de estudio y técnicas de estudio",
      "Estrategias metacognitivas y autorregulación del aprendizaje",
      "Motivación académica",
      "Habilidades digitales del estudiantado",
      "Evaluación de apoyos educativos y evaluación inclusiva"]),
    ("15", "orientacion-vocacional-y-competencias-profesionales",
     "Orientación vocacional y competencias profesionales", "intermedio", "3-4",
     "Intereses, valores y competencias para la orientación académica y profesional.",
     ["Teoría de intereses de Holland",
      "Intereses y O*NET Interest Profiler",
      "Valores laborales y de vida",
      "Madurez y toma de decisiones vocacionales",
      "Competencias transversales y empleabilidad",
      "Portafolios de evidencias",
      "Orientación en educación media técnico-profesional",
      "Orientación en educación superior y transición laboral",
      "Formación continua y reconversión laboral",
      "Diseño de un programa de orientación basado en evidencia"]),
    ("16", "evaluacion-socioemocional-y-bienestar", "Evaluación socioemocional y bienestar",
     "avanzado", "4-5",
     "Medición de bienestar y habilidades socioemocionales, con protocolos de protección y derivación.",
     ["Bienestar subjetivo y calidad de vida",
      "Estrés percibido",
      "Resiliencia y autoeficacia",
      "Regulación emocional",
      "Habilidades sociales y empatía",
      "Satisfacción académica y laboral",
      "Escalas de síntomas: qué no se puede hacer sin un profesional",
      "Protocolo de derivación y de riesgo",
      "Evaluación socioemocional escolar",
      "Intervenciones: recomendaciones, intervención profesional y tratamiento"]),
    ("17", "investigacion-psicometrica-y-analisis-de-datos",
     "Investigación psicométrica y análisis de datos", "avanzado", "4-5",
     "Diseño de estudios de validación, simulación y análisis reproducible.",
     ["Diseño de un estudio de validación",
      "Tamaño muestral y potencia",
      "Simulación de datos psicométricos",
      "Datos faltantes en instrumentos",
      "Análisis longitudinal y cambio confiable",
      "Estimación de incertidumbre y bootstrap",
      "Funcionamiento diferencial del ítem en la práctica",
      "Reproducibilidad: preregistro, datos y código",
      "Metaanálisis psicométrico",
      "Redacción y revisión de un informe de validación"]),
    ("18", "ingenieria-de-sistemas-de-evaluacion-digital",
     "Ingeniería de sistemas de evaluación digital", "avanzado", "4-5",
     "Arquitectura, accesibilidad y seguridad de plataformas de evaluación.",
     ["Arquitectura de un motor de evaluación declarativo",
      "Modelos de ítems y esquemas versionados",
      "Baterías de evaluación y sesiones reanudables",
      "Telemetría de interacción y tiempos de respuesta",
      "Evaluación adaptativa: implementación",
      "Accesibilidad de evaluaciones digitales",
      "Auditoría de cálculo y trazabilidad",
      "Seguridad y privacidad por diseño",
      "Interoperabilidad y exportación de resultados",
      "Herramientas abiertas: jsPsych, PsychoPy, lab.js, PEBL"]),
    ("19", "aplicaciones-avanzadas-y-proyectos-integradores",
     "Aplicaciones avanzadas y proyectos integradores", "avanzado", "5-6",
     "Proyectos que integran las partes anteriores con datos sintéticos y decisiones responsables.",
     ["Proyecto: batería educativa de cribado con datos sintéticos",
      "Proyecto: batería laboral con ajuste justificado",
      "Proyecto: adaptación de un instrumento abierto",
      "Proyecto: informe para familias y docentes",
      "Proyecto: informe para una organización",
      "Proyecto: estudio de validación simulado de extremo a extremo",
      "Proyecto: auditoría ética de un instrumento",
      "Proyecto: tablero de seguimiento longitudinal",
      "Proyecto: instrumento original con protocolo de validación",
      "Defensa final y plan de desarrollo profesional"]),
]


def slug(texto: str) -> str:
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return "-".join(s.split("-")[:7])


def clase(num: int, titulo: str, dirparte: str) -> dict:
    return {"id": f"{num:03d}", "numero": num, "titulo": titulo,
            "ruta": f"classes/{dirparte}/{num:03d}-{slug(titulo)}",
            "horas_estimadas": 4, "estado": "planificada"}


def main() -> None:
    ruta_c = RAIZ / "curriculum.yaml"
    curr = yaml.safe_load(ruta_c.read_text(encoding="utf-8"))
    ids = [int(c["id"]) for p in curr["temario"] for c in p["clases"]]
    siguiente = max(ids) + 1
    por_id = {p["id"]: p for p in curr["temario"]}
    nuevas: list[tuple[dict, str]] = []

    for pid, titulos in NUEVAS_EN_EXISTENTES.items():
        p = por_id[pid]
        dirparte = pathlib.Path(p["clases"][0]["ruta"]).parent.name
        tit_existentes = {c["titulo"] for c in p["clases"]}
        for t in titulos:
            if t in tit_existentes:
                continue
            c = clase(siguiente, t, dirparte)
            p["clases"].append(c)
            nuevas.append((c, pid))
            siguiente += 1

    for pid, sl, tit, nivel, sem, desc, titulos in PARTES_NUEVAS:
        if pid in por_id:
            continue
        p = {"id": pid, "slug": sl, "titulo": tit, "nivel": nivel, "semanas": sem,
             "descripcion": desc, "clases": []}
        for t in titulos:
            c = clase(siguiente, t, f"part-{pid}-{sl}")
            p["clases"].append(c)
            nuevas.append((c, pid))
            siguiente += 1
        curr["temario"].append(p)

    curr["partes"] = len(curr["temario"])
    curr["clases"] = sum(len(p["clases"]) for p in curr["temario"])
    cab = ("# Curriculo del programa. Fuente unica de verdad sobre que clases existen\n"
           "# y cual es su estado real. scripts/validate_repository.py comprueba que\n"
           "# lo declarado aqui coincida con el arbol classes/.\n"
           "# Las clases 001-040 conservan su identificador. Las 041+ las agrego\n"
           "# scripts/expand_curriculum.py y estan PLANIFICADAS, no escritas.\n")
    ruta_c.write_text(cab + yaml.safe_dump(curr, allow_unicode=True, sort_keys=False, width=100),
                      encoding="utf-8")

    for c, pid in nuevas:
        carpeta = RAIZ / c["ruta"]
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "lesson.yaml").write_text(
            f'id: "{c["id"]}"\nnumero: {c["numero"]}\ntitulo: "{c["titulo"]}"\n'
            f'parte: "{pid}"\nhoras_estimadas: 4\nestado: planificada\nlaboratorio: null\n',
            encoding="utf-8")
    for p in curr["temario"]:
        d = RAIZ / "classes" / f"part-{p['id']}-{p['slug']}"
        d.mkdir(parents=True, exist_ok=True)
        if not (d / "README.md").exists():
            (d / "README.md").write_text(
                f"# Parte {p['id']} - {p['titulo']}\n\n{p['descripcion']}\n\n"
                "Estado: planificada. Ver `curriculum.yaml` para el estado real de cada clase.\n",
                encoding="utf-8")
    print(f"partes={curr['partes']} clases={curr['clases']} nuevas={len(nuevas)}")


if __name__ == "__main__":
    main()
