from biblioteka import prideti_knyga

def main():
    while True:
        print("\nBibliotekos valdymas:")
        print("1. Prideti knyga")
        print("2. Isjungti")

        pasirinkimas = input("Pasirinkite: ")

        if pasirinkimas == "1":
            prideti_knyga()
        elif pasirinkimas == "2":
            print("Isjungta")
            break
        else:
            print("Blogai. Pasirinkite dar karta")

if __name__== "__main__":
    main()