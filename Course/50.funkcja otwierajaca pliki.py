def OtwieraniePliku(plik):
    with open(plik, encoding='UTF - 8') as plik:
        tresc = plik.readlines()
        for Ladnaskladnia in tresc:
            Ladnaskladnia = Ladnaskladnia.strip()
            print(Ladnaskladnia)

plik = input("Podaj nazwe pliku:")

try:
    OtwieraniePliku(plik)
except:
    print("Nie ma takiego")


