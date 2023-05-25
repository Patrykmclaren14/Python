a = {8,3,4,2,1}
print(a)
a.add(23)
print(a)

b = {4,32,5,12,3,2}

print(a&b) #wszystkie wspolne elementy
print(a|b) #suma wszystkich zbiorow
print(a-b) 

print(a.issubset(b)) # czy a jest podzbiorem a /false

a = {1,2,3,4,5,6}
b = {4,6}

print(b.issubset(a)) #b jest podzbiorem a