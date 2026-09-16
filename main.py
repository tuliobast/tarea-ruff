import json
from pathlib import Path


def cargar(ruta, extras=None):
    if extras is None:
        extras = []
    archivo = Path(Path.cwd()) / ruta
    with Path.open(archivo) as f:
        datos = json.load(f)
    for e in extras:
        datos.append(e)
    return datos


def resumen(datos, nombre):
    print("Procesando %s con %d registros" % (nombre, len(datos)))  # noqa: UP031
    resultado = []
    for d in datos:
        if d is not None:
            resultado.append(d)
    return resultado


cargar("data.json")
resumen(cargar("data.json"), "data.json")
