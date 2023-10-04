'''Resolvemos el ej3 de la guia 6, sin usar el if '''

import math

# 1.


def algunoEsCero(x: float, y: float) -> bool:
    '''dice si alguno de los dos numeros es cero'''
    return x == 0 or y == 0

# 2.


def ambosSonCero(x: float, y: float) -> bool:
    '''dice si ambos numeros son cero'''
    return x == 0 and y == 0

# 3.


def es_nombre_largo(x: str):
    '''the function says if the name is long.
    is long if 3 <= name.length() <= 8 '''
    return (3 <= len(x)) and (8 >= len(x))


# 4.
def es_bisitesto(anio: int) -> bool:
    '''dice si el anio es bisiesto'''
    return anio % 4 == 0 and anio % 100 != 0
