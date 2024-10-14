import json
import os
import datetime
from knyga import Knyga

DATA_FILE = 'data/knygos.json'

def prideti_knyga(biblioteka_file):
    autorius = input("Irasykite knygos autoriu: ")
    pavadinimas = input("Irasykite knygos pavadinima: ")
    isleidimo_metai = input("Irasykite isleidimo metus: ")
    zanras = input("Irasykite knygos zanra: ")
    try:
        likusios_knygos = int(input("Irasykite kiek norite prideti: "))

        knyga = Knyga(autorius, pavadinimas, isleidimo_metai, zanras, likusios_knygos)

        if os.path.exists(biblioteka_file):
            with open(biblioteka_file, 'r') as file:
                knygos_data = json.load(file)
        else:
            knygos_data = []

        for existing_knyga in knygos_data:
            if existing_knyga['pavadinimas'].lower() == knyga.pavadinimas.lower():
                existing_knyga['likusios_knygos'] += knyga.likusios_knygos
                print(f"Knyga '{knyga.pavadinimas}' buvo atnaujinta. Liko knygu: {existing_knyga['likusios_knygos']}")
                break
        else:
            knygos_data.append(knyga.to_dict())
            print(f"Knyga '{knyga.pavadinimas}' prideta. Liko knygu: {knyga.likusios_knygos}")

        with open(biblioteka_file, 'w') as file:
            json.dump(knygos_data, file, indent=4)

    except ValueError:
        print("Klaida: Prašome įvesti galiojantį skaičių.")
    except Exception as e:
        print(f"Nepavyko pridėti knygos: {e}")

def issaugoti_knyga(knyga, biblioteka_file):
    try:
        if os.path.exists(biblioteka_file):
            with open(biblioteka_file, 'r') as file:
                knygos_data = json.load(file)
        else:
            knygos_data = []

        for existing_knyga in knygos_data:
            if existing_knyga['pavadinimas'].lower() == knyga.pavadinimas.lower():
                existing_knyga['likusios_knygos'] += knyga.likusios_knygos
                break
        else:
            knygos_data.append(knyga.to_dict())

        with open(biblioteka_file, 'w') as file:
            json.dump(knygos_data, file, indent=4)

    except Exception as e:
        print(f"Nepavyko issaugoti knygos: {e}")

def panaikinti_knygas():
    try:
        ribiniai_metai = int(input("Irasykite metu riba: "))
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                knygos = json.load(file)
        else:
            print("Nera ko naikinti")
            return
            
        naujos_knygos = [knyga for knyga in knygos if knyga['isleidimo_metai'] >= ribiniai_metai]

        if len(knygos) == len(naujos_knygos):
            print("Jokiu knygu nepanaikinta. Visos knygos naujesnes nei ribiniai metai")
        else:
            print(f"{len(knygos) - len(naujos_knygos)} knyga(os) panaikintos")

        with open(DATA_FILE, 'w') as file:
            json.dump(naujos_knygos, file, indent=4)

    except ValueError:
        print("Neteisingai. Metai turi buti skaicius")
    except Exception as e:
        print(f"Ivyko klaida: {e}")

def pasiimti_knyga(biblioteka_file, pavadinimas):
    try:
        with open(biblioteka_file, 'r') as file:
            knygos_data = json.load(file)

        knygos = [Knyga.from_dict(knyga_data) for knyga_data in knygos_data]

        for knyga in knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                if knyga.likusios_knygos > 0:
                    knyga.likusios_knygos -= 1
                    knyga.pasiemimo_data = datetime.datetime.now()
                    knyga.grazinimo_data = knyga.pasiemimo_data + datetime.timedelta(days=14)
                    print(f"Pasiemete knyga '{pavadinimas}'. Grazinimo data: {knyga.grazinimo_data.strftime('%Y-%m-%d')}")
                else:
                    print(f"Knygos '{pavadinimas}' nebeliko!")
                break
        else:
            print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

        with open(biblioteka_file, 'w') as file:
            json.dump([knyga.to_dict() for knyga in knygos], file, indent=4)

    except FileNotFoundError:
        print("Bibliotekoje failas neegzistuoja.")
    except Exception as e:
        print(f"Ivyko klaida: {e}")

def ieskoti_knygos(biblioteka_file, ieskoti_pagal, reiksme):
    try:
        with open(biblioteka_file, 'r') as file:
            knygos = json.load(file)

        reiksme = reiksme.lower()
        rastos_knygos = [knyga for knyga in knygos if knyga[ieskoti_pagal].lower() == reiksme]

        if rastos_knygos:
            for knyga in rastos_knygos:
                print(f"Knyga rasta: {knyga['pavadinimas']} - Autorius: {knyga['autorius']}, Liko knygu: {knyga.get('likusios_knygos', 'N/A')}")
        else:
            print(f"Nerasta knygu pagal {ieskoti_pagal} '(reiksme)'")

    except FileNotFoundError:
        print("Bibliotekoje failas neegzistuoja")

def pasimti_knyga(biblioteka_file, pavadinimas):
    try:
        with open(biblioteka_file, 'r') as file:
            knygos_data = json.load(file)

        knygos = [Knyga.from_dict(knyga_data) for knyga_data in knygos_data]

        for knyga in knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                if knyga.likusios_knygos > 0:
                    knyga.likusios_knygos -= 1
                    knyga.pasiemimo_data = datetime.datetime.now()
                    knyga.grazinimo_data = knyga.pasiemimo_data + datetime.timedelta(days=14)
                    print(f"Pasiemete knyga '{pavadinimas}'. Grazinimo data: {knyga.grazinimo_data.strftime('%Y-%m-%d')}")
                else:
                    print(f"Knygos '{pavadinimas}' nebeliko!")
                break
        else:
            print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

        with open(biblioteka_file, 'w') as file:
            json.dump([knyga.to_dict() for knyga in knygos], file, indent=4)

    except FileNotFoundError:
        print("Bibliotekoje failas neegzistuoja.")
    except Exception as e:
        print(f"Ivyko klaida: {e}")

def grazinti_knyga(biblioteka_file, pavadinimas):
    try:
        with open(biblioteka_file, 'r') as file:
            knygos_data = json.load(file)

        knygos = [Knyga.from_dict(knyga_data) for knyga_data in knygos_data]

        for knyga in knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                if knyga.likusios_knygos < knyga.likusios_knygos + 1:
                    knyga.likusios_knygos += 1
                    knyga.pasiemimo_data = None
                    knyga.grazinimo_data = None
                    knyga.ar_veluojama = False
                    print(f"Grazinote knyga '{pavadinimas}'")
                else:
                    print(f"Knygu kiekis '{pavadinimas}' nevirsyti pradinio kiekio")
                break
        else:
            print(f"Knygos '{pavadinimas}' negalima grazinti, nes ji nerasta bibliotekoje")

        with open(biblioteka_file, 'w') as file:
            json.dump([knyga.to_dict() for knyga in knygos], file, indent=4)

    except FileNotFoundError:
        print("Bibliotekoje failas neegzistuoja")
    except Exception as e:
        print(f"Ivyko klaida: {e}")

def patikrinti_pavelavimus(biblioteka_file):
    try:
        with open(biblioteka_file, 'r') as file:
            knygos_data = json.load(file)

        knygos = [Knyga.from_dict(knyga_data) for knyga_data in knygos_data]
        now = datetime.datetime.now()
        ar_veluojama = []

        for knyga in knygos:
            if knyga.grazinimo_data and knyga.grazinimo_data < now:
                knyga.ar_veluojama = True
                ar_veluojama.append(knyga)
            else:
                knyga.ar_veluojama = False

        with open(biblioteka_file, 'w') as file:
            json.dump([knyga.to_dict() for knyga in knygos], file, indent=4)

        if ar_veluojama:
            print("Paveluotos knygos:")
            for knyga in ar_veluojama:
                print(f"- {knyga.pavadinimas} (turejo buti grazinta {knyga.ar_veluojama.strftime('%Y-%m-%d')})")
        else:
            print("Nera paveluotu knygu")
    
    except FileNotFoundError:
        print("Bibliotekos failas neegzistuoja")
    except Exception as e:
        print(f"Ivyko klaida: {e}")