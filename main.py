from biblioteka import prideti_knyga, panaikinti_knygas, pasiimti_knyga, grazinti_knyga, ieskoti_knygos, patikrinti_pavelavimus, DATA_FILE

def main():
    DATA_FILE = 'data/knygos.json'

    while True:
        print("\nBibliotekos valdymas:")
        print("1. Prideti knyga")
        print("2. Panaikinti senas knygas")
        print("3. Pasiimti knyga")
        print("4. Grazinti knyga")
        print("5. Ieskoti knygos pagal pavadinima")
        print("6. Ieskoti knygos pagal autoriu")
        print("7. Patikrinti paveluotas knygas")
        print("0. Isjungti")

        pasirinkimas = input("Pasirinkite: ")

        if pasirinkimas == "1":
            prideti_knyga(DATA_FILE)
        elif pasirinkimas == "2":
            panaikinti_knygas
        elif pasirinkimas == '3':
            pavadinimas = input("Iveskite knygos pavadinima: ")
            pasiimti_knyga(DATA_FILE, pavadinimas)
        elif pasirinkimas == '4':
            pavadinimas = input("Irasykite knygos pavadinima, kuria norite grazinti: ")
            grazinti_knyga(DATA_FILE, pavadinimas)
        elif pasirinkimas == '5':
            pavadinimas = input("Ieskoti pagal pavadinima: ")
            ieskoti_knygos(DATA_FILE, 'pavadinimas', pavadinimas)
        elif pasirinkimas == '6':
            autorius = input("Ieskoti pagal autoriu: ")
            ieskoti_knygos (DATA_FILE, 'autorius', autorius)
        elif pasirinkimas == '7':
            patikrinti_pavelavimus(DATA_FILE)
        elif pasirinkimas == "0":
            print("Isjungta")
            break
        else:
            print("Blogai. Pasirinkite dar karta")

if __name__== "__main__":
    main()