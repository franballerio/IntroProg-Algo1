# ej 19):
from queue import LifoQueue as Pila


def agrupar_por_long(archivo: str) -> dict:
    file = open(f"guia8\\dicc\\{archivo}", "r", encoding="UTF-8")
    lines: list = [line.split() for line in file.readlines()]
    # ya tenemos los renglones del archivo en una lista

    largos: list = []
    apariciones: list = []

    for line in lines:
        for word in line:
            largos.append(len(word))
    for num in largos:
        apariciones.append((num, largos.count(num)))
    # metemos en la lista el largo de todas las palabras

    # y ahora solo queda meter en el diccionario la cantidad de apariciones de los largos de las palabras no pasa nada si hay repetidos xq el dict los saca solo
    apariciones: dict = dict(apariciones)

    return apariciones
# res = agrupar_por_long("archivo.txt")


# ej 20):
def promedio_de(LU: str):
    promedios = open(f"guia8\dicc\promiedos.csv", "r", encoding="UTF-8")
    promiedos = []
    res: list = []

    for line in promedios.readlines():
        promiedos.append(line.split(","))
    promiedos.pop(0)

    for nota in promiedos:
        if LU == nota[0]:
            res.append(float(nota[3]))
    return round(sum(res) / len(res), 2)


def promedios_alumnos(archivo: str) -> dict:
    '''calcula el promedio de todos los alumnos del archivo.csv
    y los devuelve en un diccionario'''

    file = open(f"guia8\dicc\promiedos.csv", "r", encoding="UTF-8")
    alumnos = []
    for line in file.readlines():
        alumnos.append(line.split(",")[0])
    alumnos.pop(0)
    alumnos = set(alumnos)
    # creamos una lista con las LU de cada alumno

    promedios: list = []
    for LU in alumnos:
        promedios.append((LU, promedio_de(LU)))
    promedios: dict = dict(promedios)

    return promedios
# res = promedios_alumnos("promiedos.csv")


# ej 21):
def la_palabra_mas_frecuente(archivo: str) -> str:
    file = open(f"guia8\\dicc\\{archivo}", "r", encoding="UTF-8")
    words: list = []

    for line in file.readlines():
        linea = line.strip()
        words.extend(linea.split(" "))

    apariciones: list = []

    for word in words:
        apariciones.append((word, words.count(word)))

    apariciones: dict = dict(apariciones)

    for word, times in apariciones.items():
        if max(apariciones.values()) == times:
            res = word
    return res
# print(la_palabra_mas_frecuente("archivo.txt"))


# ej 22):

historiales: dict = {}
historiales_aux: dict = {}


def visitar_sitio(historiales: dict, usuario: str, sitio: str):
    historial: Pila = Pila()
    historial.put(sitio)
    historiales[usuario] = historial


def navegar_atras(historiales: dict, usuario: str):
    historial: Pila = historiales[usuario]
    x = historial.get()
    historiales_aux[usuario] = x
    return x


def navegar_adelante(historiales: dict, usuario: str, y=historiales_aux):
    visitar_sitio(historiales, usuario, historiales_aux[usuario])


'''
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")
'''


# ej 23):
def agregar_producto(inventario: dict, nombre: str, precio: float, cantidad: float):
    '''agrega el producto al inventario que le pasemos'''
    if not nombre in inventario:
        inventario[nombre] = {
            "Precio": precio,
            "Cantidad": cantidad
        }
    return inventario


def actualizar_stock(inventario: dict, nombre: str, cantidad: str):
    if nombre in inventario:
        inventario[nombre]["Cantidad"] = cantidad
        return inventario
    else:
        print("Producto no disponible")


def actualizar_precios(inventario: dict, nombre: str, precio: str):
    if nombre in inventario:
        inventario[nombre]["Precio"] = precio
        return inventario
    else:
        print("Producto no disponible")


def calcular_valor_inventario(inventario: dict) -> float:
    precioXcant: list = []
    for producto, info in inventario.items():
        precioXcant.append(info["Cantidad"] * info["Precio"])
    return sum(precioXcant)


inventario: dict = {}
# inventario tiene como key el producto y como value un diccionario con (precio, cantidad)

agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)
