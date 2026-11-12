"""Laboratorio 188 - Seudonimizacion con clave (HMAC) y retencion automatica.

1. Seudonimos con HMAC-SHA256: el codigo de una persona se deriva de su identificador con una
   CLAVE secreta guardada aparte. Sin la clave no se puede recalcular ni verificar el seudonimo
   (a diferencia de un hash simple, que se puede probar contra una lista de RUT posibles). Se
   demuestra un ataque de diccionario contra un hash simple y su fallo contra HMAC.
   El identificador usado es FICTICIO (formato de ejemplo, no un RUT real).
2. Retencion: una politica de plazos por categoria elimina lo vencido; se verifica que los
   registros dentro del plazo se conservan.
"""
from __future__ import annotations

import hashlib
import hmac

CLAVE = b"clave-de-demostracion-no-usar-en-produccion"


def hash_simple(identificador: str) -> str:
    return hashlib.sha256(identificador.encode()).hexdigest()[:16]


def seudonimo(identificador: str, clave: bytes = CLAVE) -> str:
    return hmac.new(clave, identificador.encode(), hashlib.sha256).hexdigest()[:16]


def main() -> None:
    universo = [f"10.000.{i:03d}-K" for i in range(1000)]            # identificadores FICTICIOS
    victima = universo[437]
    objetivo_simple = hash_simple(victima)
    hallado = next((c for c in universo if hash_simple(c) == objetivo_simple), None)
    print(f"Hash simple: un atacante con la lista de identificadores recupera a la persona: {hallado == victima}")
    objetivo_hmac = seudonimo(victima)
    hallado2 = next((c for c in universo if hash_simple(c) == objetivo_hmac), None)
    print(f"HMAC: el mismo ataque sin la clave encuentra a la persona: {hallado2 == victima}")
    print(f"HMAC es estable con la clave: {seudonimo(victima) == objetivo_hmac}; "
          f"cambia con otra clave: {seudonimo(victima, b'otra') != objetivo_hmac}")

    politica_dias = {"respuestas": 365, "telemetria_agregada": 180, "consentimientos": 1825}
    registros = [("respuestas", 100), ("respuestas", 400), ("telemetria_agregada", 200),
                 ("telemetria_agregada", 30), ("consentimientos", 1000)]
    conservar = [(cat, edad) for cat, edad in registros if edad <= politica_dias[cat]]
    eliminar = [r for r in registros if r not in conservar]
    print(f"\nPolitica de retencion (dias): {politica_dias}")
    print(f"  conservar: {conservar}")
    print(f"  eliminar : {eliminar}")
    print()
    print("Lectura: seudonimizar con HMAC separa los resultados de la identidad; la clave se guarda fuera del")
    print("conjunto de datos y se rota con un procedimiento. Los plazos de retencion deben fijarse segun la")
    print("finalidad y la normativa vigente (clases 076 y 078); la eliminacion incluye copias de seguridad.")


if __name__ == "__main__":
    main()
