import Renszarvas

def beolvas():
    lista = []
    fajlbol = open("Mikulasszan.txt", "r", encoding="utf-8")
    adatokListaja = fajlbol.readlines()
    for i in range(1, len(adatokListaja), 1):
        # if not adatokListaja[i].startswith("Santa Claus"):
        if not ("Santa Claus" in adatokListaja[i]):
            daraboltSor = adatokListaja[i].split("@")
            # print(daraboltSor)
            szarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            # print(szarvas)
            lista.append(szarvas)
    fajlbol.close()
    return lista
def hetes():
    # alap feladat
    szarvasokListaja = beolvas()
    # A feladat
    for szarvas in szarvasokListaja:
        print(szarvas.kiir())
    # B feladat
    print("Rénszarvasok száma: " + str(len(szarvasokListaja)))
    # C feladat
    cfel("Pompás", szarvasokListaja)
    # D feladat
    mikulasSzam(szarvasokListaja)
    # E feladat
    atlagMagassag(szarvasokListaja)
    # F feladat
    parosHelyenRepul(szarvasokListaja)
    # G feladat
    leghoszabb(szarvasokListaja)

def leghoszabb(lista):
    maxErt = len(lista[0].leiras)
    maxInd = 0
    ind = 1
    while ind < len(lista):
        if len(lista[ind].leiras) > maxErt:
            maxErt = len(lista[ind].leiras)
            maxInd = ind
        ind += 1

def parosHelyenRepul(lista):
    i = 0
    while i < len(lista):
        daraboltHely = lista[i].hely
        if daraboltHely[i] % 2 == 0:
            print(f"{lista[i].nev} -> {daraboltHely[i]}")


def atlagMagassag(lista: list):
    osszeg = 0
    index = 0
    atlag = 0.0
    while index < len(lista):
        osszeg += lista[index].magassag
        index += 1
    if len(lista) == 0:
        print("Az átlag: 0.")
    else:
        atlag = osszeg / len(lista)
        print(f"A szarvasok átlag magassága: {atlag:2f}")


def mikulasSzam(lista: list):
    i = 0
    db = 0
    while i < len(lista):
        daraboltLeiras = lista[i].leiras.split(" ")
        i2 = 0
        while i2 < len(daraboltLeiras):
            if daraboltLeiras[i2] == "Mikulás":
                db += 1
            index += 1
    print(f"A Mikulás szó előfordulásának száma: {db}")

def cfel(nev: str, lista: list):
    index = 0
    talalt = True
    while index < len(lista) and talalt:
        index += 1
        if lista[index].magyarNev == nev:
            print(f"A szarvas angol neve: {szarvas.angolNev}")
            talalt = False
    if not(talalt):
        print(f"Szarvas angol neve: {lista[index].angolNev}")
    else:
        print("Nincs ilyen rénszarvas")
