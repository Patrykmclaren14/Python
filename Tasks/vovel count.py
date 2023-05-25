sentence = "ssssabracadabra"
def get_count(sentence):
    result = 0
    i = ['i','u','e','a','u']
    for x in range(0,len(sentence)):
        if i in sentence:
            result +=1
    return result
    
print(get_count("ssssabracadabra"))





