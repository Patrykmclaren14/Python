def consonant_count(s):
    s = s.replace(" ","")
    result = 0
    i = ['i','e','u','o','a','A','E','U','O','I']
    for word in s:
        if (ord(word) >= 65 and ord(word) <= 90) or (ord(word) >= 97 and ord(word) <= 122 ) :
            if word not in i:
                result += 1
    return result

print(consonant_count('KFZzRJJFAz'))


string = 'ab c '
string = string.replace(" ", "")
print(string)

print(ord('A'))

txt = "Company10"

x = txt.isalpha() # funkcja ktora zwraca tylko litery bez liczb i znakow

print(x)


def consonant_count(s):
    s = s.replace(" ","")
    result = 0
    i = ['i','e','u','o','a']
    for word in s:
        word = word.lower()
        print(word)
        if (ord(word) >= 65 and ord(word) <= 90) or (ord(word) >= 97 and ord(word) <= 122 ) :
            if word not in i:
                result += 1
    return result

print(consonant_count("Company10"))