def filter_list(l):
    tab = []
    for x in range(0,len(l)):
        if type(l[x]) == int:
            tab.append(l[x])
    return tab

print(filter_list([1, 'a', 'b', 0, 15]))

if type(1) == int:
    print(1)