
def wiadomosc_powitalna():
    print("test")           #nie wywolana

wiadomosc_powitalna() #wywolana wypisalo test

def wiadomosc(imie):
    print("Czesc",imie,"milo mi powitac Cie w moim programie")

wiadomosc("Arku")
wiadomosc("Wiolu")
wiadomosc("Kuba")

imiona = ["Arku","Wiolu","Bartku"]

for imie in imiona:
    wiadomosc(imie)
