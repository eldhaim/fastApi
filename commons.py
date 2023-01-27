from fastapi import HTTPException


def mensaje_con_parametros(
        mensaje: str,
        parametros: list
):
    """Funcion que se encarga de retornar un mensaje
reemplazando las ocurrencias del mensaje
en '[0]' donde 0 es el consecutivo que debe
aumentar en caso de que existan varias variables
que se deban reemplazar.
:param mensaje: Mensaje el cual sera tratado (Debe tener
la misma cantidad de '[contador]' que los
parametros).
:param parametros: Lista que contiene los parametros que
seran reemplazados en el mensaje"""
    contador = 0
    for parametro in list(map(str, parametros)):
        mensaje = mensaje.replace(f'[{str(contador)}]', parametro)
        contador += 1
    return mensaje


def validation_for_response(condition: bool,
                            status_code: int,
                            detail: dict):
    if not condition:
        raise HTTPException(
            status_code=status_code,
            detail=detail
        )
