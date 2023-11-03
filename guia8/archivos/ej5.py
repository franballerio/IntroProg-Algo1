def agregar_al_principio(archivo: str, frase: str):
    file = open(
        f"guia8\{archivo}", "r", encoding="UTF-8")
    # en el primer argumento de open cambiar el enrutamiento
    fileL = file.readlines()
    file.close()
    fileL.insert(0, f"{frase}")
    file = open(
        f"guia8\{archivo}", "w", encoding="UTF-8")
    file.writelines(fileL)
    file.close()


agregar_al_principio("ej3.txt", "Esto es el principio del archivo \n")
