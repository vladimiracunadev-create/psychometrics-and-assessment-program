"""Laboratorio 069 - Acomodaciones: tiempo extendido en pruebas de velocidad y de poder.

Modelo simple de una prueba de 40 items. Cada persona trabaja a una velocidad (items por
minuto) y acierta cada item intentado con probabilidad p segun su habilidad. Puntaje esperado =
min(40, velocidad * tiempo) * p. Dos grupos con la MISMA habilidad (p = 0.80):
    sin necesidad de apoyo: velocidad 1.2 items/min | con necesidad (procesamiento lento): 0.6
Se compara el efecto del tiempo extendido (x1.5) en una prueba de VELOCIDAD (poco tiempo) y en
una de PODER (tiempo holgado). Es un modelo de juguete: la velocidad y la habilidad se separan
por construccion, lo que en la realidad es una hipotesis a verificar.
"""
from __future__ import annotations

P = 0.80
ITEMS = 40
VEL = {"sin necesidad de apoyo": 1.2, "con necesidad de apoyo": 0.6}


def puntaje(vel: float, tiempo: float) -> float:
    return min(ITEMS, vel * tiempo) * P


def main() -> None:
    print(f"{'prueba':<28} {'grupo':<24} {'normal':>8} {'extendido':>10} {'ganancia':>9}")
    print("=" * 84)
    for nombre, t in (("VELOCIDAD (30 min)", 30), ("PODER (90 min)", 90)):
        for grupo, v in VEL.items():
            a, b = puntaje(v, t), puntaje(v, t * 1.5)
            print(f"{nombre:<28} {grupo:<24} {a:8.1f} {b:10.1f} {b - a:9.1f}")
        print()
    print("Lectura: en la prueba de VELOCIDAD el tiempo extendido ayuda al grupo con necesidad y")
    print("tambien al otro (la velocidad es parte de lo que se mide); en la de PODER, donde todos")
    print("terminan, no cambia nada. La pregunta de diseno es si la velocidad forma parte del")
    print("constructo. Si no, la acomodacion corrige un sesgo; si si, cambia lo que se mide.")
    print("El diseno universal reduce la necesidad de acomodar: tiempo holgado cuando el constructo")
    print("no es la velocidad, instrucciones claras, formatos accesibles desde el inicio.")


if __name__ == "__main__":
    main()
