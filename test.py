'''empezando con python 02/10/2023'''

# ejercicio 1 practica


def saludar():
    '''function returns "Hola mundo"'''
    return print("Hola mundo")

# saludar()

# ej 2 practica


def es_multiplo_de(n: int, m: int):
    '''nos dice si n es multiplo de m, osea n = m*k'''
    return n % m == 0

# ej 3 practica


def es_nombre_largo(x: str):
    '''the function says if the name is long.
    is long if 3 <= name.length() <= 8 '''
    return (3 <= len(x)) and (8 >= len(x))

# ej 5 practica


def devolver_el_doble_si_es_par(x: int):
    '''Si el numero es par, devuelve el doble, sino devuelve el mismo num'''
    if x % 2 == 0:
        print(f"{x*2}")
    else:
        print(f"{x}")

# ej 6 practica


def nums_40():
    '''imprime los numeros pares del 10 al 40'''
    x = 10
    while x < 41 and x > 0:
        if x % 2 == 0:
            print(x)
            x = x + 1
        else:
            x = x + 1


def nums2():
    '''hace lo mismo q la funcion nums_40'''
    for num in range(10, 41, 1):
        if num % 2 == 0:
            print(num)


caa = [1,2,3,4,5,4,3,3,3,2,2,2,2,2,2,2]

print(caa.index(3))
