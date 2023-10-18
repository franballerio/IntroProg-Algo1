'''arrancamos la guia 7, guia de listas'''

# 1.


def pertenece(lista: list, elem: int) -> bool:
    '''dice si un elemento pertenece a la lista'''
    for x in lista:
        if x == elem:
            print(True)
            return True
    print(False)
    return False


# sino podes usar la funcion x in list


# 2.
def divide_todos(nums: list, e: int) -> bool:
    '''nos dice si un numero divide a todos los de la lista'''
    x: int = 0
    while x <= len(nums)-1:
        if nums[x] % e == 0:
            x += 1
        else:
            print("No divide")
            return False
    print("Divide")
    return True
# acordarse que len(nums) devuelve el tamanio real de la lista, y que los index de los elementos siempre llegan hasta len(nums)-1


# 3.
def suma_total(nums: int) -> int:
    '''recibe una lista de numeros enteros y devuelve la suma de todos ellos'''
    x: int = 0
    for num in nums:
        x += num
    print(x)
    return x


# 4.
def ordenados(nums: list) -> list:
    '''agarra una lista y la ordena de menor a mayor'''
    desorden: list = nums
    orden: list = []
    x: int = len(nums)
    while x > 0:
        orden.append(min(desorden))
        desorden.remove(min(desorden))
        x -= 1
    print(orden)
    return orden

# igual existe .sort() o list = sorted(list)


# 5.
def alguna_mayor_a_7(words: list) -> bool:
    '''retorna True si alguna palabra de la lista tiene mayor long q 7'''
    for word in words:
        if len(word) > 7:
            print(f"La palabra {word} tiene mas de 7 letras")
            return True
    print("No hay ninguna")
    return False


# 6.
def del_espacios(txt: str) -> str:
    '''borra los espacios entre las palabras del string'''
    txt_new: str = []
    for i in txt:
        if i != " ":
            txt_new.append(i)
    return txt_new


def palindromo(text: str) -> bool:
    '''da true si es palindromo'''
    txt: str = text.lower()
    txt: str = del_espacios(txt)
    txt2: list = []
    for char in txt:
        txt2.append(char)
    print(txt2 == txt2[::-1])
    return txt2 == txt2[::-1]


# 7.
def passwords(passw: str) -> str:
    '''devuelve un color segun la fortaleza de la contrasenia,
    verde si es fuerte, roja si es malarda, y sino amarillo
    los requisitos son: La contrasena sera VERDE si:
    a) la longitud es mayor a 8 caracteres
    b) tiene al menos 1 letra minuscula.
    c) tiene al menos 1 letra mayuscula.
    d) tiene al menos 1 digito numerico (0..9)
    La contrasena sera ROJA si:
    a) la longitud es menor a 5 caracteres.
    En caso contrario sera AMARILLA.'''

    x: list = str([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y: list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    z: list = []
    for i in y:
        z.append(i.capitalize())
    if len(passw) < 5:
        return print("Rojo")
    if len(passw) > 8 and (letra in y for letra in passw) and (letra in x for letra in passw) and (letra in z for letra in passw):
        return print("Verde")
    return print("Amarillo")


# 8.
def banco(historial: list) -> int:
    '''recibe una lista de tuplas del tipo ("R",$$) y ("I", $$), donde R es retiro e I ingreso,
    y devuelve el dinero que haya quedado en la cuenta'''
    saldo: int = 0
    for (x, y) in historial:
        if x == "I":
            saldo += y
        if x == "R":
            saldo -= y
    print(saldo)
    return saldo


# 9.
def delete_times(x, lis):
    if x in lis:
        for i in range(0, lis.count(x)):
            lis.remove(x)


def mas_3_vocales(palabra: str) -> bool:
    '''dice si una palabra tiene mas de 3 vocales'''
    palabra2: list = list(palabra)
    x: int = 0
    for i in palabra2:
        if i == "a":
            delete_times("a", palabra2)
            x += 1
        if i == "e":
            delete_times("e", palabra2)
            x += 1
        if i == "i":
            delete_times("i", palabra2)
            x += 1
        if i == "o":
            delete_times("o", palabra2)
            x += 1
        if i == "u":
            delete_times("u", palabra2)
            x += 1
    print(x >= 3)
    return x >= 3


mas_3_vocales("Camarero")
