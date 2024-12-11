from Autok import Auto

def flotta(autok):
    return len(autok)

def legfiatalabb_auto(autok):
    fiatal_auto = min(autok)
    return fiatal_auto

def kiir():
    autok = ("auto.txt")

    print(f"III/Flotta:\n         Autók száma: {flotta(autok)}.")

    fiatal_auto = legfiatalabb_auto(autok)
    print(f"III/Legfiatalabb\n         A legfiatalabb autó: {fiatal_auto.tipus} {fiatal_auto.nev} ({fiatal_auto.gyartas}).")

    aktualis_ev = 2024
    print(f"III/Átlag kor\n         Az autók átlagos kora: {atlag_kor(autok, aktualis_ev):.2f} év.")
