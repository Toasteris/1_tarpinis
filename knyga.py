class Knyga:
    def __init__(self, autorius, pavadinimas, isleidimo_metai, zanras):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.isleidimo_metai = isleidimo_metai
        self.genre = zanras

    def __repr__(self):
        return f"Knyga({self.autorius}, {self.pavadinimas}, {self.isleidimo_metai}, {self.zanras})"