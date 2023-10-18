'''ejercicios de la practica del dia 09/10/2023'''


def suma_total(nums: list) -> int:
    '''suma el total de los elementos de la lista'''
    x: int = 0
    for num in nums:
        x += num
    print(x)
    return x


# suma_total([1, 2, 3, 4, 45, 56, 6, 7, 56])


def pertenece(lista: list, x: int) -> bool:
    '''dice si pertenece a la lista un elemento'''
    for i in lista:
        if i == x:
            print("Pertenece")
            return True
    print("No pertenece")
    return False


def pertenece2(lista: list, x: int) -> bool:
    '''dice si pertenece a la lista un elemento'''
    leng = len(lista) - 1
    while leng > 0:
        if lista[leng] == x:
            print("Pertenece")
            return True
        leng -= 1
    print("No pertenece")
    return False


def pertenece3(lista: list, x: int) -> bool:
    '''dice si pertenece a la lista un elemento'''
    return x in lista


pertenece3([1, 2, 3, 4, 45, 56, 6, 7, 56], 4)