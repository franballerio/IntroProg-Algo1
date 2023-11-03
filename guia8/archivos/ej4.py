def agregar_frase(archivo: str, frase: str):
    file = open(f"/home/clinux01/Escritorio/fb-simulacro/{archivo}", "a", encoding="UTF-8")
    # abrimos el archivo en modo "a" (append), para agregar lineas.
    # si lo abrimos en "w" (write), lo que hace es 
    # borrar todo el contenido y escribir lo que pasamos
    file.write(f"\n{frase}")
    file.close()

agregar_frase("ej3.txt", "Esta es la ultima linea")