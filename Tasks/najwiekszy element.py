ending = 'abc'
text = 'abc'





def solution(text,ending):
    if  text[-1] == ending[-1]:
        if ending in text:
            return True
        else: return False
    else: return False

print(solution('abc','abc'))