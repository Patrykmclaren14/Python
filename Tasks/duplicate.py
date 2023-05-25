def distinct(seq):
    tab = []
    for x in range(0,len(seq)):
        if seq[x] not in tab:
            tab.append(seq[x])
    return tab