def get_middle(s):
    if len(s) % 2 == 0:
        string = s[int(len(s)/2) - 1] + s[int(len(s)/2)]
    else:
        string = s[int(len(s)/2)]
    return string


print(get_middle('a'))
