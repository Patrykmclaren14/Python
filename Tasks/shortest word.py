def find_short(s):
    s = s.split()
    number = 100
    for x in range(0,len(s)):
        if len(s[x]) < number:
            number = len(s[x])
    return number

