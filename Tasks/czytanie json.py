'''''''''
[0, 0, 0, 0, 0, 1]  -->  1
# 1 group of 5 zeros (>= 4), thus the result is 1

[0, 0, 0, 0, 1, 0, 0, 0, 0]  -->  2
# 2 group of 4 zeros (>= 4), thus the result is 2

[0, 0, 0, 0, 1, 0]  -->  0 
# 1 group of 4 zeros and 1 group of 1 zero (< 4)
# _every_ sequence of zeros must be at least 4 long, thus the result is 0

[0, 0, 0, 1, 0, 0]  -->  0
# 1 group of 3 zeros (< 4) and 1 group of 2 zeros (< 4)

[1, 2, 3, 4, 5]  -->  0
# no zeros

[]   0
# no zeros
'''''''''

def zero_plentiful(arr):   
        result = 0
        amount = 0 
        for x in range(0,len(arr)):
            if 0 in arr:
                if arr[x] == 0:
                    result += 1
                    if result >= 4:
                        result = 0
                        amount += 1
                else:
                    if arr[x] != 0:
                        result = 0
            else: amount = 0
        return amount   

print(zero_plentiful([0,0,0,0,0,0]),1)


import webbrowser


webbrowser.open('https://www.youtube.com/')

webbrowser.open('https://www.google.com')

webbrowser.open('https://www.chess.com/home')
