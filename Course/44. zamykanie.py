with open("test2.txt", 'w') as file:
    file.write("sample")
    print(0/0)
    a = 5
    file.write("sample")
    file.close()