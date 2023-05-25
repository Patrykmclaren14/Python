def count(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
 
    return sum
 
print("Suma wszystkich argumentów:", count(2,4,1,2,4,5,10))









