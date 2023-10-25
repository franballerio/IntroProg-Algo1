'''empezamos a usar el input'''
import random
# 1.


def estudiantes() -> list:
    '''metemos el nombre de los estudiantes que queramos, y nos pasa una lista con ellos'''
    x: str = input(
        "Ingrese Nombre de Estudiante, o Listo para terminar ")
    lista_estudiantes: list = []
    while x != "Listo":
        lista_estudiantes.append(x)
        x: str = input(
            "Ingrese Nombre de Estudiante, o Listo para terminar ")
    return lista_estudiantes


# 2.
def historial_sube() -> list:
    '''el usuario sube las operaciones realizadas y le devolvemos una lista con ellas'''
    operacion: str = input("Ingrese operacion, o X para finalizar: ")
    monedero: list = []
    if operacion not in ["X", "C", "D"]:
        operacion: str = input("Ingrese operacion valida: ")
    while operacion == "C" or operacion == "D" and operacion != "X":
        monto: int = input("Ingrese monto deseado: ")
        monedero.append((operacion, monto))
        operacion: str = input("Ingrese operacion, o X para finalizar: ")
        if operacion not in ["X", "C", "D"]:
            operacion: str = input("Ingrese operacion valida: ")
    return monedero


# 3.
def mas_cerca_y_menor(jugador: int, crupier: int, numero: int) -> int:
    '''dados 2 numeros dice cual esta mas cerca del 3ro'''
    if jugador > numero:
        return crupier
    if crupier > numero:
        return jugador
    if numero - jugador < numero - crupier:
        return jugador
    else:
        return crupier


def jugar_7_y_medio() -> str:

    print("\nBienvenido, juguemos!\n------")

    cartasj: list = []
    cartasc: list = []
    valor_j: int = 0
    valor_c: int = 0
    # creamos la lista con las cartas del jugador y del crupier, ademas de las variables que controlan los valores totales

    p1: int = random.choice([1, 2, 3, 4, 5, 6, 7, 11, 12, 10])
    print(f"Tu carta es: {p1}")
    cartasj.append(p1)
    if p1 not in [11, 10, 12]:
        valor_j += p1
    else:
        valor_j += 0.5
    # elige de manera aleatoria tu carta

    crupier: int = random.choice([1, 2, 3, 4, 5, 6, 7, 11, 12, 10])
    print(f"La carta del crupier es: {crupier}")
    cartasc.append(crupier)
    if crupier not in [11, 10, 12]:
        valor_c += crupier
    else:
        valor_c += 0.5
    # ahora la del crupier

    usuario: str = input(
        "Si desea plantarse digite Plantarse, si desea sacar otra carta digite Sacar: ")

    while usuario in ("Plantarse", "Sacar"):
        if usuario == "Plantarse":
            # cuando el usuario se planta, el crupier saca sus cartas hasta llegar o pasarse de 7.5
            while valor_c < 7.5:
                crupier: int = random.choice(
                    [1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
                cartasc.append(crupier)
                if crupier not in [11, 10, 12]:
                    valor_c += crupier
                else:
                    valor_c += 0.5
            if valor_j == valor_c:
                return print(f"Empate!, tus cartas fueron: {cartasj}, las cartas del crupier fueron: {cartasc}")
            if mas_cerca_y_menor(valor_j, valor_c, 7.5) == valor_j:
                return print(f"Ganaste!, tus cartas fueron: {cartasj}, las cartas del crupier fueron: {cartasc}")
            return print(f"Perdiste!, tus cartas fueron: {cartasj}, las cartas del crupier fueron: {cartasc}")
        p1: int = random.choice([1, 2, 3, 4, 5, 6, 7, 11, 12, 10])
        print(f"Tu carta es: {p1}")
        cartasj.append(p1)
        if p1 not in [11, 10, 12]:
            valor_j += p1
        else:
            valor_j += 0.5
        if valor_j > 7.5:
            return print(f"Perdiste!, tus cartas fueron: {cartasj}, las cartas del crupier fueron: {cartasc}")
        usuario: str = input(
            "Si desea plantarse digite Plantarse, si desea sacar otra carta digite Sacar: ")
