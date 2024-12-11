import random


def generalt_lottoszamok():
    lottoszamok = []
    while len(lottoszamok) < 5: 
        szam = random.randint(1, 90)
        lottoszamok.append(szam)
    return lottoszamok


def egyjegyuek_szama(lottoszamok):
    egyjegyu = 0
    for szam in lottoszamok:
        if 1 <= szam <= 9:
            egyjegyu += 1
    return egyjegyu


def konzol_kiir(lottoszamok, egyjegyuek):

    print(*lottoszamok, sep="; ", end="; \n")  
    print(f"Az egyjegyűek száma: {egyjegyuek}.")


def file_kiir(lottoszamok, egyjegyuek):
    with open("szamok.txt", "w") as file:
        file.write("; ".join(map(str, lottoszamok)) + ";\n")
        file.write(f"Az egyjegyűek száma: {egyjegyuek}.\n")



