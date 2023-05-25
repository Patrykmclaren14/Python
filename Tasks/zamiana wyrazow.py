a = (input("Zapisz Zdanie: "))


def reverse_v3(a):
  y = a.split()
  return " ".join(reversed(y))

print(reverse_v3(a))

y = a.split()
print(y[0:4])

txt = "Jakub ma cztery jablka"
print(txt.split())

#.split() usuwa dany znak wyraz (element) z ciagu znakow (zdania)

x = txt.split()

print(' '.join(reversed(x)))