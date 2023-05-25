

def to_jaden_case(string):
    string = string.split()
    tab = []
    for x in range(0,len(string)):
        string[x] = string[x].capitalize()
        tab.append(string[x])
    result = ' '.join(tab)
    return result
    
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))