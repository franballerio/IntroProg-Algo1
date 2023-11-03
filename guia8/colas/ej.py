from queue import Queue as Cola
import numpy as np
import random

# ej 13):


def generar_nros_al_azar(n: int, desde: int = 0, hasta: int = 100) -> Cola:
    cola: Cola = Cola()
    for i in range(0, n):
        cola.put(np.random.randint(desde, hasta))
    return cola


"""res = generar_nros_al_azar(7)
while not res.empty():
    print(res.get())
"""

# ej 14):


def cantidad_de_elem(cola: Cola) -> int:
    x: int = 0
    while not cola.empty():
        cola.get()
        x += 1
    return x


"""rest = cantidad_de_elem(res)
print(rest)
"""


# ej 15):
def buscar_el_maximo(cola: Cola) -> int:
    res: list = []
    while not cola.empty():
        res.append(cola.get())
    print(res)
    return max(res)


"""c: Cola = generar_nros_al_azar(7)
resu = buscar_el_maximo(c)
print(resu)"""


# ej 16):
def armar_sec_bingo():
    sec: Cola = Cola()
    nums: list = list(range(100))
    random.shuffle(nums)
    for num in nums:
        sec.put(num)
    return sec


def jugar_carton_bingo(carton: list, bolillero: Cola = armar_sec_bingo()) -> int:
    '''esta funcion nos dice cuantas tiradas tardamos en terminar nuestro carton'''
    print(f"Tu carton para jugar es: {carton}\n-----")

    jugadas: int = 0

    while len(carton) > 0:
        x = bolillero.get()
        if x in carton:
            carton.remove(x)
        jugadas += 1

    print(f"Tardaste {jugadas} tiradas en completarlo")


# ej 17):
turnos: Cola = Cola()


def sacar_turno(nivel: int, paciente: str, especialidad: str):
    if 1 <= int(nivel) <= 10:
        return turnos.put([nivel, paciente, especialidad])


def n_pacientes_urgentes(fila: Cola) -> int:
    urgentes: int = 0
    while not fila.empty():
        paciente = fila.get()
        if int(paciente[0]) in [1, 2, 3]:
            urgentes += 1
    return urgentes


for i in range(15):
    paciente = random.choice(["Laura Martinez", "Carlos Rodriguez", "Ana Gomez", "Javier Fernandez",
                             "María Lopez", "Pedro Sánchez", "Sofía Pérez", "Diego García", "Lucía Gonzalez", "Manuel Ramírez"])
    especialidad = random.choice(["Cardiología", "Dermatología", "Gastroenterología", "Neurología",
                                 "Oftalmología", "Oncología", "Pediatría", "Psiquiatría", "Traumatología", "Urología"])
    urgencia = random.choice(list(range(1, 10)))
    sacar_turno(urgencia, paciente, especialidad)
    # print(paciente, especialidad, urgencia)

# print(n_pacientes_urgentes(turnos))


# ej 18):
lista_banco: Cola = Cola()


def ingresar_atencion():
    nombre: str = str(input("Ingrese Nombre y Apellido: "))
    dni: int = int(input("Ingrese numero de DNI: "))
    if 3000000 < dni < 47000000:
        cuenta: str = str(input("Su cuenta es preferencial? (si/no): "))
        prioridad: str = str(
            input("Es +65, embarazada o con movilidad reducida? (si/no): "))
        print("Ingresando...\n------")

        cliente = [nombre, dni, cuenta, prioridad]

        return lista_banco.put(cliente)
    else:
        print("Dni invalido")


def atencion_a_clientes(fila: Cola) -> Cola:
    prioridad: Cola = Cola()
    preferencial: Cola = Cola()
    resto: Cola = Cola()

    while not fila.empty():
        cliente = fila.get()
        if cliente[-1] == "si":
            prioridad.put(cliente)
        if cliente[-2] == "si":
            preferencial.put(cliente)
        if cliente[-1] != "si" and cliente[-2] != "si":
            resto.put(cliente)
    # ordenamos los clientes de acuerdo a sus necesidades

    res: Cola = prioridad
    while not preferencial.empty():
        res.put(preferencial.get())
    while not resto.empty():
        res.put(resto.get())
    # creamos la cola final, en el orden prioridad, preferencial, resto

    return res


for i in range(3):
    ingresar_atencion()
fila = list(atencion_a_clientes(lista_banco).queue)
print(fila)



