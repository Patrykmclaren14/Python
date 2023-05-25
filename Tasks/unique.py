string = 'Countmyuniqueconsonants'

string = set(string)

print(len(string))


def count_consonants(text):
    result = 0
    countener = ['i','e','u','a','o']
    text = text.lower()
    text = text.replace(" ","")
    text = set(text)
    print(text)
    for tex in text:
        if tex not in countener:
            tex = tex.isalpha()
            if tex == True:
                result += 1
    return result

print(count_consonants('Count my unique consonants!!'))



