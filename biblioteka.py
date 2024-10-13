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
            with open(DATA_FILE, 'r')as file:
                knygos = json.load(file)
        else:
            knygos = []

        knygos.append(knyga.__dict__)

        with open(DATA_FILE, 'w') as file:
            json.dump(knygos, file, indent=4)

    except Exception as e:
        print(f"nepavyko issaugoti knygos: {e}")

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
            print("Blogai irasyta. Metai turi buti skaicius")
        except Exception as e:
            print(f"Ivyko klaida: {e}")