class Renszarvas:

    def __init__(self, nev: str, magassag: str, hely: str, leiras: str):
        self.nev = nev
        daraboltNev = nev.split(" – ")
        self.angolNev = daraboltNev[0]
        self.magyarNev = daraboltNev[1]
        self.magassag = int(magassag)
        self.hely = int(hely)
        self.leiras = leiras

    def kiir(self) -> str:
        return f"Rénszarvas neve: {self.nev}\nMagassága: {self.magassag}"

    def __str__(self) -> str:
        return f"Rénszarvas adatai: \nAngol név: {self.angolNev}\nMagyar név: {self.magyarNev}\nMagasság: {self.hely}\nSorban elfoglalt helye: {self.magassag}\nLeírás: {self.leiras}"