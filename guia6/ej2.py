'''ejercicios 2 de la guia 6'''
import math


# 1.


def imprimirSaludo(x: str) -> str:
    '''imprime un saludo personalizado'''
    print(f"Hola {x}")


# 2.
def raizCuadrada(x: int) -> float:
    '''devuelve la raiz cuadrada del numero que le pasamos'''
    x = round(math.sqrt(x), 2)
    print(x)


# 3.
def farenheitACelcius(x: float) -> float:
    '''convierte a grados celcius los grados farenheit que le pasamos'''
    y: float = round(((x - 32) * 5)/9, 3)
    print(y)

# 4.


def imprimirDoble(x: str) -> str:
    '''imprime el doble de lo que le pasamos'''
    print(x * 2)


# 6.
def esPar(x: int) -> bool:
    '''dice si es par ono, y usamos la funcion 
    es_multiplo_de del test, la cual importamos con sys'''
    return es_multiplo_de(x, 2)


def es_multiplo_de(n: int, m: int) -> bool:
    '''nos dice si n es multiplo de m, osea n = m*k'''
    return n % m == 0


# 7.
def cantDePizzas(comensales: int, porcMin: int) -> int:
    ''''devuelve la cantidad de pizzas que necesitamos, segun la cantidad de porciones que
    deberia comer cada uno, siendo q cada pizza tiene 8 porciones y preferimos que sobre'''
    # por ejemplo si son 10 comensales y cada uno come 3 porciones, necesitamos 4 pizzas
    # 10 * 3 = 30 porciones en total y si cada pizza tiene 8 porciones, 30/8 = 3.75 pizzas,
    # pero como queremos que sobre redondeamos en 4
    x = comensales * porcMin
    y = math.ceil(x/8)
    print(
        f"Necesitaremos {y} pizzas, para que coman los {comensales} comensales, cada uno {porcMin} porciones, y encima sobren")
