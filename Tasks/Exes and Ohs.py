def xo(s):
    sumX = 0
    sumO = 0
    for x in range(0, len(s)):
        if s[x] == 'x' or s[x] == 'X':
            sumX += 1
        elif s[x] == 'o' or s[x] == 'O':
            sumO += 1
        else: 
            continue
    if sumO == sumX:
        return True
    else: return False

print(xo('OxOx'))


    
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
       