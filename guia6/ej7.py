'''vamos a hacer las funciones del ej6 pero con for in range()'''


# 1.
def from_1_to_10():
    for i in range(1, 11, 1):
        print(i)


# 2.
def from_10_to_40() -> int:
    for i in range(10, 41, 1):
        print(i)


# 3.
def eco10() -> int:
    for i in range(1, 11):
        print("eco")

# 4.


def lanzar_cohete(num: int):
    '''hace una cuenta regresiva segun el numero de parametro'''
    for i in range(num, 0, -1):
        print(i)
    print("Despegue!!")

# lanzar_cohete(10)


# 5.
def viaje_pasado(partida: int, llegada: int):
    if partida > llegada:
        print(
            f"Estamos en el anio {partida} y queremos ir al anio {llegada} \n-------")
        for i in range(partida, llegada-1, -1):
            print(f"Viajo un anio al pasado, estamos en el anio {i}")
        print("Llegamos!")

# viaje_pasado(2000, 1990)


# 6.
def viajar_con_aris(partida: int):
    '''vamos del anio q pasan por parametro, de 20 en 20 hasta lo mas cercano al 384'''
    if partida > -384:
        if partida >= 0:
            print(
                f"Estamos en el anio {partida} d.C. y viajaremos a visitar a Aristoteles")
        else:
            print(
                f"Estamos en el anio {partida} a.C. y viajaremos a visitar a Aristoteles")
        for year in range(partida, -385, -20):
            if year >= -384:
                if year >= 0:
                    print(f"Viajamos al anio {year} d.C.")
                else:
                    print(f"Viajamos al anio {-year} a.C.")
        print("Llegamos con Aristoteles!!!")


viajar_con_aris(0)
