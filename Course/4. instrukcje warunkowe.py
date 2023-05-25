if(5>3):
    print("lalala")
if(5<3):
    print("ojojo")
else:
    print("ojojo")
'''
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if(a<b):
    print(b,"jest wieksze od",a)
elif(a>b):
    print(a,"jest wieksze od",b)
else:
    print("liczby sa sobie rowne")
'''
wybor = (input("* - mnozenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potegowanie, % - reszta z dzielenia: "))

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))


if(wybor == '*'):
    print(a * b)
elif(wybor == '/'):
    if(b==0):
        print("nie dzielimy przez 0")
    else:
        print(a/b)
elif(wybor == '+'):
        print(a+b)
elif(wybor == '-'):
    print(a-b)
elif(wybor == '**'):
    print(a**b)
elif(wybor == '%'):
    print(a%b)
else:
    print("błąd")