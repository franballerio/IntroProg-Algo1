'''ejercicio 1 de la guia 6'''
import math
# 1.


def imprimir_un_verso() -> str:
    '''imprime el verso de duki en Trapperz'''
    print("""Voy con una nota que veo todo en cámara lenta 
Una colorada que mide un metro setenta
Una zapas retro que parecen los noventa 
Un perro que si hablas te vacía la cuarenta (prra, prra, prra)
Baby, ando fresco, todo aumenta, yeah
El que no tiene su movie se la inventa, yeah (se la inventa, yeah)
Con tanto billes de cien y de cincuenta (de ciencuenta yeah yeah)
Subo el ticket como si tuviese un checkback, yeah
Mami, ahora estoy puesto pa'l money, money (money, money)
No tengo otra cosa en qué pensar (no, no, no), yeah
Aunque no te tengo yo me siento falling
Solo me he aprendido a levantar (yeah, yeah, yeah)
Whippin' in the corner, esquivando a la poli
Negocio con solo una llamá' (bang, bang, bang)
Viajes en avión y reuniones en el lobby
Siempre vistiendo informal
Con Supreme y Fila, fumando noche y día
Hoes está en la esquina
No sabemos lo que hay
Con Supreme y Fila, fumando noche y día
Hoes está en la esquina
No sabemos lo que hay""")


# 2.

def raizDe2() -> float:
    '''devuelve la raiz de 2 con '''
    x: complex = 2
    x: complex = round(math.sqrt(x), 4)
    print(x)


# 3.

def fact2() -> int:
    '''nos da el factorial de 2'''
    x = math.factorial(2)
    print(x)


# 4.

def factorial() -> int:
    '''le pasamos un numero y nos da el factorial'''
    x = int(input("Dame un numero mayor a cero "))
    x = math.factorial(x)
    print(x)


# 5.

def perimetro() -> float:
    '''devuelve el perimetro de una cirunferencia de radio 1'''
    x = 2 * math.pi
    print(x)


# 6.
