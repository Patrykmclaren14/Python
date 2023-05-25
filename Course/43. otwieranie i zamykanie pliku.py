try:  # proboj nawet jesli to
    file = open("test.txt", "w")  # tworzenie pliku
    file.write("sample")  # cos co jest po errorze sie nie wykona
    a = 5
    file.write("sample")
finally:  # finalnie i tak zwroc
    file.close()
