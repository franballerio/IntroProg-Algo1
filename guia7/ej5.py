'''funciones sobre listas de listas'''
import numpy as np
import random
import array
# debemos reutilizar estas funciones que definimos en el ejercicio 1


def pertenece(lista: list, elem: int) -> bool:
    '''dice si un elemento pertenece a la lista'''
    for x in lista:
        if x == elem:
            return True
    return False


def ordenados(nums: list) -> list:
    '''agarra una lista y la ordena de menor a mayor'''
    desorden: list = nums
    orden: list = []
    x: int = len(nums)
    while x > 0:
        orden.append(min(desorden))
        desorden.remove(min(desorden))
        x -= 1
    return orden

# 1.
# por la especific. tenemos que pasarle una lista de listas de enteros yel entero que queremos ver si pertenece
# y devuelve una lista con bools en las posiciones de las listas originales, y si e pertenece a la lista[x] tiene un True, sino False


def pertenece_a_cu(number_lists: list, e: int) -> list:
    res: list = []
    for i in number_lists:
        if pertenece(i, e):
            res.append(True)
        else:
            res.append(False)
    return res


# 2.
def es_matriz(matrix: list, x: int = 0, y: int = 1) -> bool:
    '''dice si la lista es una matriz ono'''
    if y < len(matrix) and len(matrix[0]) > 1:
        if len(matrix[x]) == len(matrix[y]):
            return es_matriz(matrix, x + 1, y + 1)
        else:
            return False
    return True


# 3.


def filas_ordenadas(matrix: list) -> bool:

    resu: list = []

    if es_matriz(matrix):
        for fila in matrix:
            if sorted(fila) == fila:
                resu.append(True)
            else:
                resu.append(False)
    return resu


# 4.

def matriz_elevada(d: int, p: int):
    '''eleva a la p, una matriz random de d x d dimensiones'''
    m = np.random.randint(0, 3, (d, d)) ^ 3
    m = np.array(m)
    print(m)  # mostramos la matriz original creada
    print("-----")

    mE = m
    for i in range(1, p):
        mE = m @ mE
    # multiplicamos a la matriz x ella misma p veces
    return mE


print(matriz_elevada(2, 4))
