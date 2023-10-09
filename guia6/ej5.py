'''ejercicio 5 guia 6, ahora si usamos if'''

# aux


def par(num: int) -> bool:
    return num % 2 == 0


# 1.
def devolver_el_doble_si_es_par(numero: int) -> int:
    '''devuelve el doble del numero si es par, sino devuelve el numero
    si ponemos el print, lo que hace es devolver y mostrar'''
    if par(numero):
        # print(f"{numero*2}")
        return numero * 2
    # print(f"{numero}")
    return numero

# devolver_el_doble_si_es_par(12)


# 2.
def devolver_valor_si_es_par_sino_el_siguiente(numero: int) -> int:
    '''devuelve el num si es par, sino el siguiente'''
    if par(numero):
        return numero
    return numero + 1


# 3.
def ej3_6(num: int) -> int:
    '''devuelve el doble si num es multiplo de 3 y el triple si es multiplo de 9, sino
    devuelve el numero original'''
    if num % 9 == 0:
        return num * 3
    elif num % 3 == 0:
        return num * 2
    return num


# 4.
def lindo_nombre(nombre: str) -> str:
    '''dice si tu nombre tiene mas de 5 letras'''
    if len(nombre) >= 5:
        return print(f"Tu nombre es muy largo, {nombre}")
    return print("Tu nombre tiene menos de 5 caracteres")


# 5.
def el_rango(x: int) -> int:
    '''imprime por pantalla “Menor a 5” si el numero es menor a 5, “Entre 10 y 20” 
    si el numero esta en ese rango y “Mayor a 20” si el numero es mayor a 20'''
    if x < 5:
        return print("Menor a 5")
    elif 10 <= x <= 20:
        return print("Entre 10 y 20")
    elif x > 20:
        return print("Mayor a 20")


# 6.
def vacas(sexo: chr, edad: int) -> str:
    '''En Argentina una persona del sexo femenino se jubila a los 60 anos, 
    mientras que aquellas del sexo masculino se jubilan a los 65 anos. 
    Quienes son menores de 18 anos se deben ir de vacaciones junto al grupo que se jubila. 
    Al resto de las personas se les ordena ir a trabajar. 
    Implemente una funcion que, dados los parametros de sexo (F o M) y edad,
    imprima la frase que corresponda segun el caso: “Anda de vacaciones” o “Te toca trabajar”'''
    x = sexo
    y = edad
    if 0 < y <= 18:
        return print("Anda de vacaciones")
    if x == "M" and 18 < y < 65:
        return print("Te toca trabajar")
    if x == "F" and 18 < y < 60:
        return print("Te toca trabajar")
    return print("Anda de vacaciones")
