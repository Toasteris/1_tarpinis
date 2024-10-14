from biblioteka import prideti_knyga, panaikinti_knygas, pasiimti_knyga, ieskoti_knygos, DATA_FILE

def main():
    while True:
        print("\nBibliotekos valdymas:")
        print("1. Prideti knyga")
        print("2. Panaikinti senas knygas")
        print("3. Pasiimti knyga")
        print("4. Ieskoti knygos pagal pavadinima")
        print("5. Ieskoti knygos pagal autoriu")
        print("0. Isjungti")

        pasirinkimas = input("Pasirinkite: ")

        if pasirinkimas == "1":
            prideti_knyga()
        elif pasirinkimas == "2":
            panaikinti_knygas
        elif pasirinkimas == '3':
            pavadinimas = input("Iveskite knyga kuria norite pasiskolinti: ")
            pasiimti_knyga(DATA_FILE, pavadinimas)
        elif pasirinkimas == '4':
            pavadinimas = input("Ieskoti pagal pavadinima: ")
            ieskoti_knygos(DATA_FILE, 'pavadinimas', pavadinimas)
        elif pasirinkimas == '5':
            autorius = input("Ieskoti pagal autoriu: ")
            ieskoti_knygos (DATA_FILE, 'autorius', autorius)
        elif pasirinkimas == "0":
            print("Isjungta")
            break
        else:
            print("Blogai. Pasirinkite dar karta")

if __name__== "__main__":
    main()