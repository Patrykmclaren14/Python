from itertools import count


image = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
]


def count_islands(image):
    tab = []
    answer = []
    z = 0
    for x in range(0, len(image)):
        tab.append([]*x)

    for x in range(0, len(image)):
        for y in range(0, 4):
            if image[x][y] == 0:
                tab[x].append('`')
            else:
                tab[x].append('X')
    for x in range(0, len(tab)):
        for y in range(len(tab[x])-1):
            if tab[x][y] == 'X' and tab[x][y] == tab[x][y+1]:
                answer.append(1)
            else:
                answer.append(0)
    print(answer)


count_islands(image)
