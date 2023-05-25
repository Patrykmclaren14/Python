def binary_search(list, element):
    middle = 0  # (2) middle = 6
    start = 0  # (2) start = 7
    end = len(list)  # 12
    steps = 0

    while (start <= end):  # (1) 0 < 12
        # (1) lista od 0 do 12
        # (1) wszystkie liczby (2) od 7 elementu do 12
        print("Step", steps, ":", str(list[start:end+1]))

        steps += 1
        # (1) middle = 12//2 = 6 (2) middle = 19//2 = 9
        middle = (start+end) // 2

        if element == list[middle]:  # (1) element = 1
            return middle
        if element < list[middle]:
            end = middle - 1
        else:   # element > 1
            start = middle + 1  # (1) start = 6 + 1 (2) start = 9 + 1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 5

binary_search(my_list, target)
