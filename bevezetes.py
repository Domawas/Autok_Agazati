def autok():
    auto = input("Adja meg az autó nevét: ")
    gyartas = int(input("Adja meg a gyártás évét: ")) 
    print(f"Az autó neve: {auto}")
    print(f"Gyártási dátum: {gyartas}")
    if gyartas == 2024:
        print(f"Ez a(z) {auto} friss gyártás")
    elif gyartas < 2000:
        print(f"Ez a(z) {auto} öreg autó")
    else:
        print(f"Ez a(z) {auto} átlagos korú")

