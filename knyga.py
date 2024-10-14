import datetime

class Knyga:
    def __init__(self, autorius, pavadinimas, isleidimo_metai, zanras, likusios_knygos=1):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras
        self.likusios_knygos = likusios_knygos
        self.pasiemimo_data = None
        self.grazinimo_data = None
        self.ar_veluojama = False

    def to_dict(self):
        return {
            'autorius': self.autorius,
            'pavadinimas': self.pavadinimas,
            'isleidimo_metai': self.isleidimo_metai,
            'zanras': self.zanras,
            'likusios_knygos': self.likusios_knygos,
            'pasiemimo_data': self.pasiemimo_data.strftime('%Y-%m-%d') if self.pasiemimo_data else None,
            'grazinimo_data': self.grazinimo_data.strftime('%Y-%m-%d') if self.grazinimo_data else None,
            'ar_veluojama': self.ar_veluojama
        }

    def from_dict(data):
        knyga = Knyga(
            data['autorius'],
            data['pavadinimas'],
            data['isleidimo_metai'],
            data['zanras'],
            data.get('likusios_knygos', 1)
        )
        if data.get('pasiemimo_data'):
            knyga.pasiemimo_data = datetime.datetime.strptime(data['pasiemimo_data'], '%Y-%m-%d')
        if data.get('grazinimo_data'):
            knyga.grazinimo_data = datetime.datetime.strptime(data['grazinimo_data'], '%Y-%m-%d')
        knyga.ar_veluojama = data.get('ar_veluojama', False)
        return knyga

    def __str__(self):
        return f"{self.pavadinimas}, autorius {self.autorius} ({self.isleidimo_metai}) - Zanras: {self.zanras}, Kiekis: {self.likusios_knygos}"