import itertools


def unique_in_order(sequence):
    uniqueList = []
    for key, group in itertools.groupby(sequence):
        uniqueList.append(key)
    return uniqueList


print(unique_in_order('AAAABBBCCDAABBB'))
