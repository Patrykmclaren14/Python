def cakes(recipe, available):
    possibilities = 0
    sum = []
    for repositories in available:
        if repositories in recipe:
            possibilities += 1
    if possibilities == len(recipe):
        for repositories in recipe:
            for repositories2 in available:
                if repositories2 == repositories:
                    sum.append(available[repositories2] //
                               recipe[repositories])
    else:
        return 0
    return min(sum)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))

for x in recipe:
    print(available.get(x, 0))
