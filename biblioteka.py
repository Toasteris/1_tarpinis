import json
import os
from knyga import Knyga

DATA_FILE = 'data/knygos.json'

def prideti_knyga():
    try:
        autorius = input("Irasykite knygos autoriu: ")
        pavadinimas = input("Irasykite knygos pavadinima: ")
        isleidimo_metai = int(input("Irasykite isleidimo metus: "))
        zanras = input("Irasykite knygos zanra: ")
        
        knyga = Knyga(autorius, pavadinimas, isleidimo_metai, zanras)

        issaugoti_knyga(knyga)
        print("Knyga prideta")
    except ValueError:
        print("Neteisingai. Isleidimo metai turi buti skaicius")
    except Exception as e:
        print(f"Ivyko klaida: {e}")

def issaugoti_knyga(knyga):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                knygos = json.load(file)
        else:
            knygos = []

        knygos.append(knyga.__dict__)

        with open(DATA_FILE, 'w') as file:
            json.dump(knygos, file, indent=4)

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
            knygos = json.load(file)

        for knyga in knygos:
            if knyga['pavadinimas'].lower() == pavadinimas.lower():
                if knyga['likusios_knygos'] > 0:
                    knyga['likusios_knygos'] -= 1
                    print(f"Pasiskolinote knyga '{pavadinimas}'")
                else:
                    print(f"Sios knygos '{pavadinimas}' nebeturime")
                break
        else:
            print(f"Knygos '{pavadinimas}' bibliotekoje neturime")
    except FileNotFoundError:
        print("Bibliotekoje failas neegzistuoja")        

        with open(biblioteka_file, 'w') as file:
            json.dump(knygos, file, indent=4)

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
    except ValueError:
        print("Blogai irasyta. Metai turi buti skaicius")
    except Exception as e:
        print(f"Ivyko klaida: {e}")