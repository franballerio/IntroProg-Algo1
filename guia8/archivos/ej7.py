'''leemos un archivo .csv y operamos con el'''


def promedio_de(LU: str):
    promedios = open(f"guia8\\archivos\\promiedos.csv", "r", encoding="UTF-8")
    promiedos = []
    res: list = []
    for line in promedios.readlines():
        promiedos.append(line.split(","))
    # print(promiedos)
    promiedos.pop(0)
    for nota in promiedos:
        if LU == nota[0]:
            res.append(float(nota[3]))
    return round(sum(res) / len(res), 2)


print(promedio_de("444"))
