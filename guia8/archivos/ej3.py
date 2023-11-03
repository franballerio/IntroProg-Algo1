'''implementamos una fun que agarra un archivo de texto 
y devuelve uno nuevo con las lineas de atras para adelante'''

def reverso(archivo: str):
    file = open(f"/home/clinux01/Escritorio/fb-simulacro/{archivo}", "r", encoding="UTF-8")
    file_rev = open(f"/home/clinux01/Escritorio/fb-simulacro/reverso.txt", "w", encoding="UTF-8")
    lineas: list = file.readlines()
    for linea in lineas[::-1]:
        file_rev.write(linea)
    file.close()
    file_rev.close()

reverso("ej3.txt")
