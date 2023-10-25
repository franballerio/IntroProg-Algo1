'''segunda parte guia 7'''


# 1.
def ceros(nums: list) -> list:
    idx = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            nums.insert(idx, 0)
            nums.pop(idx + 1)
            idx += 1
        else:
            idx += 1
    print(nums)
    return nums


# 2.
def ceros2(numes: list) -> list:
    nums = numes
    idx = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            nums.insert(idx, 0)
            nums.pop(idx + 1)
            idx += 1
        else:
            idx += 1
    print(nums)
    return nums


# 3.
def del_vocales(txt: str) -> str:
    '''le pasamos una cadena de strings y la devuelve sin vocales'''
    vocales: list = ["a", "e", "i", "o", "u"]
    txtt: list = list(txt.lower())
    no_vocales: list = []
    for char in txtt:
        if char not in vocales:
            no_vocales.append(char)
    print("".join(no_vocales))
    return "".join(no_vocales)

# 4.


def reemplaza_vocales(txt: str) -> str:
    '''reemplaza las vocales por "_" en la cadena que le pasamos'''
    vocales: list = ["a", "e", "i", "o", "u"]
    txtt: list = list(txt.lower())
    no_vocales: list = []
    for char in txtt:
        if char not in vocales:
            no_vocales.append(char)
        else:
            no_vocales.append("_")
    print("".join(no_vocales))
    return "".join(no_vocales)


# 5.
def dar_vuelta(txt: str) -> str:
    '''da vuelta el str q le pasemos'''
    txtt: list = list(txt)
    res: list = txtt[::-1]
    print("".join(res))
    return "".join(res)


# 6.
def del_repes(seq: str) -> str:
    '''elimina las letras repetidas'''
    seqq: list = list(seq.lower())
    for x in seqq:
        while seqq.count(x) > 1:
            seqq.remove(x)
    print("".join(seqq))
    return "".join(seqq)


