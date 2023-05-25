with open("oceany.txt", "r", encoding="UTF-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(4)
    print(file.readline())
    print(file.tell())