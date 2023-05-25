'''''''''
Napisz program, który:
 utworzy pustą listę i wypełni ją pięcioma liczbami losowymi z dowolnego zakresu, np. [−1, 1] (do
generowania liczb możesz użyć np. funkcji uniform z modułu random, której wywołanie uniform(a,
b) zwraca liczbę z przedziału [a, b]);
 wypisze po kolei wszystkie elementy listy wraz z indeksami w następujący sposób:
4
lista [0]: 0.1
lista [1]: -0.92
itd .
 wypisze długość listy, czyli ilość jej elementów;
 znajdzie i wypisze największy element listy oraz jego indeks.
'''''''''
import random
a = []

for x in range(0,5):
    a = random.uniform(4,6)
    print(list(a))
