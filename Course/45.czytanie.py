with open("oceany.txt", "r") as file:
    for line in file:
        print(line)
    oceany = file.read().splitlines() #tworzy tablice
    print(oceany)