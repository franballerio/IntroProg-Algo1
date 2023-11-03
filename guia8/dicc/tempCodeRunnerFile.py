def agrupar_por_long(archivo: str) -> dict:
    file = open(f"guia8\\dicc\\{archivo}", "r", encoding="UTF-8")
    lineas: list = [line.strip() for line in file.readlines()]
    # print(lineas)
    # ya tenemos los renglones del archivo en una lista

    palabras: list = []
    largos: list = []
    apariciones: list = []

    for line in lineas:
        palabras.extend(line.split())
    for palabra in palabras:
        largos.append(len(palabra))
    for num in largos:
        apariciones.append((num, largos.count(num)))
    # metemos en la lista el largo de todas las palabras

    # y ahora solo queda meter en el diccionario la cantidad de apariciones de los largos de las palabras
    # y no pasa nada si hay repetidos xq el dict los saca solo
    apariciones: dict = dict(
        apariciones
    )

    return apariciones


res = agrupar_por_long("archivo.txt")
print(res)
