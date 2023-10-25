'''nos dice el estado de aprobacion de una materia.
por la especificacion podemos decir que:
- las notas pueden se entre 0 y 10
- podemos tenes 3 resultados:
> 1, si todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7
> 2 , si todos los elementos de notas son mayores o iguales a 4 y el promedio esta entre 4 (inclusive) y 7
> 3, si alguno de los elementos de notas es menor a 4 o el promedio es menor a 4'''


# primero hacemos la funcion promedio para q sea mas facil
def promedio(notas: list) -> int:
    '''da el promedio de la lista de notas que le pasamos'''
    res = sum(notas) / len(notas)
    return round(res, 2)


def algu_menor_4(notas: list) -> bool:
    '''dice si alguna nota es menor que 4'''
    for nota in notas:
        if nota < 4:
            return True


def estado_aprobacion(notas: list) -> int:
    '''nos devuelve el estado de las notas del alumno'''
    prom: int = promedio(notas)
    if (x >= 4 for x in notas) and prom >= 7:
        return 1
    if (x >= 4 for x in notas) and 4 <= prom < 7:
        return 2
    if algu_menor_4(notas) or prom < 4:
        return 3
