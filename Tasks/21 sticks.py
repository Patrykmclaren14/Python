def make_move(sticks):
    all = 21
    while 0 < all:
        print('Bob takes', sticks)
        all - sticks
    return all, 'sticks'


print(make_move(3))
