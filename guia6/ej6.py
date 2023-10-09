'''ej6 guia 6, empezamos a usar while'''

# 1.


def from1to10():
    '''imprime del 1 al 10'''
    x: int = 1
    while x < 11:
        print(x)
        x += 1


# from1to10()


# 2.
def pares_10_a_40():
    '''imprime los pares del 10 al 40'''
    x: int = 10
    while x < 41:
        if x % 2 == 0:
            print(x)
            x += 1
        else:
            x += 1

# pares_10_a_40()


# 3.
def eco():
    x: int = 1
    while x < 11:
        print(f"{x}. eco")
        x += 1

# 4.


def lanzar_cohete(num: int) -> str:
    x: int = num
    while x > 0:
        print(x)
        x -= 1
    return print("Despegue!")


# lanzar_cohete(100)


# 4.1
def lanzar_cohete2() -> str:
    '''aca hicimos el ej4 pero con un input'''
    x: int = int(input("Escriba el numero por donde desea comenzar: "))
    while x > 0:
        print(x)
        x -= 1
    return print("Despegue!")


# 5.
def viaje_al_pasado(partida:  int, llegada: int) -> str:
    '''llegada < partida'''
    x: int = partida
    y: int = llegada
    print(f"Estamos en el anio {x} y viajaremos al {y}")
    x -= 1
    while x >= y:
        print(f"Viajo un anio al pasado, estamos en el anio {x}")
        x -= 1
    print("Llegamos!!")


# viaje_al_pasado(2023, 2017)
# como veran tengo un teclado en ingles y no tengo ni tildes ni enies


# 6.
def viaje_a_arist(partida:  int) -> str:
    '''384 < partida'''
    x: int = partida
    y: int = 384
    z: int = 0
    print(f"Estamos en el anio {x} y viajaremos al {y}")
    x -= 20
    while x >= y:
        z += 20
        print(f"Viajo veinte anios al pasado, estamos en el anio {x}")
        x -= 20
    print(f"Llegamos con Aristoteles!!, viajamos en total {z} anios")


# viaje_a_arist(446)
