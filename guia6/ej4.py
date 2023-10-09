''' ahora resolvemos el ejercicio 4 de la guia 6, usando min y max'''

# altura de pinos en metros, su peso depende de su altura.
# por centimetro hay 3kg hasta los 3mts, dsp 2kg por centimetro.
# 2 metros pesan 200cm * 3kg = 600kg y 5 metros pesan 300cm * 3kg + 200cm * 2kg = 1300kg
# necesitamos pinos de entre 400 y 1000kg


def peso_pino(altura: int) -> int:
    '''por la altura del pino en metros nos da el peso, segun las reglas que pusimos antes'''
    alt_cent: int = altura * 100
    peso: int = 0
    if alt_cent > 300:
        peso = (alt_cent - 300) * 2 + 300 * 3
        return peso
    else:
        peso = alt_cent * 3
        return peso


def es_peso_util(peso: int) -> bool:
    '''recibe un peso en kg y dice si nos sirve el pino ono'''
    return 400 <= peso <= 1000


def sirve_pino(altura: int) -> bool:
    '''dada la altura en metros del pino, nos dice si sirve ono'''
    return es_peso_util(peso_pino(altura))
