from queue import LifoQueue as Pila
import numpy as np

# ej 8:


def generar_al_azar(cuantos: int, desde: int, hasta: int) -> Pila:
    '''genera una Pila de n numeros random, los numeros pertenecen al intervalo [desde, hasta]'''
    lifo: Pila = Pila(maxsize=cuantos)
    for i in range(0, cuantos):
        lifo.put(np.random.randint(desde, hasta))
    return lifo
# podemos hacer una que los vaya mostrando:


def generar2(cuantos: int, desde: int, hasta: int) -> Pila:
    lifo: Pila = generar_al_azar(cuantos, desde, hasta)
    for i in range(0, cuantos):
        lifo.put(np.random.randint(desde, hasta))
    while not lifo.empty():
        print(f"- {lifo.get()}")
# generar2(7, -10, 10)


# ej 9:

def cant_elementos(p: Pila) -> int:
    x: int = 0
    p_copy: Pila = Pila()
    while not p.empty():
        p_copy.put(p.get())
    while not p_copy.empty():
        p_copy.get()
        x += 1
    while not p_copy.empty():
        p.put(p_copy.get())
    return x


# y: Pila = generar_al_azar(26, 0, 10000)
# print(cant_elementos(y))


# ej 10:
def Pila_max(Pila: Pila) -> int:
    Pila_l: Pila = []
    while not Pila.empty():
        Pila_l.append(Pila.get())
    return max(Pila_l)
# print(Pila_max(y))


# ej 11:
def esta_bien_balanceada(suma: str) -> bool:
    p: Pila = Pila()
    res = True

    for i in suma[::-1]:
        if i == "(" or i == ")":
            p.put(i)

    parentesis: int = 0
    while not p.empty():
        if parentesis >= 0:
            if p.get() == "(":
                parentesis += 1
            else:
                parentesis -= 1
        if parentesis < 0:
            res = False

    return res


"""print(
    esta_bien_balanceada("3*(1x2)-(5-4)"),
    esta_bien_balanceada("7((2x7)"),
    esta_bien_balanceada("(8*(9/3)))"),
    esta_bien_balanceada("(8*(9/3)))")
)"""


# 12.
def evaluar(expression: str) -> int:
    '''le pasamos un calculo matematico en notacion postfix y nos da el res'''
    res: Pila = Pila()
    nums: str = "1,2,3,4,5,6,7,8,9,0"
    expresion: list = expression.split()

    for i in expresion:
        if i in nums.split(","):
            res.put(int(i))
        if i == "+":
            res.put(res.get() + res.get())
        if i == "-":
            res.put(-res.get() + res.get())
        if i == "*":
            res.put(res.get() * res.get())
        if i == "/":
            res.put((1/res.get()) / res.get())

    return res.get()


resultado = evaluar("3 4 + 5 * 2 -")
print(resultado)
