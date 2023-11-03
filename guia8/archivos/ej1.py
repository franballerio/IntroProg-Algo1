# 1.
def contar_lineas(archivo: str) -> int:
    arch = open(f"guia8\\{archivo}", "r", encoding='UTF-8')
    res: int = len(arch.readlines())
    arch.close()
    return res
# print(contar_lineas('archivo_palabras.txt'))


# 2.
def existe_palabra_en(palabra: str, archivo: str) -> bool:
    file = open(f"guia8\\{archivo}", "r", encoding='UTF-8')
    for line in file.readlines():
        if palabra in line:
            return True
    return False
# print(existe_palabra_en("que", "archivo_palabras.txt"))


# 3.
def apariciones(word: str, archivo: str):
    file = open(f"guia8\\{archivo}", "r", encoding='UTF-8')
    apariciones: list = []
    for linea in file.readlines():
        apariciones.append(linea.count(word))
    return sum(apariciones)
print(apariciones("prueba", "archivo_palabras.txt"))
