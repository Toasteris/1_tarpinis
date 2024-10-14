class Knyga:
    def __init__(self, autorius, pavadinimas, isleidimo_metai, zanras, likusios_knygos):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.isleidimo_metai = isleidimo_metai
        self.genre = zanras
        self.likusios_knygos = likusios_knygos

    def __str__(self):
        return f"{self.pavadinimas}, autorius {self.autorius} ({self.isleidimo_metai}) - Zanras: {self.zanras}, Kiekis: {self.likusios_knygos}"