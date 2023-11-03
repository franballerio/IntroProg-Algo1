# 1.
def del_espacios(txt: str) -> str:
    '''borra los espacios entre las palabras del string'''
    txt_new: str = []
    for i in txt:
        if i != " ":
            txt_new.append(i)
    return txt_new


def cinco_mentarios(archivo: str):
    file = open(f"guia8\\{archivo}", "r", encoding='UTF-8')
    arch = archivo.replace(".txt", "_sin_comentarios.txt")
    arch = open(f"guia8\\{arch}", "w",  encoding='UTF-8')
    lineas = file.readlines()
    lineas_nuevas = []
    # abrimos el archuivo y metemos sus lineas en una lista, creamos la lista para las nuevas lineas, creamos el archivo nuevo

    for line in lineas:
        if line[0] != "#":
            if line[0] != " ":
                lineas_nuevas.append(line)
            else:
                if del_espacios(line)[0] != "#":
                    # para hacer esto tambien existe el metodo .strip()
                    # ej: line.strip() que borra los espacios del principio
                    lineas_nuevas.append(line)
    # metemos las lineas que no son comentarios en la lista

    for linea in lineas_nuevas:
        arch.write(linea)
    # escribimos en el archivo nuevo

    file.close()
    arch.close()


cinco_mentarios("archivo_palabras_copy.txt")
