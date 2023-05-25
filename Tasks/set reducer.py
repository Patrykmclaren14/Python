tab = [0, 4, 6, 8, 8, 8, 5, 5, 7]
pusta = []
score = 1
for x in range(0, len(tab)-1):
    print(tab[x], tab[x+1])
    if tab[x] == tab[x+1]:
        score += 1
    else:
        pusta.append(score)
        score = 1

print(pusta)
