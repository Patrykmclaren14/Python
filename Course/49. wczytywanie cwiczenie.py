ImionaINazwiska = []

with open("imiona_i_nazwiska.txt", 'r', encoding='UTF-8') as plik:
    for linia in plik:
        ImionaINazwiska.append(tuple(linia.replace('\n',"").split( ))) #rozdziela wszystko na liste, replace usuwa \n na nic
    print(ImionaINazwiska)

with open("imiona.txt", 'w', encoding='UTF-8') as plik:
    for imiona in ImionaINazwiska:
        plik.write(imiona[0] + '\n')

with open("nazwiska.txt", 'w', encoding='UTF-8') as plik:
    for imiona in ImionaINazwiska:
        plik.write(imiona[1] + '\n')



'''''''''
with open("nazwiska.txt", 'w', encoding='UTF-8') as plik:
    for imiona in ImionaINazwiska:
        try:
            plik.write(imiona[1] + '\n')
                                        jesli ktos podal tylko imie bez nazwiska wyskoczy blad
                                        zeby uniknac tego bledu dajac try i finally lub except
        except:
            file.write('nie bylo nazwiska')
'''''''''